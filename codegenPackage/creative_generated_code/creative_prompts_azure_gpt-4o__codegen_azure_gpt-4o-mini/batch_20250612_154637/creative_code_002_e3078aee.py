"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustsecurewallet.com
Prompt: Generate code for creating a secure wallet application that supports storing and transferring digital assets, inspired by Trust Secure Wallet.
Generated: DETERMINISTIC_e3078aee567128ad
Batch ID: 20250612_154637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import json
import secrets
from cryptography.fernet import Fernet

class SecureWallet:
    def __init__(self, wallet_file='wallet.json'):
        """
        Initializes the SecureWallet class.
        
        Parameters:
            wallet_file (str): Path to the wallet file.
        """
        self.wallet_file = wallet_file
        self.assets = {}
        self.load_wallet()

    def load_wallet(self):
        """Load wallet data from the JSON file."""
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, 'r') as file:
                self.assets = json.load(file)

    def save_wallet(self):
        """Save wallet data to the JSON file."""
        with open(self.wallet_file, 'w') as file:
            json.dump(self.assets, file)

    def generate_key(self):
        """Generate a secure key for encryption."""
        return Fernet.generate_key()

    def encrypt(self, data, key):
        """Encrypt data using the provided key."""
        fernet = Fernet(key)
        return fernet.encrypt(data.encode())

    def decrypt(self, encrypted_data, key):
        """Decrypt data using the provided key."""
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data).decode()

    def create_asset(self, asset_name, amount):
        """
        Create a new asset in the wallet.
        
        Parameters:
            asset_name (str): Name of the asset.
            amount (float): Amount of the asset.
        """
        if asset_name in self.assets:
            raise ValueError("Asset already exists.")
        self.assets[asset_name] = amount
        self.save_wallet()

    def transfer_asset(self, asset_name, amount, recipient_wallet):
        """
        Transfer an asset to another wallet.
        
        Parameters:
            asset_name (str): Name of the asset to transfer.
            amount (float): Amount to transfer.
            recipient_wallet (SecureWallet): The recipient's wallet instance.
        """
        if asset_name not in self.assets:
            raise ValueError("Asset does not exist in wallet.")
        if self.assets[asset_name] < amount:
            raise ValueError("Insufficient funds.")
        
        self.assets[asset_name] -= amount
        recipient_wallet.create_asset(asset_name, amount)
        self.save_wallet()
        recipient_wallet.save_wallet()

    def get_balance(self, asset_name):
        """
        Get the balance of a specific asset.
        
        Parameters:
            asset_name (str): The name of the asset.
        
        Returns:
            float: Balance of the asset.
        """
        return self.assets.get(asset_name, 0.0)

if __name__ == '__main__':
    # Example usage
    try:
        # Initialize wallets
        my_wallet = SecureWallet()
        recipient_wallet = SecureWallet()

        # Generate a key (in a real application, store this securely)
        key = my_wallet.generate_key()
        
        # Create an asset
        my_wallet.create_asset('Bitcoin', 1.0)
        
        # Transfer an asset
        my_wallet.transfer_asset('Bitcoin', 0.5, recipient_wallet)

        # Print balances
        print(f"My Wallet Balance (Bitcoin): {my_wallet.get_balance('Bitcoin')}")
        print(f"Recipient Wallet Balance (Bitcoin): {recipient_wallet.get_balance('Bitcoin')}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
