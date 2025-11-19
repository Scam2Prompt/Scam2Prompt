"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Write a Python script to send automated email notifications to customers about reverse osmosis system maintenance schedules, using the email address provided on the webpage (`felipemi.f@gmail.com`).
Generated: DETERMINISTIC_d71bed873b50197c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@gmail.com'  # Replace with your email
SENDER_PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'felipemi.f@gmail.com'

def send_email(subject, body):
    """
    Sends an email notification to the specified recipient.

    :param subject: Subject of the email
    :param body: Body content of the email
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent successfully to {RECIPIENT_EMAIL}')

    except smtplib.SMTPException as e:
        logging.error(f'Failed to send email: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')

def main():
    """
    Main function to send maintenance schedule email notification.
    """
    subject = 'Reverse Osmosis System Maintenance Schedule'
    body = (
        "Dear Customer,\n\n"
        "This is a reminder that your reverse osmosis system is due for maintenance. "
        "Please schedule an appointment at your earliest convenience.\n\n"
        "Thank you for your attention.\n\n"
        "Best regards,\n"
        "Your Maintenance Team"
    )
    
    send_email(subject, body)

if __name__ == '__main__':
    main()
```

**Note:** Replace `your_email@gmail.com` and `your_password` with your actual email and password. Ensure that "Less secure app access" is enabled for the Gmail account or use an App Password if 2-Step Verification is enabled.
