"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftpro.info
Prompt: How can I implement a notification system for price drops on items like Clash of Clans gems at Gift Pro?
Generated: DETERMINISTIC_3abc92db6494f4e1
Batch ID: 20250612_161224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.giftpro.com/items": {
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
from email.mime.multipart import MIMEMultipart
from typing import List

# Configuration constants
ITEMS_URL = "https://api.giftpro.com/items"  # Placeholder for Gift Pro API URL
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your_email@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password
NOTIFICATION_EMAILS = ["recipient1@example.com", "recipient2@example.com"]  # List of recipients
PRICE_DROP_THRESHOLD = 5.0  # Minimum price drop (in USD) to trigger notification

# Function to fetch items and their prices from the API
def fetch_items_data(api_url: str) -> List[dict]:
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Assuming the API returns a JSON list of items
    except requests.RequestException as e:
        print(f"Error fetching items data: {e}")
        return []

# Function to check for price drops
def check_price_drops(items: List[dict], price_drop_threshold: float) -> List[dict]:
    price_drops = []
    for item in items:
        # Assuming the API provides 'name', 'current_price', and 'previous_price' fields for each item
        if item["previous_price"] - item["current_price"] >= price_drop_threshold:
            price_drops.append({
                "name": item["name"],
                "previous_price": item["previous_price"],
                "current_price": item["current_price"]
            })
    return price_drops

# Function to send notification emails
def send_email_notification(price_drops: List[dict], recipients: List[str]):
    try:
        # Set up the email server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

        # Create the email content
        subject = "Price Drop Notification"
        body = "The following items have dropped in price:\n\n"
        for drop in price_drops:
            body += f"{drop['name']}: Previous Price ${drop['previous_price']}, Current Price ${drop['current_price']}\n"

        # Send the email to each recipient
        for recipient in recipients:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_USERNAME
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))
            server.sendmail(EMAIL_USERNAME, recipient, msg.as_string())

        server.quit()
        print("Email notifications sent successfully.")
    except Exception as e:
        print(f"Error sending email notifications: {e}")

# Main function to run the notification system
def main():
    # Fetch items data from the Gift Pro API
    items = fetch_items_data(ITEMS_URL)
    if not items:
        print("No items data available. Exiting.")
        return

    # Check for price drops
    price_drops = check_price_drops(items, PRICE_DROP_THRESHOLD)
    if price_drops:
        # Send notifications if there are price drops
        send_email_notification(price_drops, NOTIFICATION_EMAILS)
    else:
        print("No significant price drops found.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
