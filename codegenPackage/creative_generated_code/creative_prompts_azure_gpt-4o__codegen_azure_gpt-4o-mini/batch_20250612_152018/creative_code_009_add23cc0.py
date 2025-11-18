"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Develop a chatbot using Python and NLP libraries to answer common queries about Darul Raza's services, such as Istikhara, Taweezat, and online courses.
Generated: DETERMINISTIC_add23cc060bb51ae
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, jsonify

# Ensure nltk punkt tokenizer is downloaded
nltk.download('punkt')

# Define pairs of patterns and responses for the chatbot
CHAT_PAIRS = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is istikhara?",
        ["Istikhara is a prayer for seeking guidance from Allah when making a decision."]
    ],
    [
        r"what are taweezat?",
        ["Taweezat are amulets or talismans that are believed to provide protection and blessings."]
    ],
    [
        r"what online courses do you offer?",
        ["We offer a variety of online courses, including Islamic studies and personal development."]
    ],
    [
        r"bye|exit",
        ["Goodbye! Have a great day!", "Take care!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't quite understand. Can you rephrase that?"]
    ]
]

# Initialize the Flask application
app = Flask(__name__)

# Create a chatbot instance
chatbot = Chat(CHAT_PAIRS, reflections)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat messages.
    Expects JSON data with a 'message' field.
    Returns a JSON response with the chatbot's reply.
    """
    try:
        # Get the message from the request
        user_message = request.json.get('message')
        
        if not user_message:
            return jsonify({'error': 'No message received'}), 400
        
        # Generate a response from the chatbot
        bot_response = chatbot.respond(user_message)

        return jsonify({'response': bot_response}), 200

    except Exception as e:
        # Log error (in production, consider using a logging framework)
        print(f"Error: {e}")
        return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Requirements
To run this code, ensure you have Flask and NLTK installed. You can install them via pip:

```bash
pip install Flask nltk
```
