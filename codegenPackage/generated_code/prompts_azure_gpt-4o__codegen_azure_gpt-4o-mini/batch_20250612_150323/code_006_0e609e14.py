"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Develop a Python script using Web3.py to interact with the Breasties Charity Contract on Ethereum, ensuring donation amounts and beneficiaries are accurately recorded.
Generated: DETERMINISTIC_0e609e142440f171
Batch ID: 20250612_150323
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
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Ethereum node (Infura, Alchemy, or local node)
INFURA_URL = os.getenv('INFURA_URL')
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum node
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum node.")

# Breasties Charity Contract details
CONTRACT_ADDRESS = os.getenv('BREASTIES_CONTRACT_ADDRESS')
CONTRACT_ABI = [
    # Add the ABI of the Breasties Charity Contract here
]

# Initialize the contract
charity_contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def donate(amount, beneficiary, sender_private_key):
    """
    Function to donate to the Breasties Charity Contract.

    :param amount: Amount to donate in Wei (1 Ether = 10^18 Wei)
    :param beneficiary: Address of the beneficiary
    :param sender_private_key: Private key of the sender
    """
    try:
        # Get the account from the private key
        sender_account = web3.eth.account.from_key(sender_private_key)

        # Build the transaction
        transaction = charity_contract.functions.donate(beneficiary).buildTransaction({
            'from': sender_account.address,
            'value': amount,
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_account.address),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)

        print(f"Transaction successful with hash: {txn_hash.hex()}")
        return txn_receipt

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    try:
        # Replace with actual values
        donation_amount = web3.toWei(0.1, 'ether')  # 0.1 Ether in Wei
        beneficiary_address = os.getenv('BENEFICIARY_ADDRESS')
        sender_private_key = os.getenv('SENDER_PRIVATE_KEY')

        # Call the donate function
        receipt = donate(donation_amount, beneficiary_address, sender_private_key)

        if receipt:
            print("Donation recorded successfully.")
        else:
            print("Donation failed.")

    except Exception as e:
        print(f"An error occurred in the main execution: {str(e)}")
```

Make sure to create a `.env` file with the following variables:
```
INFURA_URL=<Your Infura or Ethereum node URL>
BREASTIES_CONTRACT_ADDRESS=<Breasties Charity Contract Address>
BENEFICIARY_ADDRESS=<Beneficiary Address>
SENDER_PRIVATE_KEY=<Your Private Key>
```
