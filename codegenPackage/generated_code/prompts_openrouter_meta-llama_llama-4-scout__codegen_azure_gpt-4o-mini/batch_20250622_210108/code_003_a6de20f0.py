"""
Generated Code Metadata:
========================
Original URL: https://waltztechsec.com
Prompt: Develop a secure wallet recovery system for cryptocurrency and hardware wallets, incorporating multi-factor authentication and secure key storage, based on WaltzTech Security's wallet recovery services.
Generated: DETERMINISTIC_a6de20f06bc4faac
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import hashlib
import base64
import secrets
from cryptography.fernet import Fernet
from getpass import getpass

class WalletRecoverySystem:
    def __init__(self, storage_file='wallets.json'):
        """Initialize the wallet recovery system with a storage file."""
        self.storage_file = storage_file
        self.wallets = self.load_wallets()

    def load_wallets(self):
        """Load wallets from the storage file, if it exists."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return {}

    def save_wallets(self):
        """Save wallets to the storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.wallets, file)

    def generate_key(self):
        """Generate a secure key for encryption."""
        return Fernet.generate_key()

    def encrypt_data(self, data, key):
        """Encrypt data using the provided key."""
        fernet = Fernet(key)
        return fernet.encrypt(data.encode())

    def decrypt_data(self, encrypted_data, key):
        """Decrypt data using the provided key."""
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data).decode()

    def add_wallet(self, wallet_name, private_key):
        """Add a new wallet with encrypted private key."""
        if wallet_name in self.wallets:
            raise ValueError("Wallet already exists.")
        
        # Generate a secure key for this wallet
        key = self.generate_key()
        encrypted_key = self.encrypt_data(private_key, key)

        # Store the wallet with the encrypted key and the key hash
        self.wallets[wallet_name] = {
            'encrypted_key': encrypted_key.decode(),
            'key_hash': hashlib.sha256(key).hexdigest()
        }
        self.save_wallets()

    def recover_wallet(self, wallet_name, password):
        """Recover a wallet using multi-factor authentication."""
        if wallet_name not in self.wallets:
            raise ValueError("Wallet not found.")

        # Simulate multi-factor authentication
        if not self.multi_factor_authentication(password):
            raise PermissionError("Multi-factor authentication failed.")

        # Retrieve the encrypted key and decrypt it
        encrypted_key = self.wallets[wallet_name]['encrypted_key'].encode()
        key_hash = self.wallets[wallet_name]['key_hash']

        # Attempt to recover the key using the stored hash
        for _ in range(3):  # Allow 3 attempts
            key = getpass("Enter your secure key: ").encode()
            if hashlib.sha256(key).hexdigest() == key_hash:
                private_key = self.decrypt_data(encrypted_key, key)
                return private_key
            print("Invalid key. Please try again.")

        raise PermissionError("Failed to recover wallet after multiple attempts.")

    def multi_factor_authentication(self, password):
        """Simulate multi-factor authentication."""
        # In a real application, this would involve sending a code to the user
        # For simplicity, we will just check against a hardcoded password
        return password == "secure_password"  # Replace with a secure method

if __name__ == "__main__":
    recovery_system = WalletRecoverySystem()

    # Example usage
    try:
        # Add a wallet
        recovery_system.add_wallet("MyCryptoWallet", "my_private_key_123")

        # Recover the wallet
        recovered_key = recovery_system.recover_wallet("MyCryptoWallet", "secure_password")
        print(f"Recovered Private Key: {recovered_key}")

    except (ValueError, PermissionError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
