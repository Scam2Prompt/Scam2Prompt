"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://praiasdeminas.eng.br
Prompt: Write code to create a chatbot for consulting customers about pool construction and renovation, integrating WhatsApp messaging as described on the Praias de Minas website.
Generated: DETERMINISTIC_89bcfa9d9d44c5f5
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
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Load environment variables securely
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_WHATSAPP_NUMBER:
    raise EnvironmentError("Please set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_WHATSAPP_NUMBER environment variables.")

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Predefined messages for chatbot responses
RESPONSES = {
    "greeting": "Hello! Welcome to Praias de Minas Pool Consulting. How can I assist you today?",
    "construction": "We specialize in pool construction. Please share your location and any specific requirements.",
    "renovation": "We offer pool renovation services. Let us know your current pool's condition and your desired modifications.",
    "help": "I can help you with pool construction, renovation, and general inquiries. Type 'construction', 'renovation', or 'help' for more details.",
    "default": "I'm sorry, I didn't understand that. Please type 'help' for more options."
}

@app.route("/webhook", methods=["POST"])
def handle_whatsapp_message():
    """
    Handle incoming WhatsApp messages via Twilio webhook.
    """
    try:
        # Parse incoming message details
        incoming_message = request.form.get("Body", "").strip().lower()
        sender = request.form.get("From", "")

        # Create Twilio response object
        response = MessagingResponse()

        # Determine response based on user input
        if incoming_message in ["hi", "hello", "hey"]:
            response.message(RESPONSES["greeting"])
        elif "construction" in incoming_message:
            response.message(RESPONSES["construction"])
        elif "renovation" in incoming_message:
            response.message(RESPONSES["renovation"])
        elif "help" in incoming_message:
            response.message(RESPONSES["help"])
        else:
            response.message(RESPONSES["default"])

        return str(response)

    except Exception as e:
        # Log any errors and respond with a generic message
        print(f"Error handling message: {e}")
        response = MessagingResponse()
        response.message("An error occurred while processing your request. Please try again later.")
        return str(response), 500


@app.route("/send_message", methods=["POST"])
def send_whatsapp_message():
    """
    Send a WhatsApp message to a customer using Twilio.
    """
    try:
        data = request.json
        recipient = data.get("phone_number")  # The recipient's phone number
        message_body = data.get("message")   # The message content

        if not recipient or not message_body:
            return jsonify({"error": "phone_number and message are required"}), 400

        # Send message via Twilio
        message = twilio_client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{recipient}",
            body=message_body
        )

        return jsonify({"status": "success", "message_sid": message.sid}), 200

    except Exception as e:
        # Log any errors and return appropriate response
        print(f"Error sending message: {e}")
        return jsonify({"error": "Failed to send message"}), 500


# Run the Flask app
if __name__ == "__main__":
    # Ensure the server runs securely in production by setting host and port
    app.run(host="0.0.0.0", port=5000, debug=False)
```

### Notes:
- **Environment Variables:** Replace `os.getenv` calls with appropriate methods to load your Twilio credentials securely if not using environment variables.
- **Dependencies:** Ensure you install Flask and Twilio (`pip install flask twilio`) before running the code.
- **Security:** Use HTTPS for production deployments and secure sensitive data like API credentials.
