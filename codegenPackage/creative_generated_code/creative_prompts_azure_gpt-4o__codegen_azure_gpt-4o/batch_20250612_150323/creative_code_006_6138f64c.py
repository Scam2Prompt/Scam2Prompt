"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.com
Prompt: Generate code to use the Etherscan API for fetching and analyzing the latest NFT mints on the Ethereum blockchain.
Generated: DETERMINISTIC_6138f64cc1720d33
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
import json
from datetime import datetime

# Etherscan API Configuration
ETHERSCAN_API_KEY = 'your_etherscan_api_key'  # Replace with your Etherscan API key
ETHERSCAN_BASE_URL = 'https://api.etherscan.io/api'

# Function to fetch the latest transactions of an address
def fetch_latest_transactions(contract_address, page=1, offset=10, sort='desc'):
    """
    Fetches the latest transactions from the Etherscan API for a given address.
    
    Parameters:
        contract_address (str): The Ethereum address of the contract.
        page (int): The page number of transactions to fetch.
        offset (int): The number of records per page.
        sort (str): Sorting preference ('asc' or 'desc').

    Returns:
        dict: Parsed JSON response containing transaction data.
    """
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': contract_address,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': ETHERSCAN_API_KEY
    }

    try:
        response = requests.get(ETHERSCAN_BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()

        if data['status'] != '1':  # Check API response status
            raise ValueError(f"Etherscan API error: {data['message']}")

        return data['result']  # Return the list of transactions
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None
    except ValueError as ve:
        print(f"API Error: {ve}")
        return None

# Function to analyze NFT mints
def analyze_nft_mints(transactions):
    """
    Analyzes transactions to identify NFT mints.

    Parameters:
        transactions (list): List of transaction data.

    Returns:
        list: List of NFT mint transactions.
    """
    nft_mints = []

    for tx in transactions:
        # Check for 'to' address and input data indicating token mint (ERC-721 or ERC-1155 standards)
        if tx['to'] and tx['input'].startswith('0x'):  # Basic input check
            nft_mints.append({
                'blockNumber': tx['blockNumber'],
                'hash': tx['hash'],
                'from': tx['from'],
                'to': tx['to'],
                'value': int(tx['value']) / (10 ** 18),  # Convert wei to ether
                'timestamp': datetime.utcfromtimestamp(int(tx['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            })

    return nft_mints

# Main function to execute the script
def main():
    """
    Main function to fetch and analyze latest NFT mint transactions.
    """
    # Example Ethereum contract address for an NFT collection (replace with actual address)
    contract_address = '0xYourContractAddressHere'

    print("Fetching latest transactions...")
    transactions = fetch_latest_transactions(contract_address, page=1, offset=10)

    if not transactions:
        print("No transactions fetched. Exiting...")
        return

    print("Analyzing NFT mints...")
    nft_mints = analyze_nft_mints(transactions)

    if nft_mints:
        print("NFT Mint Transactions:")
        for mint in nft_mints:
            print(json.dumps(mint, indent=4))
    else:
        print("No NFT mint transactions found.")

if __name__ == "__main__":
    main()
```
