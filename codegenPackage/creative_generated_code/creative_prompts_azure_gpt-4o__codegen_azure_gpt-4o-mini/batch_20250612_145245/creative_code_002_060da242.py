"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Generate a script to automate the process of sending email notifications to students about their visa application status, using the contact information format provided by Ikogwe International Limited.
Generated: DETERMINISTIC_060da2420c593147
Batch ID: 20250612_145245
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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailNotificationSystem with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str) -> None:
        """
        Send an email notification to a specified recipient.

        :param to_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {to_email}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {to_email}: {e}")

    def notify_students(self, students: List[Dict[str, str]], status: str) -> None:
        """
        Notify a list of students about their visa application status.

        :param students: List of dictionaries containing student information
        :param status: The visa application status to notify about
        """
        for student in students:
            try:
                email = student['email']
                name = student['name']
                subject = f"Visa Application Status Update for {name}"
                body = f"Dear {name},\n\nYour visa application status is: {status}\n\nBest regards,\nIkogwe International Limited"
                self.send_email(email, subject, body)
            except KeyError as e:
                logging.error(f"Missing information for student: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Initialize the email notification system
    email_system = EmailNotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of students to notify
    students_to_notify = [
        {'name': 'John Doe', 'email': 'john.doe@example.com'},
        {'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    ]

    # Status to notify students about
    visa_status = 'Approved'

    # Notify students about their visa application status
    email_system.notify_students(students_to_notify, visa_status)
```
