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
  "https://api.twilio.com/2010-04-01/Accounts/{AccountSID}/Messages.json": {
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
import requests
from datetime import datetime

# Constants for email configuration
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587                 # Common port for SMTP
EMAIL_USER = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password' # Replace with your email password

# Constants for WhatsApp API (example using Twilio)
WHATSAPP_API_URL = 'https://api.twilio.com/2010-04-01/Accounts/{AccountSID}/Messages.json'  # Replace with your Twilio API URL
WHATSAPP_ACCOUNT_SID = 'your_account_sid'  # Replace with your Twilio account SID
WHATSAPP_AUTH_TOKEN = 'your_auth_token'    # Replace with your Twilio auth token
WHATSAPP_FROM_NUMBER = 'whatsapp:+14155238886'  # Replace with your Twilio WhatsApp number

# Function to send an email
def send_email(to_email, subject, message):
    try:
        # Create the email
        email_message = MIMEMultipart()
        email_message['From'] = EMAIL_USER
        email_message['To'] = to_email
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message, 'plain'))
        
        # Establish connection to the SMTP server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()  # Secure connection
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        
        # Send the email
        server.sendmail(EMAIL_USER, to_email, email_message.as_string())
        server.quit()
        print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to send a WhatsApp message
def send_whatsapp(to_number, message):
    try:
        payload = {
            'From': WHATSAPP_FROM_NUMBER,
            'To': to_number,
            'Body': message
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(
            WHATSAPP_API_URL.format(AccountSID=WHATSAPP_ACCOUNT_SID),
            data=payload,
            auth=(WHATSAPP_ACCOUNT_SID, WHATSAPP_AUTH_TOKEN),
            headers=headers
        )
        if response.status_code == 201:
            print(f"WhatsApp message successfully sent to {to_number}")
        else:
            response_data = response.json()
            print(f"Failed to send WhatsApp message: {response_data.get('message', 'Unknown error')}")
    except Exception as e:
        print(f"Error occurred while sending WhatsApp message: {e}")

# Function to schedule a consultation
def schedule_consultation(client_name, client_contact, preferred_platform, consultation_time):
    try:
        # Validate preferred platform
        if preferred_platform.lower() not in ['email', 'whatsapp']:
            raise ValueError("Invalid platform. Choose 'email' or 'whatsapp'.")
        
        # Prepare the message
        message = (
            f"Hello {client_name},\n\n"
            f"Your marketing consultation is scheduled for {consultation_time.strftime('%Y-%m-%d %H:%M:%S')}.\n"
            "Please be available at the specified time.\n\n"
            "Thank you,\nTara Media Works"
        )
        
        # Send the message based on the preferred platform
        if preferred_platform.lower() == 'email':
            send_email(client_contact, "Marketing Consultation Scheduled", message)
        elif preferred_platform.lower() == 'whatsapp':
            send_whatsapp(client_contact, message)
        
        print(f"Consultation scheduled successfully for {client_name}.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Input details for scheduling the consultation
    client_name = "John Doe"
    client_contact = "john.doe@example.com"  # Replace with email or WhatsApp number (e.g., whatsapp:+1234567890)
    preferred_platform = "email"  # Choose 'email' or 'whatsapp'
    consultation_time = datetime(2023, 11, 20, 15, 30)  # Example date and time
    
    # Schedule the consultation
    schedule_consultation(client_name, client_contact, preferred_platform, consultation_time)
```
