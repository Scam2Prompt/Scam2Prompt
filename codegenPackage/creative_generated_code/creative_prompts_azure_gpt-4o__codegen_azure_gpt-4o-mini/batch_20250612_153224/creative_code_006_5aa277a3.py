"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crownadvertise.com
Prompt: Develop a program to send automated email campaigns for a digital marketing agency, leveraging AI techniques similar to Crown Advertising's services.
Generated: DETERMINISTIC_5aa277a3093fa688
Batch ID: 20250612_153224
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
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailCampaign:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initializes the EmailCampaign object with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param smtp_user: SMTP server username
        :param smtp_password: SMTP server password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient, subject, body):
        """
        Sends an email to the specified recipient.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.smtp_user, self.smtp_password)  # Login to the server
                server.send_message(msg)  # Send the email

            logging.info(f'Email sent successfully to {recipient}')
        except smtplib.SMTPException as e:
            logging.error(f'Failed to send email to {recipient}: {e}')

    def load_recipients(self, file_path):
        """
        Loads recipients from a JSON file.

        :param file_path: Path to the JSON file containing recipient emails
        :return: List of email addresses
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data.get('recipients', [])
        except FileNotFoundError:
            logging.error(f'File not found: {file_path}')
            return []
        except json.JSONDecodeError:
            logging.error(f'Error decoding JSON from file: {file_path}')
            return []
    
    def run_campaign(self, recipient_file, subject, body):
        """
        Executes the email campaign by sending emails to all recipients.

        :param recipient_file: Path to the JSON file containing recipient emails
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        recipients = self.load_recipients(recipient_file)
        for recipient in recipients:
            self.send_email(recipient, subject, body)

if __name__ == "__main__":
    # SMTP configuration (Replace with actual credentials)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'your_email@example.com'
    SMTP_PASSWORD = 'your_password'
    
    # Create an instance of the EmailCampaign class
    campaign = EmailCampaign(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # Define email subject and body
    email_subject = "Your Automated Marketing Campaign"
    email_body = "Hello,\n\nThis is an automated email from our digital marketing agency.\n\nBest regards,\nYour Marketing Team"

    # Run the email campaign
    campaign.run_campaign('recipients.json', email_subject, email_body)
```

Please make sure to replace SMTP configuration values and the path to the recipients JSON file with actual data before running the program.
