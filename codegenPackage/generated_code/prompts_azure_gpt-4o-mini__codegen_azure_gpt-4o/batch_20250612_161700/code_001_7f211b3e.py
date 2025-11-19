"""
Generated Code Metadata:
========================
Original URL: https://ammaparivaar.org
Prompt: Write a Python script that automates sending thank-you emails to donors of a charity organization, inspired by the gratitude expressed by Amma Parivaar Orphanage.
Generated: DETERMINISTIC_7f211b3ee87ef491
Batch ID: 20250612_161700
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
import csv
import logging

# Configure logging
logging.basicConfig(
    filename='email_sender.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email server configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# File containing donor information
DONOR_FILE = 'donors.csv'  # Replace with the path to your CSV file

def send_email(to_email, donor_name, donation_amount):
    """
    Sends a thank-you email to the donor.

    Args:
        to_email (str): Recipient's email address.
        donor_name (str): Name of the donor.
        donation_amount (float): Donation amount.
    """
    try:
        # Create the email content
        subject = "Thank You for Your Generous Donation!"
        body = f"""
        Dear {donor_name},

        We at Amma Parivaar Orphanage are deeply grateful for your generous donation of ${donation_amount:.2f}.
        Your support helps us provide better care and opportunities for the children in our orphanage.

        Thank you for being a part of our mission to make a difference.

        Warm regards,
        Amma Parivaar Orphanage Team
        """

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        logging.info(f"Email sent successfully to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def read_donor_data(file_path):
    """
    Reads donor data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of donor records, where each record is a dictionary.
    """
    donors = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                donors.append(row)
        logging.info(f"Successfully read donor data from {file_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Error reading donor data: {e}")
    return donors

def main():
    """
    Main function to automate sending thank-you emails to donors.
    """
    # Read donor data from the CSV file
    donors = read_donor_data(DONOR_FILE)

    # Send thank-you emails to each donor
    for donor in donors:
        try:
            donor_name = donor['Name']
            donor_email = donor['Email']
            donation_amount = float(donor['DonationAmount'])
            send_email(donor_email, donor_name, donation_amount)
        except KeyError as e:
            logging.error(f"Missing required field in donor data: {e}")
        except ValueError as e:
            logging.error(f"Invalid donation amount for donor {donor.get('Name', 'Unknown')}: {e}")

if __name__ == "__main__":
    main()
```
