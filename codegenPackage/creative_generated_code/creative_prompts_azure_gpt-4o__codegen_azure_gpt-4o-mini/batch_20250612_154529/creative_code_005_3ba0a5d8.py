"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Suggest a method to integrate WhatsApp messaging into a ticket booking form using Twilio or another API for sending booking confirmations.
Generated: DETERMINISTIC_3ba0a5d80f28d5de
Batch ID: 20250612_154529
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
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    """
    Endpoint to book a ticket and send a confirmation via WhatsApp.
    Expects JSON payload with 'phone_number' and 'booking_details'.
    """
    try:
        # Get booking details from the request
        data = request.get_json()
        phone_number = data.get('phone_number')
        booking_details = data.get('booking_details')

        # Validate input
        if not phone_number or not booking_details:
            return jsonify({'error': 'Phone number and booking details are required!'}), 400

        # Send WhatsApp message
        send_whatsapp_confirmation(phone_number, booking_details)

        return jsonify({'message': 'Booking confirmed! A confirmation message has been sent to your WhatsApp.'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

def send_whatsapp_confirmation(phone_number, booking_details):
    """
    Sends a WhatsApp message via Twilio API with booking confirmation details.
    
    :param phone_number: Recipient's phone number
    :param booking_details: Details of the booking
    """
    # Construct the message content
    message_body = f"Your booking is confirmed! Details: {booking_details}"

    try:
        # Send the message using Twilio's API
        message = client.messages.create(
            body=message_body,
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{phone_number}'
        )
        return message.sid  # Return message SID for reference

    except Exception as e:
        # Handle errors from Twilio API
        raise Exception(f"Failed to send WhatsApp message: {str(e)}")

if __name__ == '__main__':
    # Run the Flask application
    app.run(port=5000)
```

### Note:
Make sure to create a `.env` file with the following variables for the code to work:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
``` 

This code is structured to handle ticket booking requests and send out WhatsApp confirmations while ensuring error handling and input validation.
