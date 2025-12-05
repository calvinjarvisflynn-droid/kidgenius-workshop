from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/api/generate", methods=["POST"])
def generate_worksheet():
    data = request.json
    topic = data.get("topic", "")
    prompt = f"Create a printable kids educational worksheet about: {topic}"
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate kids worksheets."},
            {"role": "user", "content": prompt}
        ]
    )
    text_output = response.choices[0].message["content"]
    return jsonify({"worksheet": text_output})

if __name__ == "__main__":
    app.run()
