"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gmpinvestments.co.uk
Prompt: Write a Python script to send automated email updates to clients about property transactions, ensuring transparency and highlighting benefits like no fees or hidden costs.
Generated: DETERMINISTIC_54c3de72f0ec001b
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
from email.utils import formataddr
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Email server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@example.com"
SENDER_NAME = "Your Company Name"
SENDER_PASSWORD = "your_email_password"  # Use environment variables or a secure method to store this

def send_email(recipient_email: str, subject: str, body: str) -> None:
    """
    Sends an email to a single recipient.

    Args:
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.

    Raises:
        Exception: If there is an error sending the email.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())

        logging.info(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")
        raise

def send_bulk_emails(client_emails: List[str], subject: str, body: str) -> None:
    """
    Sends bulk emails to a list of clients.

    Args:
        client_emails (List[str]): List of client email addresses.
        subject (str): The subject of the email.
        body (str): The body content of the email.
    """
    for email in client_emails:
        try:
            send_email(email, subject, body)
        except Exception as e:
            logging.warning(f"Skipping email for {email} due to error: {e}")

def main() -> None:
    """
    Main function to send automated property transaction updates.
    """
    # Sample data
    client_emails = [
        "client1@example.com",
        "client2@example.com",
        "client3@example.com"
    ]

    subject = "Property Transaction Updates - Transparency Guaranteed!"
    body = (
        "Dear Client,\n\n"
        "We are writing to update you on your property transactions. "
        "We pride ourselves on ensuring transparency and keeping you informed every step of the way.\n\n"
        "Benefits:\n"
        "- No fees\n"
        "- No hidden costs\n\n"
        "Thank you for trusting us with your property needs.\n\n"
        "Best regards,\n"
        "Your Company Name"
    )

    # Send bulk emails
    send_bulk_emails(client_emails, subject, body)

if __name__ == "__main__":
    main()
```
