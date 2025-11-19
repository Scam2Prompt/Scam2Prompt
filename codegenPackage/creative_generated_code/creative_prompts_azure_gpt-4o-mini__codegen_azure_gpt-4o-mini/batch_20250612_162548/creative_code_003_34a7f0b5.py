"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimsteth.net
Prompt: Generate a Python script that utilizes the 126网易邮箱 features for sending automated emails.
Generated: DETERMINISTIC_34a7f0b585ef4a41
Batch ID: 20250612_162548
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
from email.utils import formataddr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server, port, username, password):
        """
        Initializes the EmailSender with SMTP server details.

        :param smtp_server: SMTP server address
        :param port: Port for the SMTP server
        :param username: Username for authentication
        :param password: Password for authentication
        """
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, subject, recipient_email, body):
        """
        Sends an email with the specified subject and body to the recipient.

        :param subject: Subject of the email
        :param recipient_email: Recipient's email address
        :param body: Body of the email
        :raises Exception: Raises an exception if sending fails
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = formataddr((self.username, self.username))
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Login to the SMTP server
                server.sendmail(self.username, recipient_email, msg.as_string())  # Send the email

            logging.info(f"Email sent to {recipient_email} successfully.")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    SMTP_SERVER = 'smtp.126.com'  # SMTP server for 126网易邮箱
    PORT = 587  # Port for TLS
    USERNAME = 'your_email@126.com'  # Your 126邮箱 email address
    PASSWORD = 'your_password'  # Your 126邮箱 email password

    email_sender = EmailSender(SMTP_SERVER, PORT, USERNAME, PASSWORD)
    
    subject = "Test Email"
    recipient = "recipient@example.com"  # Replace with actual recipient email
    body = "This is a test email sent from a Python script using 126网易邮箱."

    try:
        email_sender.send_email(subject, recipient, body)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
