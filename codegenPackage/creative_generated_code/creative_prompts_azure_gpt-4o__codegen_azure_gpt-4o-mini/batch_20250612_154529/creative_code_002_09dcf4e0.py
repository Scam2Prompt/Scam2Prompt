"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Recommend a library or API for sending booking confirmation messages via SMS, WhatsApp, and Email, based on the user's selected communication method in a ticket booking form.
Generated: DETERMINISTIC_09dcf4e0af1e3b25
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from twilio.rest import Client as TwilioClient
from whatsapp_api_client import WhatsAppAPI  # Hypothetical library for WhatsApp
from typing import Dict, Any


class NotificationService:
    """Service for sending booking confirmations via SMS, WhatsApp, or Email."""

    def __init__(self, twilio_account_sid: str, twilio_auth_token: str, email_config: Dict[str, Any]):
        """Initialize NotificationService with Twilio and Email configurations."""
        self.twilio_client = TwilioClient(twilio_account_sid, twilio_auth_token)
        self.email_config = email_config
        self.whatsapp_client = WhatsAppAPI()  # Assume this sets up a client for WhatsApp

    def send_sms(self, to: str, message: str) -> None:
        """Send an SMS using Twilio."""
        try:
            message_response = self.twilio_client.messages.create(
                body=message,
                from_=self.twilio_client.phone_number,  # Your Twilio phone number
                to=to
            )
            print(f"SMS sent: {message_response.sid}")
        except Exception as e:
            print(f"Error sending SMS: {e}")

    def send_whatsapp(self, to: str, message: str) -> None:
        """Send a message via WhatsApp."""
        try:
            response = self.whatsapp_client.send_message(to, message)
            print(f"WhatsApp message sent: {response['id']}")
        except Exception as e:
            print(f"Error sending WhatsApp message: {e}")

    def send_email(self, to: str, subject: str, body: str) -> None:
        """Send an email using SMTP."""
        try:
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()
                server.login(self.email_config['username'], self.email_config['password'])
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail(self.email_config['from'], to, message)
                print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def send_confirmation(self, method: str, to: str, subject: str = "", message: str = "") -> None:
        """Send a booking confirmation based on the selected communication method."""
        if method.lower() == "sms":
            self.send_sms(to, message)
        elif method.lower() == "whatsapp":
            self.send_whatsapp(to, message)
        elif method.lower() == "email":
            self.send_email(to, subject, message)
        else:
            print(f"Unsupported communication method: {method}")


# Usage example:
if __name__ == "__main__":
    # Configuration values should be securely stored in environment variables or a config file
    twilio_account_sid = "your_twilio_account_sid"
    twilio_auth_token = "your_twilio_auth_token"
    email_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'username': 'your_email@example.com',
        'password': 'your_email_password',
        'from': 'your_email@example.com'
    }

    notification_service = NotificationService(twilio_account_sid, twilio_auth_token, email_config)

    # Example of sending a booking confirmation
    method = "email"  # This could come from a user input
    recipient = "user@example.com"
    subject = "Your Booking Confirmation"
    message = "Thank you for your booking! Here are your details..."

    notification_service.send_confirmation(method, recipient, subject, message)
```
