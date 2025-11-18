"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://websea-login.com
Prompt: Write code to implement a "forgot password" feature for a cryptocurrency exchange platform, including email and phone number recovery options, similar to Websea Login.
Generated: DETERMINISTIC_9a4e378c7cc29bce
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import smtplib
from email.mime.text import MIMEText
from random import randint
from twilio.rest import Client

# Simulating a database of users
user_db = {
    "user@example.com": {
        "phone": "+1234567890",
        "password": "hashed_password",  # In practice, store hashed passwords
        "recovery_code": None
    }
}

# Twilio API credentials (replace with your credentials)
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_email_password'

def send_email(recipient, subject, body):
    """Send an email to the specified recipient."""
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, recipient, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_sms(recipient, message):
    """Send an SMS to the specified recipient using Twilio."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(to=recipient, from_=TWILIO_PHONE_NUMBER, body=message)
        print("SMS sent successfully")
    except Exception as e:
        print(f"Error sending SMS: {e}")

def generate_recovery_code():
    """Generate a random recovery code."""
    return randint(100000, 999999)

def forgot_password(email, recovery_method):
    """Handle the forgot password process with recovery options."""
    user = user_db.get(email)
    
    if not user:
        print("Email not found.")
        return

    recovery_code = generate_recovery_code()
    user['recovery_code'] = recovery_code
    
    if recovery_method == 'email':
        send_email(email, "Your Recovery Code", f"Your recovery code is: {recovery_code}")
    elif recovery_method == 'sms':
        send_sms(user['phone'], f"Your recovery code is: {recovery_code}")
    else:
        print("Invalid recovery method. Choose 'email' or 'sms'.")

def reset_password(email, recovery_code, new_password):
    """Reset the user's password if the recovery code is valid."""
    user = user_db.get(email)
    
    if not user:
        print("Email not found.")
        return

    if user['recovery_code'] == recovery_code:
        # In practice, hash the new password before storing
        user['password'] = new_password
        user['recovery_code'] = None  # Invalidate the recovery code
        print("Password reset successfully.")
    else:
        print("Invalid recovery code.")

# Example usage:
forgot_password("user@example.com", "email")  # Initiate forgot password process
reset_password("user@example.com", 123456, "new_hashed_password")  # Resetting password
```
