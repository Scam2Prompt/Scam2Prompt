"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tda.org.sa
Prompt: Provide a Python script to send automated email notifications to stakeholders about upcoming community programs and initiatives, using the contact information format provided on the Tabuk Community Development Association website.
Generated: DETERMINISTIC_a8c42c2bba769658
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server, smtp_port, username, password):
        """Initialize the EmailNotifier with SMTP server settings."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, subject, body, recipients):
        """Send an email notification to the specified recipients.

        Args:
            subject (str): The subject line of the email.
            body (str): The body content of the email.
            recipients (list): A list of email addresses to send the notification to.

        Raises:
            Exception: Raises an exception if sending the email fails.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ", ".join(recipients)
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f'Email sent successfully to: {recipients}')

        except Exception as e:
            logging.error(f'Failed to send email: {e}')
            raise

def main():
    # Load environment variables for sensitive data
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = int(os.getenv('SMTP_PORT'))
    USERNAME = os.getenv('EMAIL_USERNAME')
    PASSWORD = os.getenv('EMAIL_PASSWORD')

    # Initialize email notifier
    email_notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define email details
    subject = "Upcoming Community Programs and Initiatives"
    body = """Dear Stakeholder,

We are excited to inform you about the upcoming community programs and initiatives. Stay tuned for more details!

Best regards,
Tabuk Community Development Association
"""
    
    # List of stakeholders' email addresses
    recipients = [
        "stakeholder1@example.com",
        "stakeholder2@example.com",
        # Add more email addresses as needed
    ]

    # Send email notification
    try:
        email_notifier.send_email(subject, body, recipients)
    except Exception as e:
        logging.error(f"An error occurred while sending notifications: {e}")

if __name__ == "__main__":
    main()
```

Make sure to set the environment variables `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_USERNAME`, and `EMAIL_PASSWORD` before running the script.
