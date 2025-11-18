"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rectifywallet.42web.io
Prompt: Create a script to configure email accounts on a hosting platform that supports multiple email accounts and provides SSL certificates.
Generated: DETERMINISTIC_3037449d9cd181a9
Batch ID: 20250612_154423
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
import ssl
import logging

# Configure logging for debug information
logging.basicConfig(
    filename='email_account_setup.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class EmailAccountManager:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailAccountManager with SMTP server details and credentials.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server (usually 465 or 587).
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to a specified recipient.

        :param recipient_email: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :raises Exception: If the email sending fails.
        """
        try:
            # Create the email content
            message = MIMEMultipart()
            message['From'] = self.username
            message['To'] = recipient_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Create a secure SSL context
            context = ssl.create_default_context()

            # Connect to the SMTP server and send the email
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient_email, message.as_string())
                logging.info(f'Email sent successfully to {recipient_email}')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient_email}: {e}')
            raise

    def configure_email_account(self, email_address, password):
        """
        Configures an email account by sending a configuration email.

        :param email_address: The email address to be configured.
        :param password: The password for the email account.
        :raises Exception: If the email configuration fails.
        """
        subject = 'Email Account Configuration'
        body = (f'Your email account has been configured successfully.\n'
                f'Email: {email_address}\n'
                f'Password: {password}\n'
                'Please ensure to change your password after the first login.')

        try:
            self.send_email(email_address, subject, body)
            logging.info(f'Configuration email sent to {email_address}')
        except Exception as e:
            logging.error(f'Failed to configure email account for {email_address}: {e}')
            raise

def main():
    # SMTP server details for the hosting platform
    SMTP_SERVER = 'smtp.yourhostingprovider.com'
    SMTP_PORT = 465
    USERNAME = 'your-email@example.com'
    PASSWORD = 'your-email-password'

    # List of email accounts to configure
    email_accounts = {
        'user1@example.com': 'user1password',
        'user2@example.com': 'user2password',
    }

    # Initialize EmailAccountManager
    email_manager = EmailAccountManager(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Configure email accounts
    for email, pwd in email_accounts.items():
        try:
            email_manager.configure_email_account(email, pwd)
        except Exception as e:
            logging.error(f'Error configuring account {email}: {e}')

if __name__ == '__main__':
    main()
```
