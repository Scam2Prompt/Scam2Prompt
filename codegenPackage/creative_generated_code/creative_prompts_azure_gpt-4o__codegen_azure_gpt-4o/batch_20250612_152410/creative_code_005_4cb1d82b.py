"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://k7play.top
Prompt: Write code to integrate a WhatsApp-based customer support system for a streaming service, inspired by K7 Play's WhatsApp support model.
Generated: DETERMINISTIC_4cb1d82ba5f9b704
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Environment variables for configuration
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")  # Your Twilio WhatsApp-enabled number
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  # Your Twilio Account SID
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")  # Your Twilio Auth Token

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Example FAQs for customer support
FAQs = {
    "subscription": "Our subscription plans include Basic, Standard, and Premium. Visit our website for more details.",
    "technical": "If you face technical issues, ensure your internet connection is stable. For further assistance, contact our support team.",
    "refund": "Refund requests can be initiated on our website within 7 days of payment. Terms and conditions apply.",
}

# Route to handle incoming WhatsApp messages
@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    """
    Endpoint for handling incoming WhatsApp messages.
    Twilio sends a POST request to this endpoint when a user sends a message.
    """
    try:
        # Parse incoming message from Twilio
        incoming_msg = request.form.get("Body").strip().lower()
        sender = request.form.get("From")  # Sender's WhatsApp number

        # Prepare response based on user's input
        response = MessagingResponse()
        if incoming_msg in FAQs:
            response.message(FAQs[incoming_msg])
        else:
            response.message(
                "Hi! Welcome to StreamX customer support. Reply with 'subscription', 'technical', or 'refund' to get relevant FAQs."
            )

        # Send response back to Twilio
        return str(response)

    except Exception as e:
        # Handle unexpected errors and respond appropriately
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong. Please try again later."}), 500

# Function to send proactive messages (for admins)
def send_whatsapp_message(to, body):
    """
    Send a proactive WhatsApp message to a customer.
    Args:
        to (str): Receiver's WhatsApp number in the format 'whatsapp:+14155238886'.
        body (str): Message content.
    Returns:
        dict: Response from Twilio API.
    """
    try:
        message = twilio_client.messages.create(
            from_=WHATSAPP_NUMBER,  # Your Twilio WhatsApp number
            body=body,  # Message content
            to=to,  # Receiver's number
        )
        return {"status": "success", "message_sid": message.sid}
    except Exception as e:
        print(f"Error sending message: {e}")
        return {"status": "error", "error": str(e)}

# Main entry point
if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
1. Before running the code, make sure to set up Twilio WhatsApp integration and configure the necessary environment variables (`WHATSAPP_NUMBER`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`).
2. Install dependencies using `pip install flask twilio`.
3. Set up the `/whatsapp` endpoint as the webhook in Twilio for incoming WhatsApp messages.
4. This code is designed for production use with error handling and extensibility in mind.
