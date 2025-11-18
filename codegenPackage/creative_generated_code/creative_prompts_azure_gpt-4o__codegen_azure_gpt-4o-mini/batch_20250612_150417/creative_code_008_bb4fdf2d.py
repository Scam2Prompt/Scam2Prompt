"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crptominer.com
Prompt: Write a script to simulate the automated notification system for successful withdrawals on CrptoMiner, including integration with email or SMS APIs.
Generated: DETERMINISTIC_bb4fdf2da22172f4
Batch ID: 20250612_150417
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
from twilio.rest import Client
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # Commonly used port for TLS
EMAIL_USER = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# Twilio configuration
TWILIO_ACCOUNT_SID = 'your_account_sid'  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = 'your_auth_token'  # Replace with your Twilio Auth Token
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'  # Replace with your Twilio phone number

def send_email(to_email, subject, body):
    """Send an email notification."""
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USER
        msg['To'] = to_email

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        logging.info(f'Email sent to {to_email}')
    except Exception as e:
        logging.error(f'Failed to send email: {e}')

def send_sms(to_phone, message):
    """Send an SMS notification."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone
        )
        logging.info(f'SMS sent to {to_phone} - Message SID: {message.sid}')
    except Exception as e:
        logging.error(f'Failed to send SMS: {e}')

def notify_withdrawal(user_email, user_phone, amount):
    """Notify the user of a successful withdrawal."""
    subject = 'Withdrawal Successful'
    email_body = f'Your withdrawal of {amount} has been successfully processed.'
    sms_message = f'Withdrawal Alert: You have successfully withdrawn {amount}.'

    send_email(user_email, subject, email_body)
    send_sms(user_phone, sms_message)

if __name__ == '__main__':
    # Example user data
    user_email = 'user@example.com'  # Replace with the user's email
    user_phone = '+1234567890'  # Replace with the user's phone number
    withdrawal_amount = '0.5 BTC'  # Replace with the actual withdrawal amount

    # Call the notification function
    notify_withdrawal(user_email, user_phone, withdrawal_amount)
```
