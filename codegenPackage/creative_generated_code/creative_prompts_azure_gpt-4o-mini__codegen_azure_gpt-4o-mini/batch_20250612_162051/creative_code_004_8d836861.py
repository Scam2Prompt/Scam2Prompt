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
from typing import List
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """Initialize the NotificationSystem with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient: str, subject: str, message: str) -> None:
        """Send an email notification.

        Args:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The body of the email.

        Raises:
            Exception: Raises an exception if email sending fails.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the message body
            msg.attach(MIMEText(message, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")
            raise

    def notify_patients(self, patients: List[str], subject: str, message: str) -> None:
        """Notify multiple patients of clinic hour changes.

        Args:
            patients (List[str]): List of patient email addresses.
            subject (str): The subject of the email.
            message (str): The body of the email message.
        """
        for patient_email in patients:
            try:
                self.send_email(patient_email, subject, message)
            except Exception as e:
                logging.error(f"Error notifying {patient_email}: {e}")

# Example usage
if __name__ == "__main__":
    # Define email settings
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_email_password"

    # Create a notification system instance
    notification_system = NotificationSystem(smtp_server, smtp_port, smtp_user, smtp_password)

    # List of patients to notify
    patients_list = ["patient1@example.com", "patient2@example.com"]

    # Subject and message for the notification
    subject = "Important: Changes to Clinic Hours"
    message = "Dear Patient,\n\nPlease note that there have been changes to our clinic hours. " \
              "Check our website for the latest updates.\n\nBest regards,\nGelenkzentrum Mönchengladbach"

    # Notify patients
    notification_system.notify_patients(patients_list, subject, message)
```
