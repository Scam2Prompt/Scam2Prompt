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
from web3 import Web3
import json
import os

# Load environment variables (e.g., Infura URL, contract address, sender private key)
from dotenv import load_dotenv
load_dotenv()

# Constants
INFURA_URL = os.getenv('INFURA_URL')  # Infura/Alchemy URL for Ethereum node
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')  # Address of the Breasties Charity Contract
SENDER_PRIVATE_KEY = os.getenv('SENDER_PRIVATE_KEY')  # Private key of the sender
SENDER_ADDRESS = os.getenv('SENDER_ADDRESS')  # Account address of the sender

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection to the Ethereum network
if not web3.is_connected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Load contract's ABI (Application Binary Interface)
with open("BreastiesCharityContract_abi.json", "r") as abi_file:
    contract_abi = json.load(abi_file)

# Initialize contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def donate_to_charity(beneficiary_address: str, amount_in_ether: float):
    """
    Function to donate to the Breasties Charity Contract.

    Args:
        beneficiary_address (str): The Ethereum address of the beneficiary.
        amount_in_ether (float): The donation amount in Ether.

    Returns:
        str: Transaction hash of the donation transaction.
    """
    if not web3.isAddress(beneficiary_address):
        raise ValueError("Invalid Ethereum address for the beneficiary.")

    # Convert Ether to Wei
    amount_in_wei = web3.to_wei(amount_in_ether, 'ether')

    # Build the transaction payload
    transaction = contract.functions.donate(beneficiary_address).build_transaction({
        'from': SENDER_ADDRESS,
        'value': amount_in_wei,
        'gas': 200000,  # Estimate sufficient gas
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.get_transaction_count(SENDER_ADDRESS),
    })

    # Sign the transaction
    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=SENDER_PRIVATE_KEY)

    # Send the signed transaction
    tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

    # Wait for transaction receipt
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    # Confirm the transaction was mined successfully
    if receipt['status'] == 1:
        return f"Donation successful. Transaction hash: {tx_hash.hex()}"
    else:
        raise RuntimeError("Donation transaction failed.")

if __name__ == "__main__":
    try:
        # Example inputs (replace with actual inputs)
        beneficiary = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with real address
        amount = 0.1  # Amount in Ether

        # Make the donation
        result = donate_to_charity(beneficiary, amount)
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")
```
