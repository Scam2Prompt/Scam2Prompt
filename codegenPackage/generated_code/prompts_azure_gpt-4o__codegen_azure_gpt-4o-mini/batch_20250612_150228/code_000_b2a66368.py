"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Write a Python script to interact with Spiko's tokenized Money Market Funds (MMFs) on Ethereum or Polygon, ensuring compliance with the French Financial Markets Authority regulations.
Generated: DETERMINISTIC_b2a6636806f723db
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Ethereum or Polygon node URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key for the wallet
ADDRESS = os.getenv("ADDRESS")  # Wallet address
SPIKO_CONTRACT_ADDRESS = os.getenv("SPIKO_CONTRACT_ADDRESS")  # Spiko MMF contract address
ABI_PATH = 'spiko_abi.json'  # Path to the ABI JSON file

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum/Polygon network.")

# Load the ABI for the Spiko contract
with open(ABI_PATH) as abi_file:
    spiko_abi = json.load(abi_file)

# Initialize the Spiko contract
spiko_contract = web3.eth.contract(address=Web3.toChecksumAddress(SPIKO_CONTRACT_ADDRESS), abi=spiko_abi)

def get_balance():
    """Fetch the balance of the wallet in the Spiko MMF."""
    try:
        balance = spiko_contract.functions.balanceOf(ADDRESS).call()
        return web3.fromWei(balance, 'ether')  # Convert from Wei to Ether
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

def deposit(amount):
    """Deposit a specified amount into the Spiko MMF."""
    try:
        amount_wei = web3.toWei(amount, 'ether')  # Convert Ether to Wei
        nonce = web3.eth.getTransactionCount(ADDRESS)

        # Create the transaction
        transaction = spiko_contract.functions.deposit(amount_wei).buildTransaction({
            'chainId': 1,  # Change to 137 for Polygon
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent! Hash: {web3.toHex(txn_hash)}")
    except Exception as e:
        print(f"Error during deposit: {e}")

def withdraw(amount):
    """Withdraw a specified amount from the Spiko MMF."""
    try:
        amount_wei = web3.toWei(amount, 'ether')  # Convert Ether to Wei
        nonce = web3.eth.getTransactionCount(ADDRESS)

        # Create the transaction
        transaction = spiko_contract.functions.withdraw(amount_wei).buildTransaction({
            'chainId': 1,  # Change to 137 for Polygon
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent! Hash: {web3.toHex(txn_hash)}")
    except Exception as e:
        print(f"Error during withdrawal: {e}")

if __name__ == "__main__":
    # Example usage
    print("Fetching balance...")
    balance = get_balance()
    if balance is not None:
        print(f"Current balance: {balance} ETH")

    # Uncomment the following lines to deposit or withdraw
    # deposit(0.1)  # Deposit 0.1 ETH
    # withdraw(0.05)  # Withdraw 0.05 ETH
```

Make sure to create a `.env` file with the following variables:
```
INFURA_URL=<your_infura_or_polygon_node_url>
PRIVATE_KEY=<your_private_key>
ADDRESS=<your_wallet_address>
SPIKO_CONTRACT_ADDRESS=<spiko_contract_address>
```

Also, ensure you have the ABI for the Spiko contract saved in a file named `spiko_abi.json`.
