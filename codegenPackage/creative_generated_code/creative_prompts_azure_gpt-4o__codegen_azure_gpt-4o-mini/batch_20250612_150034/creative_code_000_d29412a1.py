"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chat.dabaimi.top
Prompt: Write code to integrate a chatbot interface similar to the one described on NextChat, using natural language processing techniques.
Generated: DETERMINISTIC_d29412a1f7b22539
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask application
app = Flask(__name__)

# Load the chatbot model (using Hugging Face Transformers for simplicity)
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chatbot conversations.
    Expects a JSON payload with a 'message' key.
    Returns a JSON response with the chatbot's reply.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Get the chatbot's response
        response = chatbot(user_message)

        # Format the response
        bot_reply = response[0]['generated_text']
        
        return jsonify({'reply': bot_reply}), 200

    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format'}), 400
    except Exception as e:
        # Capture any other exceptions and return a generic error message
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on the specified port
    app.run(host='0.0.0.0', port=5000)
```

Ensure you have the required libraries installed before running the code:

```bash
pip install Flask transformers torch
```
