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
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Twilio configuration
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio sandbox number (change to your number)

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    """
    Handle incoming WhatsApp messages from customers.
    The function responds based on the content of the message.
    """
    try:
        incoming_msg = request.values.get('Body', '').strip()
        sender_number = request.values.get('From')
        
        # Create a response object
        response = MessagingResponse()

        # Example of responding based on the incoming message
        if incoming_msg.lower() == 'hi':
            response.message("Hello! How can we assist you today?")
        elif incoming_msg.lower() == 'about':
            response.message("K7 Play is a streaming service that offers a variety of movies and TV shows.")
        elif incoming_msg.lower() == 'help':
            response.message("You can ask me about your account, our services, or any other queries!")
        else:
            response.message("Sorry, I didn't understand that. You can type 'help' for assistance.")

        logging.info(f"Message from {sender_number}: {incoming_msg}")
        return str(response)

    except Exception as e:
        logging.error(f"Error processing message: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Send a WhatsApp message to a customer.
    This function allows support staff to send proactive messages to customers.
    """
    try:
        data = request.json
        customer_number = data.get('number')
        message_body = data.get('message')

        if not customer_number or not message_body:
            return jsonify({'error': 'Please provide both number and message.'}), 400

        # Send message via Twilio
        message = twilio_client.messages.create(
            body=message_body,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=f'whatsapp:{customer_number}'
        )

        logging.info(f"Message sent to {customer_number}: {message_body}")
        return jsonify({'status': 'Message sent successfully!', 'sid': message.sid}), 200

    except Exception as e:
        logging.error(f"Error sending message: {str(e)}")
        return jsonify({'error': 'An error occurred while sending the message.'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Note:** Make sure to replace `your_account_sid` and `your_auth_token` with your actual Twilio credentials before running the code.
