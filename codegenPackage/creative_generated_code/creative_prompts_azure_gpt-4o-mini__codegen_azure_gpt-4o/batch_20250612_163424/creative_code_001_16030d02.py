"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: Write a code snippet that integrates SMS and email messaging for lead engagement, inspired by the Sales Studios Online System.
Generated: DETERMINISTIC_16030d02e03ec8b5
Batch ID: 20250612_163424
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

# Configuration for email and SMS services
EMAIL_HOST = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"

def send_email(recipient_email, subject, message):
    """
    Sends an email to the specified recipient.
    
    :param recipient_email: Email address of the recipient.
    :param subject: Subject line of the email.
    :param message: Message body of the email.
    """
    try:
        # Create email message
        mime_message = MIMEText(message)
        mime_message["From"] = EMAIL_USERNAME
        mime_message["To"] = recipient_email
        mime_message["Subject"] = subject
        
        # Connect to email server and send email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, recipient_email, mime_message.as_string())
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def send_sms(recipient_phone, message):
    """
    Sends an SMS to the specified recipient using Twilio.
    
    :param recipient_phone: Phone number of the recipient (E.164 format).
    :param message: SMS message content.
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Send SMS
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient_phone
        )
        print(f"SMS sent successfully to {recipient_phone}")
    except Exception as e:
        print(f"Failed to send SMS to {recipient_phone}: {e}")

def engage_lead(lead_email, lead_phone, engagement_message):
    """
    Engages a lead via both email and SMS.
    
    :param lead_email: Email address of the lead.
    :param lead_phone: Phone number of the lead (E.164 format).
    :param engagement_message: Engagement message content.
    """
    email_subject = "We'd love to connect!"
    
    # Send email and SMS
    send_email(lead_email, email_subject, engagement_message)
    send_sms(lead_phone, engagement_message)

# Example usage:
if __name__ == "__main__":
    # Replace these with actual lead information
    lead_email = "lead@example.com"
    lead_phone = "+1987654321"
    engagement_message = "Hi there! We noticed your interest in our services. Let's talk!"

    engage_lead(lead_email, lead_phone, engagement_message)
```
