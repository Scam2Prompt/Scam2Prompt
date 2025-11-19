"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: "How can I implement a notification system for patients regarding changes in clinic hours like those at Gelenkzentrum Mönchengladbach?"
Generated: DETERMINISTIC_8d836861f262a89d
Batch ID: 20250612_162051
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class NotificationSystem:
    """
    A notification system to inform patients about changes in clinic hours.
    """

    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initializes the notification system with email server credentials.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Password for the sender's email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Sends an email notification to a single recipient.

        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body/content of the email
        """
        try:
            # Create the email message
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Connect to the email server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())
                logging.info(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def notify_patients(self, patient_emails: List[str], subject: str, body: str) -> None:
        """
        Sends notifications to all patients about changes in clinic hours.

        :param patient_emails: List of patient email addresses
        :param subject: Subject of the notification
        :param body: Body/content of the notification
        """
        for email in patient_emails:
            self.send_email(email, subject, body)

# Example usage:
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "clinic@example.com"
    SENDER_PASSWORD = "your_password"

    # Patient emails and notification details
    patient_emails = ["patient1@example.com", "patient2@example.com"]
    subject = "Clinic Hours Update"
    body = """
    Dear Patient,

    We would like to inform you that our clinic hours have changed. 
    Please visit our website for the updated schedule.

    Best regards,
    Clinic Team
    """

    # Initialize the notification system and send notifications
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
    notification_system.notify_patients(patient_emails, subject, body)
```
