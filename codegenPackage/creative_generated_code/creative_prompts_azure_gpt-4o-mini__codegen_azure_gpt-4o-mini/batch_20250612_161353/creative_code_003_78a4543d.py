"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.io
Prompt: What libraries or APIs can help manage site maintenance notifications for users?
Generated: DETERMINISTIC_78a4543d8c61a2af
Batch ID: 20250612_161353
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

class MaintenanceNotification:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the MaintenanceNotification instance.

        :param smtp_server: SMTP server address.
        :param smtp_port: Port for the SMTP server.
        :param username: Username for SMTP authentication.
        :param password: Password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification.

        :param recipient: Email address of the recipient.
        :param subject: Subject of the email.
        :param body: Body text of the email.
        """
        try:
            # Create a multipart email message
            message = MIMEMultipart()
            message['From'] = self.username
            message['To'] = recipient
            message['Subject'] = subject
            
            # Attach the email body to the message
            message.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(message)

            print(f"Notification sent to {recipient}")

        except Exception as e:
            print(f"Failed to send email to {recipient}: {str(e)}")

    def notify_users(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Notify a list of users about site maintenance.

        :param recipients: List of email addresses to notify.
        :param subject: Subject of the email notification.
        :param body: Body content of the email notification.
        """
        for recipient in recipients:
            self.send_email(recipient, subject, body)


if __name__ == "__main__":
    # Example configuration (to be replaced with actual values)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Create an instance of MaintenanceNotification
    notifier = MaintenanceNotification(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define the list of recipients
    recipients_list = ["user1@example.com", "user2@example.com"]

    # Define the subject and body of the notification
    email_subject = "Scheduled Maintenance Notification"
    email_body = "Dear User,\n\nPlease be informed that the site will undergo maintenance on the scheduled date. Thank you for your understanding.\n\nBest Regards,\nTeam"

    # Notify users
    notifier.notify_users(recipients_list, email_subject, email_body)
```
