"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Create a chatbot integration using Python and Twilio that allows users to chat with customer service on WhatsApp, as described in the "Chatea con nosotros" feature of the Nueva Ciudad website.
Generated: DETERMINISTIC_7c8e562ae8b52a21
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Environment variable for Twilio credentials
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    """
    Respond to incoming WhatsApp messages and route them to customer service.

    Returns:
        str: Twilio's XML response to the incoming message
    """
    try:
        # Get the message from the incoming request
        incoming_msg = request.values.get('Body', '').strip()
        sender_number = request.values.get('From', '')

        # Log the incoming message
        logging.info(f"Received message from {sender_number}: {incoming_msg}")

        # Create a Twilio response object
        response = MessagingResponse()
        
        # Simple bot response logic
        if 'hello' in incoming_msg.lower():
            response.message("Hello! How can we assist you today?")
        elif 'help' in incoming_msg.lower():
            response.message("You can ask me about our services or any issues you're facing.")
        elif 'bye' in incoming_msg.lower():
            response.message("Goodbye! If you need further assistance, feel free to reach out again.")
        else:
            response.message("Sorry, I didn't understand that. Please try asking something else.")

        return str(response)
    
    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Requirements:
- Install Flask and Twilio's library with pip:
```bash
pip install Flask twilio
```

### Note:
- Ensure you set the environment variables `TWILIO_AUTH_TOKEN` and `TWILIO_ACCOUNT_SID` with your Twilio credentials before running the application.
