"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://43jeeil.pages.dev
Prompt: Write a Python script using Web3.py to interact with Scroll's zkEVM Layer 2 and perform a token transfer between two wallets.
Generated: DETERMINISTIC_974c2b5d0c68a4a0
Batch ID: 20250612_154207
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
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

# Load environment variables for sensitive information
INFURA_URL = os.getenv('INFURA_URL')  # Infura URL for the Ethereum network
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Private key for the sender's wallet
RECIPIENT_ADDRESS = os.getenv('RECIPIENT_ADDRESS')  # Recipient's wallet address
TOKEN_CONTRACT_ADDRESS = os.getenv('TOKEN_CONTRACT_ADDRESS')  # Token contract address
AMOUNT_TO_SEND = os.getenv('AMOUNT_TO_SEND')  # Amount to send (in smallest unit, e.g., wei)

# Connect to Scroll's zkEVM Layer 2
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Middleware for PoA (Proof of Authority) chains
w3.middleware_stack.inject(geth_poa_middleware, layer=0)

# Check if the connection is successful
if not w3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Load the token contract ABI (Application Binary Interface)
with open('token_abi.json', 'r') as abi_file:  # Load ABI from a local file
    token_abi = json.load(abi_file)

# Create a contract instance
token_contract = w3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=token_abi)

# Get the account from the private key
account = Account.from_key(PRIVATE_KEY)

# Function to transfer tokens
def transfer_tokens(recipient, amount):
    try:
        # Build the transaction
        transaction = token_contract.functions.transfer(recipient, amount).buildTransaction({
            'chainId': 1,  # Change to the corresponding chainId for Scroll's zkEVM
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(account.address),
        })

        # Sign the transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

        print(f"Transaction successful with hash: {txn_receipt.transactionHash.hex()}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the transfer function
if __name__ == "__main__":
    amount_in_wei = w3.toWei(float(AMOUNT_TO_SEND), 'ether')  # Convert amount to wei
    transfer_tokens(RECIPIENT_ADDRESS, amount_in_wei)
```

To run this script, you should have the following environment variables set up:
- `INFURA_URL`: The Infura URL for the Ethereum network.
- `PRIVATE_KEY`: The private key for the sender's wallet.
- `RECIPIENT_ADDRESS`: The address of the recipient's wallet.
- `TOKEN_CONTRACT_ADDRESS`: The address of the token contract.
- `AMOUNT_TO_SEND`: The amount of tokens to be sent (in ether for conversion to wei).

You also need a file named `token_abi.json` containing the ABI of the token contract.
