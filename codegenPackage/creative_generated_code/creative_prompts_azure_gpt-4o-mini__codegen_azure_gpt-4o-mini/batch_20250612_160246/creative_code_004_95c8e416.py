"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalmaxtrading.com
Prompt: Explain how to securely store and manage Bitcoin wallets for users of Capital Max Trading, including best practices for encryption and data protection.
Generated: DETERMINISTIC_95c8e416f7de6b6e
Batch ID: 20250612_160246
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
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

class WalletManager:
    """
    A class to manage Bitcoin wallets securely, including storage and encryption.
    """

    def __init__(self, storage_file='wallets.json'):
        """
        Initialize the WalletManager with a storage file.

        :param storage_file: The path to the JSON file for storing wallet data.
        """
        self.storage_file = storage_file
        self.key = self.load_or_generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key():
        """
        Generate a new encryption key and save it to a file.
        """
        key = Fernet.generate_key()
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)
        return key

    @staticmethod
    def load_or_generate_key():
        """
        Load the encryption key from a file, or generate a new one if not found.

        :return: The encryption key.
        """
        if os.path.exists('secret.key'):
            with open('secret.key', 'rb') as key_file:
                return key_file.read()
        else:
            return WalletManager.generate_key()

    def encrypt_wallet(self, wallet_data):
        """
        Encrypt the wallet data.

        :param wallet_data: The wallet data to encrypt.
        :return: The encrypted wallet data.
        """
        return self.cipher.encrypt(wallet_data.encode())

    def decrypt_wallet(self, encrypted_data):
        """
        Decrypt the wallet data.

        :param encrypted_data: The encrypted wallet data.
        :return: The decrypted wallet data.
        """
        try:
            return self.cipher.decrypt(encrypted_data).decode()
        except Exception as e:
            print("Error decrypting wallet data:", e)
            return None

    def save_wallet(self, wallet_name, wallet_data):
        """
        Save the encrypted wallet data to the storage file.

        :param wallet_name: The name of the wallet.
        :param wallet_data: The wallet data to save.
        """
        encrypted_data = self.encrypt_wallet(wallet_data)
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r+') as file:
                    wallets = json.load(file)
                    wallets[wallet_name] = encrypted_data.decode()
                    file.seek(0)
                    json.dump(wallets, file)
                    file.truncate()
            else:
                with open(self.storage_file, 'w') as file:
                    json.dump({wallet_name: encrypted_data.decode()}, file)
        except Exception as e:
            print("Error saving wallet:", e)

    def load_wallet(self, wallet_name):
        """
        Load and decrypt the wallet data from the storage file.

        :param wallet_name: The name of the wallet to load.
        :return: The decrypted wallet data or None if not found.
        """
        try:
            with open(self.storage_file, 'r') as file:
                wallets = json.load(file)
                if wallet_name in wallets:
                    encrypted_data = wallets[wallet_name].encode()
                    return self.decrypt_wallet(encrypted_data)
                else:
                    print("Wallet not found.")
                    return None
        except FileNotFoundError:
            print("Storage file not found.")
            return None
        except json.JSONDecodeError:
            print("Error reading wallet data.")
            return None

# Example usage:
if __name__ == "__main__":
    wallet_manager = WalletManager()
    
    # Prompt user for wallet name and data
    wallet_name = input("Enter wallet name: ")
    wallet_data = getpass("Enter wallet data (e.g., private key): ")
    
    # Save the wallet
    wallet_manager.save_wallet(wallet_name, wallet_data)
    
    # Load the wallet
    loaded_data = wallet_manager.load_wallet(wallet_name)
    if loaded_data:
        print(f"Loaded wallet data: {loaded_data}")
```
