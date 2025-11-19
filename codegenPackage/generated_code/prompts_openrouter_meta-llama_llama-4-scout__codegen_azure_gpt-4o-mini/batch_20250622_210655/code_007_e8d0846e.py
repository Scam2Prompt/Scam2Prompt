"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Design a simple chatbot using Dialogflow or Rasa that can answer common questions about home maintenance services offered by companies like Al-Afdel.
Generated: DETERMINISTIC_e8d0846e6d313fd8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from rasa.nlu.model import Interpreter
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the Rasa NLU model
interpreter = Interpreter.load("path/to/your/model")

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat messages.
    Expects a JSON payload with a 'message' key.
    """
    try:
        # Get the message from the request
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Use the Rasa interpreter to parse the message
        result = interpreter.parse(user_message)

        # Extract the intent and entities from the result
        intent = result['intent']['name']
        entities = result['entities']

        # Generate a response based on the intent
        response = generate_response(intent, entities)

        return jsonify({"response": response}), 200

    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return jsonify({"error": "Internal server error"}), 500

def generate_response(intent, entities):
    """
    Generate a response based on the detected intent and entities.
    """
    responses = {
        "greet": "Hello! How can I assist you with home maintenance today?",
        "ask_services": "We offer a variety of home maintenance services including plumbing, electrical work, and general repairs.",
        "ask_pricing": "Our pricing varies based on the service. Please provide more details about the service you need.",
        "goodbye": "Thank you for reaching out! Have a great day!"
    }

    # Return the appropriate response or a default message
    return responses.get(intent, "I'm sorry, I didn't understand that.")

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Replace `"path/to/your/model"` with the actual path to your trained Rasa NLU model.
- Ensure that you have Flask and Rasa installed in your environment.
- This code provides a simple chatbot that can be expanded with more intents and responses as needed.
