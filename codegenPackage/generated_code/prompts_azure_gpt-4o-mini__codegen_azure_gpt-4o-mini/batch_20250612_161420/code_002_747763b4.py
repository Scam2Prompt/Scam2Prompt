"""
Generated Code Metadata:
========================
Original URL: https://ndhc.edu.bd
Prompt: Create a notification for students about the importance of regular attendance in classes to avoid being marked as non-collegiate, as mentioned by the acting principal of Nazirpur Degree College.
Generated: DETERMINISTIC_747763b438776606
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

class NotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the NotificationService with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_notification(self, recipients: List[str], subject: str, message: str) -> None:
        """
        Sends an email notification to the specified recipients.

        :param recipients: A list of email addresses to send the notification to.
        :param subject: The subject of the email.
        :param message: The body of the email.
        """
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the server
                server.sendmail(self.username, recipients, msg.as_string())  # Send the email
            print("Notification sent successfully.")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of NotificationService
    notification_service = NotificationService(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define the recipients and message
    recipients = ['student1@example.com', 'student2@example.com']
    subject = "Important Notice: Attendance Policy"
    message = (
        "Dear Students,\n\n"
        "This is a reminder from the acting principal of Nazirpur Degree College regarding the importance of "
        "regular attendance in classes. Please be aware that consistent absence may lead to being marked as "
        "non-collegiate.\n\n"
        "We encourage you to attend all your classes to ensure your academic success.\n\n"
        "Best regards,\n"
        "Nazirpur Degree College"
    )

    # Send the notification
    notification_service.send_notification(recipients, subject, message)

if __name__ == "__main__":
    main()
```
