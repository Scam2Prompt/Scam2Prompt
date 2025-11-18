"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillahgems.com
Prompt: Write a Python script to send automated WhatsApp messages to customers using the contact information provided on the "Bismillah Gems" website.
Generated: DETERMINISTIC_519afe87d0ab2e06
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twilio Account SID and Auth Token
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to: str, message: str) -> None:
    """
    Sends a WhatsApp message to a specified number.

    Parameters:
    to (str): The recipient's WhatsApp number (must include 'whatsapp:' prefix).
    message (str): The message content to be sent.

    Raises:
    Exception: Raises an exception if the message could not be sent.
    """
    try:
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            body=message,
            to=to
        )
        print(f"Message sent to {to}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {to}: {str(e)}")

def main():
    """
    Main function to send messages to customers.
    Replace the following list with actual contact information from your source.
    """
    # Sample customer contacts (in a real scenario, this could be fetched from a database)
    customers = [
        {"name": "Customer A", "contact": "whatsapp:+1234567890"},
        {"name": "Customer B", "contact": "whatsapp:+0987654321"}
    ]
    
    # Sample message
    message_template = "Hello {name}, thank you for your interest in Bismillah Gems!"

    # Send messages to each customer
    for customer in customers:
        message = message_template.format(name=customer["name"])
        send_whatsapp_message(customer["contact"], message)

if __name__ == "__main__":
    main()
```

### .env File Example
```plaintext
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
```

### Requirements
Make sure to install the required packages:
```bash
pip install twilio python-dotenv
```

### Note
- Ensure that you replace the sample contacts with actual contacts obtained from the "Bismillah Gems" website.
- The message template can be customized as per your requirements.
- This script assumes you have valid Twilio account credentials and have set up WhatsApp messaging in your Twilio account.
