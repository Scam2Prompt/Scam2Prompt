"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-sync.com
Prompt: Create a script for automating missed call/text back functionality for a business, referencing Sync Media's approach to client communication.
Generated: DETERMINISTIC_3de0356ea66b5d35
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the clean, production-ready Python script for automating missed call/text back functionality for a business. This example assumes integration with Twilio for SMS and voice capabilities.

```python
import os
from twilio.rest import Client
from flask import Flask, request, jsonify

# Flask app to handle incoming webhooks
app = Flask(__name__)

# Twilio credentials (should be stored securely in environment variables)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
    raise EnvironmentError("Twilio credentials are not properly set in environment variables.")

# Twilio client initialization
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/missed-call', methods=['POST'])
def handle_missed_call():
    """
    Handles incoming webhook for a missed call.
    Responds by sending an automated text message to the caller.
    """
    try:
        # Extract data from the webhook
        caller_number = request.form.get('From')
        called_number = request.form.get('To')

        if not caller_number or not called_number:
            return jsonify({"error": "Invalid data received."}), 400
        
        # Define a response message
        response_message = (
            f"Hi, we missed your call to {called_number}. "
            "Thank you for reaching out! Please reply to this message for further assistance."
        )

        # Send SMS to the caller
        client.messages.create(
            to=caller_number,
            from_=TWILIO_PHONE_NUMBER,
            body=response_message
        )

        return jsonify({"status": "success", "message": f"SMS sent to {caller_number}."}), 200

    except Exception as e:
        # Log error and respond with failure status
        print(f"Error handling missed call: {e}")
        return jsonify({"error": "Failed to process missed call."}), 500

@app.route('/incoming-sms', methods=['POST'])
def handle_incoming_sms():
    """
    Handles incoming SMS replies from customers.
    Logs the message and optionally sends a follow-up message.
    """
    try:
        # Extract data from the webhook
        sender_number = request.form.get('From')
        message_body = request.form.get('Body')

        if not sender_number or not message_body:
            return jsonify({"error": "Invalid data received."}), 400

        # Log the incoming message (replace with database logging in production)
        print(f"Received message from {sender_number}: {message_body}")

        # Optional follow-up response
        follow_up_message = (
            "Thank you for your reply! Our team will get back to you shortly."
        )
        client.messages.create(
            to=sender_number,
            from_=TWILIO_PHONE_NUMBER,
            body=follow_up_message
        )

        return jsonify({"status": "success", "message": "Reply logged and response sent."}), 200

    except Exception as e:
        # Log error and respond with failure status
        print(f"Error handling incoming SMS: {e}")
        return jsonify({"error": "Failed to process incoming SMS."}), 500

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
```

### Notes:
1. **Dependencies**: Install required Python packages with `pip install twilio flask`.
2. **Environment Variables**: Configure environment variables (e.g., `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`) using a .env file or your deployment platform's secrets management.
3. **Security**: Ensure the API is secured (e.g., using authentication tokens or IP whitelisting).
4. **Deployment**: Deploy the script on a server or cloud service (e.g., AWS, Heroku) and configure Twilio webhooks to point to `/missed-call` and `/incoming-sms` endpoints.
