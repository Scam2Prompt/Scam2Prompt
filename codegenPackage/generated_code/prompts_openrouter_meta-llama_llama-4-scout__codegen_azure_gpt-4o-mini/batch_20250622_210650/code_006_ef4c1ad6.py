"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Generate a sample code for automating the process of sending enquiries for spares and consumables to Aayra International Limited using their contact information.
Generated: DETERMINISTIC_ef4c1ad6fd4ddf53
Batch ID: 20250622_210650
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
from email.utils import formataddr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SpareEnquirySender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the SpareEnquirySender with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port for the SMTP server
        :param username: The username for SMTP authentication
        :param password: The password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_enquiry(self, recipient_email, subject, message):
        """
        Sends an email enquiry to the specified recipient.

        :param recipient_email: The email address of the recipient
        :param subject: The subject of the email
        :param message: The body of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = formataddr((self.username, self.username))
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the message body
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Enquiry sent to {recipient_email} successfully.")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send enquiry: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    USERNAME = 'your_email@example.com'  # Replace with your email
    PASSWORD = 'your_password'  # Replace with your email password

    # Recipient details
    RECIPIENT_EMAIL = 'contact@aayrainternational.com'  # Aayra International Limited contact email
    SUBJECT = 'Enquiry for Spares and Consumables'
    MESSAGE = """\
    Dear Aayra International Limited,

    I would like to inquire about the availability of spares and consumables. 
    Please provide me with the necessary details at your earliest convenience.

    Thank you.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """

    # Create an instance of SpareEnquirySender and send the enquiry
    enquiry_sender = SpareEnquirySender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    enquiry_sender.send_enquiry(RECIPIENT_EMAIL, SUBJECT, MESSAGE)
```
