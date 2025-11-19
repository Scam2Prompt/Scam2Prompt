"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setcar.com.br
Prompt: How can I set up an email notification system for users when a website goes live, as mentioned for the Viskoo site?
Generated: DETERMINISTIC_ed197c3fa73281a2
Batch ID: 20250612_162605
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://{website_name.lower": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initialize the EmailNotifier with SMTP server details.
        
        :param smtp_server: The SMTP server address.
        :param smtp_port: The SMTP server port.
        :param smtp_user: The SMTP username (email).
        :param smtp_password: The SMTP password (app-specific or regular).
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Send an email notification.

        :param recipient_email: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")

    def notify_users(self, user_emails: List[str], website_name: str) -> None:
        """
        Notify a list of users that the specified website is now live.

        :param user_emails: A list of user email addresses to notify.
        :param website_name: The name of the website that is now live.
        """
        subject = f"{website_name} is now live!"
        body = f"Hello,\n\nWe are excited to inform you that {website_name} is now live! Visit us at http://{website_name.lower()}.com to check it out.\n\nBest regards,\nThe Team"

        for email in user_emails:
            self.send_email(email, subject, body)

# Example usage:
if __name__ == "__main__":
    # SMTP configuration (use environment variables in production)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'your_email@example.com'
    SMTP_PASSWORD = 'your_password'
    
    # List of user emails to notify
    users_to_notify = ['user1@example.com', 'user2@example.com', 'user3@example.com']
    
    # Create an EmailNotifier instance
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
    
    # Notify users that the website is live
    notifier.notify_users(users_to_notify, "Viskoo")
```
