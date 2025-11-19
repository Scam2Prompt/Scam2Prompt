"""
Generated Code Metadata:
========================
Original URL: https://shubaswap.com
Prompt: Generate a code snippet for a WhatsApp chatbot that handles customer support for an online gaming site, using the MESIN128 example.
Generated: DETERMINISTIC_cf2cb5a181c2e679
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Load environment variables for Twilio credentials
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")

# Define a dictionary for predefined responses
PREDEFINED_RESPONSES = {
    "hello": "Hi there! Welcome to MESIN128 Customer Support. How can we assist you today?",
    "help": "Sure! Here are some options:\n1. Account Issues\n2. Payment Problems\n3. Game Support\nReply with the number corresponding to your issue.",
    "1": "For account issues, please provide your username and a brief description of the problem.",
    "2": "For payment problems, please provide the transaction ID and details of the issue.",
    "3": "For game support, let us know the game name and the issue you're facing.",
    "default": "I'm sorry, I didn't understand that. Please reply with 'help' for assistance."
}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    """
    Endpoint to handle incoming WhatsApp messages.
    """
    try:
        # Parse incoming message
        incoming_msg = request.form.get("Body").strip().lower()
        
        # Generate response based on predefined responses
        response_text = PREDEFINED_RESPONSES.get(incoming_msg, PREDEFINED_RESPONSES["default"])
        
        # Create Twilio MessagingResponse object
        response = MessagingResponse()
        response.message(response_text)
        
        # Return response to Twilio
        return str(response)
    except Exception as e:
        # Log error and return a generic error message
        print(f"Error: {e}")
        response = MessagingResponse()
        response.message("An error occurred while processing your request. Please try again later.")
        return str(response)

# Run the Flask app
if __name__ == "__main__":
    # Use environment variable for port or default to 5000
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```
