"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.io
Prompt: Write a script to use the Etherscan API to retrieve and analyze the top Ethereum accounts by balance.
Generated: DETERMINISTIC_0e54f73e65c537b8
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

# Configuration for the Etherscan API
ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY'  # Replace with your Etherscan API key
ETHERSCAN_API_URL = 'https://api.etherscan.io/api'


def get_top_accounts(limit=10):
    """
    Retrieves the top Ethereum accounts by balance from the Etherscan API.

    Args:
        limit (int): The number of top accounts to retrieve.

    Returns:
        list: A list of dictionaries containing account addresses and balances.

    Raises:
        Exception: If the API request fails or returns an error.
    """
    try:
        # Preparing the API request parameters
        params = {
            'module': 'account',
            'action': 'list',
            'sort': 'desc',
            'count': limit,
            'apikey': ETHERSCAN_API_KEY
        }
        
        # Making the API request
        response = requests.get(ETHERSCAN_API_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()

        # Check if the API returned an error
        if data['status'] != '1':
            raise Exception(f"Error from Etherscan API: {data['message']}")

        # Extracting account addresses and balances
        return [
            {
                'address': account['account'],
                'balance': float(account['balance']) / 1e18  # Convert Wei to Ether
            }
            for account in data['result']
        ]

    except requests.RequestException as e:
        raise Exception(f"An error occurred while fetching data from Etherscan: {e}")


def analyze_accounts(accounts):
    """
    Analyzes the list of top Ethereum accounts and prints their details.

    Args:
        accounts (list): A list of top Ethereum account dictionaries.
    """
    print("Top Ethereum Accounts by Balance:")
    print("-" * 40)
    for account in accounts:
        print(f"Address: {account['address']}, Balance: {account['balance']:.4f} ETH")


if __name__ == "__main__":
    # Main execution block
    try:
        top_accounts = get_top_accounts(limit=10)
        analyze_accounts(top_accounts)
    except Exception as e:
        print(f"Error: {e}")
```
