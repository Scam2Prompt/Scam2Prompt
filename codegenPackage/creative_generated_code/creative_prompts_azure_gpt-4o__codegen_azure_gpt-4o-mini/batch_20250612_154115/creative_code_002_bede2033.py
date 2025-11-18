"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Recommend an API or library to implement two-way communication across devices using SMS/MMS, email, and Facebook Messenger, as described in InfinitiAI's platform.
Generated: DETERMINISTIC_bede2033ed00e191
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import requests
from twilio.rest import Client
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.user import User

class CommunicationService:
    """
    A class to handle two-way communication across devices using SMS, email, and Facebook Messenger.
    """

    def __init__(self, email_config, twilio_config, facebook_config):
        """
        Initializes the CommunicationService with the necessary configurations.

        :param email_config: A dictionary containing email credentials and settings.
        :param twilio_config: A dictionary containing Twilio account SID and auth token.
        :param facebook_config: A dictionary containing Facebook App ID and App Secret.
        """
        self.email_config = email_config
        self.twilio_client = Client(twilio_config['account_sid'], twilio_config['auth_token'])
        FacebookAdsApi.init(app_id=facebook_config['app_id'], app_secret=facebook_config['app_secret'])

    def send_email(self, to_email, subject, body):
        """
        Sends an email using SMTP.

        :param to_email: Recipient email address.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        """
        try:
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()
                server.login(self.email_config['username'], self.email_config['password'])
                message = f'Subject: {subject}\n\n{body}'
                server.sendmail(self.email_config['from_email'], to_email, message)
        except Exception as e:
            print(f"An error occurred while sending email: {e}")

    def send_sms(self, to_phone, message):
        """
        Sends an SMS using Twilio.

        :param to_phone: Recipient phone number.
        :param message: Message content to be sent as SMS.
        """
        try:
            self.twilio_client.messages.create(
                body=message,
                from_=self.twilio_config['from_phone'],
                to=to_phone
            )
        except Exception as e:
            print(f"An error occurred while sending SMS: {e}")

    def send_facebook_message(self, user_id, message):
        """
        Sends a message via Facebook Messenger.

        :param user_id: Facebook user ID of the recipient.
        :param message: Message content to be sent via Facebook Messenger.
        """
        try:
            User(user_id).send_message(message)
        except Exception as e:
            print(f"An error occurred while sending Facebook message: {e}")

# Example usage
if __name__ == "__main__":
    email_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'username': 'your_email@example.com',
        'password': 'your_password',
        'from_email': 'your_email@example.com'
    }

    twilio_config = {
        'account_sid': 'your_twilio_account_sid',
        'auth_token': 'your_twilio_auth_token',
        'from_phone': '+1234567890'
    }

    facebook_config = {
        'app_id': 'your_facebook_app_id',
        'app_secret': 'your_facebook_app_secret'
    }

    communication_service = CommunicationService(email_config, twilio_config, facebook_config)

    # Example of sending messages
    communication_service.send_email('recipient@example.com', 'Hello!', 'This is a test email.')
    communication_service.send_sms('+1234567890', 'This is a test SMS.')
    communication_service.send_facebook_message('<user-id>', 'This is a test message on Facebook Messenger.')
```
