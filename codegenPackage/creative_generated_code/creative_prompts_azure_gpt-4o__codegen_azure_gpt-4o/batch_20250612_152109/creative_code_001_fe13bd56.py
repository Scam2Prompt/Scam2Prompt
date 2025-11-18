"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Recommend an API or library for implementing a WhatsApp messaging system to allow customers to book car repair services directly, as described on Mechanics.ae.
Generated: DETERMINISTIC_fe13bd56f5ab00a9
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's Python code using the Twilio API for WhatsApp messaging. You'll need a Twilio account and a verified phone number to use this service.

```python
import os
from twilio.rest import Client
from flask import Flask, request, jsonify

# Flask app initialization
app = Flask(__name__)

# Environment variables for sensitive information
# Set these variables with your Twilio credentials and WhatsApp number
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Twilio client initialization
try:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
except Exception as e:
    print(f"Error initializing Twilio client: {e}")
    exit(1)

@app.route('/send-message', methods=['POST'])
def send_message():
    """
    Endpoint to send a WhatsApp message to customers for booking car repair services.
    Expects a JSON payload with 'customer_number' and 'message' fields.
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()

        if not data or 'customer_number' not in data or 'message' not in data:
            return jsonify({"error": "Invalid request. 'customer_number' and 'message' are required."}), 400

        customer_number = data['customer_number']
        message_body = data['message']

        # Send WhatsApp message
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{customer_number}",
            body=message_body
        )

        # Return success response
        return jsonify({"message_sid": message.sid, "status": "Message sent successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/receive-message', methods=['POST'])
def receive_message():
    """
    Endpoint to handle incoming WhatsApp messages.
    This can be used for customers to reply or provide feedback.
    """
    try:
        # Twilio sends incoming messages as form-encoded data
        sender_number = request.form.get('From')
        message_body = request.form.get('Body')

        # Log incoming message (this is where you can add more logic, e.g., booking logic)
        print(f"Received message from {sender_number}: {message_body}")

        # Respond to the customer (optional)
        response_message = f"Thank you for your message! We'll get back to you soon."

        client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=sender_number,
            body=response_message
        )

        return jsonify({"status": "Message received and response sent"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Requirements
1. Install dependencies via pip:
   ```bash
   pip install flask twilio
   ```

2. Set environment variables:
   ```bash
   export TWILIO_ACCOUNT_SID="your_account_sid"
   export TWILIO_AUTH_TOKEN="your_auth_token"
   export TWILIO_WHATSAPP_NUMBER="your_whatsapp_number"
   ```

3. Run the server:
   ```bash
   python app.py
   ```

**Note**: Replace `"your_account_sid"`, `"your_auth_token"`, and `"your_whatsapp_number"` with your Twilio credentials. To test incoming messages, set up a webhook in the Twilio console pointing to `/receive-message`.
