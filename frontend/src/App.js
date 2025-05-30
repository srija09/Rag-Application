// import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
function App() {
  const [question, setQuestion] = useState("");
  const [results, setResults] = useState([]);

  const handleKeyPress = async (e) => {
    if (e.key === "Enter" && question.trim() !== "") {
      try {
        const response = await fetch("http://localhost:5000/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            // "Authorization": "RAGAPPLICATION"
          },
          body: JSON.stringify({ question }),
        });

        const data = await response.json();
        setResults(data.results || []);
      } catch (err) {
        console.error("Error:", err);
      }
    }
  };
  return (
    <div className="app-container">
      
      <h1 className="heading">LLM-Powered Chatbot with FastAPI and SQL Integration</h1>
      
        <div className="chatbox-container">
        <input
          className="chatbox"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={handleKeyPress}
        />
      </div>

      
      {results.length > 0 ? (
        <div className="table-container">
          <table>
            <thead>
              <tr>
                {Object.keys(results[0]).map((col, idx) => (
                  <th key={idx}>{col}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {results.map((row, idx) => (
                <tr key={idx}>
                  {Object.values(row).map((val, i) => (
                    <td key={i}>{val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ): (
  question && (
    <div className="no-results-message">
      Data is either not present in DB or you might have to recheck your question.
    </div>
  ))}
    </div>
  );
}

export default App;
