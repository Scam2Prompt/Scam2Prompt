"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Write a Python script to send automated email notifications to customers about reverse osmosis system maintenance schedules, using the email address provided on the webpage (`felipemi.f@gmail.com`).
Generated: DETERMINISTIC_d71bed873b50197c
Batch ID: 20250612_153224
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
from email.mime.base import MIMEBase
from email import encoders
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@gmail.com'  # Replace with your email
SENDER_PASSWORD = 'your_password'  # Replace with your email password

# Recipient email
RECIPIENT_EMAIL = 'felipemi.f@gmail.com'

def create_email(subject, body):
    """Create an email with the given subject and body."""
    # Create a multipart email
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))
    return message

def send_email(email_message):
    """Send an email message."""
    try:
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login to the email server
            server.send_message(email_message)  # Send the email
            logging.info(f'Email sent to {RECIPIENT_EMAIL}')
    except Exception as e:
        logging.error(f'Failed to send email: {e}')

def main():
    """Main function to send maintenance schedule email."""
    subject = 'Maintenance Schedule for Your Reverse Osmosis System'
    body = (
        "Dear Customer,\n\n"
        "We would like to inform you that your reverse osmosis system maintenance is scheduled for next week.\n"
        "Please ensure that access to the system is available during this time.\n\n"
        "Thank you for your attention.\n\n"
        "Best Regards,\n"
        "Your Service Team"
    )

    # Create the email
    email_message = create_email(subject, body)

    # Send the email
    send_email(email_message)

if __name__ == '__main__':
    main()
```

**Note:** 
- Replace `your_email@gmail.com` and `your_password` with your actual email credentials. 
- Make sure to enable "Less secure app access" in your Google account settings or use an App Password if you have 2-Step Verification enabled. 
- Consider using environment variables or a configuration file for sensitive information like email and password instead of hardcoding them in the script for security reasons.
