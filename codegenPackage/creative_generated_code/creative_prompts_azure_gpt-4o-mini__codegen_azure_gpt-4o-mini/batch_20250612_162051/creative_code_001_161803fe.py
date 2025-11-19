"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bee-property.com
Prompt: Write a Python script that automates communication with guests, ensuring 24/7 customer service like Bee Property offers.
Generated: DETERMINISTIC_161803fe92749509
Batch ID: 20250612_162051
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
import time
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GuestCommunication:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initialize the communication system with SMTP server details.
        
        :param smtp_server: str: SMTP server address
        :param smtp_port: int: SMTP server port
        :param smtp_user: str: SMTP username
        :param smtp_password: str: SMTP password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient_email, subject, message):
        """
        Send an email to a guest.

        :param recipient_email: str: Recipient's email address
        :param subject: str: Subject of the email
        :param message: str: Body of the email
        :raises Exception: If email sending fails
        """
        try:
            # Prepare the email
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Connect to SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
                logging.info(f'Email sent to {recipient_email} with subject "{subject}"')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient_email}: {e}')
            raise

    def automate_communication(self, guest_list):
        """
        Automate communication with guests.

        :param guest_list: list: List of tuples containing guest email and message
        """
        while True:
            for guest_email, message in guest_list:
                subject = "Welcome to Bee Property!"
                try:
                    self.send_email(guest_email, subject, message)
                except Exception as e:
                    logging.error(f'Error communicating with guest {guest_email}: {e}')
            time.sleep(3600)  # Wait for an hour before sending the next round of emails

if __name__ == "__main__":
    # Sample SMTP configuration - Please update with real credentials
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'your_email@example.com'
    SMTP_PASSWORD = 'your_password'

    # Sample guest list with email and welcome message
    guests = [
        ('guest1@example.com', 'Dear Guest 1, welcome to our property!'),
        ('guest2@example.com', 'Dear Guest 2, we hope you enjoy your stay!'),
    ]

    # Create an instance of the GuestCommunication class and start communication
    guest_communication = GuestCommunication(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
    try:
        guest_communication.automate_communication(guests)
    except KeyboardInterrupt:
        logging.info("Communication automation stopped by user.")
```
