"""
Generated Code Metadata:
========================
Original URL: https://www.betterbooking.pk
Prompt: Create a Python script that uses the Twilio API to send WhatsApp messages to Better Booking's contact number for travel inquiries.
Generated: DETERMINISTIC_fe506af3002c51d1
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from twilio.rest import Client

# Define constants for Twilio API credentials and Better Booking's contact number
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.environ.get('TWILIO_WHATSAPP_NUMBER')
BETTER_BOOKING_WHATSAPP_NUMBER = os.environ.get('BETTER_BOOKING_WHATSAPP_NUMBER')

def send_travel_inquiry(message):
    """
    Send a WhatsApp message to Better Booking's contact number for travel inquiries.

    Args:
        message (str): The message to be sent.

    Returns:
        bool: True if the message is sent successfully, False otherwise.
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send WhatsApp message
        message = client.messages.create(
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{BETTER_BOOKING_WHATSAPP_NUMBER}',
            body=message
        )

        # Check if the message is sent successfully
        if message.sid:
            return True
        else:
            return False

    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"An error occurred: {e}")
        return False

def main():
    # Example usage
    message = "Hello, I'm inquiring about travel options."
    if send_travel_inquiry(message):
        print("Message sent successfully.")
    else:
        print("Failed to send message.")

if __name__ == "__main__":
    main()
```
