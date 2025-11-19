"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myetherwallet.kr
Prompt: Explain how to securely manage private keys when using MyEtherWallet, including best practices for Keystore files and mnemonic phrases.
Generated: DETERMINISTIC_f5f15aabef9a2881
Batch ID: 20250612_164205
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
import getpass
from eth_account import Account
from cryptography.fernet import Fernet

class PrivateKeyManager:
    """
    A class to manage private keys securely, including generating, encrypting, 
    and storing them using a keystore file and mnemonic phrases.
    """

    def __init__(self):
        self.keystore_file = 'keystore.json'
        self.encryption_key = self.generate_encryption_key()

    def generate_encryption_key(self):
        """Generates a Fernet encryption key for encrypting the private key."""
        return Fernet.generate_key()

    def create_account(self):
        """Creates a new Ethereum account and returns the private key."""
        account = Account.create()
        return account.privateKey

    def encrypt_private_key(self, private_key):
        """
        Encrypts the private key using the encryption key.
        
        :param private_key: The private key to encrypt.
        :return: The encrypted private key.
        """
        fernet = Fernet(self.encryption_key)
        encrypted_key = fernet.encrypt(private_key)
        return encrypted_key

    def save_keystore(self, encrypted_key):
        """Saves the encrypted private key to a keystore file."""
        try:
            with open(self.keystore_file, 'w') as f:
                json.dump({'encrypted_key': encrypted_key.decode(), 'encryption_key': self.encryption_key.decode()}, f)
            print(f"Keystore saved to {self.keystore_file}")
        except IOError as e:
            print(f"Error saving keystore: {e}")

    def load_keystore(self):
        """Loads the encrypted private key from the keystore file."""
        try:
            with open(self.keystore_file, 'r') as f:
                keystore = json.load(f)
            return keystore
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading keystore: {e}")
            return None

    def decrypt_private_key(self, encrypted_key, encryption_key):
        """
        Decrypts the private key using the provided encryption key.
        
        :param encrypted_key: The encrypted private key.
        :param encryption_key: The encryption key used for decryption.
        :return: The decrypted private key.
        """
        fernet = Fernet(encryption_key)
        decrypted_key = fernet.decrypt(encrypted_key)
        return decrypted_key

    def main(self):
        """Main function to create, encrypt, and save the private key."""
        private_key = self.create_account()
        encrypted_key = self.encrypt_private_key(private_key)
        self.save_keystore(encrypted_key)

        # Load and decrypt example
        keystore = self.load_keystore()
        if keystore:
            decrypted_key = self.decrypt_private_key(keystore['encrypted_key'].encode(), keystore['encryption_key'].encode())
            print(f"Decrypted Private Key: {decrypted_key}")

if __name__ == "__main__":
    manager = PrivateKeyManager()
    manager.main()
```
