"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Provide a Python script for scheduling marketing consultations via email or WhatsApp, inspired by the consultation scheduling feature on Tara Media Works' website.
Generated: DETERMINISTIC_760041ede52dcfa6
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.whatsapp.com/send": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import pytz
import requests

# Constants for email configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Constants for WhatsApp API
WHATSAPP_API_URL = 'https://api.whatsapp.com/send'
WHATSAPP_PHONE_NUMBER = 'recipient_phone_number'

def send_email(subject, body, recipient_email):
    """
    Sends an email with the specified subject and body to the given recipient.
    
    :param subject: Subject of the email
    :param body: Body content of the email
    :param recipient_email: Recipient's email address
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))

        # Set up the server connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        print(f'Email sent to {recipient_email} successfully.')
    except Exception as e:
        print(f'Error sending email: {e}')

def send_whatsapp_message(message, phone_number):
    """
    Sends a WhatsApp message to the specified phone number.

    :param message: The message content to send via WhatsApp
    :param phone_number: Recipient's phone number
    """
    try:
        payload = {
            'phone': phone_number,
            'text': message
        }
        response = requests.get(WHATSAPP_API_URL, params=payload)

        if response.status_code == 200:
            print(f'WhatsApp message sent to {phone_number} successfully.')
        else:
            print(f'Failed to send WhatsApp message: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'Error sending WhatsApp message: {e}')

def schedule_consultation(method, contact_info, datetime_str):
    """
    Schedules a marketing consultation via the specified method (email or WhatsApp).

    :param method: 'email' or 'whatsapp'
    :param contact_info: Email address or phone number
    :param datetime_str: Scheduled date and time in ISO format
    """
    try:
        # Convert the datetime string to a timezone-aware datetime object
        local_tz = pytz.timezone("UTC")
        scheduled_time = datetime.fromisoformat(datetime_str).astimezone(local_tz)
        
        # Prepare the message
        message_body = f'Your consultation is scheduled on {scheduled_time.strftime("%Y-%m-%d %H:%M:%S %Z")}'

        # Send the message based on the selected method
        if method == 'email':
            send_email('Consultation Scheduled', message_body, contact_info)
        elif method == 'whatsapp':
            send_whatsapp_message(message_body, contact_info)
        else:
            print('Invalid method specified. Use "email" or "whatsapp".')
    except Exception as e:
        print(f'Error scheduling consultation: {e}')

if __name__ == '__main__':
    # Example usage
    schedule_consultation('email', 'client@example.com', '2023-10-25T15:00:00')
    schedule_consultation('whatsapp', WHATSAPP_PHONE_NUMBER, '2023-10-25T15:00:00')
```
