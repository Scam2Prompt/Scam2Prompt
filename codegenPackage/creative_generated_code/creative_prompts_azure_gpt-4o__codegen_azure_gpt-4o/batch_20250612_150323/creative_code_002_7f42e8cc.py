"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.com
Prompt: Using the Etherscan API, create a script to track and decode input data for Ethereum transactions in real-time.
Generated: DETERMINISTIC_7f42e8cc81b66e82
Batch ID: 20250612_150323
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
  "https://mainnet.infura.io/v3/your_infura_project_id_here": {
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
import json
from web3 import Web3

# Configuration
ETHERSCAN_API_KEY = "your_etherscan_api_key_here"  # Replace with your Etherscan API key
WEB3_PROVIDER_URL = "https://mainnet.infura.io/v3/your_infura_project_id_here"  # Replace with your Infura/Mainnet provider URL
ADDRESS_TO_TRACK = "0xYourWalletAddressHere"  # Replace with the Ethereum address you want to track
POLL_INTERVAL = 15  # Polling interval in seconds

# Initialize Web3 provider
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

# Base URL for Etherscan API
ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"

# Function to fetch transaction list for the address
def fetch_transactions(address):
    """
    Fetches the list of transactions for the given address using the Etherscan API.
    :param address: Ethereum address to track.
    :return: List of transactions.
    """
    try:
        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": 0,
            "endblock": 99999999,
            "sort": "desc",
            "apikey": ETHERSCAN_API_KEY,
        }
        response = requests.get(ETHERSCAN_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Check for errors in API response
        if data["status"] != "1":
            print(f"Error fetching transactions: {data['message']}")
            return []
        return data["result"]
    except requests.RequestException as e:
        print(f"Error connecting to Etherscan API: {e}")
        return []
    except KeyError:
        print("Unexpected response format from Etherscan API.")
        return []

# Function to decode input data
def decode_input_data(input_data):
    """
    Decodes the input data of a transaction.
    :param input_data: Hexadecimal input data from the transaction.
    :return: Decoded data (if applicable).
    """
    try:
        # Check if input data exists
        if input_data and len(input_data) > 2:
            # Decode the input data
            return web3.toText(web3.toBytes(hexstr=input_data))
        else:
            return "No input data"
    except Exception as e:
        return f"Error decoding input data: {e}"

# Main function to track transactions in real-time
def track_transactions():
    """
    Tracks Ethereum transactions for the given address in real-time.
    """
    print(f"Starting to track transactions for address: {ADDRESS_TO_TRACK}")
    seen_tx_hashes = set()

    while True:
        try:
            transactions = fetch_transactions(ADDRESS_TO_TRACK)
            
            # Process transactions
            for tx in transactions:
                tx_hash = tx["hash"]
                if tx_hash not in seen_tx_hashes:
                    seen_tx_hashes.add(tx_hash)
                    print(f"New Transaction Detected: {tx_hash}")
                    print(f"From: {tx['from']}, To: {tx['to']}, Value: {web3.fromWei(int(tx['value']), 'ether')} Ether")
                    print(f"Decoded Input Data: {decode_input_data(tx['input'])}")
                    print("-" * 80)

            # Sleep before polling again
            time.sleep(POLL_INTERVAL)
        except KeyboardInterrupt:
            print("Tracking stopped by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(POLL_INTERVAL)  # Pause before retrying

# Entry point
if __name__ == "__main__":
    track_transactions()
```

Ensure that you replace the placeholders with your actual Etherscan API key, Infura (or another provider) URL, and the Ethereum address you want to track. This script continuously polls for new transactions and decodes any input data associated with them.
