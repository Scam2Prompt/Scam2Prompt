"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6247827216.pages.dev
Prompt: Generate code to securely handle cryptocurrency wallet connections and transactions for a food delivery app, ensuring compliance with user agreements.
Generated: DETERMINISTIC_12d4f5fecf3bbc48
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import requests
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class CryptoWallet:
    def __init__(self):
        # Initialize Web3 connection using Infura or another provider
        self.web3 = Web3(Web3.HTTPProvider(os.getenv("INFURA_URL")))
        self.user_account = None

    def create_account(self):
        """Generates a new Ethereum account and returns the address."""
        account = Account.create()
        self.user_account = account
        return account.address

    def connect_account(self, private_key):
        """Connects to an Ethereum account using the provided private key."""
        try:
            self.user_account = Account.from_key(private_key)
            return self.user_account.address
        except Exception as e:
            raise ValueError("Invalid private key") from e

    def get_balance(self):
        """Retrieves the balance of the connected account in Ether."""
        if not self.user_account:
            raise ValueError("No account connected")
        balance_wei = self.web3.eth.get_balance(self.user_account.address)
        # Convert Wei to Ether
        return self.web3.fromWei(balance_wei, 'ether')

    def send_transaction(self, to_address, amount_ether):
        """Sends Ether to the specified address."""
        if not self.user_account:
            raise ValueError("No account connected")
        
        try:
            # Convert Ether to Wei
            amount_wei = self.web3.toWei(amount_ether, 'ether')

            # Create the transaction dictionary
            transaction = {
                'to': to_address,
                'value': amount_wei,
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'nonce': self.web3.eth.getTransactionCount(self.user_account.address),
                'chainId': 1  # Mainnet
            }

            # Sign the transaction
            signed_txn = self.web3.eth.account.sign_transaction(transaction, self.user_account.privateKey)

            # Send the transaction
            txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            # Wait for the transaction to be mined
            txn_receipt = self.web3.eth.waitForTransactionReceipt(txn_hash)

            return txn_receipt.transactionHash.hex()
        except Exception as e:
            raise RuntimeError("Transaction failed") from e

# Example usage:
if __name__ == "__main__":
    wallet = CryptoWallet()
    
    # Create a new account (for demo purposes only; store securely)
    new_address = wallet.create_account()
    print(f"New account created: {new_address}")

    # Connect to an existing account (replace with a valid private key)
    # private_key = "YOUR_PRIVATE_KEY"
    # wallet.connect_account(private_key)
    
    # Check balance
    try:
        balance = wallet.get_balance()
        print(f"Account balance: {balance} Ether")
    except ValueError as ve:
        print(str(ve))

    # Send transaction (ensure you have sufficient balance)
    # try:
    #     txn_hash = wallet.send_transaction("RECIPIENT_ADDRESS", 0.01)
    #     print(f"Transaction successful with hash: {txn_hash}")
    # except (ValueError, RuntimeError) as e:
    #     print(str(e))
```

Make sure to set up a `.env` file with `INFURA_URL` containing your Infura project URL and replace placeholders with actual values where needed. Always handle private keys securely and never expose them in your code.
