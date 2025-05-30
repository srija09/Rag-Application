import os
from groq import Groq
import google.generativeai as genai
api_key = os.getenv("GEMINI_API_KEY")

class GrokLLM:
    def __init__(self):
        self.llm = Groq(api_key = api_key)
    def invoke(self, prompt):
        response = self.llm.chat.completions.create(
            model = "qwen-qwq-32b",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
class GeminiLLM:
    def __init__(self):
        self.client = genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
    def invoke(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

