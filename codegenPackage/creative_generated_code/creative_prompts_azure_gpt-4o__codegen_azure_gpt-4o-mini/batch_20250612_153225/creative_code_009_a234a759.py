"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://934ummfm.com
Prompt: Write a program to send automated email notifications using the contact email (radio.ummfm@gmail.com) for updates about UMM FM's events and broadcasts.
Generated: DETERMINISTIC_a234a7599c4d5159
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailNotifier with SMTP server details.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port to connect to the SMTP server.
            username (str): The email address to send from.
            password (str): The password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body, attachment=None):
        """
        Sends an email notification.

        Args:
            to_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body content of the email.
            attachment (str, optional): The path to a file to attach. Default is None.

        Raises:
            Exception: If sending the email fails.
        """
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Attach a file if provided
        if attachment:
            try:
                with open(attachment, "rb") as attachment_file:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment_file.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={attachment}')
                    msg.attach(part)
            except IOError as e:
                logging.error(f"Error attaching file: {e}")
                raise

        # Send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {to_email}")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email: {e}")
            raise

if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    USERNAME = "radio.ummfm@gmail.com"
    PASSWORD = "your_password_here"  # Replace with your actual password or use environment variables

    # Create an instance of EmailNotifier
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Email details
    TO_EMAIL = "recipient@example.com"  # Replace with the actual recipient's email
    SUBJECT = "UMM FM Event Update"
    BODY = "Hello, we have updates about our upcoming events and broadcasts. Stay tuned!"
    ATTACHMENT = None  # Specify file path if you want to attach a file

    # Send the email
    try:
        notifier.send_email(TO_EMAIL, SUBJECT, BODY, ATTACHMENT)
    except Exception as e:
        logging.error(f"Error occurred while sending email: {e}")
```
