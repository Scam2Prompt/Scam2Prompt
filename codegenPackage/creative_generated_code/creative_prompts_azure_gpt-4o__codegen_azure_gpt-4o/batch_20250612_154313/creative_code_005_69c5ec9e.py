"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-limited.com
Prompt: Write code to implement a notification system for informing users about updates to the privacy policy, including push notifications and email alerts, as described by STELLAR TECHNOLOGY LIMITED.
Generated: DETERMINISTIC_69c5ec9e7df7be59
Batch ID: 20250612_154313
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pushnotificationprovider.com/send": {
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
import json
import requests

class NotificationSystem:
    """
    A notification system for informing users about updates to the privacy policy
    via email alerts and push notifications.
    """

    def __init__(self, smtp_server, smtp_port, email_user, email_password, push_notification_api_url, push_notification_api_key):
        """
        Initialize the notification system with email and push notification configurations.

        :param smtp_server: The SMTP server for sending emails.
        :param smtp_port: The port for the SMTP server.
        :param email_user: The email account username.
        :param email_password: The email account password.
        :param push_notification_api_url: The API endpoint for sending push notifications.
        :param push_notification_api_key: The API key for authenticating push notifications.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password
        self.push_notification_api_url = push_notification_api_url
        self.push_notification_api_key = push_notification_api_key

    def send_email(self, recipient_email, subject, message):
        """
        Send an email notification to the specified recipient.

        :param recipient_email: The recipient's email address.
        :param subject: The subject of the email.
        :param message: The body of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(self.email_user, self.email_password)  # Log in to the server
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {recipient_email}")

        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")

    def send_push_notification(self, device_id, title, message):
        """
        Send a push notification to the specified device.

        :param device_id: The unique identifier for the recipient's device.
        :param title: The title of the push notification.
        :param message: The body of the push notification.
        """
        try:
            payload = {
                "device_id": device_id,
                "title": title,
                "message": message
            }
            headers = {
                "Authorization": f"Bearer {self.push_notification_api_key}",
                "Content-Type": "application/json"
            }
            response = requests.post(self.push_notification_api_url, headers=headers, json=payload)

            if response.status_code == 200:
                print(f"Push notification sent successfully to device {device_id}")
            else:
                print(f"Failed to send push notification to device {device_id}. Response: {response.text}")

        except Exception as e:
            print(f"Error while sending push notification to device {device_id}: {e}")

    def notify_users(self, users, email_subject, email_message, push_notification_title, push_notification_message):
        """
        Notify the list of users about updates to the privacy policy.

        :param users: List of dictionaries containing user information (email and device_id).
        :param email_subject: The subject of the email notification.
        :param email_message: The body of the email notification.
        :param push_notification_title: The title of the push notification.
        :param push_notification_message: The body of the push notification.
        """
        for user in users:
            email = user.get("email")
            device_id = user.get("device_id")

            # Send email notification
            if email:
                self.send_email(email, email_subject, email_message)

            # Send push notification
            if device_id:
                self.send_push_notification(device_id, push_notification_title, push_notification_message)


# Example usage
if __name__ == "__main__":
    # Configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587
    email_user = "your_email@example.com"
    email_password = "your_email_password"
    push_notification_api_url = "https://api.pushnotificationprovider.com/send"
    push_notification_api_key = "your_push_notification_api_key"

    # Initialize the notification system
    notification_system = NotificationSystem(
        smtp_server,
        smtp_port,
        email_user,
        email_password,
        push_notification_api_url,
        push_notification_api_key
    )

    # List of users to notify
    users = [
        {"email": "user1@example.com", "device_id": "device1234"},
        {"email": "user2@example.com", "device_id": "device5678"}
    ]

    # Messages
    email_subject = "Privacy Policy Update"
    email_message = "Dear user, we have updated our privacy policy. Please visit our website to learn more."
    push_notification_title = "Privacy Policy Update"
    push_notification_message = "We have updated our privacy policy. Learn more on our website."

    # Notify users
    notification_system.notify_users(users, email_subject, email_message, push_notification_title, push_notification_message)
```
