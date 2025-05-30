This project is deployed on Vercel. Access with the below link. 
https://rag-application-two.vercel.app/

## customers DB present right now for you to query and test
 
 - **(1, 'Sahil', 'Male', 'Mumbai')**
 - **(2, 'Tanvi', 'Female', 'Pune')**
 - **(3, 'Aniket', 'Male', 'Gurgaon')**
 - **(4, 'Tanuja', 'Female', 'Pune')**
 - **(5, 'Srija', 'Female', 'Hyderabad')**
 - **(6, 'Anurag', 'Male', 'Hyderabad')**

## LLM-Powered Natural Language to SQL Chatbot

This project is a full-stack chatbot application that converts natural language queries into SQL commands internally and respond with tables as output using a Gemini API. 
It fetches and displays data from a relational database based on user input. The backend is powered by FastAPI, LLM, and the frontend is built with ReactJS.

## Tech Stack

- **Backend:** Python FastAPI
- **Frontend:** ReactJS
- **Database:** SQLite3
- **LLM Endpoint:** Gemini API (Since Groq doesn't offer free credits anymore

## Setup Instructions
### 1. Clone the Repository
    git clone https://github.com/srija09/Rag-Application.git
### 2. Run Backend server
    cd Backend

### 3. Create and run Virtual environment**
    python -m venv venv
    venv\Scripts\activate   
### 4. Install dependencies
    pip install -r requirements.txt
### 5. Run the Flask app
    python app.py

### 6. Run frontend in another powershell
    cd frontend
    
### 7. Setup Frontend
    npm install
### 8. Since the app is deployed remotely, U just have to make small change in App.js
    Change the backend deployed url in **App.js** to **http://localhost:5000/chat** 
### 9. Run frontend
    npm start

    
