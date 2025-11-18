"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalflightguide.com
Prompt: Develop a script that automates sending SMS notifications for flight updates, cancellations, or exclusive deals, adhering to TCPA compliance guidelines like those mentioned on globalflightguide.com.
Generated: DETERMINISTIC_e3ae8e627bd2c28d
Batch ID: 20250612_151412
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

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# SMS Notification Class
class SMSNotifier:
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_sms(self, to_number, message):
        """
        Sends an SMS message to the specified phone number.

        Parameters:
            to_number (str): The recipient's phone number.
            message (str): The message content to be sent.

        Raises:
            ValueError: If the phone number is invalid.
            Exception: For any other issues during sending SMS.
        """
        if not self._is_valid_phone_number(to_number):
            logger.error("Invalid phone number format.")
            raise ValueError("Invalid phone number format.")

        try:
            logger.info(f"Sending SMS to {to_number}.")
            message_response = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            logger.info(f"Message sent successfully: {message_response.sid}")
        except Exception as e:
            logger.error(f"Failed to send SMS: {e}")
            raise

    def _is_valid_phone_number(self, phone_number):
        """
        Validates the phone number format.

        Parameters:
            phone_number (str): The phone number to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Basic validation: Check if the phone number is a string of digits
        return isinstance(phone_number, str) and phone_number.isdigit() and len(phone_number) in [10, 11]

# Usage example
if __name__ == "__main__":
    try:
        notifier = SMSNotifier(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER)
        
        # Example usage: Sending flight update notification
        flight_update_message = "Flight AB123 has been updated. Check your email for details."
        notifier.send_sms("+12345678901", flight_update_message)  # Replace with the actual destination number

    except Exception as e:
        logger.error(f"Error in SMS notification process: {e}")
```
