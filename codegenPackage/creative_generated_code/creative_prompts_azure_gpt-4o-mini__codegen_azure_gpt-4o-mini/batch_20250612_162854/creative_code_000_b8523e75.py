"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calib3r.io
Prompt: What are the potential reasons for a website like Calib3r to shut down, and how can I implement a notification system in my code to alert users of such changes?
Generated: DETERMINISTIC_b8523e751643f2ea
Batch ID: 20250612_162854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.calib3r.com": {
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
import requests
import smtplib
from email.mime.text import MIMEText
from time import sleep

# Constants for the monitoring system
URL_TO_MONITOR = "https://www.calib3r.com"  # Target website URL
CHECK_INTERVAL = 3600  # Time in seconds between checks (1 hour)
EMAIL_SENDER = "your_email@example.com"
EMAIL_RECEIVER = "recipient@example.com"
EMAIL_SUBJECT = "Website Status Alert"
SMTP_SERVER = "smtp.example.com"  # SMTP server address
SMTP_PORT = 587  # SMTP server port
SMTP_USER = "your_smtp_username"
SMTP_PASSWORD = "your_smtp_password"

def send_email_alert(message):
    """Send an email alert to the user."""
    msg = MIMEText(message)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_website_status(url):
    """Check the status of the website and return True if it's up, False otherwise."""
    try:
        response = requests.get(url)
        # Check if the status code indicates success (200-299)
        return 200 <= response.status_code < 300
    except requests.RequestException as e:
        print(f"Error checking website status: {e}")
        return False

def monitor_website():
    """Monitor the specified website and notify the user if it goes down."""
    while True:
        if not check_website_status(URL_TO_MONITOR):
            alert_message = f"Alert: The website {URL_TO_MONITOR} is currently down."
            print(alert_message)
            send_email_alert(alert_message)
        else:
            print(f"The website {URL_TO_MONITOR} is up and running.")
        
        sleep(CHECK_INTERVAL)  # Wait for the specified interval before checking again

if __name__ == "__main__":
    monitor_website()
```

**Note:** Ensure that SMTP credentials, email addresses, and the URL to monitor are updated before running this code.
