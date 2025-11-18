"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitechcareindia.com
Prompt: Write a Python script for automating email marketing campaigns, inspired by the email marketing solutions offered by DigiTech Care India.
Generated: DETERMINISTIC_99c2d8ded096352a
Batch ID: 20250612_151403
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
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='email_campaign.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class EmailCampaign:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailCampaign with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port for the SMTP server
        :param username: The SMTP username
        :param password: The SMTP password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def create_email(self, recipient_email, subject, body):
        """
        Creates an email message.

        :param recipient_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        :return: The email message object
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            return msg
        except Exception as e:
            logging.error(f"Error creating email: {e}")
            raise

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the specified recipient.

        :param recipient_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        """
        try:
            # Create email message
            msg = self.create_email(recipient_email, subject, body)
            
            # Set up the server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient_email}")
        except Exception as e:
            logging.error(f"Error sending email to {recipient_email}: {e}")

    def load_recipients(self, file_path):
        """
        Loads the recipients from a CSV file.

        :param file_path: Path to the CSV file containing email addresses
        :return: List of email addresses
        """
        try:
            df = pd.read_csv(file_path)
            recipients = df['email'].tolist()
            return recipients
        except Exception as e:
            logging.error(f"Error loading recipients from {file_path}: {e}")
            raise

    def run_campaign(self, recipients_file, subject, body):
        """
        Executes the email marketing campaign.

        :param recipients_file: Path to the CSV file with recipient emails
        :param subject: The subject of the emails
        :param body: The body content of the emails
        """
        try:
            recipients = self.load_recipients(recipients_file)
            for email in recipients:
                self.send_email(email, subject, body)
        except Exception as e:
            logging.error(f"Error running email campaign: {e}")

if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_email_password'
    
    # Email campaign details
    RECIPIENTS_FILE = 'recipients.csv'
    EMAIL_SUBJECT = 'Your Marketing Subject Here'
    EMAIL_BODY = 'Hello,\n\nThis is a test email from our marketing campaign.\n\nBest regards,\nDigiTech Care India'

    # Initiate the email campaign
    campaign = EmailCampaign(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    campaign.run_campaign(RECIPIENTS_FILE, EMAIL_SUBJECT, EMAIL_BODY)
```
