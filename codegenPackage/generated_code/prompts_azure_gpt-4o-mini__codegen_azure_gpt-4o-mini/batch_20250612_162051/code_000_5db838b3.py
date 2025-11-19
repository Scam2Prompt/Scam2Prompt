"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: Write a Python script to send an email invitation for the Holy Saraswati Puja Celebration organized by the India (Bengal) Cultural Association Japan, including details about the event date, location, and entry fees.
Generated: DETERMINISTIC_5db838b3b331334e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email_invitation(to_email, subject, body, smtp_server, smtp_port, sender_email, sender_password):
    """
    Sends an email invitation for the Holy Saraswati Puja Celebration.

    Parameters:
    to_email (str): Recipient's email address.
    subject (str): Subject of the email.
    body (str): Body content of the email.
    smtp_server (str): SMTP server address.
    smtp_port (int): SMTP server port.
    sender_email (str): Sender's email address.
    sender_password (str): Sender's email password.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            logging.info(f"Email sent successfully to {to_email}")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Email details
    recipient_email = "recipient@example.com"  # Replace with the recipient's email address
    email_subject = "Invitation to Holy Saraswati Puja Celebration"
    email_body = (
        "Dear Community Member,\n\n"
        "We are pleased to invite you to the Holy Saraswati Puja Celebration organized by the India (Bengal) Cultural Association Japan.\n\n"
        "Event Details:\n"
        "Date: February 10, 2024\n"
        "Location: Tokyo Community Center, 123 Sakura Street, Tokyo, Japan\n"
        "Entry Fee: 1000 JPY\n\n"
        "Join us for a day of cultural festivities, prayers, and community bonding.\n\n"
        "Best Regards,\n"
        "India (Bengal) Cultural Association Japan"
    )

    # SMTP server configuration
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password

    # Send the email invitation
    send_email_invitation(recipient_email, email_subject, email_body, smtp_server, smtp_port, sender_email, sender_password)
```
