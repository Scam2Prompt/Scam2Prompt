"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-partners.com
Prompt: Provide instructions for setting up email hosting using Xserver's hosting services.
Generated: DETERMINISTIC_b87e63ca76bbbbb1
Batch ID: 20250612_150342
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

class EmailSetup:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailSetup with SMTP server settings.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port for the SMTP server
        :param username: The email account username
        :param password: The email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        """
        Sends an email using the configured SMTP server.

        :param to_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        """
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(msg)  # Send the email
                logging.info("Email sent successfully to %s", to_email)
        except smtplib.SMTPException as e:
            logging.error("Failed to send email: %s", e)

# Example usage
if __name__ == "__main__":
    # Replace with your actual SMTP server details and credentials
    SMTP_SERVER = 'smtp.xserver.com'
    SMTP_PORT = 587
    USERNAME = 'your-email@domain.com'
    PASSWORD = 'your-password'

    email_setup = EmailSetup(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    
    # Example email details
    TO_EMAIL = 'recipient@example.com'
    SUBJECT = 'Test Email'
    BODY = 'This is a test email sent using Xserver email hosting.'

    email_setup.send_email(TO_EMAIL, SUBJECT, BODY)
```
