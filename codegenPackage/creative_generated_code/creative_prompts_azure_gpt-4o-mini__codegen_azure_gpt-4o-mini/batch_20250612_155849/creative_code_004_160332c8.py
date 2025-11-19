"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Provide an example of how to set up a 24/7 customer support chatbot for an online betting site, similar to the support offered by BaxBet.
Generated: DETERMINISTIC_160332c81731a032
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from transformers import pipeline

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# Configure database for storing chat logs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ChatLog model for storing interactions
class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.String(256), nullable=False)
    response_message = db.Column(db.String(256), nullable=False)

# Initialize the chatbot using Hugging Face's transformers
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint for sending messages to the chatbot.
    Expects a JSON payload with a 'message' field.
    Returns a JSON response with the chatbot's reply.
    """
    try:
        # Get user message from request
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "Message field is required."}), 400
        
        # Generate response using the chatbot
        bot_response = chatbot(user_message)
        response_message = bot_response[0]['generated_text']  # Extract the generated response

        # Log the interaction
        log_chat(user_message, response_message)

        # Return the response to the user
        return jsonify({"response": response_message}), 200

    except Exception as e:
        logging.error(f"Error processing message: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

def log_chat(user_message, response_message):
    """
    Logs the interaction between the user and the chatbot to the database.
    """
    new_log = ChatLog(user_message=user_message, response_message=response_message)
    db.session.add(new_log)
    db.session.commit()

@app.route('/logs', methods=['GET'])
def get_logs():
    """
    Endpoint for retrieving chat logs.
    Returns a JSON array of stored chat logs.
    """
    try:
        logs = ChatLog.query.all()
        return jsonify([
            {"user_message": log.user_message, "response_message": log.response_message}
            for log in logs
        ]), 200

    except Exception as e:
        logging.error(f"Error retrieving logs: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving logs."}), 500

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```
