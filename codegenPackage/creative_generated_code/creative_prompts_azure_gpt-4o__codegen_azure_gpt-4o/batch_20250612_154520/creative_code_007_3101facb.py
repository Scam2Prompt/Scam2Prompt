"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Develop a chatbot using a Python framework that helps users inquire about plant machinery training courses at CoLa Training Services.
Generated: DETERMINISTIC_3101facb81e95982
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Load the Hugging Face conversational model
chatbot_model = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Predefined responses for common queries
FAQ_RESPONSES = {
    "course types": "We offer basic, intermediate, and advanced courses for plant machinery. Contact us for details.",
    "pricing": "Our course prices depend on the level and machinery type. Please reach out to get a detailed quote.",
    "location": "Our training center is located at XYZ Street, City, Country.",
    "contact": "You can contact us at info@colatrainingservices.com or via phone at +1234567890.",
}

# Error messages
ERROR_RESPONSE = "I'm sorry, I couldn't understand your query. Please try rephrasing or ask about course types, pricing, location, or contact details."

# Endpoint to handle chatbot queries
@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Handles incoming requests from users to the chatbot.
    Expects JSON input with the key 'message'.
    
    Returns:
        JSON response containing chatbot reply.
    """
    try:
        # Get user input
        user_message = request.json.get("message", "").lower()
        if not user_message:
            return jsonify({"error": "Message field is required"}), 400
        
        # Check for predefined FAQ responses
        for keyword, response in FAQ_RESPONSES.items():
            if keyword in user_message:
                return jsonify({"reply": response}), 200

        # Generate dynamic response using the conversational model
        conversation = chatbot_model(user_message)
        bot_reply = conversation.generated_responses[-1] if conversation.generated_responses else ERROR_RESPONSE

        return jsonify({"reply": bot_reply}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Start Flask application
if __name__ == '__main__':
    # Load host and port from environment variables or use defaults
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 5000))

    # Run the development server
    app.run(host=host, port=port, debug=True)
```
