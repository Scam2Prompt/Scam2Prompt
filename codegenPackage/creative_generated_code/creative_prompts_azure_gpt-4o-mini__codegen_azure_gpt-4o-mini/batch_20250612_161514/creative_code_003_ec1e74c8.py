"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.napatablets.com
Prompt: Provide a sample configuration for setting up a professional company email address with Office 365 for NAPA jobbers.
Generated: DETERMINISTIC_ec1e74c895a8a5fb
Batch ID: 20250612_161514
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

class EmailConfig:
    """
    A class to represent the configuration for sending emails using Office 365.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailConfig with SMTP server details.

        :param smtp_server: The SMTP server address (e.g., 'smtp.office365.com').
        :param smtp_port: The port number for the SMTP server (e.g., 587 for Office 365).
        :param username: The email address used for authentication.
        :param password: The password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_addresses: List[str], subject: str, body: str) -> None:
        """
        Sends an email using the configured SMTP settings.

        :param to_addresses: List of recipient email addresses.
        :param subject: The subject of the email.
        :param body: The HTML or plain text body of the email.
        """
        # Create the message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ', '.join(to_addresses)
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email
                print("Email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")  # Log the error message

# Sample configuration for Office 365 email
if __name__ == "__main__":
    # Replace these placeholder values with your actual information
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_password'

    email_config = EmailConfig(smtp_server, smtp_port, username, password)

    # Define the email parameters
    to_addresses = ['recipient1@example.com', 'recipient2@example.com']
    subject = 'NAPA Jobbers: Welcome to Our Service'
    body = 'Dear valued customer,\n\nThank you for choosing NAPA jobbers!\n\nBest regards,\nThe NAPA Team'

    # Send the email
    email_config.send_email(to_addresses, subject, body)
```
