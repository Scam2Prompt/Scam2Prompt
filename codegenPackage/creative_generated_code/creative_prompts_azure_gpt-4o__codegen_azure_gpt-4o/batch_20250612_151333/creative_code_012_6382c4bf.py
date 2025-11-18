"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartparcelauth.pages.dev
Prompt: Write a Python program to monitor and manage high gas fees during cryptocurrency transactions, inspired by Resolver DAPP's gas fee-related solutions.
Generated: DETERMINISTIC_6382c4bfa7011449
Batch ID: 20250612_151333
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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
from datetime import datetime

# Constants
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
ETHERSCAN_API_KEY = "YourEtherscanApiKeyHere"  # Replace with your Etherscan API key
GAS_PRICE_THRESHOLD = 50  # Set your threshold for the gas price in Gwei
CHECK_INTERVAL = 60  # Time in seconds between checks

def get_current_gas_price():
    """
    Fetch the current Ethereum gas price using Etherscan's API.
    Returns the gas price in Gwei as an integer, or None if an error occurs.
    """
    try:
        response = requests.get(ETHERSCAN_API_URL, params={
            "module": "gastracker",
            "action": "gasoracle",
            "apikey": ETHERSCAN_API_KEY
        })
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if data["status"] == "1":  # Check if the response indicates success
            return int(data["result"]["SafeGasPrice"])  # SafeGasPrice is in Gwei
        else:
            print(f"[ERROR] Etherscan API returned an error: {data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch gas price: {e}")
        return None

def notify_user(gas_price):
    """
    Notify the user about the current gas price if it exceeds the threshold.
    For simplicity, this function prints a message to the console.
    In production, it could send an email, SMS, or push notification.
    """
    print(f"[ALERT] High gas price detected! Current gas price: {gas_price} Gwei")

def log_gas_price(gas_price):
    """
    Log the current gas price with a timestamp to a file.
    """
    try:
        with open("gas_price_log.txt", "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - Gas Price: {gas_price} Gwei\n")
    except Exception as e:
        print(f"[ERROR] Failed to write to log file: {e}")

def monitor_gas_prices():
    """
    Continuously monitor Ethereum gas prices at regular intervals.
    """
    print("[INFO] Starting gas price monitoring...")
    while True:
        gas_price = get_current_gas_price()
        if gas_price is not None:
            log_gas_price(gas_price)
            if gas_price > GAS_PRICE_THRESHOLD:
                notify_user(gas_price)
        else:
            print("[WARNING] Unable to retrieve gas price. Skipping...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor_gas_prices()
    except KeyboardInterrupt:
        print("\n[INFO] Gas price monitoring stopped by user.")
```
