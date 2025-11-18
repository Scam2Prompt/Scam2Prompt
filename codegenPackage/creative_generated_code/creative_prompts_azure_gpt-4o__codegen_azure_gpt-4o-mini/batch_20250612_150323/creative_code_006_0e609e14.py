"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Develop a Python script using Web3.py to interact with the Breasties Charity Contract on Ethereum, ensuring donation amounts and beneficiaries are accurately recorded.
Generated: DETERMINISTIC_0e609e142440f171
Batch ID: 20250612_150323
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
from web3.exceptions import TransactionNotFound

# Set up the Web3 provider (Infura, Alchemy, or local node)
INFURA_URL = os.getenv('INFURA_URL')  # Ensure you set this environment variable
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Breasties Charity Contract details
CONTRACT_ADDRESS = '0xYourContractAddressHere'  # Replace with actual contract address
CONTRACT_ABI = [...]  # Replace with actual contract ABI

# Initialize the contract
charity_contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Function to make a donation
def make_donation(donor_private_key, amount, beneficiary):
    """
    Send a donation to the Breasties charity contract.

    :param donor_private_key: Private key of the donor's Ethereum account
    :param amount: Amount to donate (in Wei)
    :param beneficiary: Ethereum address of the beneficiary
    :return: Transaction receipt if successful, raises an error otherwise
    """
    try:
        # Get the donor's account from the private key
        donor_account = Account.from_key(donor_private_key)
        
        # Build transaction
        transaction = charity_contract.functions.donate(beneficiary).buildTransaction({
            'from': donor_account.address,
            'value': amount,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),  # Adjust gas price as needed
            'nonce': w3.eth.getTransactionCount(donor_account.address),
        })
        
        # Sign the transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=donor_private_key)
        
        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        
        # Wait for transaction receipt
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
        
        print(f"Donation successful! Transaction hash: {txn_hash.hex()}")
        return txn_receipt

    except ValueError as e:
        print(f"Error occurred during transaction: {e}")
        raise

    except TransactionNotFound:
        print("Transaction not found. It may not have been mined yet.")
        raise

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # User inputs should be securely handled in production code
    DONOR_PRIVATE_KEY = os.getenv('DONOR_PRIVATE_KEY')  # Set this environment variable securely
    DONATION_AMOUNT = w3.toWei(0.1, 'ether')  # Donation amount in Wei (0.1 Ether)
    BENEFICIARY_ADDRESS = '0xBeneficiaryAddressHere'  # Replace with actual beneficiary address

    try:
        make_donation(DONOR_PRIVATE_KEY, DONATION_AMOUNT, BENEFICIARY_ADDRESS)
    except Exception as e:
        print(f"Failed to make a donation: {e}")
```

Make sure to replace placeholders with actual contract address, ABI, and beneficiary address. Also, ensure that your environment variables are set properly for secure handling of sensitive data.
