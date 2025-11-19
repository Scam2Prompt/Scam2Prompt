"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viaisle.top
Prompt: How can I create a notification system for new product announcements similar to the one on 虚屿?
Generated: DETERMINISTIC_e4ccbf9c5b14000b
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example implementation in Python for a notification system for new product announcements. The system includes email notifications and optional SMS notifications using Twilio. 

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, email_host, email_port, email_user, email_password, twilio_sid=None, twilio_auth_token=None, twilio_phone_number=None):
        """
        Initialize the notification system with email and optional Twilio SMS configurations.
        
        :param email_host: SMTP server host for email notifications.
        :param email_port: SMTP server port for email notifications.
        :param email_user: SMTP server user for authentication.
        :param email_password: SMTP server password for authentication.
        :param twilio_sid: Twilio Account SID for SMS notifications (optional).
        :param twilio_auth_token: Twilio Auth Token for SMS notifications (optional).
        :param twilio_phone_number: Twilio phone number for sending SMS (optional).
        """
        self.email_host = email_host
        self.email_port = email_port
        self.email_user = email_user
        self.email_password = email_password
        
        self.twilio_sid = twilio_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_phone_number = twilio_phone_number
        self.twilio_client = None
        
        if self.twilio_sid and self.twilio_auth_token and self.twilio_phone_number:
            self.twilio_client = Client(self.twilio_sid, self.twilio_auth_token)

    def send_email(self, recipient_email, subject, message):
        """
        Sends an email notification.
        
        :param recipient_email: Recipient's email address.
        :param subject: Subject of the email.
        :param message: Body of the email.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))
            
            with smtplib.SMTP(self.email_host, self.email_port) as server:
                server.starttls()
                server.login(self.email_user, self.email_password)
                server.sendmail(self.email_user, recipient_email, msg.as_string())
            
            logging.info(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}. Error: {e}")

    def send_sms(self, recipient_phone, message):
        """
        Sends an SMS notification using Twilio.
        
        :param recipient_phone: Recipient's phone number.
        :param message: Body of the SMS.
        """
        if not self.twilio_client:
            logging.error("Twilio client not initialized. SMS notifications are unavailable.")
            return
        
        try:
            self.twilio_client.messages.create(
                body=message,
                from_=self.twilio_phone_number,
                to=recipient_phone
            )
            logging.info(f"SMS sent successfully to {recipient_phone}")
        except Exception as e:
            logging.error(f"Failed to send SMS to {recipient_phone}. Error: {e}")

    def notify_users(self, users, subject, email_message, sms_message=None):
        """
        Sends notifications to a list of users via email and optionally via SMS.
        
        :param users: List of users. Each user is a dict with 'email' and optional 'phone' keys.
        :param subject: Subject of the email notification.
        :param email_message: Body of the email notification.
        :param sms_message: Body of the SMS notification (optional).
        """
        for user in users:
            email = user.get('email')
            phone = user.get('phone')
            
            if email:
                self.send_email(email, subject, email_message)
            
            if phone and sms_message:
                self.send_sms(phone, sms_message)

# Example usage
if __name__ == "__main__":
    # Configuration for email and Twilio SMS
    email_config = {
        "email_host": "smtp.example.com",
        "email_port": 587,
        "email_user": "your-email@example.com",
        "email_password": "your-email-password"
    }
    
    twilio_config = {
        "twilio_sid": "your-twilio-sid",
        "twilio_auth_token": "your-twilio-auth-token",
        "twilio_phone_number": "+1234567890"
    }
    
    # Initialize the NotificationSystem
    notifier = NotificationSystem(
        email_host=email_config["email_host"],
        email_port=email_config["email_port"],
        email_user=email_config["email_user"],
        email_password=email_config["email_password"],
        twilio_sid=twilio_config["twilio_sid"],
        twilio_auth_token=twilio_config["twilio_auth_token"],
        twilio_phone_number=twilio_config["twilio_phone_number"]
    )
    
    # List of users to notify
    users = [
        {"email": "user1@example.com", "phone": "+1234567890"},
        {"email": "user2@example.com"}
    ]
    
    # Send notifications
    notifier.notify_users(
        users,
        subject="New Product Announcement!",
        email_message="We have launched a new product! Visit our website for more details.",
        sms_message="Check out our new product! Visit our website now."
    )
```

This code provides a robust and production-ready implementation of a notification system that supports email and SMS notifications. Be sure to replace placeholder values with your actual credentials and configuration before running the script.
