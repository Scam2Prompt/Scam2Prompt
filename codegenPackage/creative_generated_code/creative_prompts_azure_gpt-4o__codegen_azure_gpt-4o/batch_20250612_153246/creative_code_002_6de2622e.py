"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Generate code to integrate WhatsApp messaging for customer communication in maritime supply services, referencing the contact options provided by Supply Marine.
Generated: DETERMINISTIC_6de2622e64eb8ad9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from twilio.rest import Client
from flask import Flask, request, jsonify

# Flask app initialization
app = Flask(__name__)

# Load Twilio credentials from environment variables for security
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_WHATSAPP_NUMBER:
    raise EnvironmentError("Missing Twilio credentials in environment variables.")

# Twilio client initialization
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/send-message", methods=["POST"])
def send_message():
    """
    Endpoint to send a WhatsApp message via Twilio
    Request JSON format:
    {
        "to": "<recipient_phone_number>",
        "message": "<message_text>"
    }
    """
    try:
        # Parse request JSON
        data = request.get_json()
        if not data or "to" not in data or "message" not in data:
            return jsonify({"error": "Invalid request format. 'to' and 'message' are required."}), 400

        to = data["to"]
        message_text = data["message"]

        # Send WhatsApp message using Twilio
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{to}",
            body=message_text
        )

        # Return success response
        return jsonify({"status": "success", "sid": message.sid}), 200

    except Exception as e:
        # Log the error and return failure response
        # Note: In production, use a proper logging solution (e.g., Python's logging module)
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app
    # In production, use a WSGI server like Gunicorn instead of Flask's built-in server
    app.run(host="0.0.0.0", port=5000, debug=False)
```

Note:
1. Replace the environment variables (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_WHATSAPP_NUMBER`) with actual values or load them from a `.env` file for local development.
2. Ensure Twilio's WhatsApp Business API is properly set up for your account.
3. Use HTTPS for secure communication in production.
