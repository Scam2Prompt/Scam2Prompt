"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egrowmax.com
Prompt: Write a Python script to automate email marketing campaigns leveraging the CRM strategies mentioned on Egrowmax.
Generated: DETERMINISTIC_33cc41ca9f441aff
Batch ID: 20250612_160454
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailMarketingCampaign:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_pass):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_pass = smtp_pass

    def send_email(self, recipient_email, subject, body):
        """Sends an email to a single recipient."""
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Use TLS for security
                server.login(self.smtp_user, self.smtp_pass)
                server.sendmail(self.smtp_user, recipient_email, msg.as_string())
                logging.info(f"Email sent successfully to {recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def load_contacts(self, csv_file):
        """Loads contacts from a CSV file."""
        contacts = []
        try:
            with open(csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contacts.append(row['email'])  # Assuming the CSV has an 'email' field
            logging.info(f"Loaded {len(contacts)} contacts from {csv_file}")
        except Exception as e:
            logging.error(f"Error loading contacts from {csv_file}: {e}")
        return contacts

    def run_campaign(self, csv_file, subject, body):
        """Runs the email marketing campaign."""
        contacts = self.load_contacts(csv_file)
        for email in contacts:
            self.send_email(email, subject, body)

if __name__ == "__main__":
    # SMTP server configuration (replace with your own credentials)
    SMTP_SERVER = 'smtp.your-email-provider.com'
    SMTP_PORT = 587
    SMTP_USER = 'your-email@example.com'
    SMTP_PASS = 'your-email-password'

    # Create an instance of the EmailMarketingCampaign class
    campaign = EmailMarketingCampaign(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS)

    # Define campaign details
    CSV_FILE = 'contacts.csv'  # Path to the CSV file containing email addresses
    SUBJECT = 'Your Subject Here'
    BODY = 'This is the body of the email.'

    # Run the email marketing campaign
    campaign.run_campaign(CSV_FILE, SUBJECT, BODY)
```
