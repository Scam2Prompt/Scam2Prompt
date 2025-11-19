"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enkrpt.com
Prompt: How can I implement strong encryption for private keys in a multicurrency crypto wallet application?
Generated: DETERMINISTIC_5179402fb823062e
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
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

class CryptoWallet:
    def __init__(self, key=None):
        """
        Initializes the CryptoWallet with a key for encryption/decryption.
        If no key is provided, a new key will be generated.

        :param key: Optional encryption key. If None, a new key will be generated.
        """
        self.key = key or self.generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key():
        """
        Generates a new encryption key using the cryptography library.

        :return: A base64 encoded string representing the encryption key.
        """
        return Fernet.generate_key()

    def encrypt_private_key(self, private_key):
        """
        Encrypts a given private key.

        :param private_key: The private key to encrypt.
        :return: The encrypted private key as a base64 encoded string.
        """
        if not isinstance(private_key, str):
            raise ValueError("Private key must be a string.")
        
        encrypted_key = self.cipher.encrypt(private_key.encode())
        return encrypted_key.decode()

    def decrypt_private_key(self, encrypted_key):
        """
        Decrypts an encrypted private key.

        :param encrypted_key: The encrypted private key to decrypt.
        :return: The original private key as a string.
        """
        try:
            decrypted_key = self.cipher.decrypt(encrypted_key.encode())
            return decrypted_key.decode()
        except InvalidToken:
            raise ValueError("Invalid key or corrupted encrypted data.")

    def save_wallet(self, filepath):
        """
        Saves the encryption key to a file. This should be done securely.

        :param filepath: The file path where the key will be saved.
        """
        try:
            with open(filepath, 'wb') as key_file:
                key_file.write(self.key)
        except IOError as e:
            raise RuntimeError("Failed to save the wallet key.") from e

    @staticmethod
    def load_wallet(filepath):
        """
        Loads an encryption key from a file.

        :param filepath: The file path from which the key will be loaded.
        :return: The encryption key.
        """
        try:
            with open(filepath, 'rb') as key_file:
                return key_file.read()
        except IOError as e:
            raise RuntimeError("Failed to load the wallet key.") from e

# Example usage:
if __name__ == "__main__":
    # Generate a new wallet and encrypt a private key
    wallet = CryptoWallet()
    private_key = "my_private_key_for_currency"
    
    # Encrypt the private key
    encrypted_key = wallet.encrypt_private_key(private_key)
    print(f"Encrypted Key: {encrypted_key}")

    # Decrypt the private key
    decrypted_key = wallet.decrypt_private_key(encrypted_key)
    print(f"Decrypted Key: {decrypted_key}")

    # Save the encryption key to a file
    wallet.save_wallet('wallet_key.key')

    # Load the encryption key from a file
    loaded_key = CryptoWallet.load_wallet('wallet_key.key')
    print(f"Loaded Key: {loaded_key.decode()}")
```
