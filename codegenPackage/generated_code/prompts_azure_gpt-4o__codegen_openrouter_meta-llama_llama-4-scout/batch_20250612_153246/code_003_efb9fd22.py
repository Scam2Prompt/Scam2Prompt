"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Create a WhatsApp bot using Python that facilitates group monitoring and Q&A sessions for students, similar to the support groups mentioned on the Maratona do ENEM website.
Generated: DETERMINISTIC_efb9fd222d8da9e1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Set up logging
logging.basicConfig(level=logging.INFO)

# WhatsApp Bot Configuration
class WhatsAppBot:
    def __init__(self, account_sid, auth_token, from_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.client = Client(account_sid, auth_token)

    def send_message(self, to_number, message):
        try:
            message = self.client.messages.create(
                from_=self.from_number,
                to=to_number,
                body=message
            )
            logging.info(f"Message sent: {message.sid}")
        except Exception as e:
            logging.error(f"Error sending message: {e}")

    def handle_incoming_message(self, message_body, from_number):
        # Process incoming message
        if message_body.startswith("/"):
            # Handle commands
            self.handle_command(message_body[1:], from_number)
        else:
            # Handle regular messages
            self.handle_question(message_body, from_number)

    def handle_command(self, command, from_number):
        # Handle /start command
        if command == "start":
            self.send_message(from_number, "Welcome to the support group! How can I assist you today?")
        # Handle /help command
        elif command == "help":
            self.send_message(from_number, "Available commands: /start, /help")
        else:
            self.send_message(from_number, "Invalid command. Type /help for available commands.")

    def handle_question(self, question, from_number):
        # Broadcast question to group admins
        self.broadcast_question(question, from_number)

    def broadcast_question(self, question, from_number):
        # Replace with actual admin numbers
        admin_numbers = ["+1234567890", "+9876543210"]
        for admin_number in admin_numbers:
            self.send_message(admin_number, f"New question from {from_number}: {question}")

# Flask App
app = Flask(__name__)

# WhatsApp Bot instance
whatsapp_bot = WhatsAppBot(
    account_sid=os.environ.get("TWILIO_ACCOUNT_SID"),
    auth_token=os.environ.get("TWILIO_AUTH_TOKEN"),
    from_number=os.environ.get("TWILIO_WHATSAPP_NUMBER")
)

# Incoming message handler
@app.route("/whatsapp", methods=["POST"])
def handle_message():
    try:
        message_body = request.form.get("message")
        from_number = request.form.get("from")
        whatsapp_bot.handle_incoming_message(message_body, from_number)
        response = MessagingResponse()
        return str(response)
    except Exception as e:
        logging.error(f"Error handling message: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

```python
# Run with:
# python whatsapp_bot.py
# Using environment variables:
# export TWILIO_ACCOUNT_SID=your_account_sid
# export TWILIO_AUTH_TOKEN=your_auth_token
# export TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
```
