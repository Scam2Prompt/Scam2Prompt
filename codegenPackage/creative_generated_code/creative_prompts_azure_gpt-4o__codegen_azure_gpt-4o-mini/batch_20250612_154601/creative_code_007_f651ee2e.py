"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Write Python code to automate email marketing campaigns for a business website, incorporating the targeted communication strategies outlined by Solutech System's email marketing services.
Generated: DETERMINISTIC_f651ee2e8a997ad8
Batch ID: 20250612_154601
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
import csv
import logging
from typing import List, Dict

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailCampaign:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailCampaign with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email to the specified recipient.

        :param recipient: Email address of the recipient
        :param subject: Subject line for the email
        :param body: Body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the body of the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def load_recipients(self, filepath: str) -> List[Dict[str, str]]:
        """
        Load recipient data from a CSV file.

        :param filepath: Path to the CSV file containing recipient data
        :return: List of dictionaries containing recipient information
        """
        recipients = []
        try:
            with open(filepath, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    recipients.append(row)
            logging.info(f"Loaded {len(recipients)} recipients from {filepath}")
        except FileNotFoundError:
            logging.error(f"File not found: {filepath}")
        except Exception as e:
            logging.error(f"Error loading recipients: {e}")
        return recipients

    def run_campaign(self, recipients_filepath: str, subject: str, body_template: str) -> None:
        """
        Run the email marketing campaign.

        :param recipients_filepath: Path to the CSV file with recipient data
        :param subject: Subject line for the email
        :param body_template: Template for the email body
        """
        recipients = self.load_recipients(recipients_filepath)
        for recipient in recipients:
            recipient_email = recipient.get('email')
            if recipient_email:
                body = body_template.format(**recipient)  # Format the body with recipient details
                self.send_email(recipient_email, subject, body)

# Example usage:
if __name__ == "__main__":
    # SMTP server configuration (example)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of EmailCampaign
    campaign = EmailCampaign(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define the subject and body template
    SUBJECT = "Exciting News from Solutech System!"
    BODY_TEMPLATE = """
    Hello {name},

    We are excited to share with you our latest updates and offers at Solutech System!
    
    Best Regards,
    The Solutech Team
    """

    # Run the campaign
    campaign.run_campaign('recipients.csv', SUBJECT, BODY_TEMPLATE)
```
