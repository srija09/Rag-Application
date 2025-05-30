from flask import Flask, request
from llmconfig import GrokLLM, GeminiLLM
from systemprompt import sql_query_generation_prompt
from flask_cors import CORS
import sqlite3
import logging
import os

import mysql.connector as mysql
app = Flask(__name__)
allowed_origins = ["http://localhost:3000"]
CORS(app, resources={r"/*": {"origins": allowed_origins}}, supports_credentials=True)


logging.basicConfig(
    filename='ragapp.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)


# conn = mysql.connect(
#     host="shinkansen.proxy.rlwy.net",
#     port=53037,
#     user="root",
#     password="nRioaaFHMzDJY",
#     database="railway"
# )



@app.route('/')
def home():
    return "Hello, Flask!"

# @app.before_request
# def verify_token():
#     token = request.headers.get('Authorization')
#     expected_token = os.getenv("API_TOKEN")
#     if token != expected_token:
#         return {"error": "Unauthorized request"}, 401

@app.route('/chat', methods = ['POST'])
def generate():
    try:
        data = request.json
        question = data.get('question')
        # llm = GrokLLM()
        llm = GeminiLLM()
        prompt = sql_query_generation_prompt()
        prompt1 = prompt.format(
            question=question
        )
        response = llm.invoke(prompt1)
        print("Response is:", response)
        logging.info(f"User Question: {question}")
        logging.info(f"Generated SQL Query: {response}")
        response_container = {}
        response_container["question"]=question
        response_container["response"]=response

        conn = sqlite3.connect("customers.db")
        cursor = conn.cursor()
        cursor.execute(response)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        column_names = [description[0] for description in cursor.description]
        conn.close()
        response_container["results"] = [dict(zip(column_names, row)) for row in rows]
        return response_container
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return {"error": "Database query failed."}, 500

    except Exception as e:
        logging.error(f"Unhandled exception: {e}")
        return {"error": "Unexpected error occured."}, 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
