"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodlit.rf.gd
Prompt: Recommend libraries or tools for managing email accounts programmatically on a hosting platform that supports multiple email accounts, such as iFastNet.
Generated: DETERMINISTIC_af9ceb91e3e6e4f7
Batch ID: 20250612_151504
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
from typing import List, Dict, Any
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailManager:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailManager with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email to the specified recipient.
        
        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        :raises Exception: If sending the email fails
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)  # Login to the email account
                server.sendmail(self.username, recipient, msg.as_string())  # Send the email
            
            logging.info(f"Email sent successfully to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")
            raise

def manage_email_accounts(accounts: List[Dict[str, Any]], recipients: List[str], subject: str, body: str) -> None:
    """
    Manage multiple email accounts and send emails.
    
    :param accounts: List of dictionaries containing account details
    :param recipients: List of recipient email addresses
    :param subject: Subject for the emails
    :param body: Body content for the emails
    """
    for account in accounts:
        try:
            email_manager = EmailManager(
                smtp_server=account['smtp_server'],
                smtp_port=account['smtp_port'],
                username=account['username'],
                password=account['password']
            )

            for recipient in recipients:
                email_manager.send_email(recipient, subject, body)

        except Exception as e:
            logging.error(f"Error managing account {account['username']}: {e}")

# Example usage
if __name__ == "__main__":
    email_accounts = [
        {
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587,
            'username': 'user1@example.com',
            'password': 'password1'
        },
        {
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587,
            'username': 'user2@example.com',
            'password': 'password2'
        }
    ]
    
    recipients_list = ['recipient@example.com']
    email_subject = 'Test Email'
    email_body = 'This is a test email.'

    manage_email_accounts(email_accounts, recipients_list, email_subject, email_body)
```
