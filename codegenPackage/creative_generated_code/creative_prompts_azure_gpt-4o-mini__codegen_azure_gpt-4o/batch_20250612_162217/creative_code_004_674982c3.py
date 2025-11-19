"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bromptonsciences.com
Prompt: Generate code to set alerts for specific on-chain transactions using Arkham Intel features while trading on the Arkham Exchange.
Generated: DETERMINISTIC_674982c3d55e5265
Batch ID: 20250612_162217
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.arkhamintel.com/v1": {
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
import time

# Constants
ARKHAM_API_URL = "https://api.arkhamintel.com/v1"
API_KEY = "your_api_key_here"  # Replace with your Arkham API key
TRANSACTION_ALERT_CRITERIA = {
    "sender_address": "0x1234567890abcdef",  # Example Ethereum address
    "recipient_address": "0xfedcba0987654321",
    "min_value": 1.0,  # Minimum transaction value in ETH
}
POLLING_INTERVAL = 60  # Time in seconds to poll the Arkham API

def get_recent_transactions(api_key):
    """
    Fetches the most recent transactions from Arkham Intel API.
    """
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(f"{ARKHAM_API_URL}/transactions/recent", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return None

def matches_alert_criteria(transaction, criteria):
    """
    Checks if a given transaction meets the specified alert criteria.

    Args:
        transaction (dict): A transaction object from the API response.
        criteria (dict): The alert criteria.

    Returns:
        bool: True if the transaction matches the criteria, False otherwise.
    """
    try:
        sender_matches = transaction.get("sender") == criteria.get("sender_address")
        recipient_matches = transaction.get("recipient") == criteria.get("recipient_address")
        value_matches = float(transaction.get("value", 0)) >= criteria.get("min_value")
        return sender_matches and recipient_matches and value_matches
    except (ValueError, TypeError):
        print("Error processing transaction data.")
        return False

def send_alert(transaction):
    """
    Sends an alert when a transaction matches the criteria.
    For demonstration purposes, this will just print the transaction.
    """
    print("ALERT: Matching transaction detected!")
    print(json.dumps(transaction, indent=4))

def monitor_transactions(api_key, criteria, interval):
    """
    Continuously monitors transactions and sends alerts for matches.

    Args:
        api_key (str): Arkham API key.
        criteria (dict): Alert criteria for transactions.
        interval (int): Polling interval in seconds.
    """
    print("Starting transaction monitoring...")
    while True:
        transactions = get_recent_transactions(api_key)
        if transactions:
            for transaction in transactions:
                if matches_alert_criteria(transaction, criteria):
                    send_alert(transaction)
        time.sleep(interval)

if __name__ == "__main__":
    try:
        # Start monitoring transactions
        monitor_transactions(API_KEY, TRANSACTION_ALERT_CRITERIA, POLLING_INTERVAL)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
