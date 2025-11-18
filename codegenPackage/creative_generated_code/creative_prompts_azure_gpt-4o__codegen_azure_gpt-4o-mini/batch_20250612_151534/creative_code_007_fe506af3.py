"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.betterbooking.pk
Prompt: Create a Python script that uses the Twilio API to send WhatsApp messages to Better Booking's contact number for travel inquiries.
Generated: DETERMINISTIC_fe506af3002c51d1
Batch ID: 20250612_151534
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

# Load environment variables (ensure you have these set in your environment)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
BETTER_BOOKING_WHATSAPP_NUMBER = os.getenv('BETTER_BOOKING_WHATSAPP_NUMBER')

def send_whatsapp_message(to, message):
    """
    Sends a WhatsApp message using the Twilio API.

    Parameters:
        to (str): The WhatsApp phone number to send the message to.
        message (str): The content of the message to be sent.

    Raises:
        ValueError: If the message is empty or too long.
        TwilioRestException: If there is an issue with the Twilio API.
    """
    
    # Validate message content
    if not message:
        raise ValueError("Message content cannot be empty.")
    if len(message) > 1600:
        raise ValueError("Message content exceeds the maximum length of 1600 characters.")

    # Initialize Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        # Send the message
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{to}'
        )
        print(f"Message sent successfully! SID: {message.sid}")
    
    except TwilioRestException as e:
        print(f"Failed to send message: {e}")

if __name__ == "__main__":
    # Define the message content
    inquiry_message = "Hello, I would like to inquire about travel bookings. Please provide assistance."

    # Send the message to Better Booking's contact number
    try:
        send_whatsapp_message(BETTER_BOOKING_WHATSAPP_NUMBER, inquiry_message)
    except ValueError as ve:
        print(f"Error: {ve}")
```

Make sure to set the following environment variables before running the script:
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
- `TWILIO_WHATSAPP_NUMBER`: Your Twilio WhatsApp number (in the format `+14155238886`)
- `BETTER_BOOKING_WHATSAPP_NUMBER`: Better Booking's WhatsApp contact number (in the format `+1234567890`)
