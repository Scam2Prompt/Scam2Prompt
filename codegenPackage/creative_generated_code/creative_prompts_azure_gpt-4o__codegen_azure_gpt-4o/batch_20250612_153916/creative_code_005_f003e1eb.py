"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fishersclubs.com
Prompt: Create a Python script that queries Spark's governance rate changes via on-chain voting cycles and alerts users of upcoming changes to borrowing or savings rates.
Generated: DETERMINISTIC_f003e1ebcbe01bec
Batch ID: 20250612_153916
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sparkprotocol.io/governance/rates": {
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
import json
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
SPARK_API_URL = "https://api.sparkprotocol.io/governance/rates"  # Replace with the actual Spark API endpoint
ALERT_THRESHOLD_DAYS = 3  # Number of days before the rate change to alert the user
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS
EMAIL_SENDER = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password
EMAIL_RECIPIENTS = ["recipient_email@example.com"]  # List of recipients to alert

def fetch_rate_changes():
    """
    Fetch upcoming governance rate changes from Spark API.
    :return: List of rate changes.
    """
    try:
        response = requests.get(SPARK_API_URL)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Parse JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching rate changes: {e}")
        return []

def filter_upcoming_changes(rate_changes):
    """
    Filter rate changes that are within the alert threshold.
    :param rate_changes: List of rate changes from the API.
    :return: List of filtered rate changes within the alert window.
    """
    upcoming_changes = []
    current_date = datetime.utcnow()
    for change in rate_changes:
        try:
            # Parse the start date of the change
            change_date = datetime.strptime(change['start_date'], "%Y-%m-%dT%H:%M:%SZ")
            # Check if the change is within the alert threshold
            if change_date <= current_date + timedelta(days=ALERT_THRESHOLD_DAYS):
                upcoming_changes.append(change)
        except KeyError as e:
            print(f"Missing expected key in rate change data: {e}")
        except ValueError as e:
            print(f"Error parsing date format: {e}")
    return upcoming_changes

def send_email_alert(upcoming_changes):
    """
    Send an email alert for upcoming rate changes.
    :param upcoming_changes: List of upcoming rate changes.
    """
    try:
        # Create email content
        subject = "Upcoming Spark Governance Rate Changes Alert"
        body = "The following rate changes are scheduled:\n\n"
        for change in upcoming_changes:
            body += f"- Type: {change['type']}\n"
            body += f"  New Rate: {change['new_rate']}%\n"
            body += f"  Effective Date: {change['start_date']}\n\n"
        
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = ", ".join(EMAIL_RECIPIENTS)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENTS, msg.as_string())
            print("Email alert sent successfully.")
    except Exception as e:
        print(f"Error sending email alert: {e}")

def main():
    """
    Main function to execute the script.
    """
    print("Fetching rate changes...")
    rate_changes = fetch_rate_changes()
    if not rate_changes:
        print("No data available or failed to fetch rate changes.")
        return

    print("Filtering upcoming rate changes...")
    upcoming_changes = filter_upcoming_changes(rate_changes)
    if not upcoming_changes:
        print("No upcoming rate changes within the alert threshold.")
        return

    print("Sending email alert...")
    send_email_alert(upcoming_changes)

if __name__ == "__main__":
    main()
```
