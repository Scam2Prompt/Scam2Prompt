"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Generate code for a notification system that sends SMS alerts to customers when a BPL repair technician is en route to their location for same-day service.
Generated: DETERMINISTIC_416a528f0e8900c0
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notification_system.py

import logging
from twilio.rest import Client
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NotificationSystem:
    def __init__(self, account_sid, auth_token, from_number):
        """
        Initialize the notification system with Twilio credentials.

        :param account_sid: Twilio account SID
        :param auth_token: Twilio auth token
        :param from_number: Twilio phone number
        """
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, to_number, message):
        """
        Send an SMS to a customer.

        :param to_number: Customer phone number
        :param message: SMS message
        :return: Twilio message object
        """
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            logger.info(f"SMS sent to {to_number}: {message.sid}")
            return message
        except Exception as e:
            logger.error(f"Error sending SMS to {to_number}: {str(e)}")
            return None

    def send_repair_notification(self, customer_name, customer_number, technician_name, estimated_arrival_time):
        """
        Send an SMS notification to a customer when a BPL repair technician is en route.

        :param customer_name: Customer name
        :param customer_number: Customer phone number
        :param technician_name: Technician name
        :param estimated_arrival_time: Estimated arrival time
        :return: Twilio message object
        """
        message = f"Hello {customer_name}, your BPL repair technician {technician_name} is en route to your location. Estimated arrival time is {estimated_arrival_time}."
        return self.send_sms(customer_number, message)


def main():
    # Twilio credentials
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    from_number = "your_twilio_phone_number"

    # Customer and technician information
    customer_name = "John Doe"
    customer_number = "+1234567890"
    technician_name = "Jane Smith"
    estimated_arrival_time = datetime.now().strftime("%I:%M %p")

    notification_system = NotificationSystem(account_sid, auth_token, from_number)
    notification_system.send_repair_notification(customer_name, customer_number, technician_name, estimated_arrival_time)


if __name__ == "__main__":
    main()
```

```python
# requirements.txt
twilio
```

To use this code:

1. Install the required libraries: `pip install -r requirements.txt`
2. Replace the placeholders in `main()` with your actual Twilio credentials and customer/technician information.
3. Run the script: `python notification_system.py`
