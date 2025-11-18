"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Suggest an API or library for integrating WhatsApp support into an e-commerce website, allowing customers to inquire about products directly, as seen on Multan Designs.
Generated: DETERMINISTIC_621ab63ccb15f520
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to integrate WhatsApp support into an e-commerce website using 
the Twilio API for WhatsApp. Twilio provides a reliable way to send and receive WhatsApp messages.
Make sure you have a Twilio account and set up a WhatsApp sandbox for testing.

Replace placeholders with actual values from your Twilio account and set up your backend system
to handle inquiries from customers effectively.
"""

from twilio.rest import Client
from flask import Flask, request, jsonify

app = Flask(__name__)

# Twilio credentials (replace with your Twilio ACCOUNT SID and AUTH TOKEN)
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio's sandbox number or your registered number

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp():
    """
    Endpoint to send a WhatsApp message to a customer.
    The customer provides their phone number and inquiry text via POST request.
    """
    try:
        # Parse request data
        data = request.get_json()
        customer_number = data.get('customer_number')
        inquiry_message = data.get('message')

        # Validate required fields
        if not customer_number or not inquiry_message:
            return jsonify({"error": "customer_number and message are required"}), 400

        # Send WhatsApp message using Twilio
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,  # Sender (Twilio WhatsApp number)
            to=f"whatsapp:{customer_number}",  # Recipient (customer's number)
            body=inquiry_message  # Inquiry message
        )

        # Return success response
        return jsonify({"status": "Message sent successfully", "sid": message.sid}), 200

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

@app.route('/receive-whatsapp', methods=['POST'])
def receive_whatsapp():
    """
    Endpoint to receive WhatsApp messages from customers.
    This would be triggered by Twilio's webhook when a customer sends a message.
    """
    try:
        # Parse incoming Twilio webhook data
        sender_number = request.form.get('From')
        message_body = request.form.get('Body')

        if not sender_number or not message_body:
            return jsonify({"error": "Invalid webhook data"}), 400

        # Process the incoming message (e.g., log it, send to customer support, etc.)
        # For demonstration purposes, we return the received message.
        return jsonify({
            "status": "Message received successfully",
            "sender": sender_number,
            "message": message_body
        }), 200

    except Exception as e:
        # Handle webhook errors
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

### Steps to Implement:
1. Replace `your_account_sid` and `your_auth_token` with your Twilio credentials.
2. Configure Twilio to use `/receive-whatsapp` as the webhook for incoming messages.
3. Deploy this Flask application to a production server.
4. Test sending and receiving WhatsApp messages using Twilio's sandbox environment.

### Dependencies:
- Install Twilio library: `pip install twilio`
- Install Flask library: `pip install flask`

### Security Note:
Never hardcode sensitive credentials in your code. Use environment variables or a secrets manager for production applications.
