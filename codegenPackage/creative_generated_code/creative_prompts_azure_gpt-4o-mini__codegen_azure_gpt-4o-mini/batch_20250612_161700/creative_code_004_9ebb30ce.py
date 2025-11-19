"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Write a script to automate the process of sending inquiries about specialized cargo transport services, like those provided by OPC, using their contact information and service offerings.
Generated: DETERMINISTIC_9ebb30ce8b2dd8cf
Batch ID: 20250612_161700
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

class CargoInquirySender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the CargoInquirySender with SMTP server details.
        
        :param smtp_server: The SMTP server to use for sending emails.
        :param smtp_port: The port to connect to the SMTP server.
        :param username: The username for the email account.
        :param password: The password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def create_email(self, recipient_email, subject, body):
        """
        Create an email message.
        
        :param recipient_email: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body of the email.
        :return: A MIMEMultipart email message.
        """
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def send_email(self, recipient_email, subject, body):
        """
        Send an email to the specified recipient.
        
        :param recipient_email: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body of the email.
        """
        try:
            msg = self.create_email(recipient_email, subject, body)
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
            logging.info(f"Email sent to {recipient_email} successfully.")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    USERNAME = 'your_email@example.com'  # Replace with your email
    PASSWORD = 'your_password'  # Replace with your email password

    # Create an instance of CargoInquirySender
    inquiry_sender = CargoInquirySender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Inquiry details
    recipient_email = 'contact@opc.com'  # Replace with the recipient's email
    subject = 'Inquiry about Specialized Cargo Transport Services'
    body = (
        "Dear OPC Team,\n\n"
        "I am writing to inquire about your specialized cargo transport services. "
        "Could you please provide information regarding your offerings, pricing, and availability?\n\n"
        "Thank you!\n\n"
        "Best regards,\n"
        "Your Name\n"
        "Your Company\n"
        "Your Contact Information"
    )

    # Send the inquiry email
    inquiry_sender.send_email(recipient_email, subject, body)

if __name__ == '__main__':
    main()
```
