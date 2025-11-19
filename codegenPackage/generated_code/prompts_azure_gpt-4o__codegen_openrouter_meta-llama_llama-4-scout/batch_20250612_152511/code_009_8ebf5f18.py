"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: Generate a Python script to automate donor engagement and retention for nonprofits in the Global South, leveraging ideas from Emerging Gifts' content.
Generated: DETERMINISTIC_8ebf5f1822b65b51
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donor_engagement.py

import os
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Donor:
    def __init__(self, name, email, donation_amount, donation_date):
        """
        Initialize a Donor object.

        Args:
            name (str): Donor's name
            email (str): Donor's email address
            donation_amount (float): Donor's donation amount
            donation_date (str): Donor's donation date
        """
        self.name = name
        self.email = email
        self.donation_amount = donation_amount
        self.donation_date = donation_date

class DonorEngagement:
    def __init__(self, smtp_server, smtp_port, from_email, password):
        """
        Initialize a DonorEngagement object.

        Args:
            smtp_server (str): SMTP server address
            smtp_port (int): SMTP server port
            from_email (str): From email address
            password (str): Email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def send_email(self, to_email, subject, body):
        """
        Send an email to a donor.

        Args:
            to_email (str): Donor's email address
            subject (str): Email subject
            body (str): Email body
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, to_email, text)
            server.quit()
            logging.info(f"Email sent to {to_email}")
        except Exception as e:
            logging.error(f"Error sending email to {to_email}: {str(e)}")

    def engage_donors(self, donors):
        """
        Engage donors by sending a thank-you email and a follow-up email.

        Args:
            donors (list): List of Donor objects
        """
        for donor in donors:
            # Send thank-you email
            subject = "Thank you for your donation!"
            body = f"Dear {donor.name},\n\nThank you for your generous donation of ${donor.donation_amount:.2f} on {donor.donation_date}. Your support means the world to us!\n\nBest regards,"
            self.send_email(donor.email, subject, body)

            # Send follow-up email
            subject = "Your impact at our nonprofit"
            body = f"Dear {donor.name},\n\nWe wanted to share with you the impact of your donation. Your support has helped us [insert impact here].\n\nThank you again for your support!\n\nBest regards,"
            self.send_email(donor.email, subject, body)

def load_donors(csv_file):
    """
    Load donors from a CSV file.

    Args:
        csv_file (str): Path to the CSV file

    Returns:
        list: List of Donor objects
    """
    donors = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            donor = Donor(row['name'], row['email'], float(row['donation_amount']), row['donation_date'])
            donors.append(donor)
    return donors

def main():
    # Load donors from CSV file
    csv_file = 'donors.csv'
    donors = load_donors(csv_file)

    # Set up email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'your_email@gmail.com'
    password = 'your_password'

    # Engage donors
    engagement = DonorEngagement(smtp_server, smtp_port, from_email, password)
    engagement.engage_donors(donors)

if __name__ == '__main__':
    main()
```
