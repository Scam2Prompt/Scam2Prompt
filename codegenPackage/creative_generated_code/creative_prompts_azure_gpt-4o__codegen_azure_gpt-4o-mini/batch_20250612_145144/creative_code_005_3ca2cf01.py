"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Write code to send automated email notifications for weekly promotions on products like "LUVA DE SEGUR WK10 LATEX FORT G" and "TINTA SPRAY VERNIZ."
Generated: DETERMINISTIC_3ca2cf01d36d5b33
Batch ID: 20250612_145144
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
from typing import List

# Define a class for the Email Notification Service
class EmailNotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailNotificationService with SMTP server details.
        
        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str) -> None:
        """
        Sends an email notification.

        :param to_email: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(msg)  # Send the email

            print(f"Email sent to {to_email} successfully.")
        
        except smtplib.SMTPException as e:
            print(f"Failed to send email. Error: {e}")

def main():
    # Configuration for the Email Notification Service
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Replace with your SMTP port
    username = 'your_email@example.com'  # Replace with your email
    password = 'your_password'  # Replace with your email password

    # Create an instance of the EmailNotificationService
    notification_service = EmailNotificationService(smtp_server, smtp_port, username, password)

    # List of recipients
    recipients: List[str] = ['recipient1@example.com', 'recipient2@example.com']  # Replace with actual recipients

    # Promotion details
    subject = "Weekly Promotions on Products"
    body = """
    Hello,

    Check out our latest promotions on the following products:
    1. LUVA DE SEGUR WK10 LATEX FORT G
    2. TINTA SPRAY VERNIZ

    Don't miss out on these great deals!

    Best Regards,
    Your Company
    """

    # Send promotional emails to all recipients
    for recipient in recipients:
        notification_service.send_email(recipient, subject, body)

if __name__ == "__main__":
    main()
```
