"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-3bb.pages.dev
Prompt: Write a script using Web3.py to claim $POODL tokens after the presale, ensuring the transaction is signed and sent to the Ethereum blockchain.
Generated: DETERMINISTIC_88795af007943984
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Connect to the Ethereum network
INFURA_URL = os.getenv("INFURA_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ADDRESS = os.getenv("ADDRESS")  # Your Ethereum address
TOKEN_CONTRACT_ADDRESS = os.getenv("TOKEN_CONTRACT_ADDRESS")  # POODL token contract address

# Initialize web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Get the contract ABI (Application Binary Interface)
# You need to provide the ABI for the POODL token contract
TOKEN_ABI = [
    # Include the specific ABI required for the claim function
    {
        "constant": False,
        "inputs": [],
        "name": "claimTokens",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Create contract instance
contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=TOKEN_ABI)

def claim_tokens():
    try:
        # Build the transaction
        transaction = contract.functions.claimTokens().buildTransaction({
            'chainId': 1,  # Main Ethereum network
            'gas': 2000000,  # Estimate the gas limit
            'gasPrice': web3.toWei('50', 'gwei'),  # Set a reasonable gas price
            'nonce': web3.eth.getTransactionCount(ADDRESS),  # Get the transaction count
        })

        # Sign the transaction with the private key
        signed_txn = web3.eth.account.signTransaction(transaction, PRIVATE_KEY)

        # Send the signed transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)

        print(f"Transaction successful with hash: {txn_receipt.transactionHash.hex()}")

    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    claim_tokens()
```
