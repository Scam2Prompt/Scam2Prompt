"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Provide a solution for creating a scalable telemarketing system to improve customer acquisition and retention, based on Vital Corporate Solutions' sales and marketing services.
Generated: DETERMINISTIC_6f8eb15340834a52
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Any
from random import choice

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TelemarketingSystem:
    def __init__(self, email_server: str, email_port: int, email_address: str, email_password: str):
        """
        Initialize the TelemarketingSystem with email server configuration.
        
        :param email_server: SMTP server address
        :param email_port: SMTP server port
        :param email_address: Sender's email address
        :param email_password: Sender's email password
        """
        self.email_server = email_server
        self.email_port = email_port
        self.email_address = email_address
        self.email_password = email_password
        self.leads = []  # List to store leads
        self.email_client = None

    def connect_email_server(self):
        """Connect to the email server."""
        try:
            self.email_client = smtplib.SMTP(self.email_server, self.email_port)
            self.email_client.starttls()  # Secure the connection
            self.email_client.login(self.email_address, self.email_password)
            logging.info("Successfully connected to the email server.")
        except Exception as e:
            logging.error(f"Failed to connect to the email server: {e}")
            raise

    def add_leads(self, leads: List[Dict[str, Any]]):
        """
        Add leads to the telemarketing system.
        
        :param leads: List of leads, each represented as a dictionary with keys 'name' and 'email'
        """
        self.leads.extend(leads)
        logging.info(f"Added {len(leads)} leads to the system.")

    def send_email(self, recipient: str, subject: str, message: str):
        """
        Send an email to a recipient.
        
        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param message: Body of the email
        """
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.email_address
            msg['To'] = recipient
            
            self.email_client.sendmail(self.email_address, [recipient], msg.as_string())
            logging.info(f"Email sent to {recipient}.")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def execute_campaign(self, subject: str, message: str):
        """
        Execute an email campaign to all leads.
        
        :param subject: Subject of the campaign email
        :param message: Body of the campaign email
        """
        if not self.leads:
            logging.warning("No leads available to send emails.")
            return
        
        for lead in self.leads:
            self.send_email(lead['email'], subject, message)

    def close_email_server(self):
        """Close the email server connection."""
        try:
            if self.email_client:
                self.email_client.quit()
                logging.info("Email server connection closed.")
        except Exception as e:
            logging.error(f"Failed to close email server connection: {e}")

# Example usage of the TelemarketingSystem
if __name__ == "__main__":
    # Configure with your SMTP settings
    EMAIL_SERVER = 'smtp.example.com'
    EMAIL_PORT = 587
    EMAIL_ADDRESS = 'your_email@example.com'
    EMAIL_PASSWORD = 'your_password'

    telemarketing_system = TelemarketingSystem(EMAIL_SERVER, EMAIL_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    try:
        telemarketing_system.connect_email_server()
        
        # Sample leads
        leads = [
            {'name': 'John Doe', 'email': 'john@example.com'},
            {'name': 'Jane Smith', 'email': 'jane@example.com'},
        ]
        
        telemarketing_system.add_leads(leads)
        
        # Prepare and send an email campaign
        subject = "Exclusive Offer Just for You!"
        message = "Dear Customer,\n\nWe have an exclusive offer just for you!\n\nBest regards,\nVital Corporate Solutions"
        
        telemarketing_system.execute_campaign(subject, message)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        telemarketing_system.close_email_server()
```
