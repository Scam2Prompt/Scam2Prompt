"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myethereumnodedatabase.net
Prompt: How can I configure email services for my domain registered with LWS?
Generated: DETERMINISTIC_b0c2775a7351a20d
Batch ID: 20250612_135906
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
from typing import Optional

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str) -> None:
        """
        Initialize the EmailService with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port number for the SMTP server
        :param username: The username for the email account
        :param password: The password for the email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str) -> Optional[str]:
        """
        Send an email using the configured SMTP server.

        :param to_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        :return: Success message or error message
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.send_message(msg)
            
            return "Email sent successfully"

        except smtplib.SMTPException as e:
            # Log and return an error message
            error_message = f"Failed to send email: {str(e)}"
            print(error_message)  # Replace with proper logging in production
            return error_message

# Usage example
if __name__ == "__main__":
    # Configuration for the email service
    smtp_server = 'smtp.lws.com'  # Replace with actual SMTP server
    smtp_port = 587  # Common port for TLS
    username = 'your-email@your-domain.com'  # Replace with your email
    password = 'your-email-password'  # Replace with your email password

    # Initialize the email service
    email_service = EmailService(smtp_server, smtp_port, username, password)

    # Send a test email
    response = email_service.send_email(
        to_email='recipient@example.com',
        subject='Test Email',
        body='This is a test email from LWS configured email service.'
    )

    print(response)  # Output the response message
```
