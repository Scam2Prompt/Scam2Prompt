"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signetfaucet1.pages.dev
Prompt: Create a Python script using web3.py to automate claiming cryptocurrency from the Signet Faucet by specifying an amount within the allowed range.
Generated: DETERMINISTIC_d69d21bb03540019
Batch ID: 20250612_152441
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

# Load environment variables for safety (e.g., private key and RPC URL)
from dotenv import load_dotenv
load_dotenv()

# Environment variables for sensitive data
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet's private key
RPC_URL = os.getenv("RPC_URL")          # Your Ethereum RPC URL
FAUCET_CONTRACT_ADDRESS = os.getenv("FAUCET_CONTRACT_ADDRESS")  # Faucet contract address
FAUCET_ABI = '[...]'  # Replace with the ABI of the Signet Faucet contract

# Initialize web3 instance
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network. Please check your RPC_URL.")

# Get sender's wallet address from the private key
account = web3.eth.account.from_key(PRIVATE_KEY)
sender_address = account.address

# Load the faucet contract instance
faucet_contract = web3.eth.contract(address=FAUCET_CONTRACT_ADDRESS, abi=FAUCET_ABI)

def claim_tokens(amount):
    """
    Function to automate claiming tokens from the Signet Faucet.
    
    :param amount: Amount of tokens to claim (must be within the allowed range).
    :return: Transaction hash on success.
    """
    try:
        # Check if the amount is within the allowed range
        min_amount = faucet_contract.functions.MIN_CLAIM_AMOUNT().call()
        max_amount = faucet_contract.functions.MAX_CLAIM_AMOUNT().call()
        
        if not (min_amount <= amount <= max_amount):
            raise ValueError(f"Amount must be between {min_amount} and {max_amount}.")

        # Build the transaction
        txn = faucet_contract.functions.claimTokens(amount).build_transaction({
            'chainId': web3.eth.chain_id,
            'gas': 200000,  # Estimate gas amount
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender_address),
        })

        # Sign the transaction with the private key
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Return the transaction hash
        return web3.toHex(tx_hash)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ContractLogicError as cle:
        print(f"ContractLogicError: {cle}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Specify the amount to claim (example: 100)
        amount_to_claim = 100
        
        # Call the claim function
        tx_hash = claim_tokens(amount_to_claim)
        
        if tx_hash:
            print(f"Tokens successfully claimed. Transaction hash: {tx_hash}")
        else:
            print("Failed to claim tokens.")

    except Exception as e:
        print(f"An unexpected error occurred in the script: {e}")
```
