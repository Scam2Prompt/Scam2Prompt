"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: What are the best practices for managing multiple blockchain assets securely using TPWallet?
Generated: DETERMINISTIC_ba7ff3c016d7114b
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code following your request:

```python
import os
import json
from cryptography.fernet import Fernet

class TPWalletManager:
    """
    A class to securely manage multiple blockchain assets using TPWallet.
    """

    def __init__(self, encryption_key_file="encryption_key.key", wallet_data_file="wallet_data.json"):
        """
        Initialize the TPWalletManager with encryption key and wallet data file.
        """
        self.encryption_key_file = encryption_key_file
        self.wallet_data_file = wallet_data_file
        self.key = None
        self._load_or_generate_encryption_key()
        self.crypto = Fernet(self.key)

    def _load_or_generate_encryption_key(self):
        """
        Load the encryption key from a file or generate a new one if it doesn't exist.
        """
        if os.path.exists(self.encryption_key_file):
            with open(self.encryption_key_file, 'rb') as key_file:
                self.key = key_file.read()
        else:
            self.key = Fernet.generate_key()
            with open(self.encryption_key_file, 'wb') as key_file:
                key_file.write(self.key)

    def save_wallet_data(self, wallet_data):
        """
        Encrypt and save wallet data to a file.
        :param wallet_data: A dictionary containing wallet address and private keys.
        """
        try:
            # Convert the dictionary to JSON and encrypt it
            wallet_data_json = json.dumps(wallet_data)
            encrypted_data = self.crypto.encrypt(wallet_data_json.encode())

            # Write the encrypted data to the wallet data file
            with open(self.wallet_data_file, 'wb') as wallet_file:
                wallet_file.write(encrypted_data)

        except Exception as e:
            print(f"Error saving wallet data: {e}")

    def load_wallet_data(self):
        """
        Decrypt and load wallet data from a file.
        :return: A dictionary containing the wallet data.
        """
        try:
            if not os.path.exists(self.wallet_data_file):
                return {}

            # Read the encrypted data from the wallet data file
            with open(self.wallet_data_file, 'rb') as wallet_file:
                encrypted_data = wallet_file.read()

            # Decrypt the data and convert it back to a dictionary
            decrypted_data = self.crypto.decrypt(encrypted_data)
            wallet_data = json.loads(decrypted_data.decode())
            return wallet_data

        except Exception as e:
            print(f"Error loading wallet data: {e}")
            return {}

    def add_new_asset(self, asset_name, wallet_address, private_key):
        """
        Add a new blockchain asset to the wallet.
        :param asset_name: The name of the blockchain asset (e.g., Bitcoin, Ethereum).
        :param wallet_address: The wallet address for the asset.
        :param private_key: The private key for the asset.
        """
        try:
            # Load existing wallet data
            wallet_data = self.load_wallet_data()
            
            # Avoid overwriting existing assets
            if asset_name in wallet_data:
                print(f"Asset '{asset_name}' already exists. Skipping addition.")
                return

            # Add the new asset
            wallet_data[asset_name] = {
                "wallet_address": wallet_address,
                "private_key": private_key
            }

            # Save the updated wallet data
            self.save_wallet_data(wallet_data)
            print(f"Asset '{asset_name}' added successfully.")

        except Exception as e:
            print(f"Error adding new asset: {e}")

    def remove_asset(self, asset_name):
        """
        Remove a blockchain asset from the wallet.
        :param asset_name: The name of the blockchain asset to remove.
        """
        try:
            # Load existing wallet data
            wallet_data = self.load_wallet_data()

            # Remove the asset if it exists
            if asset_name in wallet_data:
                del wallet_data[asset_name]
                self.save_wallet_data(wallet_data)
                print(f"Asset '{asset_name}' removed successfully.")
            else:
                print(f"Asset '{asset_name}' does not exist.")

        except Exception as e:
            print(f"Error removing asset: {e}")


# Example usage:
if __name__ == "__main__":
    wallet_manager = TPWalletManager()

    # Add a new asset
    wallet_manager.add_new_asset(
        asset_name="Bitcoin",
        wallet_address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        private_key="SOME_SAMPLE_PRIVATE_KEY"
    )

    # Load and display wallet data
    wallet_data = wallet_manager.load_wallet_data()
    print("Current wallet data:", wallet_data)

    # Remove an asset
    wallet_manager.remove_asset("Bitcoin")
```

This code demonstrates secure storage and management of multiple blockchain assets using encryption and error handling.
