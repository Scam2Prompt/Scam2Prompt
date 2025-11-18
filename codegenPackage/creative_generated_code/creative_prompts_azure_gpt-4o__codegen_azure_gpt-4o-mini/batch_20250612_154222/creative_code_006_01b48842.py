"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Implement a script that uses the LuFix.to Sender v1.0 configuration to send emails with debug mode enabled and logs the results.
Generated: DETERMINISTIC_01b488424edf416b
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    filename='email_sender.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password, debug_mode=False):
        """
        Initialize the EmailSender with SMTP server configuration.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Username for SMTP authentication
        :param password: Password for SMTP authentication
        :param debug_mode: Flag to enable debug mode
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.debug_mode = debug_mode

    def send_email(self, to_email, subject, body):
        """
        Send an email using the configured SMTP server.
        
        :param to_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        """
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the server
                
                # Send the email
                server.send_message(msg)
                logging.info(f"Email sent successfully to {to_email}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {to_email}: {e}")
            if self.debug_mode:
                print(f"Error: {e}")  # Print error in debug mode


# Example usage
if __name__ == "__main__":
    email_sender = EmailSender(
        smtp_server='smtp.example.com',
        smtp_port=587,
        username='your_username@example.com',
        password='your_password',
        debug_mode=True
    )

    email_sender.send_email(
        to_email='recipient@example.com',
        subject='Test Email',
        body='This is a test email sent using the LuFix.to Sender v1.0 configuration.'
    )
```
