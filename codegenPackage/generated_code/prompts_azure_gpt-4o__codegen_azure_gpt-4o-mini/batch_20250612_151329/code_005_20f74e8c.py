"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Develop a marketing automation workflow in Python for increasing hotel sales, using the principles from Hampton's Hotel Institute's International Tourism & Hospitality Management course.
Generated: DETERMINISTIC_20f74e8c8465bdf1
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingAutomation:
    def __init__(self, email_server, email_port, email_user, email_password):
        """
        Initialize the MarketingAutomation class with email server details.
        
        :param email_server: SMTP server address
        :param email_port: SMTP server port
        :param email_user: Email account username
        :param email_password: Email account password
        """
        self.email_server = email_server
        self.email_port = email_port
        self.email_user = email_user
        self.email_password = email_password

    def send_email(self, recipient_email, subject, body):
        """
        Send an email to the specified recipient.
        
        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the email server and send the email
            with smtplib.SMTP(self.email_server, self.email_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email_user, self.email_password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient_email} with subject: {subject}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def create_marketing_campaign(self, guests):
        """
        Create and execute a marketing campaign for the provided guest list.
        
        :param guests: List of dictionaries containing guest information
        """
        for guest in guests:
            # Check if the guest is eligible for a promotional email
            if self.is_eligible_for_promotion(guest):
                subject = "Exclusive Offer Just for You!"
                body = f"Dear {guest['name']},\n\nWe have an exclusive offer for you at our hotel!\n\nBest regards,\nYour Hotel Team"
                self.send_email(guest['email'], subject, body)

    def is_eligible_for_promotion(self, guest):
        """
        Determine if a guest is eligible for a promotional email based on their last stay date.
        
        :param guest: Dictionary containing guest information
        :return: Boolean indicating eligibility
        """
        last_stay_date = datetime.strptime(guest['last_stay'], '%Y-%m-%d')
        eligible = (datetime.now() - last_stay_date) <= timedelta(days=365)  # Eligible if last stay was within the last year
        return eligible

# Example usage
if __name__ == "__main__":
    # Sample guest data
    guests = [
        {'name': 'John Doe', 'email': 'john.doe@example.com', 'last_stay': '2023-05-15'},
        {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'last_stay': '2022-11-20'},
        {'name': 'Alice Johnson', 'email': 'alice.johnson@example.com', 'last_stay': '2023-09-10'},
    ]

    # Initialize the marketing automation system
    marketing_automation = MarketingAutomation(
        email_server='smtp.example.com',
        email_port=587,
        email_user='your_email@example.com',
        email_password='your_password'
    )

    # Execute the marketing campaign
    marketing_automation.create_marketing_campaign(guests)
```
