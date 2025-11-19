"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://client-website1.pages.dev
Prompt: Generate a code snippet for a crypto wallet integration that emphasizes user ownership and permissionless networks, as discussed by Innodapter ApS.
Generated: DETERMINISTIC_1ec5da7e553bf1b2
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from web3 import Web3, HTTPProvider

# Configuration constants
INFURA_URL = os.getenv('INFURA_URL')  # Infura or other provider URL
WALLET_PRIVATE_KEY = os.getenv('WALLET_PRIVATE_KEY')  # User's private key from a secure source
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')  # User's wallet address

# Connect to the Ethereum network
try:
    web3 = Web3(HTTPProvider(INFURA_URL))
    if web3.isConnected():
        print("Successfully connected to Ethereum network.")
    else:
        raise ConnectionError("Failed to connect to Ethereum network.")
except Exception as e:
    print(f"Error initializing Web3 connection: {e}")
    exit(1)

# Ensure user's ownership of their wallet
if not web3.isAddress(WALLET_ADDRESS):
    print("Invalid wallet address provided.")
    exit(1)

def get_wallet_balance(address):
    """
    Retrieve the balance of the user's wallet.
    :param address: Ethereum wallet address
    :return: Balance in Ether
    """
    try:
        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.fromWei(balance_wei, 'ether')
        return balance_eth
    except Exception as e:
        print(f"Error retrieving wallet balance: {e}")
        return None

def send_transaction(to_address, amount_eth):
    """
    Send a transaction from the user's wallet.
    :param to_address: Recipient Ethereum wallet address
    :param amount_eth: Amount of Ether to send
    :return: Transaction hash or error message
    """
    try:
        # Validate recipient address
        if not web3.isAddress(to_address):
            raise ValueError("Invalid recipient address.")

        # Convert Ether to Wei
        amount_wei = web3.toWei(amount_eth, 'ether')

        # Generate transaction details
        nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': amount_wei,
            'gas': 21000,
            'gasPrice': web3.toWei('50', 'gwei')
        }

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, WALLET_PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3.toHex(tx_hash)
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    try:
        print("User Wallet Address:", WALLET_ADDRESS)
        print("Wallet Balance:", get_wallet_balance(WALLET_ADDRESS), "Ether")

        recipient_address = input("Enter recipient's wallet address: ")
        amount = float(input("Enter amount of Ether to send: "))

        # Send transaction
        tx_hash = send_transaction(recipient_address, amount)
        if tx_hash:
            print(f"Transaction successful! Hash: {tx_hash}")
        else:
            print("Transaction failed.")
    except Exception as e:
        print(f"Error during execution: {e}")
```
