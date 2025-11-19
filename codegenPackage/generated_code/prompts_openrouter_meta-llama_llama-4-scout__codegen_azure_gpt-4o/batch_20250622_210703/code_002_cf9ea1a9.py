"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Generate a code snippet to implement a chat system, similar to the one on Apple Market Bali's website, using a messaging platform like WhatsApp or a custom solution.
Generated: DETERMINISTIC_cf9ea1a97cad244f
Batch ID: 20250622_210703
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
from twilio.rest import Client
import os

# Initialize Flask app
app = Flask(__name__)

# Twilio configuration (replace with your Twilio credentials)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  # Twilio Account SID
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")    # Twilio Auth Token
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # Twilio Phone Number

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Endpoint to send a message via WhatsApp using Twilio API.
    Expects JSON payload with 'to' (recipient phone number) and 'message' (text to send).
    """
    try:
        # Parse request data
        data = request.get_json()
        recipient = data.get('to')  # Recipient phone number
        message_body = data.get('message')  # Message text

        # Validate input
        if not recipient or not message_body:
            return jsonify({"error": "Missing 'to' or 'message' in request body"}), 400

        # Send message via Twilio
        message = twilio_client.messages.create(
            from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
            to=f"whatsapp:{recipient}",
            body=message_body
        )

        # Return success response
        return jsonify({"status": "success", "message_sid": message.sid}), 200

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

@app.route('/receive_message', methods=['POST'])
def receive_message():
    """
    Endpoint to receive incoming messages from WhatsApp.
    Twilio will send a POST request to this endpoint with message details.
    """
    try:
        # Parse incoming message data
        sender = request.form.get('From')  # Sender phone number
        message_body = request.form.get('Body')  # Message text

        # Log the incoming message (or process it as needed)
        print(f"Message received from {sender}: {message_body}")

        # Respond to the sender (optional)
        response_message = "Thank you for your message! We'll get back to you shortly."
        twilio_client.messages.create(
            from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
            to=sender,
            body=response_message
        )

        # Return success response
        return jsonify({"status": "success"}), 200

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    # Use environment variables or default to port 5000
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
```

### Notes:
1. Replace `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` with your Twilio credentials.
2. Ensure Twilio's WhatsApp sandbox is configured for testing or use a production WhatsApp number.
3. Deploy this Flask app on a server (e.g., AWS, Heroku) and configure Twilio to send incoming messages to the `/receive_message` endpoint.
