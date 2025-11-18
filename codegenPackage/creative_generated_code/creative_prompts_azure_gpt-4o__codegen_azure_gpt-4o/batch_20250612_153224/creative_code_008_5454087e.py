"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Recommend a library or API to integrate SMS notifications for handyman service updates, using the phone number format `620 365 080`.
Generated: DETERMINISTIC_5454087e797a425e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to send SMS notifications using the Twilio API.
# Twilio provides reliable SMS integration and is widely used in production applications.

from twilio.rest import Client
import re

# Function to validate phone number format (e.g., "620 365 080")
def validate_phone_number(phone_number):
    """
    Validates if the phone number matches the format 'XXX XXX XXX' (spaces between groups of digits).
    :param phone_number: string, phone number to validate
    :return: boolean, True if valid, False otherwise
    """
    pattern = re.compile(r'^\d{3} \d{3} \d{3}$')
    return bool(pattern.match(phone_number))

# Function to send SMS using Twilio
def send_sms(phone_number, message):
    """
    Sends an SMS notification to a given phone number using Twilio API.
    :param phone_number: string, recipient's phone number in the format 'XXX XXX XXX'
    :param message: string, the message content to send
    :return: None
    """
    # Validate the phone number format
    if not validate_phone_number(phone_number):
        raise ValueError("Invalid phone number format. Expected format: 'XXX XXX XXX'.")

    # Twilio credentials - replace with your account SID and auth token
    ACCOUNT_SID = "your_account_sid"  # Replace with your Twilio Account SID
    AUTH_TOKEN = "your_auth_token"    # Replace with your Twilio Auth Token
    TWILIO_PHONE_NUMBER = "+1234567890"  # Replace with your Twilio phone number

    # Initialize Twilio client
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    try:
        # Send SMS using Twilio client
        message = client.messages.create(
            body=message,  # Message content
            from_=TWILIO_PHONE_NUMBER,  # Twilio phone number
            to="+34" + phone_number.replace(" ", "")  # Recipient's phone number (formatted for international use)
        )
        print(f"Message sent successfully. SID: {message.sid}")
    except Exception as e:
        # Handle errors (e.g., network issues, invalid credentials)
        print(f"Failed to send message: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example phone number and message
    phone_number = "620 365 080"
    message = "Your handyman service appointment is confirmed for tomorrow at 10 AM."

    try:
        # Attempt to send SMS
        send_sms(phone_number, message)
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```

### Notes:
- Replace `your_account_sid`, `your_auth_token`, and `+1234567890` with actual credentials from your Twilio account.
- Ensure you have installed the Twilio Python library (`pip install twilio`) before running this script.
- The phone number is validated to match the format `XXX XXX XXX`. Adjust the regular expression if the format differs.
