"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applestorebali.com
Prompt: Write a Python script to automate sending WhatsApp messages to the customer support number listed on the Apple Market Bali website (+6282285366666) using the Twilio API.
Generated: DETERMINISTIC_4f5fce644c4df87d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Constants
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')  # Your Twilio phone number
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')  # Your Twilio account SID
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')      # Your Twilio auth token
RECIPIENT_PHONE_NUMBER = '+6282285366666'                     # Customer support number

def send_whatsapp_message(message):
    """
    Sends a WhatsApp message to the specified recipient using the Twilio API.

    :param message: The message content to be sent
    :type message: str
    :raises ValueError: If the message is empty or exceeds character limit
    :raises TwilioRestException: If there is an issue with the Twilio API
    """
    # Validate input
    if not message:
        raise ValueError("Message cannot be empty.")
    if len(message) > 4096:
        raise ValueError("Message exceeds the 4096 character limit.")

    # Create a Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        # Send the message via WhatsApp
        message = client.messages.create(
            body=message,
            from_='whatsapp:' + TWILIO_PHONE_NUMBER,
            to='whatsapp:' + RECIPIENT_PHONE_NUMBER
        )
        print(f"Message sent successfully! SID: {message.sid}")
    except TwilioRestException as e:
        print(f"Failed to send message: {e}")

if __name__ == '__main__':
    # Example message to be sent
    message_content = "Hello! This is a test message from Apple Market Bali customer support."
    
    try:
        send_whatsapp_message(message_content)
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Environment Variables
Before running the script, ensure you have the following environment variables set:
- `TWILIO_PHONE_NUMBER`: Your Twilio WhatsApp-enabled phone number.
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio auth token.

You can set these variables in your terminal or use a `.env` file with the `dotenv` package to load them automatically.
