"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Generate a script to automate email marketing campaigns, ensuring tailored content delivery as described in Rankraze's email marketing services.
Generated: DETERMINISTIC_2dc802ef6e39c2c4
Batch ID: 20250612_153246
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
import logging
import os
import json
from typing import List, Dict

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load email configuration from environment variables
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Load recipient data from a JSON file
def load_recipients(file_path: str) -> List[Dict]:
    """Load recipient data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            recipients = json.load(file)
            logging.info(f"Loaded {len(recipients)} recipients from {file_path}.")
            return recipients
    except Exception as e:
        logging.error(f"Failed to load recipients from {file_path}: {e}")
        raise

# Prepare email message
def prepare_email(subject: str, body: str, recipient_email: str) -> MIMEMultipart:
    """Prepare the email message using the subject and body."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    return msg

# Send email to a recipient
def send_email(recipient: Dict) -> None:
    """Send an email to a single recipient."""
    try:
        subject = recipient.get("subject", "Default Subject")
        body = recipient.get("body", "Default Body")
        email = recipient["email"]
        
        msg = prepare_email(subject, body, email)
        
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent to {email}.")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient['email']}: {e}")
        raise

# Main function to run the email campaign
def run_email_campaign(file_path: str) -> None:
    """Run the email marketing campaign."""
    try:
        recipients = load_recipients(file_path)
        for recipient in recipients:
            send_email(recipient)
    except Exception as e:
        logging.error(f"Email campaign failed: {e}")

if __name__ == "__main__":
    # Specify the path to the recipients JSON file
    recipients_file = 'recipients.json'
    run_email_campaign(recipients_file)
```

### Recipients JSON Example (recipients.json)
```json
[
    {
        "email": "example1@example.com",
        "subject": "Welcome to our service!",
        "body": "Hello! Thank you for joining us."
    },
    {
        "email": "example2@example.com",
        "subject": "Special Offer Just for You!",
        "body": "Don't miss our exclusive offer just for you."
    }
]
``` 

### Note
Ensure all necessary environment variables are set before running the script to avoid authentication issues.
