"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Create a script to send automated email notifications to parents regarding CBSE circulars and exam schedules, as outlined in the Deepti Convent Higher Secondary School content.
Generated: DETERMINISTIC_4f36e051c6f32357
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
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailNotifier with SMTP server details.

        :param smtp_server: SMTP server address (e.g., 'smtp.gmail.com')
        :param smtp_port: SMTP server port (e.g., 587 for TLS)
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Send an email notification to a list of recipients.

        :param recipients: List of email addresses to send the notification to
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create a MIME message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.send_message(msg)
            
            logging.info(f'Email sent successfully to: {recipients}')
        
        except Exception as e:
            logging.error(f'Failed to send email to {recipients}. Error: {e}')

def create_email_body(circulars: List[str], exam_schedule: Dict[str, str]) -> str:
    """
    Create the email body content.

    :param circulars: List of circulars to include in the email
    :param exam_schedule: Dictionary with subject as key and exam date as value
    :return: Formatted email body string
    """
    body = "Dear Parents,\n\n"
    body += "Please find below the latest CBSE circulars and exam schedules:\n\n"

    body += "Circulars:\n"
    for circular in circulars:
        body += f" - {circular}\n"

    body += "\nExam Schedule:\n"
    for subject, date in exam_schedule.items():
        body += f" - {subject}: {date}\n"

    body += "\nBest Regards,\nDeepti Convent Higher Secondary School"
    
    return body

if __name__ == '__main__':
    # Configuration for the email notifier
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'  # Replace with your email
    PASSWORD = 'your_password'             # Replace with your email password

    # Recipients (list of parents' emails)
    recipients = ['parent1@example.com', 'parent2@example.com']  # Replace with actual emails

    # Sample data for circulars and exam schedules
    circulars = [
        "New admission policy for the 2023 academic year.",
        "Changes in the grading system for Class 10 and 12."
    ]

    exam_schedule = {
        "Mathematics": "2023-11-01",
        "Science": "2023-11-03",
        "English": "2023-11-05"
    }

    # Create an instance of EmailNotifier
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Create email body
    email_body = create_email_body(circulars, exam_schedule)

    # Send the email
    notifier.send_email(recipients, "CBSE Circulars and Exam Schedule Notification", email_body)
```
