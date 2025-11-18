"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://andyonblxst.pages.dev
Prompt: Write a script to interact with the Blast Network and add Blast L2 to a wallet using the contract address `0xd43d8adac6a4c7d9aeece7c3151fca8f23752cf8`.
Generated: DETERMINISTIC_cc3aa800b20781c3
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up Web3 connection to the Blast Network (replace with the actual RPC URL)
BLAST_RPC_URL = os.getenv("BLAST_RPC_URL")
web3 = Web3(Web3.HTTPProvider(BLAST_RPC_URL))

# Check if the connection is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Blast Network.")

# Contract address for Blast L2
CONTRACT_ADDRESS = "0xd43d8adac6a4c7d9aeece7c3151fca8f23752cf8"

# Load the ABI for the contract (This should be the actual ABI of the contract)
# In a production scenario, you would retrieve the ABI from a file or an API.
ABI = json.loads('''[
    {
        "constant": false,
        "inputs": [],
        "name": "addBlastL2",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]''')

# Initialize the contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def add_blast_l2(wallet_address, private_key):
    """
    Interacts with the Blast Network to add Blast L2 to a specified wallet.
    
    :param wallet_address: The address of the wallet to which Blast L2 is to be added
    :param private_key: The private key of the wallet to sign the transaction
    """
    try:
        # Get the nonce for the account
        nonce = web3.eth.getTransactionCount(wallet_address)

        # Build the transaction
        tx = contract.functions.addBlastL2().buildTransaction({
            'chainId': 1,  # Mainnet ID; change if on testnet
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_tx = web3.eth.account.signTransaction(tx, private_key)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Wait for the transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"Transaction successful with hash: {tx_receipt.transactionHash.hex()}")

    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the actual wallet address and private key (keep them secure)
    WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")

    # Check if the wallet address and private key are set
    if not WALLET_ADDRESS or not PRIVATE_KEY:
        raise ValueError("Wallet address and private key must be set in environment variables.")

    # Call the function to add Blast L2 to the wallet
    add_blast_l2(WALLET_ADDRESS, PRIVATE_KEY)
```
