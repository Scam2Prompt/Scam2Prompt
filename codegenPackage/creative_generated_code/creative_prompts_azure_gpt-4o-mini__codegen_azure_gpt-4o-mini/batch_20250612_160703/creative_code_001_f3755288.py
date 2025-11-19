"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bytnox.com
Prompt: Write a Python script that automates the process of sending project updates to clients using the features described on bytnox.com.
Generated: DETERMINISTIC_f3755288d5a5f463
Batch ID: 20250612_160703
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

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    """
    A class to send emails using SMTP.
    """
    
    def __init__(self, smtp_server: str, port: int, username: str, password: str):
        """
        Initializes the EmailSender with SMTP server details.

        :param smtp_server: SMTP server address
        :param port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, subject: str, body: str, recipients: List[str]) -> None:
        """
        Sends an email with the specified subject and body to the given recipients.

        :param subject: Subject of the email
        :param body: Body content of the email
        :param recipients: List of recipient email addresses
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
                logging.info(f'Email sent successfully to: {recipients}')
        except Exception as e:
            logging.error(f'Failed to send email. Error: {str(e)}')

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    PORT = 587  # SMTP port (typically 587 for TLS)
    USERNAME = 'your_email@example.com'  # Replace with your email
    PASSWORD = 'your_password'  # Replace with your email password

    # Create an instance of EmailSender
    email_sender = EmailSender(SMTP_SERVER, PORT, USERNAME, PASSWORD)

    # Email details
    subject = 'Project Update'
    body = 'Dear Client,\n\nHere is the latest update on your project...\n\nBest Regards,\nYour Company'
    recipients = ['client1@example.com', 'client2@example.com']  # List of client email addresses

    # Send the update email
    email_sender.send_email(subject, body, recipients)

if __name__ == '__main__':
    main()
```
