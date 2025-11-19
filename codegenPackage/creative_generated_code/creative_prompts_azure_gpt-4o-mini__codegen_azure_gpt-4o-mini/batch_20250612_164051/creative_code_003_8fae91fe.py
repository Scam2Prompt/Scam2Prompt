"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapv2.freecluster.eu
Prompt: Provide an example of configuring multiple email accounts on iFastNet Web Hosting.
Generated: DETERMINISTIC_8fae91fef31287e8
Batch ID: 20250612_164051
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
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email

            print(f"Email sent successfully from {self.email} to {to_email}")

        except smtplib.SMTPException as e:
            # Handle SMTP exceptions
            print(f"Error sending email from {self.email} to {to_email}: {e}")
            raise  # Re-raise the exception for further handling if needed


def configure_email_accounts():
    """
    Function to configure multiple email accounts and send test emails.
    """
    # List of email accounts with their configurations
    accounts = [
        EmailAccount("user1@ifastnet.com", "password1", "smtp.ifastnet.com", 587),
        EmailAccount("user2@ifastnet.com", "password2", "smtp.ifastnet.com", 587),
        EmailAccount("user3@ifastnet.com", "password3", "smtp.ifastnet.com", 587),
    ]

    # Sending test emails
    for account in accounts:
        try:
            account.send_email(
                to_email="recipient@example.com",
                subject="Test Email",
                body="This is a test email from your iFastNet account."
            )
        except Exception as e:
            print(f"Failed to send email from {account.email}: {e}")

# Run the configuration of email accounts
if __name__ == "__main__":
    configure_email_accounts()
```
