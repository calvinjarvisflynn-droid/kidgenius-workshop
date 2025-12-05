import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/api/generate", methods=["POST"])
def generate_worksheet():
    data = request.get_json()
    topic = data.get("topic", "Fun Activity")
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Create a printable kids educational worksheet about: {topic}",
            max_tokens=300
        )
        worksheet_text = response.choices[0].text.strip()
        return jsonify({"worksheet": worksheet_text})
    except Exception as e:
        return jsonify({"worksheet": f"Error: {str(e)}"})




# No need to run app.run() on Vercel

