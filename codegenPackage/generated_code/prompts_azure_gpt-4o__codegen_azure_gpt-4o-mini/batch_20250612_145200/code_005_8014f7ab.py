"""
Generated Code Metadata:
========================
Original URL: https://wombat-exchange.rf.gd
Prompt: Create a guide for setting up email accounts on iFastNet hosting and integrating them with a web application.
Generated: DETERMINISTIC_8014f7ab75d1078d
Batch ID: 20250612_145200
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
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailClient:
    """
    A class to represent an email client for sending emails through iFastNet hosting.
    """

    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailClient with SMTP server details and user credentials.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port for the SMTP server
        :param username: The email account username
        :param password: The email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body, attachment_path=None):
        """
        Sends an email with the specified subject and body to the given recipient.

        :param to_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        :param attachment_path: Optional path to a file to attach to the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Attach a file if provided
            if attachment_path:
                self._attach_file(msg, attachment_path)

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {to_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {to_email}: {e}")

    def _attach_file(self, msg, file_path):
        """
        Attaches a file to the email message.

        :param msg: The email message object
        :param file_path: The path to the file to attach
        """
        try:
            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={file_path}')
                msg.attach(part)
                logging.info(f"Attached file: {file_path}")
        except Exception as e:
            logging.error(f"Failed to attach file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your iFastNet SMTP server details and email credentials
    SMTP_SERVER = 'mail.yourdomain.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@yourdomain.com'
    PASSWORD = 'your_password'

    email_client = EmailClient(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    email_client.send_email(
        to_email='recipient@example.com',
        subject='Test Email',
        body='This is a test email sent from the iFastNet email client.',
        attachment_path='path/to/your/file.txt'  # Optional
    )
```
