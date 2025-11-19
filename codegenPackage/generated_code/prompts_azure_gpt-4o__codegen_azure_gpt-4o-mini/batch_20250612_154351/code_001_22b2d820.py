"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Generate a script to send SMS notifications for music lesson schedules, ensuring compliance with the privacy policy mentioned on the Московский Колледж Импровизационной Музыки site.
Generated: DETERMINISTIC_22b2d820bceb1092
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Function to send SMS notifications
def send_sms(to_phone_number, message):
    """
    Sends an SMS notification using Twilio's API.

    Parameters:
    to_phone_number (str): The recipient's phone number.
    message (str): The message to be sent.

    Raises:
    ValueError: If the phone number is invalid.
    Exception: If the SMS sending fails.
    """
    # Validate phone number format (basic validation)
    if not to_phone_number.startswith('+'):
        raise ValueError("Invalid phone number format. Must start with '+'.")

    # Create a Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        # Send the SMS
        message_response = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        print(f"Message sent successfully: {message_response.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Example recipient and message
    recipient_phone_number = "+1234567890"  # Replace with actual phone number
    lesson_schedule_message = "Your music lesson is scheduled for tomorrow at 3 PM."

    try:
        send_sms(recipient_phone_number, lesson_schedule_message)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to create a `.env` file in the same directory as this script with the following content:

```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```

Replace `your_account_sid`, `your_auth_token`, and `your_twilio_phone_number` with your actual Twilio credentials.
