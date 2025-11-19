"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Create a script to automate the process of sending and receiving Ziber tokens using the Ethereum blockchain platform.
Generated: DETERMINISTIC_fbed3d20daa6c15c
Batch ID: 20250622_205138
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
from web3.middleware import geth_poa_middleware
from eth_account import Account
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configuration
INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
RECIPIENT_ADDRESS = os.getenv('RECIPIENT_ADDRESS')

# Validate configuration
if not all([INFURA_URL, PRIVATE_KEY, CONTRACT_ADDRESS, RECIPIENT_ADDRESS]):
    raise ValueError("Missing required environment variables")

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Check connection
if not w3.is_connected():
    raise ConnectionError("Failed to connect to Ethereum network")

# Load contract ABI
with open('abi.json', 'r') as f:
    contract_abi = json.load(f)

# Initialize contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def get_account_balance(address):
    """Get the balance of Ziber tokens for a given address."""
    try:
        balance = contract.functions.balanceOf(address).call()
        return balance
    except Exception as e:
        raise Exception(f"Error getting balance: {str(e)}")

def send_ziber_tokens(recipient, amount):
    """Send Ziber tokens to a recipient address."""
    try:
        # Get sender account
        account = Account.from_key(PRIVATE_KEY)
        sender_address = account.address
        
        # Get nonce
        nonce = w3.eth.get_transaction_count(sender_address)
        
        # Build transaction
        tx = contract.functions.transfer(
            recipient,
            amount
        ).build_transaction({
            'chainId': w3.eth.chain_id,
            'gas': 200000,
            'gasPrice': w3.eth.gas_price,
            'nonce': nonce,
        })
        
        # Sign transaction
        signed_tx = account.sign_transaction(tx)
        
        # Send transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return receipt
    except Exception as e:
        raise Exception(f"Error sending tokens: {str(e)}")

if __name__ == "__main__":
    try:
        # Example usage
        sender_address = Account.from_key(PRIVATE_KEY).address
        
        # Get balances before transfer
        sender_balance = get_account_balance(sender_address)
        recipient_balance = get_account_balance(RECIPIENT_ADDRESS)
        
        print(f"Sender balance before: {sender_balance}")
        print(f"Recipient balance before: {recipient_balance}")
        
        # Send tokens
        amount = 100  # Amount of tokens to send
        receipt = send_ziber_tokens(RECIPIENT_ADDRESS, amount)
        
        print(f"Transaction successful with hash: {receipt.transactionHash.hex()}")
        
        # Get balances after transfer
        sender_balance = get_account_balance(sender_address)
        recipient_balance = get_account_balance(RECIPIENT_ADDRESS)
        
        print(f"Sender balance after: {sender_balance}")
        print(f"Recipient balance after: {recipient_balance}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
