"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-community.42web.io
Prompt: Develop a tutorial on how to configure multiple email accounts using iFastNet's hosting services.
Generated: DETERMINISTIC_c039330e9bc29caa
Batch ID: 20250612_164222
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

class EmailAccount:
    """Class to handle email account configuration and sending emails."""
    
    def __init__(self, smtp_server, port, username, password):
        """Initialize the EmailAccount with SMTP server details.

        Args:
            smtp_server (str): The SMTP server address.
            port (int): The port number for the SMTP server.
            username (str): The email account username.
            password (str): The email account password.
        """
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, body):
        """Send an email using the configured account.

        Args:
            recipient (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body content of the email.

        Raises:
            Exception: Raises an exception if the email fails to send.
        """
        try:
            # Create the email message
            message = MIMEMultipart()
            message['From'] = self.username
            message['To'] = recipient
            message['Subject'] = subject

            # Attach the body to the message
            message.attach(MIMEText(body, 'plain'))

            # Establish a secure session with SMTP server
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(message)  # Send the email

            print(f"Email sent successfully to {recipient}")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
            raise Exception("Failed to send email.") from e

def configure_email_accounts():
    """Configure multiple email accounts and send a test email."""
    # List of email configurations
    email_accounts = [
        EmailAccount("smtp.ifastnet.com", 587, "user1@example.com", "password1"),
        EmailAccount("smtp.ifastnet.com", 587, "user2@example.com", "password2"),
        EmailAccount("smtp.ifastnet.com", 587, "user3@example.com", "password3"),
    ]

    # Test email details
    recipient = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email from iFastNet email configuration."

    # Send a test email using each configured account
    for account in email_accounts:
        try:
            account.send_email(recipient, subject, body)
        except Exception as e:
            print(f"Failed to send from {account.username}: {e}")

if __name__ == "__main__":
    configure_email_accounts()
```
