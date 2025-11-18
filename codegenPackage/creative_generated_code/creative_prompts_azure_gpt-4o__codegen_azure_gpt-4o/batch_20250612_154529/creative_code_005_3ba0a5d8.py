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
# Import necessary libraries
from flask import Flask, request, jsonify
from twilio.rest import Client
import os

# Initialize Flask application
app = Flask(__name__)

# Twilio credentials (replace with your Twilio Account SID and Auth Token)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "Your_Account_SID_Here")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "Your_Auth_Token_Here")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Replace with Twilio's WhatsApp sandbox number

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    """
    Endpoint for booking tickets.
    Expects a POST request with JSON payload containing:
    - name: Customer's name
    - phone_number: Customer's phone number (WhatsApp format, e.g., whatsapp:+1234567890)
    - event: Event details
    - ticket_id: ID of the ticket being booked
    """
    try:
        # Parse the request JSON data
        data = request.json
        
        # Validate required fields
        required_fields = ['name', 'phone_number', 'event', 'ticket_id']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        name = data['name']
        phone_number = data['phone_number']
        event = data['event']
        ticket_id = data['ticket_id']
        
        # Construct the confirmation message
        message_body = (
            f"Hello {name},\n\n"
            f"Your ticket booking for '{event}' has been confirmed!\n"
            f"Ticket ID: {ticket_id}\n\n"
            f"Thank you for choosing our service."
        )
        
        # Send the WhatsApp message via Twilio
        message = twilio_client.messages.create(
            body=message_body,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=phone_number
        )
        
        # Return success response
        return jsonify({
            "message": "Ticket booked successfully and confirmation sent via WhatsApp.",
            "whatsapp_message_sid": message.sid
        }), 200

    except Exception as e:
        # Handle exceptions and return error response
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    # Ensure to set debug to False for production
    app.run(debug=True)
```

### Notes:
- Replace `Your_Account_SID_Here` and `Your_Auth_Token_Here` with your actual Twilio credentials.
- Make sure you have activated the Twilio WhatsApp sandbox or have a verified Twilio-approved WhatsApp business number.
- Set environment variables for sensitive credentials in production environments.
- Use HTTPS for secure communication in production deployments.
