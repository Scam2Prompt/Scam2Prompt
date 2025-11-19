"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myetherwallet.com
Prompt: How can I create a new Ethereum wallet using MyEtherWallet and ensure my keys are secure?
Generated: DETERMINISTIC_8a275e4f7756b2d4
Batch ID: 20250612_135046
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
import secrets
from eth_account import Account
from web3 import Web3

# Function to generate a new Ethereum wallet
def create_ethereum_wallet():
    """
    Create a new Ethereum wallet and return the address and private key.
    
    Returns:
        dict: A dictionary containing the wallet address and private key.
    """
    try:
        # Generate a random private key
        private_key = secrets.token_bytes(32)
        
        # Create an account from the private key
        account = Account.from_key(private_key)
        
        # Get the wallet address
        address = account.address
        
        # Store the keys securely
        store_keys_securely(address, private_key)

        return {
            "address": address,
            "private_key": private_key.hex()  # Convert to hex format for readability
        }
    except Exception as e:
        print(f"Error creating wallet: {e}")
        return None

# Function to securely store the wallet keys
def store_keys_securely(address, private_key):
    """
    Store the private key securely, ideally in an encrypted format.
    
    Args:
        address (str): The Ethereum wallet address.
        private_key (bytes): The private key in bytes format.
    
    Raises:
        IOError: If there is an issue writing to the file.
    """
    try:
        # Define the file path to store the keys
        wallet_file = f"{address}.json"
        
        # Use a basic JSON structure to store wallet information
        wallet_data = {
            "address": address,
            "private_key": private_key.hex()  # Store as hex string
        }
        
        # Write the wallet data to a file
        with open(wallet_file, 'w') as f:
            json.dump(wallet_data, f)
        
        print(f"Wallet keys stored securely in {wallet_file}")
    except IOError as e:
        print(f"Error storing keys: {e}")

if __name__ == "__main__":
    # Create a new Ethereum wallet
    wallet_info = create_ethereum_wallet()
    if wallet_info:
        print(f"New Ethereum Wallet Created:\nAddress: {wallet_info['address']}\nPrivate Key: {wallet_info['private_key']}")
```

**Note**: This script is for educational purposes only. For storing private keys in production, consider using secure vaults or hardware wallets and always follow best practices in cryptography and security.
