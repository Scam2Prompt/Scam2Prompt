"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ndhc.edu.bd
Prompt: Create a notification for students about the importance of regular attendance in classes to avoid being marked as non-collegiate, as mentioned by the acting principal of Nazirpur Degree College.
Generated: DETERMINISTIC_747763b438776606
Batch ID: 20250612_161420
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

class NotificationService:
    """
    A service to send email notifications to students.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the notification service with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port number for the SMTP server.
        :param username: Username for the SMTP server authentication.
        :param password: Password for the SMTP server authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_notification(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Sends an email notification to the given recipients.

        :param recipients: A list of email addresses to send the notification to.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        # Prepare the email
        message = MIMEMultipart()
        message['From'] = self.username
        message['To'] = ", ".join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.sendmail(self.username, recipients, message.as_string())  # Send the email
                print(f"Notification sent successfully to: {', '.join(recipients)}")
        except smtplib.SMTPException as e:
            # Handle SMTP exceptions
            print(f"Error sending email: {str(e)}")

if __name__ == "__main__":
    # Configuration for the SMTP server
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Commonly used SMTP port for TLS
    USERNAME = "your_email@example.com"  # Replace with your email
    PASSWORD = "your_password"  # Replace with your email password

    # Instantiate the notification service
    notification_service = NotificationService(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Notification details
    recipients_list = ["student1@example.com", "student2@example.com"]  # List of student email addresses
    email_subject = "Important Notice: Attendance Policy"
    email_body = (
        "Dear Students,\n\n"
        "This is a reminder about the importance of regular attendance in your classes. "
        "Please be aware that failure to maintain adequate attendance may result in being marked as non-collegiate.\n\n"
        "We encourage you to attend all classes regularly to ensure your academic success.\n\n"
        "Thank you,\n"
        "Acting Principal,\n"
        "Nazirpur Degree College"
    )

    # Send the notification
    notification_service.send_notification(recipients_list, email_subject, email_body)
```
