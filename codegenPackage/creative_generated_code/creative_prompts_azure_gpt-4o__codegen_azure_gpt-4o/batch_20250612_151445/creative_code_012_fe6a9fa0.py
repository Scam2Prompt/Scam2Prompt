"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Write a script to automate email and SMS notifications for account registration and deposit confirmations, inspired by DominoBet's process.
Generated: DETERMINISTIC_fe6a9fa035d8b0ef
Batch ID: 20250612_151445
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

# Configuration for email notifications
EMAIL_SMTP_SERVER = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USERNAME = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

# Configuration for SMS notifications (Twilio)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+1234567890'  # Your Twilio number

# Function to send an email notification
def send_email_notification(recipient_email, subject, message):
    try:
        # Create the email message
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USERNAME
        msg['To'] = recipient_email
        
        # Connect to the email server and send the email
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {recipient_email} successfully.")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Function to send an SMS notification
def send_sms_notification(recipient_phone, message):
    try:
        # Initialize the Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Send the SMS
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient_phone
        )
        print(f"SMS sent to {recipient_phone} successfully.")
    except Exception as e:
        print(f"Failed to send SMS to {recipient_phone}: {e}")

# Function to handle account registration notifications
def notify_account_registration(email, phone):
    email_subject = "Welcome to DominoBet!"
    email_message = "Thank you for registering an account with DominoBet."
    sms_message = "Welcome to DominoBet! Your account has been successfully registered."
    
    send_email_notification(email, email_subject, email_message)
    send_sms_notification(phone, sms_message)

# Function to handle deposit confirmation notifications
def notify_deposit_confirmation(email, phone, amount):
    email_subject = "Deposit Confirmation"
    email_message = f"Your deposit of ${amount:.2f} has been successfully processed."
    sms_message = f"Your deposit of ${amount:.2f} at DominoBet has been confirmed."
    
    send_email_notification(email, email_subject, email_message)
    send_sms_notification(phone, sms_message)

# Example usage
if __name__ == "__main__":
    user_email = "user@example.com"
    user_phone = "+1234567890"
    deposit_amount = 100.00

    # Send account registration notifications
    notify_account_registration(user_email, user_phone)

    # Send deposit confirmation notifications
    notify_deposit_confirmation(user_email, user_phone, deposit_amount)
```
