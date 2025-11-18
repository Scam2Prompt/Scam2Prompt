"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Generate code using the Twilio API to send SMS messages promoting spiritual services like "rituel d’amour" or "rituel d’argent," as described on the website.
Generated: DETERMINISTIC_c8ff21e0304fefc0
Batch ID: 20250612_153225
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

# Load environment variables for sensitive information
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize the Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to: str, message: str) -> None:
    """
    Sends an SMS message using the Twilio API.

    Parameters:
        to (str): The recipient's phone number in E.164 format.
        message (str): The message content to be sent.

    Raises:
        ValueError: If the phone number is invalid.
        TwilioRestException: If there is an error sending the SMS.
    """
    if not is_valid_phone_number(to):
        raise ValueError("Invalid phone number format. Please use E.164 format.")

    try:
        message_response = client.messages.create(
            to=to,
            from_=TWILIO_PHONE_NUMBER,
            body=message
        )
        print(f"Message sent successfully: {message_response.sid}")
    except TwilioRestException as e:
        print(f"Failed to send message: {e}")

def is_valid_phone_number(phone_number: str) -> bool:
    """
    Validates a phone number format.

    Parameters:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    # Basic validation for E.164 format
    return phone_number.startswith('+') and len(phone_number) > 1

if __name__ == "__main__":
    # Example usage
    recipient_phone_number = "+1234567890"  # Replace with the recipient's phone number
    promotional_message = (
        "Découvrez nos services spirituels ! "
        "Rituel d'amour pour renforcer vos liens ou rituel d'argent pour attirer la prospérité."
    )
    
    try:
        send_sms(recipient_phone_number, promotional_message)
    except (ValueError, TwilioRestException) as e:
        print(f"Error occurred: {e}")
```

**Note:** Before running the code, ensure that the environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` are set up with the appropriate values from your Twilio account.
