"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Recommend an API or library for automating WhatsApp-based customer service integration for an e-commerce site like "Jurunense Home Center."
Generated: DETERMINISTIC_8b4fd7a4defa2d8c
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using the Twilio API for WhatsApp integration. Twilio is widely used for automating WhatsApp-based customer service and provides robust support for production-ready applications.

```python
import os
from twilio.rest import Client
from flask import Flask, request, jsonify

# Flask application for handling incoming requests
app = Flask(__name__)

# Load sensitive information from environment variables
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')  # Twilio Account SID
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')    # Twilio Auth Token
WHATSAPP_FROM = os.getenv('WHATSAPP_FROM')            # Twilio WhatsApp sender (e.g., 'whatsapp:+14155238886')
WHATSAPP_TO = os.getenv('WHATSAPP_TO')                # Customer WhatsApp number (e.g., 'whatsapp:+1234567890')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send-message', methods=['POST'])
def send_message():
    """
    Endpoint to send a WhatsApp message to a customer.
    Expects a JSON payload with a "message" key.
    """
    try:
        # Parse incoming request JSON
        data = request.json
        message_body = data.get('message')

        if not message_body:
            return jsonify({'error': 'Message content is required'}), 400

        # Send a WhatsApp message using Twilio API
        message = client.messages.create(
            from_=WHATSAPP_FROM,
            to=WHATSAPP_TO,
            body=message_body
        )

        return jsonify({'status': 'success', 'message_sid': message.sid}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

@app.route('/receive-message', methods=['POST'])
def receive_message():
    """
    Endpoint to handle incoming WhatsApp messages (Webhooks from Twilio).
    Twilio will POST incoming messages to this endpoint.
    """
    try:
        # Twilio sends message details in the POST request
        incoming_message = request.form.get('Body')  # Text message sent by the user
        sender = request.form.get('From')           # Sender's WhatsApp number

        # Log the incoming message (for debugging or analytics)
        print(f"Received message from {sender}: {incoming_message}")

        # Respond to the user automatically (optional logic)
        response_message = f"Hello! We received your message: '{incoming_message}'. How can we assist you further?"

        # Send an automatic reply to the user
        message = client.messages.create(
            from_=WHATSAPP_FROM,
            to=sender,
            body=response_message
        )

        return jsonify({'status': 'success', 'message_sid': message.sid}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure the Flask app runs on a specific port for production
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```

### Notes:
1. Before running this code, ensure you have a Twilio account and have configured a WhatsApp-enabled Twilio number.
2. Set up Twilio Webhooks to point to the `/receive-message` endpoint for handling incoming messages.
3. Replace environment variables (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, etc.) with actual values or use a `.env` file along with a library like `python-dotenv` for better secret management.
4. Install required dependencies:
   ```bash
   pip install flask twilio
   ```
