"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Generate code for a notification system that sends SMS alerts to customers when a BPL repair technician is en route to their location for same-day service.
Generated: DETERMINISTIC_416a528f0e8900c0
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from twilio.rest import Client
from datetime import datetime
import logging

# Configure logging for monitoring events and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationService:
    def __init__(self, twilio_sid, twilio_auth_token, twilio_phone_number):
        """
        Initialize the NotificationService with Twilio credentials.

        :param twilio_sid: Twilio account SID
        :param twilio_auth_token: Twilio auth token
        :param twilio_phone_number: The phone number from which you will send messages
        """
        self.twilio_sid = twilio_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_phone_number = twilio_phone_number
        self.client = Client(twilio_sid, twilio_auth_token)

    def send_sms(self, customer_phone, message):
        """
        Send an SMS notification to a customer.

        :param customer_phone: The phone number of the customer
        :param message: The message content to be sent
        """
        try:
            logging.info(f'Sending SMS to {customer_phone}')
            message = self.client.messages.create(
                body=message,
                from_=self.twilio_phone_number,
                to=customer_phone
            )
            logging.info(f'SMS sent successfully: {message.sid}')
        except Exception as e:
            logging.error(f'Failed to send SMS: {e}')

def notify_customer(customer_phone, technician_name, estimated_arrival_time):
    """
    Notify the customer that a technician is en route.

    :param customer_phone: The phone number of the customer
    :param technician_name: The name of the repair technician
    :param estimated_arrival_time: Estimated arrival time of the technician
    """
    twilio_sid = 'your_twilio_sid'  # Replace with your Twilio SID
    twilio_auth_token = 'your_twilio_auth_token'  # Replace with your Twilio Auth Token
    twilio_phone_number = 'your_twilio_phone_number'  # Replace with your Twilio Phone Number

    notification_service = NotificationService(twilio_sid, twilio_auth_token, twilio_phone_number)

    message = f"Hello! Technician {technician_name} is en route to your location and is expected to arrive at {estimated_arrival_time}."
    notification_service.send_sms(customer_phone, message)

if __name__ == "__main__":
    # Example usage
    customer_phone_number = '+1234567890'  # Customer's phone number
    technician_name = 'John Doe'  # Technician's name
    estimated_arrival = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current time as estimated arrival

    notify_customer(customer_phone_number, technician_name, estimated_arrival)
```

Make sure to replace the placeholders for Twilio SID, Auth Token, and Phone Number with your actual Twilio account details.
