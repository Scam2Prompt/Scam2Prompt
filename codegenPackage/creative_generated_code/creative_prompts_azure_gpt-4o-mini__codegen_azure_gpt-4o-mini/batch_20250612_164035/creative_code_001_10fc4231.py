"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappextension.com
Prompt: How can I implement a notification system for users when their account is suspended?
Generated: DETERMINISTIC_10fc42317d40c1a3
Batch ID: 20250612_164035
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

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initializes the NotificationSystem with SMTP server details.
        
        :param smtp_server: The SMTP server address.
        :param smtp_port: The SMTP server port.
        :param smtp_user: The username for the SMTP server.
        :param smtp_password: The password for the SMTP account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email notification to the specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body of the email.
        :raises Exception: If unable to send the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Set up the server connection
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.smtp_user, self.smtp_password)  # Login to the SMTP server
                server.sendmail(self.smtp_user, recipient, msg.as_string())  # Send the email
        except Exception as e:
            # Handle exceptions during email sending
            print(f"Error sending email to {recipient}: {e}")
            raise  # Reraise the exception for further handling

    def notify_user_account_suspension(self, user_email: str) -> None:
        """
        Notifies the user that their account has been suspended.

        :param user_email: The email address of the user to notify.
        """
        subject = "Account Suspension Notification"
        body = (
            "Dear User,\n\n"
            "We regret to inform you that your account has been suspended due to policy violations.\n"
            "Please contact support for further information.\n\n"
            "Best regards,\n"
            "Support Team"
        )
        
        # Send the notification email
        self.send_email(user_email, subject, body)

# Example usage:
if __name__ == "__main__":
    # Configure the SMTP settings
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your-email@example.com"
    smtp_password = "your-email-password"

    # Create the notification system instance
    notification_system = NotificationSystem(smtp_server, smtp_port, smtp_user, smtp_password)

    # Notify the user
    user_email = "user-to-notify@example.com"
    notification_system.notify_user_account_suspension(user_email)
```

Note: Ensure to replace the SMTP configuration and user email with actual values before running the code.
