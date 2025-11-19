"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pegasus-usual-dao.vercel.app
Prompt: How do I create a user notification system for restricted regions in my application, inspired by the Usual Interface?
Generated: DETERMINISTIC_24934dff2d618372
Batch ID: 20250612_161453
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
from typing import List, Dict, Optional

class UserNotificationSystem:
    """
    A class to handle user notifications for restricted regions.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the UserNotificationSystem with SMTP server credentials.
        
        :param smtp_server: The SMTP server hostname.
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
        Sends notification emails to the specified recipients.
        
        :param recipients: A list of email addresses to notify.
        :param subject: The subject of the email.
        :param message: The body of the email.
        :raises ValueError: If no recipients are provided.
        :raises Exception: If the email sending fails.
        """
        if not recipients:
            raise ValueError("No recipients provided for the notification.")
        
        # Create the email message
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = ', '.join(recipients)

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to TLS
                server.login(self.username, self.password)  # Log in to the server
                server.sendmail(self.username, recipients, msg.as_string())  # Send the email
        except smtplib.SMTPException as e:
            raise Exception(f"Error sending email: {e}")

    def notify_users_in_restricted_region(self, users: Dict[str, str], restricted_region: str) -> None:
        """
        Notifies users who are in the specified restricted region.

        :param users: A dictionary where keys are user emails and values are their respective regions.
        :param restricted_region: The region that is restricted.
        :raises Exception: If notification fails for any user.
        """
        # Filter users in the restricted region
        users_to_notify = [email for email, region in users.items() if region == restricted_region]

        if users_to_notify:
            subject = "Important Notification: Restricted Region Alert"
            message = f"You are receiving this notification because you are in the restricted region: {restricted_region}."
            self.send_notification(users_to_notify, subject, message)
        else:
            print("No users need to be notified in the restricted region.")

# Example usage
if __name__ == "__main__":
    # Define SMTP server credentials
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Instantiate the notification system
    notification_system = UserNotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Example user data (email: region)
    users_data = {
        "user1@example.com": "Region A",
        "user2@example.com": "Restricted Region",
        "user3@example.com": "Region B",
    }

    # Notify users in the restricted region
    notification_system.notify_users_in_restricted_region(users_data, "Restricted Region")
```
