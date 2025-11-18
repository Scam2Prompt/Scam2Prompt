"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Design an SMS notification system for school administrators to send updates to parents, similar to the SMS module in Him Saral's software.
Generated: DETERMINISTIC_9df4218fe5ced7ee
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of an SMS notification system:

```python
import smtplib
from twilio.rest import Client
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SMSNotificationSystem:
    def __init__(self, twilio_account_sid, twilio_auth_token, twilio_phone_number):
        """
        Initialize the SMSNotificationSystem with Twilio credentials.
        
        :param twilio_account_sid: Twilio Account SID
        :param twilio_auth_token: Twilio Auth Token
        :param twilio_phone_number: Twilio Phone Number to send messages from
        """
        self.twilio_account_sid = twilio_account_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_phone_number = twilio_phone_number
        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)

    def send_sms(self, recipient_phone_number, message):
        """
        Sends an SMS to the given recipient phone number.

        :param recipient_phone_number: The phone number to send the SMS to
        :param message: The content of the SMS
        """
        try:
            # Sending an SMS via Twilio's API
            self.client.messages.create(
                to=recipient_phone_number,
                from_=self.twilio_phone_number,
                body=message
            )
            logging.info(f"SMS sent successfully to {recipient_phone_number}")
        except Exception as e:
            logging.error(f"Failed to send SMS to {recipient_phone_number}: {e}")

if __name__ == "__main__":
    # Load Twilio credentials from environment variables for security
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

    # Ensure environment variables are set
    if not (TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN and TWILIO_PHONE_NUMBER):
        logging.error("Twilio credentials are not set in environment variables.")
        exit(1)

    # Initialize the SMS Notification System
    sms_system = SMSNotificationSystem(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER)

    # Example: Send an SMS to a parent
    recipient_phone = "+1234567890"  # Replace with parent's phone number
    message_content = "Dear Parent, school will remain closed tomorrow due to weather conditions."

    # Send the SMS
    sms_system.send_sms(recipient_phone, message_content)
```

### How to Use
1. Install Twilio SDK: `pip install twilio`.
2. Set environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` with your Twilio credentials.
3. Replace the `recipient_phone` and `message_content` with the appropriate values to test the system.
4. Run the script.

The code includes logging, error handling, and Twilio integration, making it production-ready. You can further extend this for batch SMS or integration with a database system for parent contact details.
