"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Write a code snippet to automate WhatsApp-based sales for a hardware store, inspired by the "Manual de Ventas por Whatsapp para el negocio Ferretero" from Aula Ferretera.
Generated: DETERMINISTIC_300c69a1a258491b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for you. However, I need to clarify that I'll be using Python as the programming language, and I'll be utilizing the Twilio library to interact with the WhatsApp API.

```python
# Import required libraries
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# WhatsApp API credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Define a dictionary to store products
products = {
    '1': {'name': 'Drill', 'price': 50.0},
    '2': {'name': 'Saw', 'price': 30.0},
    '3': {'name': 'Hammer', 'price': 20.0},
}

# Define a function to send a welcome message
def send_welcome_message(to_number):
    """Send a welcome message to the customer"""
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        to=to_number,
        body='Hello! Welcome to our hardware store. How can we help you today?'
    )

# Define a function to send product catalog
def send_product_catalog(to_number):
    """Send the product catalog to the customer"""
    catalog_message = 'Our product catalog:\n'
    for product_id, product in products.items():
        catalog_message += f'{product_id}. {product["name"]}: ${product["price"]:.2f}\n'
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        to=to_number,
        body=catalog_message
    )

# Define a function to handle customer inquiries
def handle_inquiry(to_number, message):
    """Handle customer inquiries"""
    if message.lower() == 'catalog':
        send_product_catalog(to_number)
    elif message.lower() == 'hello':
        send_welcome_message(to_number)
    else:
        try:
            product_id = message.split()[0]
            if product_id in products:
                product = products[product_id]
                message = client.messages.create(
                    from_=TWILIO_WHATSAPP_NUMBER,
                    to=to_number,
                    body=f'You are interested in {product["name"]}. The price is ${product["price"]:.2f}. Would you like to proceed with the purchase?'
                )
            else:
                message = client.messages.create(
                    from_=TWILIO_WHATSAPP_NUMBER,
                    to=to_number,
                    body='Sorry, we couldn\'t find the product you are looking for.'
                )
        except Exception as e:
            message = client.messages.create(
                from_=TWILIO_WHATSAPP_NUMBER,
                to=to_number,
                body='Sorry, we didn\'t understand your message.'
            )

# Define a function to handle incoming messages
def handle_incoming_messages():
    """Handle incoming messages"""
    messages = client.messages.list(
        from_=TWILIO_WHATSAPP_NUMBER,
        message_type='inbound'
    )
    for message in messages:
        handle_inquiry(message.from_, message.body)

# Main function
def main():
    handle_incoming_messages()

if __name__ == '__main__':
    main()
```

**.env file**
```bash
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
```
