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

class NotificationSender:
    """
    A class to handle sending email and WhatsApp notifications.
    Supports SendGrid for emails and Twilio for WhatsApp.
    """
    
    def __init__(self):
        """
        Initialize the notification sender with API keys from environment variables.
        """
        self.sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
        self.twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
        
    def send_email(self, to_email, from_email, subject, html_content):
        """
        Send an email using SendGrid.
        
        Args:
            to_email (str): Recipient email address
            from_email (str): Sender email address
            subject (str): Email subject
            html_content (str): HTML content of the email
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        if not self.sendgrid_api_key:
            raise ValueError("SendGrid API key is not configured")
            
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )
        
        try:
            sg = SendGridAPIClient(self.sendgrid_api_key)
            response = sg.send(message)
            return response.status_code == 202
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
            
    def send_whatsapp(self, to_number, message_body):
        """
        Send a WhatsApp message using Twilio.
        
        Args:
            to_number (str): Recipient phone number in E.164 format (e.g., +15551234567)
            message_body (str): Message content
            
        Returns:
            bool: True if message was sent successfully, False otherwise
        """
        if not all([self.twilio_account_sid, self.twilio_auth_token, self.twilio_whatsapp_number]):
            raise ValueError("Twilio credentials are not fully configured")
            
        try:
            client = Client(self.twilio_account_sid, self.twilio_auth_token)
            message = client.messages.create(
                body=message_body,
                from_=f"whatsapp:{self.twilio_whatsapp_number}",
                to=f"whatsapp:{to_number}"
            )
            return message.sid is not None
        except Exception as e:
            print(f"Error sending WhatsApp message: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize notification sender
    notifier = NotificationSender()
    
    # Example email notification
    email_sent = notifier.send_email(
        to_email="propertyowner@example.com",
        from_email="noreply@moraragora.com",
        subject="New Property Inquiry",
        html_content="<strong>Hello!</strong> You have a new inquiry about your property."
    )
    print(f"Email sent successfully: {email_sent}")
    
    # Example WhatsApp notification
    whatsapp_sent = notifier.send_whatsapp(
        to_number="+15551234567",
        message_body="Hello! You have a new inquiry about your property."
    )
    print(f"WhatsApp message sent successfully: {whatsapp_sent}")
```
