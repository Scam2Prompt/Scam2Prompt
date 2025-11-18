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

# Set up constants for Twilio API and WhatsApp messaging
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')  # Twilio Account SID from environment variables
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')    # Twilio Auth Token from environment variables
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'      # Twilio's WhatsApp Sandbox number
BETTER_BOOKING_CONTACT = 'whatsapp:+12345678901'      # Replace with Better Booking's contact WhatsApp number

def send_whatsapp_message(message_body):
    """
    Sends a WhatsApp message using the Twilio API.

    Args:
        message_body (str): The message to be sent.

    Returns:
        str: The SID of the sent message, if successful.
    """
    try:
        # Initialize the Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send the WhatsApp message
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,  # Sender WhatsApp number
            body=message_body,            # Message content
            to=BETTER_BOOKING_CONTACT     # Recipient WhatsApp number
        )

        # Return the message SID (useful for logging or tracking)
        return message.sid

    except Exception as e:
        # Handle any errors that occur during API interaction
        print(f"Error sending WhatsApp message: {e}")
        return None

if __name__ == '__main__':
    # Example usage
    travel_inquiry_message = "Hello, Better Booking! I'm interested in travel packages. Please provide details."
    
    # Send message and print result
    message_sid = send_whatsapp_message(travel_inquiry_message)
    if message_sid:
        print(f"WhatsApp message sent successfully! Message SID: {message_sid}")
    else:
        print("Failed to send WhatsApp message.")
```

### Notes:
1. Make sure you replace `BETTER_BOOKING_CONTACT` with the actual WhatsApp number for Better Booking.
2. You will need to set up Twilio credentials (`TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`) as environment variables for security purposes.
3. Twilio's WhatsApp API requires prior approval and setup; ensure that both sender and recipient numbers are registered.
