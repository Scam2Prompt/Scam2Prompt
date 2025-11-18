"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectprotocol.42web.io
Prompt: Write a Python script to send emails using multiple email accounts on a hosting platform that supports Python apps and free SSL certificates, like iFastNet.
Generated: DETERMINISTIC_a4d31675a43dd8ee
Batch ID: 20250612_145238
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailSender instance with SMTP server details.

        :param smtp_server: The SMTP server address (e.g. smtp.example.com)
        :param smtp_port: The port for the SMTP server (usually 587 for TLS)
        :param username: The email address to use for sending emails
        :param password: The password for the email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        """
        Sends an email using the configured SMTP server.

        :param to_email: The recipient's email address
        :param subject: The subject line of the email
        :param body: The body content of the email
        :raises Exception: Raises exception if sending fails
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            
            logging.info(f"Email sent successfully to {to_email}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {to_email}: {e}")
            raise  # Raise exception for further handling if necessary

def main():
    # Example usage of the EmailSender class
    email_accounts = [
        {
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587,
            'username': 'user1@example.com',
            'password': 'password1',
        },
        {
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587,
            'username': 'user2@example.com',
            'password': 'password2',
        },
    ]

    subject = "Test Email"
    body = "This is a test email sent from a Python script."

    for account in email_accounts:
        email_sender = EmailSender(
            smtp_server=account['smtp_server'],
            smtp_port=account['smtp_port'],
            username=account['username'],
            password=account['password']
        )
        # Sending email to a static recipient for demonstration
        try:
            email_sender.send_email("recipient@example.com", subject, body)
        except Exception as e:
            logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
