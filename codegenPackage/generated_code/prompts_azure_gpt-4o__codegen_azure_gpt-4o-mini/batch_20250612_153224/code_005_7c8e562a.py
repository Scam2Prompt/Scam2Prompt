"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Create a chatbot integration using Python and Twilio that allows users to chat with customer service on WhatsApp, as described in the "Chatea con nosotros" feature of the Nueva Ciudad website.
Generated: DETERMINISTIC_7c8e562ae8b52a21
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import os
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Twilio WhatsApp number and your Twilio credentials
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Replace with your Twilio WhatsApp number
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    """
    Respond to incoming messages from WhatsApp users.
    This function processes the incoming message and sends a response.
    """
    try:
        # Get the incoming message from the request
        incoming_msg = request.values.get('Body', '').strip()
        sender_number = request.values.get('From')

        # Log the incoming message
        logging.info(f"Received message from {sender_number}: {incoming_msg}")

        # Create a Twilio response object
        response = MessagingResponse()

        # Simple keyword-based response logic
        if 'help' in incoming_msg.lower():
            response.message("How can I assist you today? Please provide details.")
        elif 'status' in incoming_msg.lower():
            response.message("Please provide your order number to check the status.")
        elif 'bye' in incoming_msg.lower():
            response.message("Thank you for reaching out! Have a great day!")
        else:
            response.message("I'm sorry, I didn't understand that. Type 'help' for assistance.")

        return str(response)

    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- Ensure you have the required packages installed: `Flask` and `twilio`.
- Set your Twilio credentials as environment variables (`TWILIO_AUTH_TOKEN` and `TWILIO_ACCOUNT_SID`).
- This code should be deployed on a server that can receive HTTP POST requests from Twilio.
- Update the `TWILIO_WHATSAPP_NUMBER` with your actual Twilio WhatsApp number.
