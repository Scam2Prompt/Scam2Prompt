"""
Generated Code Metadata:
========================
Original URL: https://pranaisland.com
Prompt: Create a customer service chatbot that responds to common inquiries about handmade jewelry products, using a library like Dialogflow or Rasa.
Generated: DETERMINISTIC_e529e8b186e104a5
Batch ID: 20250622_205709
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

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Load the Rasa NLU model
interpreter = Interpreter.load("path/to/your/rasa/model")

# Define a function to handle user messages
def handle_message(user_message):
    # Parse the user message using the Rasa interpreter
    result = interpreter.parse(user_message)
    
    # Extract intent and entities from the result
    intent = result['intent']['name']
    entities = result['entities']
    
    # Respond based on the detected intent
    if intent == "greet":
        return "Hello! How can I assist you with our handmade jewelry today?"
    elif intent == "product_inquiry":
        return "We offer a variety of handmade jewelry, including necklaces, bracelets, and earrings. What specific product are you interested in?"
    elif intent == "order_status":
        return "Please provide your order number, and I will check the status for you."
    elif intent == "return_policy":
        return "Our return policy allows returns within 30 days of purchase. Would you like more details?"
    elif intent == "thank_you":
        return "You're welcome! If you have any more questions, feel free to ask."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase your question?"

# Define a route for incoming messages
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user message from the request
        user_message = request.json.get('message')
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Get the chatbot's response
        response = handle_message(user_message)
        
        # Return the response as JSON
        return jsonify({"response": response}), 200
    
    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `"path/to/your/rasa/model"` with the actual path to your trained Rasa model.
- Ensure that Rasa is properly set up and the model is trained to recognize the intents used in the `handle_message` function.
- This code uses Flask to create a simple web server that listens for POST requests at the `/chat` endpoint.
