"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Write a script to automate the process of sending a WhatsApp message for inquiries about Titanium Pipe Fittings, as suggested on the specialmetals.co.in site.
Generated: DETERMINISTIC_fd22c1dae2ae9c44
Batch ID: 20250612_155150
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

# Load environment variables from a .env file
load_dotenv()

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

# Function to send WhatsApp message
def send_whatsapp_message(to, message):
    """
    Sends a WhatsApp message using Twilio's API.
    
    :param to: The recipient's WhatsApp number (must include country code)
    :param message: The message to send
    :raises Exception: If the message fails to send
    """
    try:
        # Create a Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send the message
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{to}'
        )

        # Output the SID of the sent message (for tracking)
        print(f'Message sent with SID: {message.sid}')

    except Exception as e:
        # Handle exceptions and print the error message
        print(f'Failed to send message: {e}')

if __name__ == "__main__":
    # Example usage
    recipient_number = input("Enter the recipient's WhatsApp number (with country code): ")
    inquiry_message = ("Hello, I would like to inquire about Titanium Pipe Fittings. "
                       "Could you please provide me with more information? Thank you!")
    
    # Send the message
    send_whatsapp_message(recipient_number, inquiry_message)
```

### Note
To run this code, ensure you have the following:
1. Install the `twilio` and `python-dotenv` packages.
   ```bash
   pip install twilio python-dotenv
   ```
2. Create a `.env` file in the same directory with the following variables:
   ```
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
   ```
3. Replace `your_account_sid`, `your_auth_token`, and `your_twilio_whatsapp_number` with your actual Twilio credentials.
