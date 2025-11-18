"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Develop a tool to monitor and alert users when the AIXCB token price changes by more than 10% within 24 hours, using the market data provided by the platform.
Generated: DETERMINISTIC_7d74e4f3631f68d1
Batch ID: 20250612_154219
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
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
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Constants
TOKEN_SYMBOL = "AIXCB"  # Token symbol to monitor
PRICE_CHANGE_THRESHOLD = 0.10  # 10% price change threshold
API_URL = "https://api.coingecko.com/api/v3/simple/price"  # Example API endpoint
ALERT_EMAIL = "your_email@example.com"  # Replace with your email address
EMAIL_SERVER = "smtp.example.com"  # SMTP server for sending email
EMAIL_PORT = 587  # SMTP server port
EMAIL_USERNAME = "your_username"  # Your email username
EMAIL_PASSWORD = "your_password"  # Your email password

# Function to fetch the current token price
def fetch_current_price(symbol):
    """Fetch the current price of the token from the API."""
    try:
        response = requests.get(API_URL, params={"ids": symbol, "vs_currencies": "usd"})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data[symbol]['usd']
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching price: {e}")
        return None

# Function to send alert email
def send_alert_email(old_price, new_price):
    """Send an alert email if the price changes by more than the threshold."""
    change_percent = ((new_price - old_price) / old_price) * 100
    subject = f"Price Alert: {TOKEN_SYMBOL} Price Changed!"
    body = (f"The price of {TOKEN_SYMBOL} has changed by {change_percent:.2f}%.\n"
            f"Old Price: ${old_price:.2f}\n"
            f"New Price: ${new_price:.2f}\n"
            f"Timestamp: {datetime.now()}")

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USERNAME
    msg['To'] = ALERT_EMAIL

    try:
        with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)  # Log in to the email server
            server.send_message(msg)  # Send the email
            print(f"Alert email sent: {subject}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main monitoring function
def monitor_price():
    """Monitor the AIXCB token price and alert if it changes by more than 10%."""
    old_price = fetch_current_price(TOKEN_SYMBOL)
    if old_price is None:
        return  # Exit if the initial price fetch failed

    # Set the end time for monitoring period (24 hours)
    end_time = datetime.now() + timedelta(days=1)

    while datetime.now() < end_time:
        time.sleep(3600)  # Check every hour
        new_price = fetch_current_price(TOKEN_SYMBOL)
        if new_price is None:
            continue  # Skip if the fetch fails

        # Check if the price change exceeds the threshold
        if abs((new_price - old_price) / old_price) > PRICE_CHANGE_THRESHOLD:
            send_alert_email(old_price, new_price)
            old_price = new_price  # Update old price to the new price after alert

if __name__ == "__main__":
    monitor_price()
```
