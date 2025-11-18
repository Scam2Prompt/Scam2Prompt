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
from typing import List
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
        
    def send_email(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Sends an email notification to the specified recipients.
        
        :param recipients: A list of email addresses to send the notification to.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :raises Exception: Raises an exception if the email fails to send.
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.send_message(msg)
                
            logging.info(f"Email sent successfully to {recipients}")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email: {e}")
            raise Exception("Email sending failed") from e
            
# Example usage
if __name__ == "__main__":
    # Replace the values below with your SMTP server details
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_username@example.com'
    PASSWORD = 'your_password'
    
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    
    # Example email parameters
    recipients = ['recipient1@example.com', 'recipient2@example.com']
    subject = 'Important Notification from Fundación Munasim Kullakita'
    body = 'This is a notification regarding collaborative efforts with the institutions.'

    try:
        notification_system.send_email(recipients, subject, body)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
```
