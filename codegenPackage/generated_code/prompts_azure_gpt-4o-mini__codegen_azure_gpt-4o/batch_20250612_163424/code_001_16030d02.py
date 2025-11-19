"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Write a code snippet that integrates SMS and email messaging for lead engagement, inspired by the Sales Studios Online System.
Generated: DETERMINISTIC_16030d02e03ec8b5
Batch ID: 20250612_163424
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
from twilio.rest import Client

# Configuration for email and SMS services
EMAIL_HOST = "smtp.example.com"  # Replace with your SMTP server
EMAIL_PORT = 587  # Common port for SMTP
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"  # Replace with your Twilio Auth Token
TWILIO_PHONE_NUMBER = "+1234567890"  # Replace with your Twilio phone number

def send_email(to_email, subject, message):
    """
    Sends an email to the specified recipient.
    
    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param message: Body of the email
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def send_sms(to_phone_number, message):
    """
    Sends an SMS to the specified phone number using Twilio.
    
    :param to_phone_number: Recipient's phone number
    :param message: SMS message content
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send the SMS
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        print(f"SMS sent successfully to {to_phone_number}")
    except Exception as e:
        print(f"Failed to send SMS to {to_phone_number}: {e}")

def engage_lead(email, phone_number, email_subject, email_message, sms_message):
    """
    Engages a lead by sending both an email and an SMS.
    
    :param email: Lead's email address
    :param phone_number: Lead's phone number
    :param email_subject: Subject of the email
    :param email_message: Body of the email
    :param sms_message: SMS message content
    """
    print("Engaging lead...")
    send_email(email, email_subject, email_message)
    send_sms(phone_number, sms_message)
    print("Lead engagement completed.")

# Example usage
if __name__ == "__main__":
    lead_email = "lead@example.com"
    lead_phone_number = "+19876543210"
    email_subject = "Welcome to Sales Studios Online!"
    email_message = "Thank you for signing up. We're excited to work with you!"
    sms_message = "Welcome to Sales Studios Online! Check your email for more details."

    engage_lead(lead_email, lead_phone_number, email_subject, email_message, sms_message)
```
