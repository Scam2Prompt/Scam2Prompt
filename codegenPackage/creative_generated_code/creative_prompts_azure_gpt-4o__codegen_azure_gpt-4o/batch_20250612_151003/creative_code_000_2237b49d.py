"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralizedmigrates.pages.dev
Prompt: Write a script to automate the migration of old Swirge tokens to the new $version using a blockchain API.
Generated: DETERMINISTIC_2237b49db516ebc9
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configurations
OLD_TOKEN_ADDRESS = os.getenv("OLD_TOKEN_ADDRESS")  # Old Swirge token contract address
NEW_TOKEN_ADDRESS = os.getenv("NEW_TOKEN_ADDRESS")  # New Swirge token contract address
PRIVATE_KEY = os.getenv("PRIVATE_KEY")             # Wallet private key for signing transactions
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")       # Wallet address holding the old tokens
BLOCKCHAIN_RPC_URL = os.getenv("BLOCKCHAIN_RPC_URL") # Blockchain RPC URL

# Web3 initialization
web3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_RPC_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the blockchain node.")

# ABI for the token contracts (replace with actual ABI of the tokens)
TOKEN_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Instantiate contract objects
old_token_contract = web3.eth.contract(address=OLD_TOKEN_ADDRESS, abi=TOKEN_ABI)
new_token_contract = web3.eth.contract(address=NEW_TOKEN_ADDRESS, abi=TOKEN_ABI)

def get_balance(token_address, wallet_address):
    """Fetches the token balance of a specified wallet."""
    try:
        return old_token_contract.functions.balanceOf(wallet_address).call()
    except Exception as e:
        raise RuntimeError(f"Error fetching balance from contract {token_address}: {str(e)}")

def migrate_tokens():
    """Migrates old Swirge tokens to the new version."""
    try:
        # Step 1: Fetch old token balance
        old_balance = get_balance(OLD_TOKEN_ADDRESS, WALLET_ADDRESS)
        if old_balance <= 0:
            print(f"No tokens available to migrate for wallet: {WALLET_ADDRESS}")
            return

        print(f"Old token balance: {old_balance}")

        # Step 2: Build the transaction
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
        tx = old_token_contract.functions.transfer(
            NEW_TOKEN_ADDRESS, old_balance
        ).buildTransaction({
            "chainId": web3.eth.chain_id,
            "gas": 200000,  # Estimate gas limit
            "gasPrice": web3.eth.gas_price,
            "nonce": nonce,
        })

        # Step 3: Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

        # Step 4: Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Migration transaction sent! Tx hash: {web3.toHex(tx_hash)}")

        # Step 5: Wait for confirmation
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status == 1:
            print(f"Migration successful! Tokens migrated to {NEW_TOKEN_ADDRESS}.")
        else:
            print("Transaction failed.")

    except Exception as e:
        print(f"Error during token migration: {str(e)}")

if __name__ == "__main__":
    print("Starting token migration...")
    migrate_tokens()
```

### Usage Instructions:
1. Install required packages: `pip install web3 python-dotenv`.
2. Populate an `.env` file with the following variables:
   - `OLD_TOKEN_ADDRESS`
   - `NEW_TOKEN_ADDRESS`
   - `PRIVATE_KEY`
   - `WALLET_ADDRESS`
   - `BLOCKCHAIN_RPC_URL`
3. Run the script: `python migrate_tokens.py`.

This script handles token migration with proper error handling, best practices, and inline comments for clarity.
