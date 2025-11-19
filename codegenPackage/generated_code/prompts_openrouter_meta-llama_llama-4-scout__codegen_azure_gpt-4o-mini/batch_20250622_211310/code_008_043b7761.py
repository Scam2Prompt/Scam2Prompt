"""
Generated Code Metadata:
========================
Original URL: https://immediate-xzen.com
Prompt: Develop a chatbot using natural language processing (NLP) techniques that provides investment education and guidance to users, integrating with Immediate ZenX's platform.
Generated: DETERMINISTIC_043b7761a397a34e
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from flask import Flask, request, jsonify
from transformers import pipeline

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Load the NLP model for conversational AI
try:
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
except Exception as e:
    logging.error("Failed to load the NLP model: %s", e)
    raise

# Define a route for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat requests from users.
    
    Expects a JSON payload with a 'message' key.
    Returns a JSON response with the chatbot's reply.
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Generate a response using the chatbot
        response = chatbot(user_message)
        bot_reply = response[0]['generated_text']

        return jsonify({"reply": bot_reply}), 200

    except json.JSONDecodeError:
        logging.error("Invalid JSON received")
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        logging.error("An error occurred: %s", e)
        return jsonify({"error": "An internal error occurred"}), 500

# Define a route for health check
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify if the service is running.
    Returns a simple JSON response indicating the service status.
    """
    return jsonify({"status": "running"}), 200

if __name__ == '__main__':
    # Set the environment variable for the Flask app
    os.environ['FLASK_ENV'] = 'production'
    app.run(host='0.0.0.0', port=5000)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask transformers torch
```

### Usage
1. Start the Flask server by running the script.
2. Send a POST request to `/chat` with a JSON body containing the user's message.
3. Use the `/health` endpoint to check if the service is running.
