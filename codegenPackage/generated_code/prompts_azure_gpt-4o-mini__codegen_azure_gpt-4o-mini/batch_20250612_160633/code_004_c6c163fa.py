"""
Generated Code Metadata:
========================
Original URL: https://jiotv.infinityfreeapp.com
Prompt: Develop a tutorial on how to set up multiple email accounts using the iFastNet Web Hosting services.
Generated: DETERMINISTIC_c6c163fad628aca1
Batch ID: 20250612_160633
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

class EmailAccount:
    """
    A class to represent an email account for sending emails.
    """

    def __init__(self, email, password, smtp_server, smtp_port):
        """
        Initializes the EmailAccount with the provided credentials and SMTP server details.

        :param email: str - The email address of the account.
        :param password: str - The password for the email account.
        :param smtp_server: str - The SMTP server address.
        :param smtp_port: int - The port number for the SMTP server.
        """
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient, subject, body):
        """
        Sends an email using the account's SMTP server.

        :param recipient: str - The recipient's email address.
        :param subject: str - The subject of the email.
        :param body: str - The body content of the email.
        :raises Exception: If there is an error sending the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {recipient}")

        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
            raise  # Re-raise the exception for further handling if needed

def setup_email_accounts():
    """
    Sets up multiple email accounts and sends a test email from each account.
    """
    # List of email accounts to set up
    email_accounts = [
        {
            'email': 'user1@example.com',
            'password': 'password1',
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587
        },
        {
            'email': 'user2@example.com',
            'password': 'password2',
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587
        }
    ]

    # Iterate through the email accounts and send a test email
    for account in email_accounts:
        email_account = EmailAccount(
            email=account['email'],
            password=account['password'],
            smtp_server=account['smtp_server'],
            smtp_port=account['smtp_port']
        )
        try:
            email_account.send_email(
                recipient='recipient@example.com',
                subject='Test Email',
                body='This is a test email from your iFastNet email account.'
            )
        except Exception as e:
            print(f"Error sending email from {account['email']}: {e}")

if __name__ == "__main__":
    setup_email_accounts()
```
