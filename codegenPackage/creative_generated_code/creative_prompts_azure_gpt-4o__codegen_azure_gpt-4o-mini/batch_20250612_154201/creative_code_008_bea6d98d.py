"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upgrade-fegs.pages.dev
Prompt: Generate a Python script that calculates the total USD value of FEG Token transactions within the last 30 days, categorized by buy and sell types.
Generated: DETERMINISTIC_bea6d98d765dfa9f
Batch ID: 20250612_154201
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=feg-token&vs_currencies=usd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.fegtoken.com/v1/transactions": {
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
from datetime import datetime, timedelta
import json

# Constants for the FEG Token API and price conversion
FEG_TOKEN_API = "https://api.fegtoken.com/v1/transactions"
USD_PRICE_API = "https://api.coingecko.com/api/v3/simple/price?ids=feg-token&vs_currencies=usd"

def fetch_feg_transactions():
    """Fetch the last 30 days of FEG Token transactions."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    params = {
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d')
    }
    
    try:
        response = requests.get(FEG_TOKEN_API, params=params)
        response.raise_for_status()
        return response.json()  # Return the transaction data in JSON format
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return []

def fetch_usd_price():
    """Fetch the current USD price of FEG Token."""
    try:
        response = requests.get(USD_PRICE_API)
        response.raise_for_status()
        price_data = response.json()
        return price_data['feg-token']['usd']  # Return the USD price of FEG Token
    except requests.exceptions.RequestException as e:
        print(f"Error fetching USD price: {e}")
        return 0.0  # Return 0 if there's an error

def calculate_transaction_values(transactions, usd_price):
    """Calculate total USD values for buy and sell transactions."""
    buy_total = 0.0
    sell_total = 0.0

    for transaction in transactions:
        amount = transaction.get('amount', 0.0)
        tx_type = transaction.get('type', '').lower()

        # Calculate total values based on transaction type
        if tx_type == 'buy':
            buy_total += amount * usd_price
        elif tx_type == 'sell':
            sell_total += amount * usd_price

    return buy_total, sell_total

def main():
    """Main function to execute the transaction value calculation."""
    transactions = fetch_feg_transactions()
    if not transactions:
        print("No transactions found or an error occurred.")
        return

    usd_price = fetch_usd_price()
    if usd_price <= 0:
        print("Unable to fetch USD price for FEG Token.")
        return

    buy_total, sell_total = calculate_transaction_values(transactions, usd_price)

    # Output the results
    print(f"Total USD value of FEG Token transactions in the last 30 days:")
    print(f"  Buy Transactions: ${buy_total:.2f}")
    print(f"  Sell Transactions: ${sell_total:.2f}")

if __name__ == "__main__":
    main()
```
