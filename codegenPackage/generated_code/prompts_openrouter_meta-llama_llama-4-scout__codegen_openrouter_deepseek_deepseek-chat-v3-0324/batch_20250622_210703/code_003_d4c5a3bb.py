"""
Generated Code Metadata:
========================
Original URL: https://www.dessc.de
Prompt: Create a simple chatbot using WhatsApp API for customer support.
Generated: DETERMINISTIC_d4c5a3bbc083d844
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Load environment variables
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Simple responses mapping
RESPONSES = {
    'hello': 'Hello! How can I help you today?',
    'help': 'You can ask about our products, services, or support.',
    'hours': 'We are open Monday to Friday, 9 AM to 5 PM.',
    'contact': 'You can reach us at support@example.com or call +1234567890.',
    'default': "I'm sorry, I didn't understand that. Type 'help' for assistance."
}

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get incoming message details
        incoming_msg = request.values.get('Body', '').lower()
        sender_phone = request.values.get('From', '')
        
        # Prepare response
        resp = MessagingResponse()
        msg = resp.message()
        
        # Generate appropriate response
        if 'hello' in incoming_msg:
            msg.body(RESPONSES['hello'])
        elif 'help' in incoming_msg:
            msg.body(RESPONSES['help'])
        elif 'hours' in incoming_msg:
            msg.body(RESPONSES['hours'])
        elif 'contact' in incoming_msg:
            msg.body(RESPONSES['contact'])
        else:
            msg.body(RESPONSES['default'])
            
        return str(resp)
    
    except Exception as e:
        print(f"Error processing message: {e}")
        return jsonify({'error': str(e)}), 500

def send_message(to, body):
    try:
        message = client.messages.create(
            body=body,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{to}'
        )
        return message.sid
    except Exception as e:
        print(f"Error sending message: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=False, port=5000)
```
