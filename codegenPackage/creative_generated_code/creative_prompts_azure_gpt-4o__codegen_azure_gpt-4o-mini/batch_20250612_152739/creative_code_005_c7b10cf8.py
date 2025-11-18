"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Write a function to send automated email notifications to members about upcoming basketball events, inspired by the announcements on the "Grad košarke" website.
Generated: DETERMINISTIC_c7b10cf8523e4cce
Batch ID: 20250612_152739
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

class EmailNotification:
    def __init__(self, smtp_server: str, port: int, username: str, password: str):
        """
        Initializes the EmailNotification object with SMTP server details.
        
        :param smtp_server: The SMTP server address.
        :param port: The port number for the SMTP server.
        :param username: The email address used for sending emails.
        :param password: The password for the email account.
        """
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_event_notification(self, recipient_email: str, event_details: str):
        """
        Sends an event notification email to a specific recipient.
        
        :param recipient_email: The email address of the recipient.
        :param event_details: Details of the basketball event to notify.
        """
        # Create the email content
        subject = "Upcoming Basketball Event Notification"
        body = f"Dear Member,\n\nWe are excited to inform you about the upcoming event:\n\n{event_details}\n\nBest Regards,\nGrad košarke Team"

        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = self.username
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.sendmail(self.username, recipient_email, message.as_string())  # Send the email
                logging.info(f"Email sent successfully to {recipient_email}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

def main():
    # Example usage of the EmailNotification class
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    port = 587  # Common SMTP port for TLS
    username = 'your_email@example.com'  # Replace with your email
    password = 'your_password'  # Replace with your email password

    email_notifier = EmailNotification(smtp_server, port, username, password)

    # Example recipient and event details
    recipient_email = 'member@example.com'  # Replace with the recipient's email
    event_details = "Basketball Championship on March 5, 2024 at 5 PM. Venue: City Arena."

    # Send the event notification
    email_notifier.send_event_notification(recipient_email, event_details)

if __name__ == "__main__":
    main()
```
