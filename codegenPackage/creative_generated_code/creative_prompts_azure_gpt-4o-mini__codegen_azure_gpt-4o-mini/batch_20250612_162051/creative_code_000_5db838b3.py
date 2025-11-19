"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ibcaj.org
Prompt: Write a Python script to send an email invitation for the Holy Saraswati Puja Celebration organized by the India (Bengal) Cultural Association Japan, including details about the event date, location, and entry fees.
Generated: DETERMINISTIC_5db838b3b331334e
Batch ID: 20250612_162051
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
SMTP_USERNAME = 'your_email@example.com'  # Replace with your email address
SMTP_PASSWORD = 'your_password'  # Replace with your email password
EMAIL_FROM = SMTP_USERNAME
EMAIL_SUBJECT = 'Invitation: Holy Saraswati Puja Celebration'

# Event details
EVENT_DATE = 'February 5, 2024'
EVENT_LOCATION = 'Cultural Hall, Tokyo, Japan'
ENTRY_FEES = 'Free entry for members, ¥500 for non-members'

def create_email_body():
    """
    Creates the email body for the invitation.
    """
    return f"""
    Dear Members,

    We are delighted to invite you to the Holy Saraswati Puja Celebration organized by the India (Bengal) Cultural Association Japan.

    Event Details:
    Date: {EVENT_DATE}
    Location: {EVENT_LOCATION}
    Entry Fees: {ENTRY_FEES}

    Join us to celebrate this auspicious occasion with prayers, cultural performances, and community bonding.

    Best Regards,
    India (Bengal) Cultural Association Japan
    """

def send_email(to_email):
    """
    Sends an email invitation to the specified recipient.

    Args:
        to_email (str): The recipient's email address.
    
    Raises:
        Exception: If there is an error while sending the email.
    """
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = formataddr(('India (Bengal) Cultural Association Japan', EMAIL_FROM))
    msg['To'] = to_email
    msg['Subject'] = EMAIL_SUBJECT

    # Attach the email body
    msg.attach(MIMEText(create_email_body(), 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email
            logging.info(f'Email successfully sent to {to_email}')
    except Exception as e:
        logging.error(f'Failed to send email to {to_email}: {e}')
        raise

if __name__ == "__main__":
    # List of recipients
    recipients = ['recipient1@example.com', 'recipient2@example.com']  # Replace with actual email addresses

    for recipient in recipients:
        try:
            send_email(recipient)
        except Exception as e:
            logging.error(f'Error sending email to {recipient}: {e}')
```

Make sure to replace the placeholders in the code with actual SMTP server details, credentials, and recipient email addresses before executing the script.
