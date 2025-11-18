"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Recommend software solutions for managing client communications and inquiries for a logistics company like OPC S.A.S., including integration with email and phone systems.
Generated: DETERMINISTIC_6f7b33af4917a18e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

class ClientCommunicationManager:
    """
    A manager class for handling client communications via email and SMS.
    """

    def __init__(self, email_config, sms_config):
        """
        Initializes the communication manager with email and SMS configurations.

        :param email_config: A dictionary containing email configuration settings.
        :param sms_config: A dictionary containing SMS configuration settings.
        """
        self.email_config = email_config
        self.sms_config = sms_config

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the specified recipient.

        :param recipient_email: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :raises Exception: If the email sending fails.
        """
        try:
            # Setting up the email server
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['port'])
            server.starttls()
            server.login(self.email_config['username'], self.email_config['password'])

            # Create the email message
            message = MIMEMultipart()
            message['From'] = self.email_config['username']
            message['To'] = recipient_email
            message['Subject'] = subject

            # Attach the email body
            message.attach(MIMEText(body, 'plain'))

            # Send the email
            server.send_message(message)
            server.quit()
            print("Email sent successfully!")

        except Exception as e:
            print(f"Failed to send email: {e}")
            raise

    def send_sms(self, recipient_number, message):
        """
        Sends an SMS to the specified recipient.

        :param recipient_number: The recipient's phone number.
        :param message: The content of the SMS.
        :raises Exception: If the SMS sending fails.
        """
        try:
            # Create a Twilio client
            client = Client(self.sms_config['account_sid'], self.sms_config['auth_token'])

            # Send the SMS
            sms_message = client.messages.create(
                body=message,
                from_=self.sms_config['from_number'],
                to=recipient_number
            )
            print("SMS sent successfully!")

        except Exception as e:
            print(f"Failed to send SMS: {e}")
            raise

if __name__ == "__main__":
    # Example email configuration
    email_config = {
        'smtp_server': 'smtp.example.com',
        'port': 587,
        'username': 'your_email@example.com',
        'password': 'your_email_password'
    }

    # Example SMS configuration
    sms_config = {
        'account_sid': 'your_twilio_account_sid',
        'auth_token': 'your_twilio_auth_token',
        'from_number': '+1234567890'
    }

    # Instantiate the communication manager
    comm_manager = ClientCommunicationManager(email_config, sms_config)

    # Send a test email
    try:
        comm_manager.send_email('client@example.com', 'Test Subject', 'This is a test email.')
    except Exception as e:
        print(e)

    # Send a test SMS
    try:
        comm_manager.send_sms('+0987654321', 'This is a test SMS.')
    except Exception as e:
        print(e)
```

This code provides a robust way to manage client communications through email and SMS in a logistics company context. It follows best practices, includes error handling, and is well-documented for clarity.
