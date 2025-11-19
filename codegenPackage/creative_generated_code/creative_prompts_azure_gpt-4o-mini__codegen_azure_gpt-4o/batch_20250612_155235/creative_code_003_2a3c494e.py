"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: Generate code to send a login code via SMS for a web application, inspired by the user login process on Pixels.
Generated: DETERMINISTIC_2a3c494ee2044180
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import smtplib
from twilio.rest import Client

def generate_login_code(length=6):
    """
    Generate a random numeric login code.

    Args:
        length (int): Length of the login code. Default is 6.

    Returns:
        str: A randomly generated login code.
    """
    return ''.join(random.choices(string.digits, k=length))

def send_sms_via_twilio(phone_number, message):
    """
    Send an SMS using Twilio API.

    Args:
        phone_number (str): Recipient's phone number in E.164 format.
        message (str): The message to send.

    Raises:
        Exception: If Twilio API call fails.
    """
    # Twilio credentials (replace with your actual credentials)
    TWILIO_ACCOUNT_SID = 'your_account_sid'
    TWILIO_AUTH_TOKEN = 'your_auth_token'
    TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send SMS
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
    except Exception as e:
        # Handle errors in sending SMS
        print(f"Failed to send SMS: {e}")
        raise

def send_login_code(phone_number):
    """
    Generate a login code and send it via SMS to the user.

    Args:
        phone_number (str): Recipient's phone number in E.164 format.
    """
    # Generate a random login code
    login_code = generate_login_code()

    # Create the message to send
    message = f"Your login code is: {login_code}"

    try:
        # Send the message via Twilio
        send_sms_via_twilio(phone_number, message)
        print("Login code sent successfully.")
    except Exception as e:
        print(f"Error sending login code: {e}")

if __name__ == "__main__":
    # Example usage
    # Replace with the recipient's phone number in E.164 format
    recipient_phone_number = "+1234567890"

    send_login_code(recipient_phone_number)
```

**NOTE**: 
- Replace `your_account_sid`, `your_auth_token`, and `your_twilio_phone_number` with your actual Twilio credentials.
- Ensure that the `phone_number` is in E.164 format (e.g., `+1234567890`).
- Install the Twilio Python library (`pip install twilio`) before running the code.
