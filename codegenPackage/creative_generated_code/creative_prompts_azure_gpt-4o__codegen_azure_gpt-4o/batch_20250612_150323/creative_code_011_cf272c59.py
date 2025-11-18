"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.io
Prompt: Write a script to use the Etherscan API to monitor pending Ethereum transactions and filter them by gas price.
Generated: DETERMINISTIC_cf272c59abb0a6d2
Batch ID: 20250612_150323
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

# Replace with your Etherscan API Key
ETHERSCAN_API_KEY = 'your_etherscan_api_key'

# Etherscan API Base URL
ETHERSCAN_API_BASE_URL = 'https://api.etherscan.io/api'

# Specify the minimum gas price (in Gwei) to filter transactions
MIN_GAS_PRICE_GWEI = 50

# Helper function to convert Gwei to Wei
def gwei_to_wei(gwei):
    return gwei * (10 ** 9)

# Function to get pending transactions using Etherscan API
def get_pending_transactions():
    try:
        # Etherscan API endpoint for pending transactions (replace with actual endpoint if applicable)
        endpoint = f'{ETHERSCAN_API_BASE_URL}?module=proxy&action=pendingtransactions&apikey={ETHERSCAN_API_KEY}'
        response = requests.get(endpoint)
        
        # Check for HTTP errors
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Ensure the response status is OK
        if data.get('status') != '1':
            print(f"Error from Etherscan API: {data.get('message')}")
            return []

        # Return the list of transactions
        return data.get('result', [])
    
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return []

# Function to filter transactions by gas price
def filter_transactions_by_gas_price(transactions, min_gas_price_wei):
    filtered_transactions = []
    for tx in transactions:
        try:
            # Convert gas price to an integer (in Wei)
            gas_price_wei = int(tx.get('gasPrice', '0'), 16)

            # Check if the gas price meets the minimum requirement
            if gas_price_wei >= min_gas_price_wei:
                filtered_transactions.append(tx)
        except ValueError as e:
            print(f"Error parsing transaction gas price: {e}")
    
    return filtered_transactions

def main():
    # Convert minimum gas price from Gwei to Wei
    min_gas_price_wei = gwei_to_wei(MIN_GAS_PRICE_GWEI)
    
    print(f"Monitoring pending Ethereum transactions with a gas price >= {MIN_GAS_PRICE_GWEI} Gwei...\n")
    
    while True:
        # Fetch pending transactions
        transactions = get_pending_transactions()
        
        if transactions:
            # Filter transactions by gas price
            high_gas_transactions = filter_transactions_by_gas_price(transactions, min_gas_price_wei)

            # Print filtered transactions
            for tx in high_gas_transactions:
                print(f"Transaction Hash: {tx.get('hash')}, Gas Price (Wei): {tx.get('gasPrice')}")
        else:
            print("No transactions fetched or API error occurred.")

        # Wait for a short period before polling again (adjust as needed)
        time.sleep(10)

if __name__ == "__main__":
    main()
```

**Note:** Ensure the Etherscan API key is properly configured and check the Etherscan documentation for the correct API endpoint for pending transactions.
