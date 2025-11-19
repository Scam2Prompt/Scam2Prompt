"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-sync.com
Prompt: What are the steps to develop a reactivation campaign for former clients using the automation services offered by Sync Media?
Generated: DETERMINISTIC_b37f8ad6fa8c515e
Batch ID: 20250612_163218
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
from datetime import datetime, timedelta
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReactivationCampaign:
    def __init__(self, client_data_file, email_server, email_port, email_user, email_password):
        """
        Initialize the reactivation campaign with client data and email server configuration.
        
        :param client_data_file: Path to the JSON file containing client data
        :param email_server: SMTP server address for sending emails
        :param email_port: Port for the SMTP server
        :param email_user: Username for the SMTP server
        :param email_password: Password for the SMTP server
        """
        self.client_data_file = client_data_file
        self.email_server = email_server
        self.email_port = email_port
        self.email_user = email_user
        self.email_password = email_password
        self.clients = self.load_client_data()

    def load_client_data(self):
        """
        Load client data from a JSON file.
        
        :return: List of clients
        """
        try:
            with open(self.client_data_file, 'r') as file:
                clients = json.load(file)
                logging.info("Client data loaded successfully.")
                return clients
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error loading client data: {e}")
            return []

    def filter_inactive_clients(self, days_inactive=30):
        """
        Filter clients who have been inactive for a specified number of days.
        
        :param days_inactive: Number of days to determine inactivity
        :return: List of inactive clients
        """
        threshold_date = datetime.now() - timedelta(days=days_inactive)
        inactive_clients = [
            client for client in self.clients 
            if datetime.strptime(client['last_active'], '%Y-%m-%d') < threshold_date
        ]
        logging.info(f"Filtered {len(inactive_clients)} inactive clients.")
        return inactive_clients

    def send_email(self, recipient_email, subject, body):
        """
        Send an email to a specified recipient.
        
        :param recipient_email: Email address of the recipient
        :param subject: Subject line of the email
        :param body: Body content of the email
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.email_server, self.email_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email_user, self.email_password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {recipient_email}.")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def launch_campaign(self):
        """
        Launch the reactivation campaign by sending emails to inactive clients.
        """
        inactive_clients = self.filter_inactive_clients()
        subject = "We Miss You at Sync Media!"
        body_template = (
            "Dear {name},\n\n"
            "We've noticed you've been away for a while. We value you as our client and would love to have you back!\n"
            "Here are some updates and offers just for you:\n\n"
            "- Exclusive discounts\n"
            "- New features\n"
            "- Personalized services\n\n"
            "We hope to see you soon!\n\n"
            "Best regards,\n"
            "The Sync Media Team"
        )

        for client in inactive_clients:
            body = body_template.format(name=client['name'])
            self.send_email(client['email'], subject, body)

# Example of using the ReactivationCampaign class
if __name__ == "__main__":
    campaign = ReactivationCampaign(
        client_data_file='clients.json',
        email_server='smtp.example.com',
        email_port=587,
        email_user='your_email@example.com',
        email_password='your_password'
    )
    campaign.launch_campaign()
```
