"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Write code to implement a feature that sends automated email updates about car rental promotions and available accommodations in nearby areas like Catania, Etna, and Giardini Naxos.
Generated: DETERMINISTIC_e0bcb23e8c603943
Batch ID: 20250612_153225
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailSender with SMTP server details.
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the specified recipient.
        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Establish connection to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            
            logging.info(f"Email sent to {recipient_email} successfully.")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {str(e)}")

def main():
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Typically 587 for TLS
    USERNAME = 'your-email@example.com'  # Replace with your email
    PASSWORD = 'your-email-password'  # Replace with your email password

    # Create an instance of EmailSender
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of recipients
    recipients = [
        'customer1@example.com',
        'customer2@example.com',
        'customer3@example.com'
    ]

    # Email content
    subject = "Exciting Car Rental Promotions!"
    body = """
    Dear valued customer,

    We are excited to inform you about our latest car rental promotions and available accommodations in nearby areas like Catania, Etna, and Giardini Naxos.

    Don't miss out on these fantastic deals!

    Best regards,
    Your Car Rental Team
    """

    # Send emails to all recipients
    for recipient in recipients:
        email_sender.send_email(recipient, subject, body)

if __name__ == "__main__":
    main()
```

Make sure to replace the SMTP server details, username, and password with your actual email account information before running this code.
