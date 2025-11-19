"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uclaimrwdist.pages.dev
Prompt: Write a Python script that interacts with a smart contract for distributing $USDC tokens during an airdrop event.
Generated: DETERMINISTIC_3badbcfc9cac64e5
Batch ID: 20250612_155557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import web3
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
USDC_ABI = json.loads(os.getenv('USDC_ABI'))

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network")

# Initialize account
account = Account.from_key(PRIVATE_KEY)

# Create contract instance
usdc_contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=USDC_ABI)

def distribute_airdrop(recipients, amounts):
    """
    Distributes $USDC tokens to a list of recipients.
    
    :param recipients: List of addresses to receive USDC
    :param amounts: List of amounts corresponding to each recipient
    :raises ValueError: If length of recipients and amounts does not match
    :raises Exception: For any other issues during transaction
    """
    
    # Check if recipients and amounts list are of the same length
    if len(recipients) != len(amounts):
        raise ValueError("Recipients and amounts lists must have the same length")
    
    # Prepare transaction
    nonce = w3.eth.getTransactionCount(account.address)
    transaction = {
        'from': account.address,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    }
    
    # Iterate through recipients and amounts
    for recipient, amount in zip(recipients, amounts):
        # Create the transaction for each recipient
        tx = usdc_contract.functions.transfer(recipient, amount).buildTransaction(transaction)
        
        # Sign the transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
        
        try:
            # Send transaction and wait for receipt
            tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(f"Transaction sent: {tx_hash.hex()}")
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            print(f"Transaction receipt: {receipt}")
        except Exception as e:
            print(f"An error occurred while sending transaction to {recipient}: {str(e)}")
            continue

if __name__ == "__main__":
    # Example usage
    recipients = [
        '0xRecipientAddress1',
        '0xRecipientAddress2',
        # Add more recipient addresses
    ]
    
    amounts = [
        1000000,  # Amount in USDC (assuming 6 decimals)
        500000,   # Amount in USDC
        # Add corresponding amounts
    ]
    
    try:
        distribute_airdrop(recipients, amounts)
    except Exception as e:
        print(f"An error occurred during the airdrop process: {str(e)}")
```

Make sure to set up the `.env` file with `INFURA_URL`, `PRIVATE_KEY`, `CONTRACT_ADDRESS`, and `USDC_ABI` for this script to work correctly.
