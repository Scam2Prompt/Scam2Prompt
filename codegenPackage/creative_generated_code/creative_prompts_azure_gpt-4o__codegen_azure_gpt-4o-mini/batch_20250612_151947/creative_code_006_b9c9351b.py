"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Develop a module for SMS notifications and delivery task automation for a business website, as described under the "Магазин приложений" section on https://ra-don.com.
Generated: DETERMINISTIC_b9c9351b5de7fd8b
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

class SMSNotificationService:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.from_phone = os.getenv('TWILIO_PHONE_NUMBER')

        # Initialize Twilio client
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, to_phone, message):
        """
        Send an SMS notification.

        :param to_phone: Recipient's phone number (string)
        :param message: Message to be sent (string)
        :raises ValueError: If the phone number or message is invalid
        :raises Exception: For any other exceptions from Twilio API
        """
        if not self.validate_phone_number(to_phone):
            raise ValueError("Invalid phone number format.")
        
        if not message:
            raise ValueError("Message cannot be empty.")

        try:
            # Send SMS using Twilio client
            message = self.client.messages.create(
                body=message,
                from_=self.from_phone,
                to=to_phone
            )
            logging.info(f"SMS sent successfully: SID {message.sid}")
            return message.sid
        except Exception as e:
            logging.error(f"Failed to send SMS: {e}")
            raise

    @staticmethod
    def validate_phone_number(phone):
        """
        Validate the phone number format.

        :param phone: Phone number (string)
        :return: True if valid; False otherwise
        """
        # Implement a simple validation logic (can be replaced with regex)
        return phone.startswith('+') and len(phone) > 10

# Usage example (should be invoked in a separate script or context)
if __name__ == "__main__":
    try:
        sms_service = SMSNotificationService()
        sms_sid = sms_service.send_sms("+1234567890", "Hello! This is a test message.")
        print(f"Message sent with SID: {sms_sid}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to create a `.env` file with the following variables:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```
