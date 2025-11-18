"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombat-exchange.rf.gd
Prompt: Create a guide for setting up email accounts on iFastNet hosting and integrating them with a web application.
Generated: DETERMINISTIC_8014f7ab75d1078d
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script serves as a guide to set up email accounts on iFastNet hosting and integrate them with a web application.
It uses Python's `smtplib` and `imaplib` libraries for sending and receiving emails via SMTP and IMAP protocols.
Make sure to replace placeholder values with actual credentials and server information from iFastNet.
"""

import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration for the email account and servers
EMAIL_ADDRESS = "your_email@ifastnet.com"  # Replace with your iFastNet email address
EMAIL_PASSWORD = "your_password"           # Replace with your email password
SMTP_SERVER = "mail.ifastnet.com"          # Replace if different from iFastNet details
SMTP_PORT = 587                            # Standard port for SMTP with TLS
IMAP_SERVER = "mail.ifastnet.com"          # Replace if different from iFastNet details
IMAP_PORT = 993                            # Standard port for IMAP with SSL

# Error handling for SMTP setup and sending emails
def send_email(to_email, subject, body):
    """
    Sends an email via SMTP.
    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body of the email
    :return: None
    """
    try:
        # Set up the SMTP connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Authenticate with the email server

            # Create the email
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")


# Error handling for IMAP setup and fetching emails
def fetch_emails():
    """
    Retrieves emails from the inbox via IMAP.
    :return: List of email subjects
    """
    try:
        # Connect to the IMAP server
        with imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Authenticate with the email server
            server.select("inbox")  # Select the inbox folder

            # Search for all emails in the inbox
            status, messages = server.search(None, 'ALL')
            if status != "OK":
                print("No messages found.")
                return []

            email_subjects = []
            for num in messages[0].split():
                status, msg_data = server.fetch(num, '(RFC822)')
                if status != "OK":
                    print(f"Failed to fetch email {num}.")
                    continue

                # Parse the email content
                msg = email.message_from_bytes(msg_data[0][1])
                email_subjects.append(msg['subject'])

            return email_subjects
    except imaplib.IMAP4.error as e:
        print(f"Failed to fetch emails: {e}")


# Example usage:
if __name__ == "__main__":
    # Sending an email
    send_email("recipient@example.com", "Test Subject", "This is a test email body.")

    # Fetching emails
    subjects = fetch_emails()
    print("Email Subjects:")
    for subject in subjects:
        print(subject)
```

This script provides a basic implementation for sending and receiving emails with iFastNet-hosted accounts. Ensure that the email server details match iFastNet's specifications and verify the credentials before running the script in a production environment.
