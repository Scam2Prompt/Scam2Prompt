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

Here is a Python implementation of a simple notification system for users when their account is suspended:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NotificationSystem:
    """
    NotificationSystem handles sending email notifications to users when their account is suspended.
    """
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the notification system with SMTP server details and credentials.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Email address used for sending notifications
        :param sender_password: Password for the sender email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email, user_name):
        """
        Send a suspension notification email to the specified user.

        :param recipient_email: The email address of the user to notify
        :param user_name: The name of the user whose account is suspended
        :return: None
        """
        try:
            # Create the email content
            subject = "Account Suspension Notification"
            body = f"""
            Dear {user_name},

            We regret to inform you that your account has been suspended due to violations of our terms of service.
            Please contact support if you believe this was a mistake.

            Regards,
            The Support Team
            """
            
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Establish connection to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure (TLS)
                server.login(self.sender_email, self.sender_password)  # Log in to the SMTP server
                server.send_message(message)  # Send the email
                print(f"Notification sent successfully to {recipient_email}")

        except smtplib.SMTPException as e:
            # Handle SMTP errors
            print(f"Failed to send notification email: {e}")
        except Exception as e:
            # Handle other unforeseen errors
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Configure SMTP credentials (replace with actual values)
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Initialize the notification system
    notifier = NotificationSystem(smtp_server, smtp_port, sender_email, sender_password)

    # Send a notification
    recipient_email = "user_email@example.com"
    user_name = "John Doe"
    notifier.send_notification(recipient_email, user_name)
```

> **Important:** Replace placeholder values like `smtp.example.com`, `your_email@example.com`, and `your_password` with your actual SMTP server details and credentials. Use environment variables or secure vaults to store sensitive information such as passwords in a production environment.
