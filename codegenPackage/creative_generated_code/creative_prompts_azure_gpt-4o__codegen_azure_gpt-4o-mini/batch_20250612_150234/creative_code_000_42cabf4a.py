"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethpai.com
Prompt: Write a script in Python using the Web3.py library to interact with an Ethereum smart contract for pledging ETH. Include functionality for checking the pledge status and retrieving transaction details.
Generated: DETERMINISTIC_42cabf4a62bd5311
Batch ID: 20250612_150234
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
from web3.exceptions import ContractLogicError

# Configuration for connecting to Ethereum node
INFURA_URL = os.getenv('INFURA_URL')  # Set your Infura URL in environment variables
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Set your private key in environment variables
ADDRESS = os.getenv('ADDRESS')  # Set your wallet address in environment variables

# Initialize Web3 connection
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure connection is established
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node.")

# Contract ABI and address (replace with actual contract ABI and address)
CONTRACT_ADDRESS = '0xYourContractAddress'  # Replace with your contract's address
CONTRACT_ABI = [
    # Replace with your contract's ABI
]

# Initialize contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def pledge_eth(amount_in_wei):
    """
    Pledge ETH to the smart contract.

    Parameters:
    - amount_in_wei: The amount of ETH to pledge, in wei.

    Returns:
    - transaction_hash: The hash of the transaction.
    """
    try:
        # Prepare transaction
        tx = contract.functions.pledge().buildTransaction({
            'from': ADDRESS,
            'value': amount_in_wei,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(ADDRESS),
        })

        # Sign transaction
        signed_tx = w3.eth.account.signTransaction(tx, private_key=PRIVATE_KEY)

        # Send transaction
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return tx_hash.hex()
    except ContractLogicError as e:
        print(f"Contract logic error: {e}")
    except Exception as e:
        print(f"An error occurred while pledging ETH: {e}")

def check_pledge_status(user_address):
    """
    Check the pledge status of a user.

    Parameters:
    - user_address: The address of the user to check.

    Returns:
    - status: The pledge status of the user.
    """
    try:
        status = contract.functions.getPledgeStatus(user_address).call()
        return status
    except Exception as e:
        print(f"An error occurred while checking pledge status: {e}")

def get_transaction_details(tx_hash):
    """
    Retrieve transaction details using the transaction hash.

    Parameters:
    - tx_hash: The hash of the transaction to retrieve.

    Returns:
    - transaction: The details of the transaction.
    """
    try:
        transaction = w3.eth.getTransaction(tx_hash)
        return transaction
    except Exception as e:
        print(f"An error occurred while retrieving transaction details: {e}")

# Example usage:
if __name__ == "__main__":
    # Pledge 0.1 ETH (100000000000000000 wei)
    pledge_amount = 100000000000000000  # 0.1 ETH in wei
    tx_hash = pledge_eth(pledge_amount)
    if tx_hash:
        print(f"Pledge transaction sent with hash: {tx_hash}")

    # Check pledge status for the current address
    status = check_pledge_status(ADDRESS)
    print(f"Pledge status for {ADDRESS}: {status}")

    # Retrieve transaction details
    if tx_hash:
        transaction_details = get_transaction_details(tx_hash)
        print(f"Transaction details: {transaction_details}")
```

Make sure to replace placeholder values for `CONTRACT_ADDRESS` and `CONTRACT_ABI` with your actual contract's address and ABI respectively. Also, set your Infura URL, private key, and address in your environment variables before running the script.
