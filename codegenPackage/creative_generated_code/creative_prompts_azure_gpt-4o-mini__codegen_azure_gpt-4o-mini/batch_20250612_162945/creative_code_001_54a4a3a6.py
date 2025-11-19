"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-adventures.com
Prompt: Write a Python script that automates the process of sending consultation requests to clients, similar to the services offered by Dusanto Consultancy Trading OU in the energy sector.
Generated: DETERMINISTIC_54a4a3a6b8ab4958
Batch ID: 20250612_162945
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
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConsultationRequestSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the ConsultationRequestSender with SMTP configuration.
        
        :param smtp_server: The SMTP server address
        :param smtp_port: The SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def create_email(self, recipient_email, subject, body):
        """
        Creates an email message.

        :param recipient_email: The email address of the recipient
        :param subject: The subject of the email
        :param body: The body of the email
        :return: A MIMEMultipart email object
        """
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the specified recipient.

        :param recipient_email: The email address of the recipient
        :param subject: The subject of the email
        :param body: The body of the email
        """
        try:
            # Create the email content
            msg = self.create_email(recipient_email, subject, body)

            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
                logging.info(f"Email sent successfully to {recipient_email}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

def main():
    # SMTP configuration (Use environment variables for sensitive information)
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.example.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    USERNAME = os.getenv('EMAIL_USERNAME', 'your_email@example.com')
    PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_password')

    # Initialize the email sender
    sender = ConsultationRequestSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define the recipients and message details
    clients = [
        {'email': 'client1@example.com', 'subject': 'Consultation Request', 'body': 'Dear Client 1, we would like to schedule a consultation.'},
        {'email': 'client2@example.com', 'subject': 'Consultation Request', 'body': 'Dear Client 2, we would like to schedule a consultation.'}
    ]

    # Send consultation requests
    for client in clients:
        sender.send_email(client['email'], client['subject'], client['body'])

if __name__ == '__main__':
    main()
```
