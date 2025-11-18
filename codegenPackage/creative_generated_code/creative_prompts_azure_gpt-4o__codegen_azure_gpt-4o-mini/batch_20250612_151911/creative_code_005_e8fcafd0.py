"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write a script to automate email filtering and anti-phishing measures for a small business, based on CyberConnect's recommendations.
Generated: DETERMINISTIC_e8fcafd07962a73a
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_HOST = 'imap.example.com'  # IMAP server
SMTP_HOST = 'smtp.example.com'    # SMTP server
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

# Define phishing keywords and phrases
PHISHING_KEYWORDS = ['urgent', 'account', 'verification', 'suspended', 'click here', 'login']

def connect_to_email():
    """Connect to the email server using IMAP."""
    try:
        mail = imaplib.IMAP4_SSL(EMAIL_HOST)
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        logging.info("Connected to email server.")
        return mail
    except imaplib.IMAP4.error as e:
        logging.error("Failed to connect to email server: %s", e)
        raise

def filter_phishing_emails(mail):
    """Filter and return phishing emails based on keywords."""
    mail.select('inbox')
    result, data = mail.search(None, 'ALL')  # Get all emails
    email_ids = data[0].split()
    phishing_emails = []

    for email_id in email_ids:
        result, msg_data = mail.fetch(email_id, '(RFC822)')
        raw_email = msg_data[0][1].decode('utf-8')

        if any(keyword in raw_email.lower() for keyword in PHISHING_KEYWORDS):
            phishing_emails.append(raw_email)
            logging.info("Phishing email detected: %s", raw_email)

    return phishing_emails

def send_alert(phishing_emails):
    """Send alert emails for detected phishing attempts."""
    if not phishing_emails:
        return

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS  # Send alert to the same address
        msg['Subject'] = 'Phishing Alert'
        body = 'The following phishing emails were detected:\n\n' + '\n\n'.join(phishing_emails)
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP(SMTP_HOST, 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info("Alert email sent successfully.")
    except Exception as e:
        logging.error("Failed to send alert email: %s", e)

def main():
    """Main function to filter and report phishing emails."""
    try:
        mail = connect_to_email()
        phishing_emails = filter_phishing_emails(mail)
        send_alert(phishing_emails)
    except Exception as e:
        logging.critical("An error occurred in the email filtering process: %s", e)
    finally:
        if mail:
            mail.logout()
            logging.info("Logged out from email server.")

if __name__ == "__main__":
    main()
```
