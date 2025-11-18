"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fareobuddy.com
Prompt: Create a Python script to send promotional offers via email to subscribed users, ensuring compliance with GDPR and privacy policies, as FareObuddy does with its newsletter.
Generated: DETERMINISTIC_95e7328cb5241a99
Batch ID: 20250612_151429
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'   # Replace with your SMTP server
SMTP_PORT = 587                     # Commonly used SMTP port
SMTP_USERNAME = 'your_email@example.com'  # Replace with your email
SMTP_PASSWORD = 'your_password'     # Replace with your password


def send_email(subject: str, body: str, recipients: List[str]) -> None:
    """
    Sends an email with the specified subject and body to the provided recipients.
    
    :param subject: Subject of the email
    :param body: Body of the email
    :param recipients: List of email addresses to send the email to
    :raises Exception: Raises an exception if email fails to send
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = SMTP_USERNAME
        message['Subject'] = subject
        
        # Attach the email body
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Login to the email server
            
            # Send email to all recipients
            for recipient in recipients:
                message['To'] = recipient
                server.sendmail(SMTP_USERNAME, recipient, message.as_string())
                logging.info(f'Email sent to {recipient}')
    except Exception as e:
        logging.error(f'Failed to send email: {e}')
        raise


def validate_email_list(email_list: List[str]) -> List[str]:
    """
    Validate a list of email addresses to ensure they conform to standard email format.
    
    :param email_list: List of email addresses
    :return: List of valid email addresses
    """
    valid_emails = []
    for email in email_list:
        if '@' in email and '.' in email.split('@')[-1]:  # Basic validation
            valid_emails.append(email)
        else:
            logging.warning(f'Invalid email address skipped: {email}')
    return valid_emails


def draft_promotion_email(offer_details: Dict[str, str]) -> (str, str):
    """
    Drafts a promotional email subject and body based on offer details.
    
    :param offer_details: Dictionary containing offer details
    :return: Tuple of subject and body for the email
    """
    subject = f"Exclusive Offer: {offer_details['title']}"
    body = f"Hello,\n\nWe are excited to share our new offer with you!\n\n{offer_details['description']}\n\nBest regards,\nFareObuddy Team"
    return subject, body


def main():
    # Example offer details
    offer_details = {
        'title': '20% Off Your Next Booking',
        'description': 'Enjoy a 20% discount on your next booking with us. Use code: FARE20 at checkout. Offer valid until the end of the month.'
    }
    
    # List of subscribed users
    subscribed_users = [
        'user1@example.com',
        'user2@example.com',
        'invalid_email.com'  # Example of an invalid email
    ]
    
    # Validate email addresses
    valid_recipients = validate_email_list(subscribed_users)
    
    if valid_recipients:
        subject, body = draft_promotion_email(offer_details)
        send_email(subject, body, valid_recipients)
    else:
        logging.error('No valid recipients found. Email not sent.')


if __name__ == '__main__':
    main()
```
