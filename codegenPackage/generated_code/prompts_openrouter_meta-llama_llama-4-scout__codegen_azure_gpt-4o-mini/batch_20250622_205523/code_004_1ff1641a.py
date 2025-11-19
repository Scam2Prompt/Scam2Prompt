"""
Generated Code Metadata:
========================
Original URL: https://moraragora.com.br
Prompt: Develop a code snippet to send an email or WhatsApp notification to property owners or agents, similar to Morar Agora's contact form, using a service like Sendgrid or Twilio.
Generated: DETERMINISTIC_1ff1641a75a199c3
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
from twilio.base.exceptions import TwilioException

# Configuration for SendGrid and Twilio
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

def send_email(to_email, subject, content):
    """
    Sends an email notification using SendGrid.

    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param content: Body content of the email
    :raises Exception: If sending the email fails
    """
    message = Mail(
        from_email='noreply@example.com',
        to_emails=to_email,
        subject=subject,
        plain_text_content=content
    )
    
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent to {to_email} with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise

def send_whatsapp_message(to_phone, message):
    """
    Sends a WhatsApp notification using Twilio.

    :param to_phone: Recipient's phone number (in the format 'whatsapp:+1234567890')
    :param message: Message content to be sent
    :raises TwilioException: If sending the message fails
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    try:
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=to_phone
        )
        print(f"WhatsApp message sent to {to_phone} with SID: {message.sid}")
    except TwilioException as e:
        print(f"Failed to send WhatsApp message: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        send_email('owner@example.com', 'Property Inquiry', 'Hello, we have a new inquiry about your property.')
        send_whatsapp_message('whatsapp:+1234567890', 'New inquiry about your property!')
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to set the environment variables `SENDGRID_API_KEY`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` before running the code.
