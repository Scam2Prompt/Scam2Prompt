"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shebatek.com
Prompt: Develop a marketing automation script for promoting services and products within budget, as highlighted by ShebaTek's marketing services.
Generated: DETERMINISTIC_8f13c50e99620867
Batch ID: 20250612_145831
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

# Configure logging
logging.basicConfig(
    filename='marketing_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load budget and email content configuration
BUDGET = 1000  # Example budget in dollars
COST_PER_EMAIL = 0.05  # Example cost per email in dollars
EMAIL_SUBJECT = "ShebaTek Marketing - Exclusive Offers!"
EMAIL_BODY = """
Hello {name},

We are excited to share ShebaTek's latest services and products designed to meet your needs within your budget.
Discover more by visiting our website or contacting us.

Best regards,
ShebaTek Marketing Team
"""

SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS
SMTP_USERNAME = "your_email@example.com"  # Replace with your email
SMTP_PASSWORD = "your_password"  # Replace with your password

# Constants
CONTACTS_FILE = "contacts.csv"  # Path to the CSV file containing contacts

def load_contacts(file_path):
    """
    Load contacts from a CSV file.
    CSV file should have 'Name' and 'Email' columns.
    """
    contacts = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append({'name': row['Name'], 'email': row['Email']})
        logging.info(f"Successfully loaded {len(contacts)} contacts.")
    except FileNotFoundError:
        logging.error(f"Contacts file not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error loading contacts file: {e}")
        raise
    return contacts

def send_email(smtp, recipient_name, recipient_email):
    """
    Send a marketing email to a single recipient.
    """
    try:
        # Create email message
        message = MIMEMultipart()
        message['From'] = SMTP_USERNAME
        message['To'] = recipient_email
        message['Subject'] = EMAIL_SUBJECT

        # Personalize the email body
        body = EMAIL_BODY.format(name=recipient_name)
        message.attach(MIMEText(body, 'plain'))

        # Send email
        smtp.send_message(message)
        logging.info(f"Email sent to {recipient_name} ({recipient_email})")

    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")
        raise

def main():
    try:
        # Load contacts
        contacts = load_contacts(CONTACTS_FILE)

        # Calculate the maximum number of emails we can send within budget
        max_emails = int(BUDGET / COST_PER_EMAIL)
        contacts_to_email = contacts[:max_emails]
        logging.info(f"Budget allows sending to {len(contacts_to_email)} contacts.")

        # Setup SMTP connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()  # Secure the connection
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)

            # Send emails to contacts
            for contact in contacts_to_email:
                send_email(smtp, contact['name'], contact['email'])

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
