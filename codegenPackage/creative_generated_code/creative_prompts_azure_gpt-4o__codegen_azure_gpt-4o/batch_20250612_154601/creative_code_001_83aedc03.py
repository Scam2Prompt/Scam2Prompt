"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltetradingsacademy.com
Prompt: Recommend libraries or APIs for implementing a "Rate Alerts" system that notifies users when specific currency exchange rates are met, as mentioned on the Grand Chase platform.
Generated: DETERMINISTIC_83aedc03a5b2989a
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate-api.com/v4/latest": {
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
# rate_alerts.py

"""
This script implements a "Rate Alerts" system that notifies users when specific currency exchange rates are met.
It uses a third-party API for exchange rate data and Python libraries for notifications.
"""

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import time

# Configure logging
logging.basicConfig(
    filename="rate_alerts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Configuration
API_URL = "https://api.exchangerate-api.com/v4/latest"
ALERT_THRESHOLD = {
    # Example: Notify when USD/INR exceeds a certain rate
    "USD_INR": {"greater_than": 83.0, "less_than": None},
    "EUR_USD": {"greater_than": None, "less_than": 1.05},
}
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "your_email@gmail.com",
    "sender_password": "your_password",  # Use app password for security
    "recipient_email": "recipient_email@gmail.com",
}

# Function to fetch exchange rate data
def fetch_exchange_rates(base_currency="USD"):
    """
    Fetches current exchange rates for the provided base currency.
    :param base_currency: The currency to use as the base (default: USD).
    :return: Dictionary containing exchange rates.
    """
    try:
        response = requests.get(f"{API_URL}/{base_currency}")
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()["rates"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching exchange rates: {e}")
        return None

# Function to check rates against thresholds
def check_alerts(rates):
    """
    Checks exchange rates against alert thresholds and generates notifications if conditions are met.
    :param rates: Dictionary of exchange rates to evaluate.
    """
    for pair, thresholds in ALERT_THRESHOLD.items():
        base, target = pair.split("_")
        rate = rates.get(target)

        if rate is None:
            logging.warning(f"Exchange rate for {pair} not found.")
            continue

        if thresholds["greater_than"] and rate > thresholds["greater_than"]:
            send_notification(pair, rate, condition="above")
        elif thresholds["less_than"] and rate < thresholds["less_than"]:
            send_notification(pair, rate, condition="below")

# Function to send email notifications
def send_notification(currency_pair, rate, condition):
    """
    Sends an email notification about the exchange rate condition.
    :param currency_pair: The currency pair being monitored.
    :param rate: The current exchange rate.
    :param condition: The condition met ("above" or "below").
    """
    try:
        subject = f"Rate Alert for {currency_pair}"
        message = (
            f"The exchange rate for {currency_pair} is now {condition} the threshold at {rate}."
        )
        email_message = MIMEMultipart()
        email_message["From"] = EMAIL_CONFIG["sender_email"]
        email_message["To"] = EMAIL_CONFIG["recipient_email"]
        email_message["Subject"] = subject
        email_message.attach(MIMEText(message, "plain"))

        with smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["smtp_port"]) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_CONFIG["sender_email"], EMAIL_CONFIG["sender_password"])
            server.send_message(email_message)

        logging.info(f"Notification sent for {currency_pair}: {message}")
    except Exception as e:
        logging.error(f"Error sending notification: {e}")

# Main function to execute the rate alerts system
def main():
    """
    Main entry point for the script. Continuously fetches exchange rates and checks alerts.
    """
    try:
        while True:
            logging.info("Fetching exchange rates...")
            rates = fetch_exchange_rates()

            if rates:
                logging.info("Checking alerts...")
                check_alerts(rates)
            else:
                logging.warning("No rates fetched. Skipping this cycle.")

            # Wait for a specified duration before the next check (e.g., 60 seconds)
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("Rate Alerts system stopped by user.")

if __name__ == "__main__":
    main()
```
