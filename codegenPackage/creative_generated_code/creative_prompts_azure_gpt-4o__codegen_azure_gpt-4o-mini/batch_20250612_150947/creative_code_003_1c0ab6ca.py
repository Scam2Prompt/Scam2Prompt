"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Write code to configure multiple email accounts on a hosting platform that supports Python apps and has no daily hit or process limits, based on iFastNet hosting specifications.
Generated: DETERMINISTIC_1c0ab6ca39bf6054
Batch ID: 20250612_150947
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailAccount:
    """A class to represent an email account configuration."""

    def __init__(self, username, password, smtp_server, smtp_port):
        """Initialize the email account with necessary credentials."""
        self.username = username
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def create_message(self, to_email, subject, body):
        """Create a MIME message for the email."""
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def send_email(self, to_email, subject, body):
        """Send an email to the specified address."""
        try:
            msg = self.create_message(to_email, subject, body)
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            logging.info(f"Email sent successfully to {to_email}")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {to_email}. Error: {str(e)}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")


def configure_email_accounts(email_configs):
    """
    Configure and send test emails to validate email account setups.
    
    Args:
    email_configs (list): A list of dictionaries containing email account configurations.
    Each dictionary should have 'username', 'password', 'smtp_server', 'smtp_port', 
    and 'to_email' for testing.
    """
    for config in email_configs:
        try:
            email_account = EmailAccount(
                username=config['username'],
                password=config['password'],
                smtp_server=config['smtp_server'],
                smtp_port=config['smtp_port']
            )
            # Send a test email
            email_account.send_email(
                to_email=config['to_email'],
                subject="Test Email",
                body="This is a test email to verify the configuration."
            )
        except KeyError as e:
            logging.error(f"Missing configuration key: {str(e)}")
        except Exception as e:
            logging.error(f"An error occurred while configuring the email account: {str(e)}")


# Example email configurations (replace with real credentials and SMTP settings)
email_configs = [
    {
        'username': 'user1@example.com',
        'password': 'password1',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'to_email': 'recipient@example.com'
    },
    {
        'username': 'user2@example.com',
        'password': 'password2',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'to_email': 'recipient@example.com'
    }
]

if __name__ == "__main__":
    configure_email_accounts(email_configs)
```
