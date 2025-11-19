"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eijhfcc.r.bh.d.sendibt3.com
Prompt: What are the best practices for using Sendinblue to avoid spam issues when sending emails?
Generated: DETERMINISTIC_de3cf88536781454
Batch ID: 20250612_161104
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
from email.utils import formataddr
import re

# Best practices for using Sendinblue and avoiding spam issues
class SendinblueMailer:
    """
    SendinblueMailer is a class to manage email sending using Sendinblue SMTP.
    Implements best practices to avoid spam issues.
    """
    
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initialize the SendinblueMailer with SMTP credentials.

        :param smtp_server: SMTP server address (e.g., smtp-relay.sendinblue.com)
        :param smtp_port: SMTP server port (e.g., 587)
        :param smtp_user: SMTP username (Sendinblue account login email)
        :param smtp_password: SMTP password (Sendinblue API key)
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, sender_name, sender_email, recipient_email, subject, body):
        """
        Send an email using Sendinblue SMTP.

        :param sender_name: Display name of the sender
        :param sender_email: Sender's email address
        :param recipient_email: Recipient's email address
        :param subject: Email subject
        :param body: Email body (plain text)
        :return: True if the email was sent successfully, False otherwise
        """
        try:
            # Validate email addresses
            if not self._is_valid_email(sender_email):
                raise ValueError("Invalid sender email address.")
            if not self._is_valid_email(recipient_email):
                raise ValueError("Invalid recipient email address.")

            # Prepare email with proper headers and content
            msg = MIMEMultipart()
            msg['From'] = formataddr((sender_name, sender_email))
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to Sendinblue SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.smtp_user, self.smtp_password)  # Authenticate
                server.sendmail(sender_email, recipient_email, msg.as_string())
            return True
        except Exception as e:
            # Log the error or handle it appropriately in production
            print(f"Error sending email: {e}")
            return False

    @staticmethod
    def _is_valid_email(email):
        """
        Validate an email address using regular expressions.

        :param email: Email address to validate
        :return: True if valid, False otherwise
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None


# Usage example
if __name__ == "__main__":
    # SMTP credentials for Sendinblue
    smtp_server = "smtp-relay.sendinblue.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"  # Replace with your Sendinblue login email
    smtp_password = "your_api_key"  # Replace with your Sendinblue API key

    # Create an instance of SendinblueMailer
    mailer = SendinblueMailer(smtp_server, smtp_port, smtp_user, smtp_password)

    # Email parameters
    sender_name = "Your Name"
    sender_email = "your_email@example.com"
    recipient_email = "recipient_email@example.com"
    subject = "Welcome to Our Service"
    body = "Hi there,\n\nThanks for signing up! We're excited to have you on board."

    # Send the email
    if mailer.send_email(sender_name, sender_email, recipient_email, subject, body):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
```
