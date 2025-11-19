"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Provide a code example for implementing a multi-channel messaging system combining email, SMS, and Facebook custom audiences, as described in the Sales Studios Online System.
Generated: DETERMINISTIC_4dd10d778a7a432a
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from twilio.rest import Client as TwilioClient
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.user import User
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class MultiChannelMessagingSystem:
    def __init__(self, email_config, sms_config, fb_config):
        """
        Initialize the messaging system with configurations for email, SMS, and Facebook.
        
        :param email_config: Dictionary containing SMTP server details and credentials.
        :param sms_config: Dictionary containing Twilio account SID and auth token.
        :param fb_config: Dictionary containing Facebook app ID, app secret, and access token.
        """
        self.email_config = email_config
        self.sms_client = TwilioClient(sms_config['account_sid'], sms_config['auth_token'])
        FacebookAdsApi.init(fb_config['app_id'], fb_config['app_secret'], fb_config['access_token'])

    def send_email(self, to_email, subject, body):
        """
        Send an email using SMTP.
        
        :param to_email: Recipient's email address.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        """
        try:
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()
                server.login(self.email_config['username'], self.email_config['password'])
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail(self.email_config['username'], to_email, message)
                logging.info(f"Email sent to {to_email}")
        except Exception as e:
            logging.error(f"Failed to send email to {to_email}: {e}")

    def send_sms(self, to_phone, message):
        """
        Send an SMS using Twilio.
        
        :param to_phone: Recipient's phone number.
        :param message: Message content of the SMS.
        """
        try:
            self.sms_client.messages.create(
                body=message,
                from_=self.sms_config['from_phone'],
                to=to_phone
            )
            logging.info(f"SMS sent to {to_phone}")
        except Exception as e:
            logging.error(f"Failed to send SMS to {to_phone}: {e}")

    def create_facebook_audience(self, audience_name, user_ids):
        """
        Create a custom audience on Facebook.
        
        :param audience_name: Name of the custom audience.
        :param user_ids: List of user IDs to add to the audience.
        """
        try:
            account = AdAccount(fb_config['ad_account_id'])
            audience = CustomAudience(parent_id=account.get_id_assured())
            audience.update({
                CustomAudience.Field.name: audience_name,
                CustomAudience.Field.subtype: CustomAudience.Subtype.custom,
            })
            audience.remote_create()
            audience.add_users(user_ids)
            logging.info(f"Custom audience '{audience_name}' created with {len(user_ids)} users.")
        except Exception as e:
            logging.error(f"Failed to create Facebook audience '{audience_name}': {e}")

# Example usage
if __name__ == "__main__":
    email_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'username': 'your_email@example.com',
        'password': 'your_password'
    }

    sms_config = {
        'account_sid': 'your_twilio_account_sid',
        'auth_token': 'your_twilio_auth_token',
        'from_phone': '+1234567890'
    }

    fb_config = {
        'app_id': 'your_facebook_app_id',
        'app_secret': 'your_facebook_app_secret',
        'access_token': 'your_facebook_access_token',
        'ad_account_id': 'act_your_ad_account_id'
    }

    messaging_system = MultiChannelMessagingSystem(email_config, sms_config, fb_config)

    # Send an email
    messaging_system.send_email('recipient@example.com', 'Test Subject', 'This is a test email.')

    # Send an SMS
    messaging_system.send_sms('+0987654321', 'This is a test SMS.')

    # Create a Facebook custom audience
    messaging_system.create_facebook_audience('Test Audience', ['user_id_1', 'user_id_2'])
```
