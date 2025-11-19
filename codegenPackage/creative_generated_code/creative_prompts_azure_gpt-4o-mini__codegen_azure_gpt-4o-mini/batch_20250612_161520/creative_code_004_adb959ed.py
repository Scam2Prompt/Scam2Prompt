"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Suggest a method to implement a notification system for students using Araform's online platform to alert them about new course offerings.
Generated: DETERMINISTIC_adb959ed5d890ec6
Batch ID: 20250612_161520
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
from datetime import datetime
from typing import List, Dict

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str) -> None:
        """
        Initializes the NotificationSystem with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port to connect to the SMTP server.
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

        :param to_email: Recipient's email address.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.send_message(msg)

            print(f"Email sent to {to_email} successfully.")

        except Exception as e:
            print(f"Failed to send email to {to_email}. Error: {str(e)}")

    def notify_students(self, students: List[Dict[str, str]], course_name: str) -> None:
        """
        Sends notifications to a list of students about new course offerings.

        :param students: A list of dictionaries with student details (name and email).
        :param course_name: The name of the new course offering.
        """
        subject = f"New Course Offering: {course_name}"
        body = f"Dear Student,\n\nWe are excited to announce a new course: {course_name}.\n\nBest Regards,\nAraform Team"

        for student in students:
            try:
                to_email = student['email']
                self.send_email(to_email, subject, body)

            except KeyError:
                print("Student data is missing email. Skipping notification.")
            except Exception as e:
                print(f"An error occurred while notifying {student.get('name', 'Unknown')}: {str(e)}")

# Example usage
if __name__ == "__main__":
    smtp_details = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'username': 'your_email@example.com',
        'password': 'your_secure_password'
    }
    
    # Instantiate the notification system
    notification_system = NotificationSystem(**smtp_details)

    # List of students to notify
    students_list = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"},
    ]

    # Notify students about a new course offering
    notification_system.notify_students(students_list, "Python Programming 101")
```
