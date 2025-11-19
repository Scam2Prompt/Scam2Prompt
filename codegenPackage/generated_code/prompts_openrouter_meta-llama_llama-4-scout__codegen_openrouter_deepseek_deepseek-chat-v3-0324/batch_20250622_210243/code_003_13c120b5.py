"""
Generated Code Metadata:
========================
Original URL: https://fetch-alliance.com
Prompt: "Explain how to integrate DeltaV with WhatsApp to create a service that allows users to book holidays through a single prompt, using Fetch.ai's platform."
Generated: DETERMINISTIC_13c120b514efb47d
Batch ID: 20250622_210243
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
from twilio.twiml.messaging_response import MessagingResponse
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.crypto import Entity
from fetchai.ledger.serialisation import transaction
import json

app = Flask(__name__)

# Configuration
WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FETCHAI_API_HOST = os.getenv('FETCHAI_API_HOST', '127.0.0.1')
FETCHAI_API_PORT = int(os.getenv('FETCHAI_API_PORT', 8000))
FETCHAI_PRIVATE_KEY = os.getenv('FETCHAI_PRIVATE_KEY')

# Initialize Fetch.ai ledger API
api = LedgerApi(FETCHAI_API_HOST, FETCHAI_API_PORT)

# Load entity from private key
entity = Entity.from_hex(FETCHAI_PRIVATE_KEY)

# Holiday booking smart contract address
CONTRACT_ADDRESS = "fetch1qy..."

def process_holiday_booking(destination, dates, num_people):
    """
    Process holiday booking through Fetch.ai smart contract
    """
    try:
        # Create transaction to interact with smart contract
        tx = transaction.Transaction(
            entity,
            api,
            contract_address=CONTRACT_ADDRESS,
            action="book_holiday",
            data={
                "destination": destination,
                "dates": dates,
                "num_people": num_people
            }
        )
        
        # Sign and submit transaction
        tx.sign(entity)
        tx.submit(api)
        
        return True, "Booking successful! You'll receive confirmation shortly."
    except Exception as e:
        return False, f"Booking failed: {str(e)}"

def parse_booking_request(message_body):
    """
    Parse natural language booking request into structured data
    """
    # This is a simplified parser - in production you'd use NLP
    parts = message_body.lower().split()
    
    try:
        destination = parts[parts.index('to') + 1] if 'to' in parts else None
        dates = parts[parts.index('on') + 1] if 'on' in parts else None
        people = parts[parts.index('for') + 1] if 'for' in parts else "1"
        
        if not destination or not dates:
            raise ValueError("Missing required information")
            
        return destination, dates, people
    except Exception as e:
        raise ValueError(f"Could not parse booking request: {str(e)}")

@app.route('/whatsapp-webhook', methods=['POST'])
def whatsapp_webhook():
    """
    Handle incoming WhatsApp messages
    """
    try:
        incoming_msg = request.values.get('Body', '').strip()
        sender = request.values.get('From', '')
        
        if not incoming_msg:
            raise ValueError("Empty message received")
            
        # Check if message is a booking request
        if 'book' in incoming_msg.lower() and 'holiday' in incoming_msg.lower():
            try:
                destination, dates, num_people = parse_booking_request(incoming_msg)
                success, message = process_holiday_booking(destination, dates, num_people)
            except ValueError as e:
                success, message = False, str(e)
        else:
            success, message = False, "Please send a message like: 'Book a holiday to Paris on 15/08/2022 for 2 people'"
        
        # Prepare response
        resp = MessagingResponse()
        resp.message(message)
        return str(resp)
        
    except Exception as e:
        error_resp = MessagingResponse()
        error_resp.message(f"An error occurred: {str(e)}")
        return str(error_resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
