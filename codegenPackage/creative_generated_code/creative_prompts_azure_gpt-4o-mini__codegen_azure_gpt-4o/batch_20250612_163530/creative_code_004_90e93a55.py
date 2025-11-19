"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartauthcontracts.pages.dev
Prompt: What libraries or APIs can I use to build a self-custodial wallet for a decentralized application?
Generated: DETERMINISTIC_90e93a5545509314
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of a Python script using the `web3` library to create a self-custodial wallet for interacting with decentralized applications (dApps). This code includes wallet generation, address creation, and sending transactions.

```python
# Import necessary libraries
from web3 import Web3, HTTPProvider
from eth_account import Account
import os
import json

# Ensure required environment variables are set for sensitive data
# (e.g., your blockchain node URL)
INFURA_URL = os.getenv('INFURA_URL')  # Replace with your node provider (e.g., Infura)
if not INFURA_URL:
    raise EnvironmentError("INFURA_URL environment variable is not set")

# Connect to Ethereum network using Web3
try:
    web3 = Web3(HTTPProvider(INFURA_URL))
    assert web3.isConnected(), "Failed to connect to Ethereum network"
except Exception as e:
    raise ConnectionError(f"Error connecting to Ethereum network: {str(e)}")

# Function to create a new wallet (self-custodial)
def create_wallet():
    """
    Generate a new Ethereum wallet.
    Returns:
        dict: A dictionary containing the wallet's private key and address.
    """
    account = Account.create()
    wallet_info = {
        "private_key": account.key.hex(),  # Keep this safe! Never expose it publicly.
        "address": account.address,       # Public address for the wallet.
    }
    return wallet_info

# Function to send Ether from the wallet
def send_transaction(private_key, to_address, amount_in_ether):
    """
    Send Ether from a self-custodial wallet to another address.

    Args:
        private_key (str): The wallet's private key (hex string).
        to_address (str): The recipient's Ethereum address.
        amount_in_ether (float): The amount of Ether to send.

    Returns:
        str: Transaction hash if successful.

    Raises:
        ValueError: If invalid inputs are provided.
        Exception: For other errors during transaction processing.
    """
    # Validate inputs
    if not Web3.isAddress(to_address):
        raise ValueError(f"Invalid recipient address: {to_address}")
    if amount_in_ether <= 0:
        raise ValueError("Amount to send must be greater than zero")

    # Get the wallet address from the private key
    account = Account.from_key(private_key)
    sender_address = account.address

    # Get the nonce for the sender's address
    try:
        nonce = web3.eth.get_transaction_count(sender_address)
    except Exception as e:
        raise Exception(f"Error fetching nonce: {str(e)}")

    # Build the transaction
    transaction = {
        'to': to_address,
        'value': web3.to_wei(amount_in_ether, 'ether'),  # Convert Ether to Wei
        'gas': 21000,  # Standard gas limit for ETH transfers
        'gasPrice': web3.eth.gas_price,  # Current gas price
        'nonce': nonce,
    }

    # Sign the transaction
    signed_txn = Account.sign_transaction(transaction, private_key)

    # Send the transaction
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return web3.to_hex(tx_hash)  # Return transaction hash
    except Exception as e:
        raise Exception(f"Error sending transaction: {str(e)}")

if __name__ == "__main__":
    # Example usage of the wallet creation and transaction functions

    print("Creating a new wallet...")
    wallet = create_wallet()
    print(f"Wallet created! Address: {wallet['address']}")
    print(f"Private Key: {wallet['private_key']} (Keep this private!)")

    # Example transaction: Send 0.01 ETH to another address
    try:
        recipient_address = "0xRecipientAddressHere"  # Replace with a valid Ethereum address
        amount_to_send = 0.01  # Ether amount to send
        print(f"Sending {amount_to_send} ETH to {recipient_address}...")
        tx_hash = send_transaction(wallet['private_key'], recipient_address, amount_to_send)
        print(f"Transaction successful! TX hash: {tx_hash}")
    except Exception as e:
        print(f"Error: {str(e)}")
```

### Notes:
- You must replace `INFURA_URL` and `recipient_address` with appropriate values.
- Use environment variables or a secure mechanism to manage sensitive data like private keys.
- The `web3` library can be installed using `pip install web3 eth-account`.
- Be aware of gas fees when sending transactions.
