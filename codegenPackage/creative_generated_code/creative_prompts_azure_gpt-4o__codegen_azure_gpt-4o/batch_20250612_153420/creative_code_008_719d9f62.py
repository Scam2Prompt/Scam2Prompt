"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safergf.pages.dev
Prompt: Write a guide for developers participating in the "March for AA Hackathon" to use Safe CORE tools for building innovative Web3 applications.
Generated: DETERMINISTIC_719d9f62f80bfe25
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Guide for Developers: Using Safe CORE Tools to Build Web3 Applications
This script demonstrates the use of Safe CORE SDK for interacting with Safe smart contracts and building innovative Web3 applications. 
It covers essential operations such as creating a Safe, fetching Safe balances, and executing transactions.

Dependencies:
- ethers
- @safe-global/safe-core-sdk
- dotenv

To run this script:
1. Install dependencies: `npm install ethers @safe-global/safe-core-sdk dotenv`
2. Configure a `.env` file with your private key and RPC endpoint.

Author: March for AA Hackathon Team
"""

# Required imports
from dotenv import load_dotenv
import os
from web3 import Web3
from eth_account import Account
from safe_core_sdk import Safe
from safe_core_sdk.tx import SafeTransaction
from safe_core_sdk.contracts.safe import SafeService
from safe_core_sdk.providers import JsonRpcProvider

# Load environment variables from .env file
load_dotenv()

# Load private key and RPC endpoint from environment variables
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_ENDPOINT = os.getenv("RPC_ENDPOINT")

if not PRIVATE_KEY or not RPC_ENDPOINT:
    raise ValueError("Please set PRIVATE_KEY and RPC_ENDPOINT in the .env file.")

# Initialize Web3 provider
web3_provider = Web3(Web3.HTTPProvider(RPC_ENDPOINT))

# Verify RPC connection
if not web3_provider.isConnected():
    raise ConnectionError("Unable to connect to the RPC endpoint.")

# Initialize wallet using the private key
account = Account.from_key(PRIVATE_KEY)
owner_address = account.address

print(f"Wallet initialized. Address: {owner_address}")

# Initialize Safe Service
safe_service = SafeService(RPC_ENDPOINT)

# Function to create a new Safe
def create_safe(owner_address, threshold=1):
    """
    Creates a new Safe with the given owner address and threshold.
    :param owner_address: Address of the Safe owner
    :param threshold: Number of signatures required to approve transactions
    :return: Address of the newly created Safe
    """
    try:
        safe_address = safe_service.create_safe(owner_addresses=[owner_address], threshold=threshold)
        print(f"Safe created successfully. Address: {safe_address}")
        return safe_address
    except Exception as e:
        print(f"Error while creating Safe: {e}")
        return None

# Function to fetch Safe balances
def fetch_safe_balances(safe_address):
    """
    Fetches the balances of the given Safe address.
    :param safe_address: Address of the Safe
    :return: Dictionary of token balances
    """
    try:
        balances = safe_service.get_balances(safe_address)
        print(f"Balances for Safe {safe_address}: {balances}")
        return balances
    except Exception as e:
        print(f"Error while fetching balances: {e}")
        return None

# Function to execute a transaction from a Safe
def execute_safe_transaction(safe_address, to, value, data):
    """
    Executes a transaction from the given Safe address.
    :param safe_address: Address of the Safe
    :param to: Recipient address
    :param value: Amount to transfer
    :param data: Transaction data (optional)
    :return: Transaction hash
    """
    try:
        safe = Safe(safe_address, web3_provider, PRIVATE_KEY)
        tx = SafeTransaction(to=to, value=value, data=data)
        tx_hash = safe.execute_transaction(tx)
        print(f"Transaction executed successfully. Hash: {tx_hash}")
        return tx_hash
    except Exception as e:
        print(f"Error while executing transaction: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Step 1: Create a Safe
    safe_address = create_safe(owner_address)

    if safe_address:
        # Step 2: Fetch Safe Balances
        fetch_safe_balances(safe_address)

        # Step 3: Execute a Transaction
        recipient = "0xRecipientAddressHere"  # Replace with actual recipient address
        value = Web3.toWei(0.01, "ether")  # Replace with desired value
        data = ""  # Optional transaction data
        execute_safe_transaction(safe_address, recipient, value, data)

"""
End of Guide Script.
"""
```
