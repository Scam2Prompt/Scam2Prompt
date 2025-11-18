"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai327k.com
Prompt: Write a Python script to log and analyze xAI327K token presale transactions using blockchain explorers for Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_382cc96778dc26d6
Batch ID: 20250612_150034
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.bscscan.com/api": {
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
import logging
from datetime import datetime

# Configure logging settings
logging.basicConfig(
    filename='xai_presale.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s'
)

# Constants for blockchain explorers APIs
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
BSC_SCAN_API_URL = "https://api.bscscan.com/api"
ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY'
BSC_SCAN_API_KEY = 'YOUR_BSCSCAN_API_KEY'

# Token contract addresses
XAI_ERC20_ADDRESS = '0xYourERC20AddressHere'
XAI_BSC_ADDRESS = '0xYourBSCAddressHere'

def fetch_transactions(api_url, api_key, address):
    """
    Fetch transactions for the given address from the specified blockchain explorer.
    
    :param api_url: URL of the blockchain explorer API
    :param api_key: API key for authentication
    :param address: Contract address to fetch transactions for
    :return: List of transactions or an empty list in case of error
    """
    try:
        response = requests.get(api_url, params={
            'module': 'account',
            'action': 'tokentx',
            'contractaddress': address,
            'apikey': api_key
        })
        response.raise_for_status()  # Raise an error forbad status codes
        data = response.json()
        
        if data['status'] == '1':  # Successful response
            return data['result']
        else:
            logging.error(f"Error fetching transactions: {data['message']}")
            return []
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")
        return []

def analyze_transactions(transactions):
    """
    Analyze the fetched transactions for the token presale.

    :param transactions: List of transactions to analyze
    :return: None
    """
    for tx in transactions:
        # Example: Log transaction details
        tx_hash = tx['hash']
        from_address = tx['from']
        to_address = tx['to']
        value = int(tx['value']) / 10**18  # Convert from Wei to Ether
        timestamp = datetime.utcfromtimestamp(int(tx['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
        
        logging.info(f"Transaction Hash: {tx_hash}, From: {from_address}, To: {to_address}, Value: {value} ETH, Time: {timestamp}")

def main():
    """
    Main function to fetch and analyze xAI327K token presale transactions.
    """
    logging.info("Starting transaction fetch for Ethereum...")
    eth_transactions = fetch_transactions(ETHERSCAN_API_URL, ETHERSCAN_API_KEY, XAI_ERC20_ADDRESS)
    analyze_transactions(eth_transactions)

    logging.info("Starting transaction fetch for Binance Smart Chain...")
    bsc_transactions = fetch_transactions(BSC_SCAN_API_URL, BSC_SCAN_API_KEY, XAI_BSC_ADDRESS)
    analyze_transactions(bsc_transactions)

if __name__ == "__main__":
    main()
``` 

Make sure to replace `'YOUR_ETHERSCAN_API_KEY'`, `'YOUR_BSCSCAN_API_KEY'`, `'0xYourERC20AddressHere'`, and `'0xYourBSCAddressHere'` with your actual API keys and token contract addresses before running the script.
