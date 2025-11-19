"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Create a script to send automated email notifications to parents regarding CBSE circulars and exam schedules, as outlined in the Deepti Convent Higher Secondary School content.
Generated: DETERMINISTIC_4f36e051c6f32357
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailNotifier with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Send an email to the specified recipients.

        :param recipients: List of email addresses to send the notification to
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
                logging.info(f"Email sent successfully to: {', '.join(recipients)}")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email: {e}")

def main():
    # Email configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    USERNAME = 'your_email@example.com'  # Replace with your email
    PASSWORD = 'your_password'  # Replace with your email password

    # Create an instance of EmailNotifier
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of parent email addresses
    parent_emails = ['parent1@example.com', 'parent2@example.com']  # Replace with actual parent emails

    # Email subject and body
    subject = "CBSE Circulars and Exam Schedules Notification"
    body = """
    Dear Parents,

    This is to inform you about the latest CBSE circulars and the upcoming exam schedules. 
    Please find the details below:

    - Circular: [Details of the circular]
    - Exam Schedule: [Details of the exam schedule]

    Thank you for your attention.

    Best regards,
    Deepti Convent Higher Secondary School
    """

    # Send the email notification
    notifier.send_email(parent_emails, subject, body)

if __name__ == "__main__":
    main()
```
