"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://88bitkan.com
Prompt: Create a Python script to interact with the WLFI token smart contract and retrieve the latest transaction details, including age and hash, as shown on the website.
Generated: DETERMINISTIC_233b8b4f4ad02661
Batch ID: 20250612_154001
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
  "https://mainnet.infura.io/v3/{INFURA_PROJECT_ID": {
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
from web3 import Web3
from datetime import datetime

# Constants
INFURA_PROJECT_ID = "your_infura_project_id"  # Replace with your Infura Project ID
ETHERSCAN_API_KEY = "your_etherscan_api_key"  # Replace with your Etherscan API key
WLFI_CONTRACT_ADDRESS = "0xYourContractAddressHere"  # Replace with WLFI smart contract address
ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"))

# Ensure successful connection to the Ethereum blockchain
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum blockchain via Infura.")

# Function to fetch latest transactions from Etherscan
def get_latest_transactions(contract_address, api_key):
    """
    Retrieve the latest transactions for a given contract from Etherscan.

    :param contract_address: Smart contract address.
    :param api_key: Etherscan API key.
    :return: List of transaction dictionaries.
    """
    try:
        # API request to retrieve contract's transaction list
        response = requests.get(
            ETHERSCAN_BASE_URL,
            params={
                "module": "account",
                "action": "txlist",
                "address": contract_address,
                "startblock": 0,
                "endblock": 99999999,
                "sort": "desc",
                "apikey": api_key,
            },
        )
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()

        # Check for Etherscan API errors
        if data["status"] != "1":
            raise ValueError(f"Etherscan API Error: {data['message']}")

        return data["result"]

    except requests.RequestException as e:
        raise RuntimeError(f"HTTP Request Failed: {e}")

    except ValueError as ve:
        raise RuntimeError(f"Data Retrieval Error: {ve}")


# Function to format transaction details
def format_transaction_details(transaction):
    """
    Format transaction details, including age and hash.

    :param transaction: Transaction dictionary.
    :return: Formatted transaction details dictionary.
    """
    try:
        # Parse timestamp and calculate age
        timestamp = int(transaction["timeStamp"])
        transaction_time = datetime.utcfromtimestamp(timestamp)
        age = datetime.utcnow() - transaction_time

        return {
            "hash": transaction["hash"],
            "age": str(age),  # Convert age to string for better readability
        }
    except KeyError:
        raise ValueError("Invalid transaction data format.")

# Main script logic
def main():
    try:
        # Fetch latest transactions
        transactions = get_latest_transactions(WLFI_CONTRACT_ADDRESS, ETHERSCAN_API_KEY)

        # Display the latest transaction details
        if transactions:
            latest_transaction = transactions[0]  # Transactions are sorted by timestamp (desc)
            details = format_transaction_details(latest_transaction)
            print("Latest Transaction Details:")
            print(f"Hash: {details['hash']}")
            print(f"Age: {details['age']}")
        else:
            print("No transactions found for the specified contract.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point
if __name__ == "__main__":
    main()
```
