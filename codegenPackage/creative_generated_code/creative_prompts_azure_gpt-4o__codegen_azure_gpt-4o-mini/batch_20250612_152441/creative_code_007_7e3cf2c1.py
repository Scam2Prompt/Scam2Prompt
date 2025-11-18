"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.maxevent.pro
Prompt: Provide a step-by-step guide to integrate WhatsApp-based customer support for an IPTV service, similar to the support model described on MaxEvent's website.
Generated: DETERMINISTIC_7e3cf2c199ffcf76
Batch ID: 20250612_152441
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

# Initialize Flask application
app = Flask(__name__)

# Twilio configuration - replace with your actual credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming WhatsApp messages and respond."""
    try:
        # Get the incoming message
        incoming_msg = request.values.get('Body', '').strip()
        sender_number = request.values.get('From', '')

        # Create a response object
        response = MessagingResponse()

        # Process the incoming message and generate a response
        if incoming_msg.lower() == 'hi':
            response.message("Hello! How can we assist you today?")
        elif incoming_msg.lower() == 'help':
            response.message("Please describe your issue, and we will guide you.")
        elif "issue" in incoming_msg.lower():
            response.message("We are sorry to hear that you're having an issue. Please provide more details.")
        else:
            response.message("Thank you for reaching out! We will get back to you shortly.")

        return str(response)

    except Exception as e:
        # Log the error and return a generic response
        print(f"Error handling message from {sender_number}: {e}")
        return jsonify({"status": "error", "message": "An error occurred."}), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    """Send a WhatsApp message to a user."""
    try:
        data = request.json
        recipient_number = data.get('recipient_number')
        message = data.get('message')

        # Validate input
        if not recipient_number or not message:
            return jsonify({"status": "error", "message": "Recipient number and message are required."}), 400

        # Send message using Twilio
        client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{recipient_number}'
        )

        return jsonify({"status": "success", "message": "Message sent successfully."}), 200

    except Exception as e:
        # Log the error and return a generic response
        print(f"Error sending message: {e}")
        return jsonify({"status": "error", "message": "An error occurred while sending the message."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Instructions to Set Up:
1. **Install Necessary Packages**:
   ```bash
   pip install Flask twilio
   ```

2. **Set Environment Variables**:
   Set your Twilio account credentials in your environment:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE_NUMBER` (your Twilio WhatsApp-enabled number)

3. **Run the Flask Application**:
   Start the application by running:
   ```bash
   python app.py
   ```

4. **Configure Twilio Webhook**: 
   In your Twilio console, set the webhook URL to point to your server's endpoint, e.g., `http://<your-server-ip>:5000/webhook`.

5. **Testing**:
   Use any WhatsApp client to send messages to your configured Twilio number and see the responses. 

Make sure to handle sensitive credentials appropriately and ensure your server is secure in a production environment.
