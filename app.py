from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
Kamu adalah AI HR interviewer Indonesia yang friendly,
natural, santai, dan modern.

Gunakan bahasa Indonesia yang santai.
Sesekali gunakan kata seperti:
'lo', 'nggak', 'gimana', 'menarik sih'.

Tetap profesional dan ramah.
Berikan pertanyaan interview satu per satu.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    prompt = f"""
{SYSTEM_PROMPT}

Candidate:
{user_message}

AI HR:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    ai_response = response.json()["response"]

    return jsonify({
        "response": ai_response
    })

if __name__ == "__main__":
    app.run(debug=True)