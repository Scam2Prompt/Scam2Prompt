"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gelato-network-cqz.pages.dev
Prompt: Write a Python script using Gelato's Web3 Functions to automate a smart contract task by bringing off-chain data on-chain.
Generated: DETERMINISTIC_1d9ba83ebc27805d
Batch ID: 20250612_145715
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/data": {
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
import json
import requests
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# ================================
# Configuration
# ================================
# RPC URL for the Ethereum network (replace with your network's RPC endpoint)
RPC_URL = os.getenv("RPC_URL", "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID")

# Smart contract address (replace with your contract address)
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "0xYourContractAddressHere")

# ABI of the smart contract (replace with your contract's ABI)
CONTRACT_ABI = json.loads(os.getenv("CONTRACT_ABI", "[]"))

# Private key to sign transactions (DO NOT SHARE THIS)
PRIVATE_KEY = os.getenv("PRIVATE_KEY", None)

# Wallet address (corresponding to the private key)
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", None)

# Off-chain API to fetch data (replace with your desired endpoint)
API_ENDPOINT = os.getenv("API_ENDPOINT", "https://api.example.com/data")

# ================================
# Initialize Web3
# ================================
web3 = Web3(HTTPProvider(RPC_URL))

# Add middleware for PoA networks (e.g., Binance Smart Chain, Polygon)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Check connection
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Convert contract address to checksum format
contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)

# Load the smart contract
contract = web3.eth.contract(address=contract_address, abi=CONTRACT_ABI)

# ================================
# Helper Functions
# ================================

def fetch_off_chain_data():
    """
    Fetch off-chain data from the API endpoint.
    Returns:
        dict: Parsed JSON data from the API response.
    """
    try:
        response = requests.get(API_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching off-chain data: {e}")

def build_transaction(function_call, gas_limit=300000):
    """
    Build a transaction for a smart contract function call.
    Args:
        function_call: The contract function call object.
        gas_limit (int): The gas limit for the transaction.
    Returns:
        dict: A transaction-ready dictionary.
    """
    nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
    return {
        'nonce': nonce,
        'gas': gas_limit,
        'gasPrice': web3.toWei('10', 'gwei'),  # Use a reasonable gas price
        'to': CONTRACT_ADDRESS,
        'data': function_call.encodeABI(),
        'chainId': web3.eth.chain_id
    }

def sign_and_send_transaction(tx):
    """
    Signs and sends a transaction to the Ethereum network.
    Args:
        tx (dict): The transaction to send.
    Returns:
        str: The transaction hash.
    """
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

# ================================
# Main Script
# ================================

def main():
    # Fetch off-chain data
    print(f"{datetime.now()} - Fetching off-chain data...")
    try:
        data = fetch_off_chain_data()
        print(f"Data fetched: {data}")
    except RuntimeError as e:
        print(e)
        return

    # Prepare the smart contract function call
    print(f"{datetime.now()} - Preparing smart contract function call...")
    try:
        # Replace `updateData` with your contract's function and pass appropriate arguments
        function_call = contract.functions.updateData(data['key'], data['value'])
        tx = build_transaction(function_call)
    except Exception as e:
        print(f"Error preparing transaction: {e}")
        return

    # Sign and send the transaction
    print(f"{datetime.now()} - Sending transaction to the blockchain...")
    try:
        tx_hash = sign_and_send_transaction(tx)
        print(f"Transaction sent! Tx Hash: {tx_hash}")
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return

    # Confirm the transaction
    print(f"{datetime.now()} - Waiting for transaction confirmation...")
    try:
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status == 1:
            print(f"Transaction confirmed! Block Number: {receipt.blockNumber}")
        else:
            print(f"Transaction failed! Receipt: {receipt}")
    except Exception as e:
        print(f"Error confirming transaction: {e}")
        return

if __name__ == "__main__":
    main()
```
