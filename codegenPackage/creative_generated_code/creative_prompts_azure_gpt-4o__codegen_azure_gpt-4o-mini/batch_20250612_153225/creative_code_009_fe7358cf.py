"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Create a script to automate sending email notifications to volunteers and donors for an NGO like Perú Makers, using Python and an email-sending library like `smtplib`.
Generated: DETERMINISTIC_fe7358cfaedc7080
Batch ID: 20250612_153225
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
from typing import List

class EmailNotifier:
    """A class to handle sending email notifications."""

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailNotifier with SMTP server configuration.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port to connect to the SMTP server.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to a specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {e}")

def main():
    """Main function to execute the email notification script."""
    # Configure SMTP settings
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    username = 'your_email@example.com'  # Replace with your email
    password = 'your_password'  # Replace with your email password

    # Create an instance of EmailNotifier
    notifier = EmailNotifier(smtp_server, smtp_port, username, password)

    # List of volunteers and donors to notify
    recipients = [
        'volunteer1@example.com',
        'donor1@example.com',
    ]

    # Email subject and body
    subject = 'Thank You for Your Support!'
    body = (
        "Dear Volunteer/Donor,\n\n"
        "Thank you for your continued support of Perú Makers. "
        "Together, we are making a difference!\n\n"
        "Best regards,\n"
        "The Perú Makers Team"
    )

    # Sending emails to all recipients
    for recipient in recipients:
        notifier.send_email(recipient, subject, body)

if __name__ == '__main__':
    main()
```
