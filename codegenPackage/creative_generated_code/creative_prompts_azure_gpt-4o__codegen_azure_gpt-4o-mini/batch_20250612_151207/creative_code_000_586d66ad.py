"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eursj.com
Prompt: Write a Python script using web3.py to interact with an Ethereum 2.0 staking contract. Include steps for depositing ETH into the staking contract.
Generated: DETERMINISTIC_586d66ad4b599212
Batch ID: 20250612_151207
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
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv('INFURA_URL')  # Your Infura URL
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Your Ethereum account private key
STAKING_CONTRACT_ADDRESS = os.getenv('STAKING_CONTRACT_ADDRESS')  # Address of the staking contract
GAS_LIMIT = 200000  # Set a reasonable gas limit
GAS_PRICE = Web3.toWei('20', 'gwei')  # Example gas price

# Initialize a Web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure Web3 is connected
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network")

# Load the staking contract ABI (Application Binary Interface)
with open('staking_contract_abi.json') as f:
    staking_contract_abi = json.load(f)

# Create a contract instance
staking_contract = web3.eth.contract(address=STAKING_CONTRACT_ADDRESS, abi=staking_contract_abi)

def deposit_eth(amount_ether):
    """
    Deposit ETH into the staking contract.

    :param amount_ether: Amount of Ether to deposit in string format
    """
    # Convert Ether to Wei
    amount_wei = web3.toWei(amount_ether, 'ether')

    # Get the account from the private key
    account = Account.from_key(PRIVATE_KEY)
    nonce = web3.eth.getTransactionCount(account.address)

    # Build the transaction
    transaction = {
        'to': STAKING_CONTRACT_ADDRESS,
        'value': amount_wei,
        'gas': GAS_LIMIT,
        'gasPrice': GAS_PRICE,
        'nonce': nonce,
    }

    # Sign the transaction
    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

    try:
        # Send the transaction
        transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        # Wait for the transaction receipt
        receipt = web3.eth.waitForTransactionReceipt(transaction_hash)

        print(f"Transaction successful with hash: {transaction_hash.hex()}")
        print(f"Transaction receipt: {receipt}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage: deposit 0.1 ETH into the staking contract
    deposit_eth("0.1")
```

**Important Note:** Ensure you have the following in your .env file:
```
INFURA_URL=<Your Infura URL>
PRIVATE_KEY=<Your Ethereum account private key>
STAKING_CONTRACT_ADDRESS=<Address of the staking contract>
```

Also, make sure to provide the proper ABI for the staking contract in a file named `staking_contract_abi.json` in the same directory as this script.
