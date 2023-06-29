from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    print("Received input:", text)  # Debugging statement
    response = get_response(text)
    print("Generated response:", response)  # Debugging statement
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")
