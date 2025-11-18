"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Recommend an API or library to integrate a car dealership website with WhatsApp for customer inquiries, as seen on Helfen Motors.
Generated: DETERMINISTIC_6bc4fab66b8aeee6
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready code that integrates a car dealership website with WhatsApp for customer inquiries using the Twilio API. Twilio is a reliable platform for WhatsApp messaging.

```python
# Import required libraries
from twilio.rest import Client
from flask import Flask, request, jsonify

# Flask application setup
app = Flask(__name__)

# Twilio API credentials (replace with your actual credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio's sandbox number for WhatsApp

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send_whatsapp', methods=['POST'])
def send_whatsapp_message():
    """
    Endpoint to send WhatsApp message to a customer.
    Expects JSON payload with 'customer_number' and 'message' fields.
    """
    try:
        # Parse JSON request data
        data = request.json
        customer_number = data.get('customer_number')  # Customer's WhatsApp number
        message = data.get('message')  # Message text
        
        # Validate input
        if not customer_number or not message:
            return jsonify({'error': 'Both customer_number and message fields are required'}), 400

        # Send WhatsApp message using Twilio
        message_response = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=f'whatsapp:{customer_number}',
            body=message
        )

        # Respond with success and message SID
        return jsonify({
            'success': True,
            'message_sid': message_response.sid
        }), 200

    except Exception as e:
        # Handle any errors during the message sending process
        return jsonify({'error': str(e)}), 500

@app.route('/webhook', methods=['POST'])
def receive_whatsapp_message():
    """
    Endpoint to receive incoming WhatsApp messages.
    This is the webhook URL that Twilio will call when a user sends a message.
    """
    try:
        # Parse Twilio webhook payload
        sender = request.form.get('From')  # Sender's WhatsApp number
        body = request.form.get('Body')  # Message content

        # Log the incoming message (in production, handle appropriately, e.g., store in DB)
        print(f"Received message from {sender}: {body}")

        # Respond to the webhook (optional)
        response_message = "Thank you for reaching out to our dealership! We will get back to you soon."
        
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=sender,
            body=response_message
        )

        return jsonify({'success': True}), 200

    except Exception as e:
        # Handle any errors during the webhook processing
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Features of this Code:
1. **Error Handling**: It gracefully handles missing fields and unexpected exceptions.
2. **Endpoints**:
   - `/send_whatsapp`: Allows the website to send WhatsApp messages to customers.
   - `/webhook`: Handles incoming WhatsApp messages from customers.
3. **Twilio Integration**: Demonstrates how to send and receive WhatsApp messages using Twilio's API.

Before running this code:
- Replace `your_account_sid` and `your_auth_token` with your actual Twilio credentials.
- Set up Twilio's WhatsApp sandbox or production account.
- Configure the `/webhook` endpoint URL in your Twilio console for receiving incoming messages.
