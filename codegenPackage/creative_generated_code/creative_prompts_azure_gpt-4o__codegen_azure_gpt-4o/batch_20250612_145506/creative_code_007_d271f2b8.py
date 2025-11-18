"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purplepepesolana.pages.dev
Prompt: Write a script to analyze transaction data for $PURPE tokens to identify trends and generate insights about the meme coin's growth on Solana.
Generated: DETERMINISTIC_d271f2b8a0a4fb2c
Batch ID: 20250612_145506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solscan.io/account/transactions": {
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
import pandas as pd
from datetime import datetime
from collections import defaultdict

# Constants
SOLANA_API_URL = "https://api.solscan.io/account/transactions"
PURPE_TOKEN_ADDRESS = "<INSERT_PURPE_TOKEN_ADDRESS_HERE>"  # Replace with the actual $PURPE token address
API_KEY = "<INSERT_YOUR_API_KEY_HERE>"  # Replace with your Solana API key

# Helper function to fetch transaction data from Solana API
def fetch_transactions(token_address, api_key, limit=1000):
    """
    Fetch transaction data for a given token address using the Solana API.

    :param token_address: Address of the token (e.g., $PURPE token address).
    :param api_key: Solana API key for authorization.
    :param limit: Maximum number of transactions to fetch (default: 1000).
    :return: List of transaction data or an empty list in case of errors.
    """
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        params = {"account": token_address, "limit": limit}
        response = requests.get(SOLANA_API_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data.get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return []

# Helper function to parse transaction data
def parse_transactions(transactions):
    """
    Parse the raw transaction data to extract meaningful insights.

    :param transactions: List of transaction data.
    :return: A list of cleaned and structured transactions.
    """
    parsed_data = []
    for txn in transactions:
        try:
            parsed_data.append({
                "timestamp": datetime.utcfromtimestamp(txn["blockTime"]),
                "signature": txn["txHash"],
                "amount": float(txn["amount"]) if "amount" in txn else 0.0,
                "sender": txn["source"],
                "receiver": txn["destination"],
                "status": txn.get("status", "unknown"),
            })
        except KeyError as e:
            print(f"Skipping transaction due to missing field: {e}")
    return parsed_data

# Function to identify trends and generate insights
def generate_insights(parsed_transactions):
    """
    Analyze parsed transactions to identify trends and generate insights.

    :param parsed_transactions: List of structured transaction data.
    :return: Dictionary containing insights and trends.
    """
    insights = defaultdict(int)
    total_volume = 0
    transaction_count = len(parsed_transactions)

    for txn in parsed_transactions:
        insights["total_transactions"] += 1
        total_volume += txn["amount"]
        insights["unique_senders"].add(txn["sender"])
        insights["unique_receivers"].add(txn["receiver"])

    insights["total_volume"] = total_volume
    insights["average_transaction_value"] = total_volume / transaction_count if transaction_count > 0 else 0
    insights["unique_sender_count"] = len(insights["unique_senders"])
    insights["unique_recipient_count"] = len(insights["unique_receivers"])

# Entry point of the script
if __name__.
```
