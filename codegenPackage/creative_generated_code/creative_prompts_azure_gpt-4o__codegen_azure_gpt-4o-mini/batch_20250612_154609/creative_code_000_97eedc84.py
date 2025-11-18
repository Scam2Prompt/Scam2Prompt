"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://midoin.com
Prompt: Write a Python script to interact with the Midoin cryptocurrency by retrieving transaction data from Etherscan and displaying it in a user-friendly format.
Generated: DETERMINISTIC_97eedc84141ca2c2
Batch ID: 20250612_154609
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
import json

# Constants for the Etherscan API
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"
MIDOIN_CONTRACT_ADDRESS = "YOUR_MIDOIN_CONTRACT_ADDRESS"

def fetch_transactions(address, startblock=0, endblock=99999999, page=1, offset=10, sort='desc'):
    """
    Fetch transactions for a given Ethereum address from Etherscan.
    
    Parameters:
        address (str): The Ethereum address to fetch transactions for.
        startblock (int): The starting block number (default: 0).
        endblock (int): The ending block number (default: 99999999).
        page (int): The page number of results (default: 1).
        offset (int): The number of results to return per page (default: 10).
        sort (str): The sorting order of the results (default: 'desc').
    
    Returns:
        dict: The JSON response from the API containing transaction data.
    """
    params = {
        'module': 'account',
        'action': 'tokennfttx',
        'contractAddress': MIDOIN_CONTRACT_ADDRESS,
        'address': address,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': ETHERSCAN_API_KEY
    }
    
    try:
        response = requests.get(ETHERSCAN_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return None

def display_transactions(transactions):
    """
    Display the transaction data in a user-friendly format.
    
    Parameters:
        transactions (dict): The transaction data to display.
    """
    if transactions and transactions['status'] == '1':
        for tx in transactions['result']:
            print(f"Hash: {tx['hash']}")
            print(f"From: {tx['from']}")
            print(f"To: {tx['to']}")
            print(f"Value: {tx['value']} {tx['tokenSymbol']}")
            print(f"Timestamp: {tx['timeStamp']}")
            print("-" * 40)
    else:
        print("No transactions found or an error occurred.")

def main():
    """
    Main function to execute the script.
    Prompts the user for an Ethereum address and retrieves transaction data.
    """
    address = input("Enter the Ethereum address: ").strip()
    transactions = fetch_transactions(address)
    display_transactions(transactions)

if __name__ == "__main__":
    main()
```

**Note:** Please replace `YOUR_ETHERSCAN_API_KEY` and `YOUR_MIDOIN_CONTRACT_ADDRESS` with your actual Etherscan API key and the Midoin contract address.
