"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Create a script to automate the process of sending thank-you messages to donors, using email APIs or libraries, based on the donation data collected by Dysnix.
Generated: DETERMINISTIC_b9317f37bf48307e
Batch ID: 20250622_211557
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# File containing donation data
DONATION_DATA_FILE = 'donation_data.csv'  # Replace with the path to your donation data file

def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.

    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body of the email
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent successfully to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def process_donation_data(file_path):
    """
    Processes the donation data file and sends thank-you emails to donors.

    :param file_path: Path to the donation data file
    """
    try:
        # Open the donation data file
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)

            # Iterate through each row in the CSV file
            for row in reader:
                donor_name = row.get('Name')
                donor_email = row.get('Email')
                donation_amount = row.get('Amount')

                # Validate required fields
                if not donor_name or not donor_email or not donation_amount:
                    logging.warning(f"Skipping incomplete record: {row}")
                    continue

                # Create the thank-you email content
                subject = "Thank You for Your Generous Donation!"
                body = (
                    f"Dear {donor_name},\n\n"
                    f"Thank you for your generous donation of ${donation_amount}. "
                    "Your support helps us continue our mission and make a difference.\n\n"
                    "Best regards,\n"
                    "The Dysnix Team"
                )

                # Send the email
                send_email(donor_email, subject, body)
    except FileNotFoundError:
        logging.error(f"Donation data file not found: {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while processing the donation data: {e}")

if __name__ == "__main__":
    # Run the script
    logging.info("Starting the thank-you email automation script...")
    process_donation_data(DONATION_DATA_FILE)
    logging.info("Script completed.")
```
