"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Write code to integrate a notification system for pre-professional practice opportunities, similar to the "Convenio para prácticas Pre-Profesionales" described on the Trentino website.
Generated: DETERMINISTIC_e26592d72d6b29da
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the NotificationSystem with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email notification.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient} with subject: {subject}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}. Error: {e}")

    def notify_opportunities(self, opportunities: List[Dict[str, str]], recipients: List[str]) -> None:
        """
        Notifies recipients about pre-professional practice opportunities.

        :param opportunities: A list of opportunities, each represented as a dictionary with 'title' and 'description'.
        :param recipients: A list of email addresses to notify.
        """
        for opportunity in opportunities:
            subject = f"New Opportunity: {opportunity['title']}"
            body = f"Description: {opportunity['description']}\n\nApply now!"
            for recipient in recipients:
                self.send_email(recipient, subject, body)

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Sample opportunities
    opportunities = [
        {'title': 'Internship at Company A', 'description': 'An exciting internship opportunity at Company A.'},
        {'title': 'Volunteer Position at Organization B', 'description': 'Join us as a volunteer at Organization B.'}
    ]

    # List of recipients
    recipients = ['recipient1@example.com', 'recipient2@example.com']

    # Notify recipients about the opportunities
    notification_system.notify_opportunities(opportunities, recipients)
```
