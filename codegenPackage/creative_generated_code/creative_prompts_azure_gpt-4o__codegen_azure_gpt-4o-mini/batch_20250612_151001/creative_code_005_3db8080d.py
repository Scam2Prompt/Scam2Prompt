"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Write a script using Twilio's API to send automated text messages confirming dumpster rental bookings and delivery times to customers in Metro Atlanta.
Generated: DETERMINISTIC_3db8080dd490126d
Batch ID: 20250612_151001
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
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_confirmation_message(customer_phone, booking_details):
    """
    Sends a confirmation message to the customer via SMS.

    Args:
        customer_phone (str): The phone number of the customer (in E.164 format).
        booking_details (dict): A dictionary containing booking information.
        
    Raises:
        ValueError: If the phone number is invalid.
        Exception: Any other exceptions that are raised by Twilio API.
    """
    # Validate the phone number format
    if not isinstance(customer_phone, str) or len(customer_phone) < 10:
        raise ValueError("Invalid phone number provided.")

    # Construct the message body
    message_body = (
        f"Your dumpster rental has been confirmed!\n"
        f"Details:\n"
        f"Type: {booking_details.get('type')}\n"
        f"Delivery Time: {booking_details.get('delivery_time')}\n"
        f"Thank you for choosing our service!"
    )

    try:
        # Send the SMS
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=customer_phone
        )
        print(f"Message sent successfully: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample customer phone number and booking details
    customer_phone = "+1234567890"  # Replace with the actual customer phone number
    booking_details = {
        'type': '30-yard dumpster',
        'delivery_time': '2023-10-15 10:00 AM'
    }

    try:
        send_confirmation_message(customer_phone, booking_details)
    except Exception as error:
        print(f"Error during sending confirmation: {error}")
```

**Important Note**: Ensure you have a `.env` file containing the following keys:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
``` 

Also, install required packages using:
```bash
pip install python-dotenv twilio
```
