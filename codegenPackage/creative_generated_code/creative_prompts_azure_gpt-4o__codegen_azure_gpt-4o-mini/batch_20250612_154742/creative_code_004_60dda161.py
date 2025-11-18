"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://datmaui.liveblog365.com
Prompt: Write a Python script to send automated emails using a hosting service that supports multiple email accounts, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_60dda1616b58cf08
Batch ID: 20250612_154742
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
from typing import List

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailSender with SMTP configuration.
        
        :param smtp_server: The SMTP server address
        :param smtp_port: The SMTP server port
        :param username: The email account username
        :param password: The email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_emails: List[str], subject: str, body: str) -> None:
        """
        Sends an email to one or multiple recipients.
        
        :param to_emails: List of recipient email addresses
        :param subject: Subject of the email
        :param body: Body content of the email
        :raises Exception: If sending the email fails
        """
        # Create a MIMEText object to represent the email
        msg = MIMEMultipart()
        msg['From'] = formataddr((self.username, self.username))
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(self.username, self.password)  # Login to the email account
                server.sendmail(self.username, to_emails, msg.as_string())  # Send the email
                print(f"Email sent successfully to: {', '.join(to_emails)}")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Configuration parameters for email server
    SMTP_SERVER = 'smtp.ifastnet.com'  # Example SMTP server, replace with actual
    SMTP_PORT = 587  # Common SMTP port for TLS
    USERNAME = 'your-email@ifastnet.com'  # Replace with your email address
    PASSWORD = 'your-email-password'  # Replace with your email password

    # Create an instance of EmailSender
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define the email details
    recipients = ['recipient1@example.com', 'recipient2@example.com']
    email_subject = 'Test Email'
    email_body = 'This is a test email sent from a Python script.'

    # Send the email
    email_sender.send_email(recipients, email_subject, email_body)
```

**Note:** Before running the script, replace the placeholder values (`SMTP_SERVER`, `USERNAME`, and `PASSWORD`) with actual credentials from your iFastNet hosting service.
