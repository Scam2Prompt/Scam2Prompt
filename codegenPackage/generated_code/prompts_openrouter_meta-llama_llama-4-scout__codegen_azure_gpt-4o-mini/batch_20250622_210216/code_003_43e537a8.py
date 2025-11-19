"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-ai.web.app
Prompt: Design a high-level architecture for a crypto companion chatbot, like ScottyChat, using AI and natural language processing (NLP) techniques.
Generated: DETERMINISTIC_43e537a8fc2b2017
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify
from transformers import pipeline

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Load the NLP model for chatbot responses
try:
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
except Exception as e:
    logging.error("Failed to load the NLP model: %s", e)
    raise

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat messages.
    Expects a JSON payload with a 'message' key.
    Returns a JSON response with the chatbot's reply.
    """
    try:
        # Get the message from the request
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Generate a response using the chatbot
        response = chatbot(user_message)
        bot_reply = response[0]['generated_text']

        return jsonify({"reply": bot_reply}), 200

    except Exception as e:
        logging.error("Error processing chat message: %s", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask transformers
```

### Usage
1. Start the Flask server by running the script.
2. Send a POST request to the `/chat` endpoint with a JSON body containing the user's message, e.g.:
   ```json
   {
       "message": "What is the current price of Bitcoin?"
   }
   ```
3. The server will respond with the chatbot's reply in JSON format.
