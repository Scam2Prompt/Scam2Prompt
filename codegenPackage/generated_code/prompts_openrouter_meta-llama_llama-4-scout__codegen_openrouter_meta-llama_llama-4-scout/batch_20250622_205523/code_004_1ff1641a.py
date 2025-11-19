"""
Generated Code Metadata:
========================
Original URL: https://moraragora.com.br
Prompt: Develop a code snippet to send an email or WhatsApp notification to property owners or agents, similar to Morar Agora's contact form, using a service like Sendgrid or Twilio.
Generated: DETERMINISTIC_1ff1641a75a199c3
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Notification Service**
=======================

### Requirements

* Python 3.8+
* Sendgrid
* Twilio

### Installation

```bash
pip install sendgrid twilio
```

### Code

```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

class NotificationService:
    def __init__(self, sendgrid_api_key, twilio_account_sid, twilio_auth_token):
        """
        Initialize the notification service.

        :param sendgrid_api_key: Sendgrid API key
        :param twilio_account_sid: Twilio account SID
        :param twilio_auth_token: Twilio auth token
        """
        self.sendgrid_api_key = sendgrid_api_key
        self.twilio_account_sid = twilio_account_sid
        self.twilio_auth_token = twilio_auth_token

    def send_email(self, to_email, subject, message):
        """
        Send an email using Sendgrid.

        :param to_email: Recipient's email
        :param subject: Email subject
        :param message: Email message
        :return: None
        """
        try:
            sg = SendGridAPIClient(self.sendgrid_api_key)
            mail = Mail(
                from_email=os.environ.get('SENDGRID_FROM_EMAIL'),
                to_emails=to_email,
                subject=subject,
                plain_text_content=message
            )
            response = sg.send(mail)
            print(f"Email sent: {response.status_code}")
        except Exception as e:
            print(f"Error sending email: {e}")

    def send_whatsapp(self, to_phone, message):
        """
        Send a WhatsApp notification using Twilio.

        :param to_phone: Recipient's phone number
        :param message: WhatsApp message
        :return: None
        """
        try:
            client = Client(self.twilio_account_sid, self.twilio_auth_token)
            message = client.messages.create(
                from_=os.environ.get('TWILIO_FROM_PHONE'),
                to=to_phone,
                body=message
            )
            print(f"WhatsApp sent: {message.sid}")
        except Exception as e:
            print(f"Error sending WhatsApp: {e}")


def main():
    sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
    twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    notification_service = NotificationService(sendgrid_api_key, twilio_account_sid, twilio_auth_token)

    # Example usage
    to_email = "recipient@example.com"
    subject = "Test Email"
    message = "Hello, this is a test email."
    notification_service.send_email(to_email, subject, message)

    to_phone = "+1234567890"
    whatsapp_message = "Hello, this is a test WhatsApp message."
    notification_service.send_whatsapp(to_phone, whatsapp_message)


if __name__ == "__main__":
    main()
```

### Environment Variables

* `SENDGRID_API_KEY`: Sendgrid API key
* `SENDGRID_FROM_EMAIL`: Sendgrid from email
* `TWILIO_ACCOUNT_SID`: Twilio account SID
* `TWILIO_AUTH_TOKEN`: Twilio auth token
* `TWILIO_FROM_PHONE`: Twilio from phone number

### Usage

1. Set the environment variables.
2. Run the script using `python notification_service.py`.
