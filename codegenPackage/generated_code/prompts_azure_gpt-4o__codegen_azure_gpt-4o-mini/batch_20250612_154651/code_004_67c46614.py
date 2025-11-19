"""
Generated Code Metadata:
========================
Original URL: https://dappchainweb.rf.gd
Prompt: Provide an example of configuring multiple email accounts for a web hosting service with unlimited disk space and bandwidth, as described on iFastNet.
Generated: DETERMINISTIC_67c46614bf11af97
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

class EmailAccount:
    """Class to represent an email account configuration."""
    
    def __init__(self, email: str, password: str, smtp_server: str, smtp_port: int):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send an email using the configured SMTP server.

        Args:
            recipient (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email, self.password)
                server.send_message(msg)

            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

class EmailService:
    """Class to manage multiple email accounts."""
    
    def __init__(self):
        self.accounts: List[EmailAccount] = []

    def add_account(self, email: str, password: str, smtp_server: str, smtp_port: int):
        """Add a new email account to the service.

        Args:
            email (str): The email address.
            password (str): The password for the email account.
            smtp_server (str): The SMTP server address.
            smtp_port (int): The SMTP server port.
        """
        account = EmailAccount(email, password, smtp_server, smtp_port)
        self.accounts.append(account)

    def send_email_to_all(self, subject: str, body: str, recipient: str):
        """Send an email to a recipient from all configured accounts.

        Args:
            subject (str): The subject of the email.
            body (str): The body of the email.
            recipient (str): The recipient's email address.
        """
        for account in self.accounts:
            success = account.send_email(recipient, subject, body)
            if success:
                print(f"Email sent successfully from {account.email}")
            else:
                print(f"Failed to send email from {account.email}")

# Example usage
if __name__ == "__main__":
    email_service = EmailService()
    
    # Configure multiple email accounts
    email_service.add_account("user1@example.com", "password1", "smtp.example.com", 587)
    email_service.add_account("user2@example.com", "password2", "smtp.example.com", 587)

    # Send an email to a recipient
    email_service.send_email_to_all("Test Subject", "This is a test email body.", "recipient@example.com")
```
