"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Write code to implement a notification system for coordinating with institutions like Defensorías de la Niñez or the Ministry of Public Justice, as described in Fundación Munasim Kullakita's collaborative efforts.
Generated: DETERMINISTIC_7784616bcee1a0b5
Batch ID: 20250612_153224
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
import logging
from typing import List

# Configure logging to track application behavior and errors
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class NotificationSystem:
    """
    A notification system to coordinate with institutions like Defensorías de la Niñez or 
    the Ministry of Public Justice. Sends email notifications to designated recipients.
    """

    def __init__(self, smtp_server: str, port: int, sender_email: str, sender_password: str):
        """
        Initialize the notification system with SMTP server details.

        :param smtp_server: SMTP server address
        :param port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipients: List[str], subject: str, message_body: str):
        """
        Sends an email notification to a list of recipients.

        :param recipients: List of recipient email addresses
        :param subject: Subject of the email
        :param message_body: Body of the email
        """
        if not recipients:
            logging.error("Recipient list is empty. Notification cannot be sent.")
            return

        try:
            # Create a MIME message
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = ", ".join(recipients)
            msg["Subject"] = subject
            msg.attach(MIMEText(message_body, "plain"))

            # Connect to SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Enable encryption for the connection
                server.login(self.sender_email, self.sender_password)  # Log in to the SMTP server
                server.sendmail(self.sender_email, recipients, msg.as_string())  # Send the email

            logging.info(f"Notification sent successfully to: {', '.join(recipients)}")
        except Exception as e:
            logging.error(f"Failed to send notification. Error: {e}")

if __name__ == "__main__":
    # Example usage of the NotificationSystem class

    # SMTP server configuration
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@gmail.com"  # Replace with your sender email
    SENDER_PASSWORD = "your_password"  # Replace with your sender email password

    # Create an instance of NotificationSystem
    notifier = NotificationSystem(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Notification details
    recipients = ["recipient1@example.com", "recipient2@example.com"]
    subject = "Urgent Coordination Request"
    message_body = (
        "Dear recipients,\n\n"
        "We kindly request your immediate attention and assistance in addressing a matter related to child welfare. "
        "Please coordinate with Fundación Munasim Kullakita for further details.\n\n"
        "Best regards,\n"
        "Fundación Munasim Kullakita Team"
    )

    # Send the notification
    notifier.send_notification(recipients, subject, message_body)
```

Make sure to replace placeholders such as `your_email@gmail.com` and `your_password` with valid email credentials before running the code.
