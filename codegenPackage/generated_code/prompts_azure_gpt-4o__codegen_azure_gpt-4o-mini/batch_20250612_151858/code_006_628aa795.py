"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Develop a chatbot using Python that integrates with WhatsApp to assist customers in browsing products from "Jurunense Home Center" and placing orders.
Generated: DETERMINISTIC_628aa7954534c8e2
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Load environment variables for Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Sample product catalog
PRODUCT_CATALOG = {
    "1": {"name": "Hammer", "price": 10.99},
    "2": {"name": "Screwdriver", "price": 5.49},
    "3": {"name": "Drill", "price": 99.99},
}

def get_product_list():
    """Generate a formatted string of available products."""
    product_list = "Available products:\n"
    for product_id, product in PRODUCT_CATALOG.items():
        product_list += f"{product_id}: {product['name']} - ${product['price']}\n"
    return product_list

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    """Handle incoming messages from WhatsApp."""
    try:
        # Get the incoming message
        incoming_msg = request.values.get('Body', '').strip()
        response = MessagingResponse()

        if incoming_msg.lower() == 'hi':
            response.message("Hello! Welcome to Jurunense Home Center. Type 'products' to see our catalog.")
        elif incoming_msg.lower() == 'products':
            product_list = get_product_list()
            response.message(product_list)
        elif incoming_msg.startswith('order'):
            product_id = incoming_msg.split(' ')[1]
            if product_id in PRODUCT_CATALOG:
                product = PRODUCT_CATALOG[product_id]
                response.message(f"Order placed for {product['name']} at ${product['price']}. Thank you!")
            else:
                response.message("Sorry, that product ID does not exist. Please check the product list.")
        else:
            response.message("Sorry, I didn't understand that. Type 'products' to see our catalog.")

        return str(response)

    except Exception as e:
        # Log the error and return a generic error message
        print(f"Error processing message: {e}")
        return jsonify({"status": "error", "message": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Environment Setup
Make sure to set the following environment variables before running the application:
- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `TWILIO_PHONE_NUMBER`

### Requirements
Install the required packages using pip:
```bash
pip install Flask twilio
```

### Running the Application
Run the application with:
```bash
python app.py
```

### Note
This code is a basic implementation and should be expanded with additional features such as user authentication, database integration for order management, and more robust error handling for production use.
