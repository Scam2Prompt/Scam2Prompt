"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappchainweb.rf.gd
Prompt: Provide an example of configuring multiple email accounts for a web hosting service with unlimited disk space and bandwidth, as described on iFastNet.
Generated: DETERMINISTIC_67c46614bf11af97
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailAccount:
    def __init__(self, username, password, smtp_server, smtp_port):
        """
        Initialize an email account with required credentials and server details.

        :param username: Email account username (email address).
        :param password: Password for the email account.
        :param smtp_server: SMTP server address for sending emails.
        :param smtp_port: Port used for SMTP server.
        """
        self.username = username
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient, subject, body):
        """
        Send an email using the SMTP server.

        :param recipient: Recipient's email address.
        :param subject: Subject of the email.
        :param body: Body of the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)  # Login to the email account
                server.send_message(msg)  # Send the email
                logging.info(f'Email sent to {recipient} successfully.')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient}: {e}')

def configure_email_accounts():
    """
    Configure multiple email accounts for a web hosting service.
    """
    # Define email account details
    accounts = [
        EmailAccount('user1@example.com', 'password1', 'smtp.example.com', 587),
        EmailAccount('user2@example.com', 'password2', 'smtp.example.com', 587),
        EmailAccount('user3@example.com', 'password3', 'smtp.example.com', 587),
    ]

    # Send a test email from each account
    for account in accounts:
        account.send_email('recipient@example.com', 'Test Email', 'This is a test email.')

if __name__ == '__main__':
    configure_email_accounts()
```
