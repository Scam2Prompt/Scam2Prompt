"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalty.finance
Prompt: Write a script that automates sending offers for the domain loyalty.finance to potential buyers.
Generated: DETERMINISTIC_57eda50fc9e06708
Batch ID: 20250612_164238
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
from email.utils import formataddr
import csv
import logging

# Configure logging
logging.basicConfig(
    filename='domain_offer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email server configuration
SMTP_SERVER = 'smtp.gmail.com'  # Change this to your SMTP server
SMTP_PORT = 587  # Standard port for TLS
SENDER_EMAIL = 'your_email@example.com'  # Replace with your email
SENDER_NAME = 'Your Name'  # Replace with your name
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# Load recipient data from CSV file
def load_recipients(csv_file):
    """
    Load recipient data from a CSV file.
    Each row in the CSV should have 'Name' and 'Email' columns.
    """
    recipients = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'Name' in row and 'Email' in row:
                    recipients.append({'name': row['Name'], 'email': row['Email']})
    except FileNotFoundError as e:
        logging.error(f"CSV file not found: {e}")
        raise
    return recipients

# Construct the email message
def create_email(recipient_name, recipient_email):
    """
    Create an email message to promote the domain loyalty.finance.
    """
    subject = "Exclusive Offer for Loyalty.finance"
    body = f"""
    Dear {recipient_name},

    We noticed your interest in premium domains, and we'd like to offer you a unique opportunity to purchase the domain loyalty.finance. 

    Loyalty.finance is perfect for businesses in the financial sector focused on loyalty programs, blockchain, or fintech solutions.

    If you are interested, feel free to reply to this email for more details.

    Best regards,
    {SENDER_NAME}
    """

    # Construct the email
    msg = MIMEMultipart()
    msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

# Send the email
def send_email(recipient_name, recipient_email):
    """
    Send an email to a recipient.
    """
    try:
        # Create SMTP connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable encryption
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)

        # Create the message
        msg = create_email(recipient_name, recipient_email)

        # Send the email
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        logging.info(f"Email sent successfully to {recipient_name} <{recipient_email}>.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {recipient_name} <{recipient_email}>: {e}")
    finally:
        server.quit()

# Main function to orchestrate sending emails
def main():
    """
    Main function to load recipients and send emails.
    """
    recipients_file = 'recipients.csv'  # Replace with your CSV file name
    try:
        recipients = load_recipients(recipients_file)
        for recipient in recipients:
            send_email(recipient['name'], recipient['email'])
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

# Entry point for the script
if __name__ == '__main__':
    main()
```

**Note:**  
1. Replace placeholders like `your_email@example.com`, `your_password`, and `recipients.csv` with your actual data.
2. Ensure you secure sensitive information like email passwords using environment variables or a secret manager in production.
