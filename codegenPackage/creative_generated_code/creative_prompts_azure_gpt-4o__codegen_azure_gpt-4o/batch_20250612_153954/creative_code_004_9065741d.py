"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrett.on-fleek.app
Prompt: Write a Python script to monitor $Brett token activity on the Base Chain and send Telegram alerts for large transactions or price changes.
Generated: DETERMINISTIC_9065741dbb7f2c56
Batch ID: 20250612_153954
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.basechain.com/v1": {
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
from telegram import Bot

# Configuration
BASE_CHAIN_API_URL = "https://api.basechain.com/v1"  # Replace with the correct Base Chain API URL
TOKEN_ADDRESS = "YOUR_BRETT_TOKEN_ADDRESS"          # Replace with the Brett token's address
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"      # Replace with your Telegram bot token
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"          # Replace with your Telegram chat ID
LARGE_TRANSACTION_THRESHOLD = 1000                 # Threshold for large transactions (e.g., in Brett tokens)
PRICE_CHANGE_THRESHOLD_PERCENT = 5                 # Threshold for percentage price change
CHECK_INTERVAL_SECONDS = 60                        # Interval to check (in seconds)

# Initialize global variables
last_price = None

# Function to fetch the latest token price
def fetch_token_price():
    try:
        response = requests.get(f"{BASE_CHAIN_API_URL}/token/{TOKEN_ADDRESS}/price")
        response.raise_for_status()  # Raise an error for non-2xx responses
        return response.json().get("price", None)
    except requests.RequestException as e:
        print(f"Error fetching token price: {e}")
        return None

# Function to fetch recent transactions
def fetch_recent_transactions():
    try:
        response = requests.get(f"{BASE_CHAIN_API_URL}/token/{TOKEN_ADDRESS}/transactions")
        response.raise_for_status()
        return response.json().get("transactions", [])
    except requests.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return []

# Function to send a Telegram alert
def send_telegram_alert(message):
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        print(f"Error sending Telegram alert: {e}")

# Function to monitor token activity
def monitor_token_activity():
    global last_price

    while True:
        # Monitor price changes
        current_price = fetch_token_price()
        if current_price is not None and last_price is not None:
            price_change = ((current_price - last_price) / last_price) * 100
            if abs(price_change) >= PRICE_CHANGE_THRESHOLD_PERCENT:
                send_telegram_alert(
                    f"[ALERT] Significant price change detected for Brett token: {price_change:.2f}%.\nNew Price: {current_price}"
                )
        last_price = current_price if last_price is None else last_price

        # Monitor large transactions
        transactions = fetch_recent_transactions()
        for transaction in transactions:
            amount = transaction.get("amount", 0)
            if amount >= LARGE_TRANSACTION_THRESHOLD:
                send_telegram_alert(
                    f"[ALERT] Large transaction detected!\nAmount: {amount}\nFrom: {transaction.get('from')}\nTo: {transaction.get('to')}"
                )

        # Wait for the next check
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    print("Starting Brett token activity monitor...")
    try:
        monitor_token_activity()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
