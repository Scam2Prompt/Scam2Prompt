"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexium-ai-system.com
Prompt: Create a script to automate sending personalized email notifications to users after registration, following the Apexium AI onboarding process.
Generated: DETERMINISTIC_59c50f76bbf6dc07
Batch ID: 20250612_150048
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    """
    A class to send personalized email notifications to users.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailNotifier with SMTP server settings.

        :param smtp_server: The SMTP server address
        :param smtp_port: The SMTP server port
        :param username: Username for SMTP authentication
        :param password: Password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email: str, user_name: str):
        """
        Sends a personalized email notification to the specified recipient.

        :param recipient_email: The email address of the recipient
        :param user_name: The name of the user to personalize the email
        """
        subject = "Welcome to Apexium AI!"
        body = f"Dear {user_name},\n\nThank you for registering with Apexium AI! We are excited to have you on board.\n\nBest regards,\nApexium AI Team"

        # Create the email message
        message = MIMEMultipart()
        message['From'] = self.username
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Attach the email body to the message
        message.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(message)  # Send the email
                logging.info(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}. Error: {str(e)}")

def main():
    """
    Main function to send email notifications after user registration.
    """
    # Example SMTP configuration (use your SMTP server details)
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your-email@example.com"
    password = "your-email-password"

    # List of registered users
    registered_users = [
        {"email": "user1@example.com", "name": "User One"},
        {"email": "user2@example.com", "name": "User Two"},
    ]

    # Initialize the EmailNotifier
    email_notifier = EmailNotifier(smtp_server, smtp_port, username, password)

    # Send email notifications
    for user in registered_users:
        email_notifier.send_email(user["email"], user["name"])

if __name__ == "__main__":
    main()
```
