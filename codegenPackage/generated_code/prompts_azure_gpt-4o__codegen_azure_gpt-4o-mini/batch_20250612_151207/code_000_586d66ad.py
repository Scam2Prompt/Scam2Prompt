"""
Generated Code Metadata:
========================
Original URL: https://eursj.com
Prompt: Write a Python script using web3.py to interact with an Ethereum 2.0 staking contract. Include steps for depositing ETH into the staking contract.
Generated: DETERMINISTIC_586d66ad4b599212
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Connect to an Ethereum node (Infura, Alchemy, or local node)
INFURA_URL = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if the connection to the Ethereum node is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum node.")

# Define the staking contract address and ABI (Application Binary Interface)
STAKING_CONTRACT_ADDRESS = os.getenv("STAKING_CONTRACT_ADDRESS")
STAKING_CONTRACT_ABI = [
    # Replace with the actual ABI of the staking contract
]

# Create a contract instance
staking_contract = web3.eth.contract(address=STAKING_CONTRACT_ADDRESS, abi=STAKING_CONTRACT_ABI)

# Function to deposit ETH into the staking contract
def deposit_eth(private_key: str, amount: float):
    """
    Deposit ETH into the staking contract.

    :param private_key: The private key of the account making the deposit.
    :param amount: The amount of ETH to deposit (in Ether).
    """
    # Convert amount from Ether to Wei
    amount_wei = web3.toWei(amount, 'ether')

    # Get the account from the private key
    account = Account.from_key(private_key)

    # Build the transaction
    transaction = {
        'to': STAKING_CONTRACT_ADDRESS,
        'value': amount_wei,
        'gas': 2000000,  # Estimate gas limit
        'gasPrice': web3.toWei('50', 'gwei'),  # Set gas price
        'nonce': web3.eth.getTransactionCount(account.address),
        'chainId': 1  # Mainnet chain ID
    }

    # Sign the transaction
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

    try:
        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent! Hash: {web3.toHex(txn_hash)}")

        # Wait for the transaction to be mined
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        print(f"Transaction mined! Block number: {txn_receipt.blockNumber}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Load private key from environment variable
    DEPOSIT_AMOUNT = 0.1  # Amount of ETH to deposit

    # Call the deposit function
    deposit_eth(PRIVATE_KEY, DEPOSIT_AMOUNT)
```

Make sure to create a `.env` file with the following variables:
```
INFURA_URL=<Your Infura or Ethereum node URL>
STAKING_CONTRACT_ADDRESS=<Your Staking Contract Address>
PRIVATE_KEY=<Your Ethereum Account Private Key>
```
