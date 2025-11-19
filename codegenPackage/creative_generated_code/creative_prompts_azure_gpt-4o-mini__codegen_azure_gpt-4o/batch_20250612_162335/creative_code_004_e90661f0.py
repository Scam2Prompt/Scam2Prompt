"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelllar.org
Prompt: Illustrate how to set up a notification system for on-time delivery updates using Stelllar Logistics' tracking features.
Generated: DETERMINISTIC_e90661f060754247
Batch ID: 20250612_162335
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.stellarlogistics.com/v1/tracking": {
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
"""
Notification System for On-Time Delivery Updates using Stellar Logistics Tracking API.

This script sets up a notification system to monitor and notify users about 
on-time delivery updates from Stellar Logistics. It fetches tracking updates 
from the API and sends notifications to users via email when a new delivery update is available.
"""

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

# Configurations for the Stellar Logistics Tracking API
STELLAR_API_URL = "https://api.stellarlogistics.com/v1/tracking"
STELLAR_API_KEY = "your_api_key_here"  # Replace with your actual API key

# Email Notification Settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"  # Use environment variables or a secure method to store secrets

def fetch_tracking_updates() -> List[dict]:
    """
    Fetch delivery updates from Stellar Logistics API.

    Returns:
        List[dict]: A list of tracking updates.
    """
    try:
        headers = {
            "Authorization": f"Bearer {STELLAR_API_KEY}"
        }
        response = requests.get(STELLAR_API_URL, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json().get("updates", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tracking updates: {e}")
        return []

def send_email_notification(recipient: str, subject: str, body: str) -> None:
    """
    Send an email notification.

    Args:
        recipient (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    try:
        # Create the email
        message = MIMEMultipart()
        message["From"] = EMAIL_SENDER
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(message)
            print(f"Notification sent to {recipient}.")
    except Exception as e:
        print(f"Error sending email notification: {e}")

def process_tracking_updates(updates: List[dict]) -> None:
    """
    Process tracking updates and send notifications for on-time deliveries.

    Args:
        updates (List[dict]): List of tracking update dictionaries.
    """
    for update in updates:
        if update.get("status") == "on-time":
            delivery_id = update.get("delivery_id", "Unknown")
            recipient_email = update.get("recipient_email", "")
            expected_date = update.get("expected_date", "Unknown")
            subject = f"On-Time Delivery Update for Delivery ID: {delivery_id}"
            body = (
                f"Good news! Your delivery with ID {delivery_id} is on track and expected "
                f"to arrive on {expected_date}.\n\nThank you for choosing Stellar Logistics!"
            )
            if recipient_email:
                send_email_notification(recipient_email, subject, body)

def main():
    """
    Main function to set up and run the notification system.
    """
    print("Fetching delivery updates...")
    updates = fetch_tracking_updates()
    if updates:
        print(f"Processing {len(updates)} updates...")
        process_tracking_updates(updates)
    else:
        print("No updates available.")

if __name__ == "__main__":
    main()
```
