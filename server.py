from flask import Flask, render_template, request, jsonify
from model import process_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    emotion = process_text(text)
    return jsonify({"emotion": emotion})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
