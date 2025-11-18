"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadihonlineex.com
Prompt: Write code to implement a notification system for tracking money transfers, inspired by the features of Dadih Online Exchange's services.
Generated: DETERMINISTIC_2b229522824fed8b
Batch ID: 20250612_153246
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
from datetime import datetime
import logging
from typing import List, Dict

# Configure logging for tracking purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the notification system with SMTP server details.
        
        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port for the SMTP server.
            username (str): Username for SMTP authentication.
            password (str): Password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification.
        
        Args:
            recipient (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body content of the email.
        
        Raises:
            Exception: If there is an issue sending the email.
        """
        try:
            # Create a multipart message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # Create a secure SSL context and send the email
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f'Email sent to {recipient} with subject: {subject}')

        except Exception as e:
            logging.error(f'Failed to send email to {recipient}: {e}')
            raise

    def notify_transfer(self, transfer_details: Dict) -> None:
        """
        Notify about a money transfer.
        
        Args:
            transfer_details (Dict): A dictionary containing transfer details.
                Expected keys: 'recipient_email', 'amount', 'currency', 'timestamp', 'status'.
        
        Raises:
            ValueError: If transfer details are missing or invalid.
        """
        # Validate transfer details
        required_keys = ['recipient_email', 'amount', 'currency', 'timestamp', 'status']
        if not all(key in transfer_details for key in required_keys):
            raise ValueError('Missing transfer details')

        # Prepare email content
        recipient = transfer_details['recipient_email']
        amount = transfer_details['amount']
        currency = transfer_details['currency']
        timestamp = transfer_details['timestamp']
        status = transfer_details['status']

        subject = f'Notification: Money Transfer of {amount} {currency}'
        body = (f'Dear User,\n\n'
                f'Your money transfer of {amount} {currency} has been processed.\n'
                f'Transfer Status: {status}\n'
                f'Transfer Time: {timestamp}\n\n'
                f'Thank you for using our service!\n')

        # Send the email notification
        self.send_email(recipient, subject, body)

# Example usage
if __name__ == "__main__":
    smtp_settings = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 465,
        'username': 'your_email@example.com',
        'password': 'your_password'
    }

    notification_system = NotificationSystem(**smtp_settings)

    # Example transfer details
    transfer_info = {
        'recipient_email': 'recipient@example.com',
        'amount': 100,
        'currency': 'USD',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'status': 'Completed'
    }

    # Notify about the transfer
    try:
        notification_system.notify_transfer(transfer_info)
    except Exception as e:
        logging.error(f'Error notifying transfer: {e}')
```
