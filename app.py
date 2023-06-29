# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from chat import get_response

# app = Flask(__name__)
# CORS(app)

# @app.get("/")
# def index_get():
#     return render_template("index.html")

# @app.post("/predict")
# def predict():
#     text = request.get_json().get("message")
#     print("Received input:", text)  # Debugging statement
#     response = get_response(text)
#     print("Generated response:", response)  # Debugging statement
#     message = {"answer": response}
#     return jsonify(message)

# if __name__ == "__main__":
#     app.run(debug = False, host = "0.0.0.0")
import streamlit as st
from chat import get_response

def main():
    st.title("Chatbot Demo")

    user_input = st.text_input("User Input:")
    if st.button("Submit"):
        response = get_response(user_input)
        st.text_area("Bot Response:", value=response, height=200)

if __name__ == "__main__":
    main()
