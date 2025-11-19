"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Write code to automate the email notifications for Worldcoin invitation code usage and reward payments.
Generated: DETERMINISTIC_bf6e05cac1285153
Batch ID: 20250612_155651
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

# Configure logging for tracking errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the EmailNotifier with SMTP server details.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port used for the SMTP connection.
            sender_email (str): The email address that will send notifications.
            sender_password (str): The password for the sender email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email notification.

        Args:
            recipient_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Raises:
            Exception: If the email fails to send.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.sender_password)  # Login to the email server
                server.send_message(msg)  # Send the email

            logging.info("Email sent successfully to %s", recipient_email)

        except Exception as e:
            logging.error("Failed to send email to %s: %s", recipient_email, str(e))
            raise

def main():
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    SENDER_EMAIL = 'your-email@example.com'  # Replace with your sender email
    SENDER_PASSWORD = 'your-password'  # Replace with your password

    # Create an instance of EmailNotifier
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Sample data for demonstration
    recipient_email = 'recipient@example.com'  # Replace with recipient email
    subject = 'Worldcoin Invitation Code Usage'
    body = 'Your invitation code has been successfully used. Thank you for participating!'

    # Send email notification
    notifier.send_email(recipient_email, subject, body)

if __name__ == '__main__':
    main()
```
