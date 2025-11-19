"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: Generate a script to automate email marketing campaigns, ensuring tailored content delivery as described in Rankraze's email marketing services.
Generated: DETERMINISTIC_2dc802ef6e39c2c4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from typing import List, Dict

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
        Send an email to a specified recipient.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'html'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            print(f"Email sent successfully to {recipient}")

        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {e}")

    def create_campaign(self, recipients: List[Dict[str, str]], subject: str, template: str) -> None:
        """
        Create and send a tailored email campaign to a list of recipients.

        :param recipients: List of dictionaries containing recipient details
        :param subject: Subject of the email
        :param template: HTML template for the email body
        """
        for recipient in recipients:
            try:
                # Personalize the email body using the recipient's data
                personalized_body = template.format(**recipient)
                self.send_email(recipient['email'], subject, personalized_body)
            except KeyError as e:
                print(f"Missing key in recipient data: {e}")
            except Exception as e:
                print(f"Error processing recipient {recipient['email']}: {e}")

def load_recipients(file_path: str) -> List[Dict[str, str]]:
    """
    Load recipient data from a CSV file.

    :param file_path: Path to the CSV file containing recipient data
    :return: List of dictionaries with recipient details
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        # Convert DataFrame to a list of dictionaries
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error loading recipients from {file_path}: {e}")
        return []

if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Load recipients from a CSV file
    recipients = load_recipients('recipients.csv')

    # Define the email subject and template
    SUBJECT = "Your Personalized Offer"
    EMAIL_TEMPLATE = """
    <html>
        <body>
            <h1>Hello {name},</h1>
            <p>We have a special offer just for you!</p>
            <p>Best regards,<br>Your Company</p>
        </body>
    </html>
    """

    # Create an instance of EmailCampaign and send the campaign
    campaign = EmailCampaign(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    campaign.create_campaign(recipients, SUBJECT, EMAIL_TEMPLATE)
```
