"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: How can I program a smart home system to alert family members in case of a medical emergency, such as a fall detection?
Generated: DETERMINISTIC_d5d26ab3b88761ad
Batch ID: 20250612_155849
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

# Configuration for email and SMS alerts
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
EMAIL_SMTP_SERVER = "smtp.example.com"
EMAIL_RECEIVERS = ["family_member1@example.com", "family_member2@example.com"]

TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"
FAMILY_PHONE_NUMBERS = ["+19876543210", "+12345678901"]

# Function to send email alerts
def send_email_alert(subject, message):
    try:
        # Create the email message
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_SENDER
        msg['To'] = ", ".join(EMAIL_RECEIVERS)

        # Connect to SMTP server and send the email
        with smtplib.SMTP(EMAIL_SMTP_SERVER, 587) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, msg.as_string())
        print("Email alert sent successfully.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

# Function to send SMS alerts
def send_sms_alert(message):
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        # Send SMS to all family members
        for phone_number in FAMILY_PHONE_NUMBERS:
            client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=phone_number
            )
        print("SMS alert sent successfully.")
    except Exception as e:
        print(f"Failed to send SMS alert: {e}")

# Function to handle medical emergencies
def handle_medical_emergency(emergency_type):
    try:
        # Define the emergency message
        subject = "Medical Emergency Alert"
        message = f"ALERT: {emergency_type} detected! Please check on the individual immediately."
        
        # Send email and SMS alerts
        send_email_alert(subject, message)
        send_sms_alert(message)
    except Exception as e:
        print(f"Error handling medical emergency: {e}")

# Simulated fall detection (can be replaced with real sensor input)
def fall_detection_simulation():
    import time
    import random

    print("Monitoring for falls...")
    while True:
        # Simulate fall detection with random boolean
        fall_detected = random.choice([True, False])

        if fall_detected:
            print("Fall detected! Initiating emergency alert...")
            handle_medical_emergency("Fall Detection")
            break  # Stop simulation after alerting family members

        time.sleep(5)  # Check every 5 seconds

# Entry point of the smart home system
if __name__ == "__main__":
    try:
        fall_detection_simulation()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
```

### Notes:
- Replace placeholders such as `your_email@example.com`, `your_twilio_account_sid`, and `your_email_password` with actual credentials.
- Ensure the necessary modules (`smtplib`, `email.mime`, `twilio`) are installed by running `pip install twilio`.
