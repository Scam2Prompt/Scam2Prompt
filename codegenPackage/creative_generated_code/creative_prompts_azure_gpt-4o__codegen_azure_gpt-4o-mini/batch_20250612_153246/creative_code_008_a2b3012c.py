"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visitabroadtravels.com.np
Prompt: Create a Python script to automate sending email inquiries to the contact email provided on the "Visit Abroad Travels" website.
Generated: DETERMINISTIC_a2b3012c5b0b0d9b
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
from typing import List
import logging

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the EmailSender with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email to the specified recipient with the given subject and body."""
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)  # Login to the server
                server.send_message(msg)
                logging.info(f'Email sent to {recipient} with subject: "{subject}"')
        except Exception as e:
            logging.error(f'Failed to send email: {e}')

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587                   # Commonly used port for TLS
    USERNAME = 'your_email@example.com'  # Replace with your email
    PASSWORD = 'your_password'          # Replace with your email password

    # Create an instance of EmailSender
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define email details
    recipient_email = 'contact@visitabroadtravels.com'  # Replace with the actual contact email
    subject = 'Inquiry about Travel Services'
    body = 'Hello,\n\nI would like to inquire about the travel services you offer. Please get back to me at your earliest convenience.\n\nThank you!\nBest regards,\n[Your Name]'

    # Send the email
    email_sender.send_email(recipient_email, subject, body)

if __name__ == '__main__':
    main()
```

Make sure to replace the placeholder values (SMTP server, port, username, and password) with valid credentials before running the script.
