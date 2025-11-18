"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afebi.org
Prompt: Write code to send automated email notifications to AFEBI members about upcoming events like "Workshop Platform OpenEdX" using the contact information provided on the website.
Generated: DETERMINISTIC_b2a9713369f46c9d
Batch ID: 20250612_153526
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotification:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initializes the EmailNotification with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Sends an email to a specified recipient.

        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Set up the SMTP server connection
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.sender_password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email
                logging.info(f'Email sent to {recipient_email}')

        except Exception as e:
            logging.error(f'Failed to send email to {recipient_email}: {e}')

def send_event_notifications(members: List[str], event_name: str, event_details: str, email_config: dict) -> None:
    """
    Sends event notifications to a list of members.

    :param members: List of member email addresses
    :param event_name: Name of the event
    :param event_details: Details of the event
    :param email_config: Configuration for the email server
    """
    subject = f'Upcoming Event: {event_name}'
    body = f'Dear AFEBI Member,\n\nWe are excited to inform you about an upcoming event:\n\n{event_name}\n\nDetails:\n{event_details}\n\nBest Regards,\nAFEBI Team'
    
    # Initialize the EmailNotification instance
    email_notifier = EmailNotification(
        smtp_server=email_config['smtp_server'],
        smtp_port=email_config['smtp_port'],
        sender_email=email_config['sender_email'],
        sender_password=email_config['sender_password']
    )
    
    for member in members:
        email_notifier.send_email(member, subject, body)

# Example usage
if __name__ == "__main__":
    member_emails = ['member1@example.com', 'member2@example.com']  # Replace with actual member emails
    event_name = 'Workshop Platform OpenEdX'
    event_details = 'Join us for an informative workshop on the OpenEdX platform on March 15, 2023 at 10 AM.'
    
    email_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'sender_email': 'your_email@example.com',
        'sender_password': 'your_password'  # Use environment variables for security in production
    }
    
    send_event_notifications(member_emails, event_name, event_details, email_config)
```
