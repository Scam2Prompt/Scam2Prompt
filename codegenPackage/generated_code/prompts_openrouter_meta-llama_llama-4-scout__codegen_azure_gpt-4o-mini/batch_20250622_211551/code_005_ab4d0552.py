"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Write a script that automates the process of obtaining explicit user consent for data collection and processing, as required by the STELLAR TECHNOLOGY LIMITED privacy policy, and provide a notification system for policy updates.
Generated: DETERMINISTIC_ab4d05529bd49ab9
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Constants
DATA_CONSENT_FILE = 'user_consent.json'
POLICY_UPDATE_FILE = 'policy_updates.json'
EMAIL_SENDER = 'your_email@example.com'
EMAIL_RECEIVER = 'user_email@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

# Function to load user consent data
def load_user_consent():
    """Load user consent data from a JSON file."""
    if os.path.exists(DATA_CONSENT_FILE):
        with open(DATA_CONSENT_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save user consent data
def save_user_consent(consent_data):
    """Save user consent data to a JSON file."""
    with open(DATA_CONSENT_FILE, 'w') as file:
        json.dump(consent_data, file)

# Function to send email notification
def send_email_notification(subject, body):
    """Send an email notification about policy updates."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to obtain user consent
def obtain_user_consent():
    """Prompt the user for consent and save the response."""
    consent = input("Do you consent to data collection and processing? (yes/no): ").strip().lower()
    if consent in ['yes', 'y']:
        consent_data = {
            'consent_given': True,
            'timestamp': datetime.now().isoformat()
        }
        save_user_consent(consent_data)
        print("Thank you for your consent.")
    else:
        consent_data = {
            'consent_given': False,
            'timestamp': datetime.now().isoformat()
        }
        save_user_consent(consent_data)
        print("You have not given consent.")

# Function to check for policy updates
def check_policy_updates():
    """Check for policy updates and notify users if there are any."""
    if os.path.exists(POLICY_UPDATE_FILE):
        with open(POLICY_UPDATE_FILE, 'r') as file:
            updates = json.load(file)
            if updates.get('updated'):
                send_email_notification("Policy Update Notification", updates['message'])

# Main function to run the script
def main():
    """Main function to execute the consent process and check for updates."""
    obtain_user_consent()
    check_policy_updates()

if __name__ == "__main__":
    main()
```
