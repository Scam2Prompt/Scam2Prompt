"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapv2.epizy.com
Prompt: Provide an example of configuring multiple email accounts on iFastNet Web Hosting.
Generated: DETERMINISTIC_8fae91fef31287e8
Batch ID: 20250612_164323
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

class EmailAccount:
    """
    Class to represent an email account on iFastNet Web Hosting.
    """

    def __init__(self, email, password, smtp_server, smtp_port):
        """
        Initialize the email account with necessary credentials.
        
        :param email: str - The email address.
        :param password: str - The password for the email account.
        :param smtp_server: str - SMTP server address.
        :param smtp_port: int - SMTP server port.
        """
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, to_email, subject, body):
        """
        Send an email using the configured account.
        
        :param to_email: str - Recipient's email address.
        :param subject: str - Subject of the email.
        :param body: str - Body content of the email.
        :raises Exception: If sending fails.
        """
        try:
            # Create a multipart email
            message = MIMEMultipart()
            message['From'] = self.email
            message['To'] = to_email
            message['Subject'] = subject

            # Attach the email body
            message.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.email, self.password)  # Log in to the server
                server.send_message(message)  # Send the email

            print(f"Email sent successfully from {self.email} to {to_email}.")
        except Exception as e:
            print(f"Failed to send email from {self.email} to {to_email}. Error: {e}")

# Configuration for multiple email accounts
email_accounts = [
    EmailAccount("user1@example.com", "password1", "smtp.example.com", 587),
    EmailAccount("user2@example.com", "password2", "smtp.example.com", 587),
    EmailAccount("user3@example.com", "password3", "smtp.example.com", 587)
]

# Sending emails from each account
for account in email_accounts:
    account.send_email("recipient@example.com", "Test Email", "This is a test email from your iFastNet account.")
```
