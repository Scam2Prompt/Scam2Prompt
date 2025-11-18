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
from email.mime.text import MIMEText
from twilio.rest import Client
from typing import Literal

def send_booking_confirmation(
    communication_method: Literal["SMS", "WhatsApp", "Email"], 
    recipient: str, 
    message: str
):
    """
    Sends a booking confirmation message using the specified communication method.
    
    :param communication_method: The selected communication method ("SMS", "WhatsApp", or "Email").
    :param recipient: The recipient's contact information (phone number for SMS/WhatsApp, email address for Email).
    :param message: The booking confirmation message to send.
    """
    try:
        if communication_method == "SMS":
            send_sms(recipient, message)
        elif communication_method == "WhatsApp":
            send_whatsapp(recipient, message)
        elif communication_method == "Email":
            send_email(recipient, message)
        else:
            raise ValueError("Invalid communication method. Choose 'SMS', 'WhatsApp', or 'Email'.")
    except Exception as e:
        print(f"Error sending booking confirmation: {str(e)}")
        # Log the error or handle it as needed in a production environment

def send_sms(recipient: str, message: str):
    """
    Sends an SMS using Twilio API.

    :param recipient: The recipient's phone number in E.164 format (e.g., "+1234567890").
    :param message: The message to send.
    """
    try:
        # Twilio credentials (replace with your credentials)
        TWILIO_ACCOUNT_SID = "your_account_sid"
        TWILIO_AUTH_TOKEN = "your_auth_token"
        TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
        
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Send SMS
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient
        )
        print("SMS sent successfully.")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")
        # Log the error or handle it as needed

def send_whatsapp(recipient: str, message: str):
    """
    Sends a WhatsApp message using Twilio API.

    :param recipient: The recipient's phone number in E.164 format (e.g., "+1234567890").
    :param message: The message to send.
    """
    try:
        # Twilio credentials (replace with your credentials)
        TWILIO_ACCOUNT_SID = "your_account_sid"
        TWILIO_AUTH_TOKEN = "your_auth_token"
        TWILIO_WHATSAPP_NUMBER = "whatsapp:+your_twilio_whatsapp_number"
        
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Send WhatsApp message
        client.messages.create(
            body=message,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=f"whatsapp:{recipient}"
        )
        print("WhatsApp message sent successfully.")
    except Exception as e:
        print(f"Error sending WhatsApp message: {str(e)}")
        # Log the error or handle it as needed

def send_email(recipient: str, message: str):
    """
    Sends an email using Python's smtplib.

    :param recipient: The recipient's email address.
    :param message: The message to send.
    """
    try:
        # Email credentials (replace with your credentials)
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        EMAIL_USERNAME = "your_email@example.com"
        EMAIL_PASSWORD = "your_email_password"
        
        # Create MIME email message
        msg = MIMEText(message)
        msg["Subject"] = "Booking Confirmation"
        msg["From"] = EMAIL_USERNAME
        msg["To"] = recipient
        
        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, recipient, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        # Log the error or handle it as needed

# Example usage:
if __name__ == "__main__":
    # Replace with actual values
    communication_method = "SMS"  # Options: "SMS", "WhatsApp", "Email"
    recipient = "+1234567890"  # Phone number for SMS/WhatsApp or email address for Email
    message = "Your booking has been confirmed. Thank you!"

    send_booking_confirmation(communication_method, recipient, message)
```
