# app.py
from flask import Flask, request, jsonify, render_template
from chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()  # Initialize the Chatbot class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    bot_response = chatbot.get_response(user_input)
    return jsonify({'response': bot_response})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
