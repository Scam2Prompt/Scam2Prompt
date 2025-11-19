"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptojustin.com
Prompt: Recommend libraries for securing crypto assets, inspired by the "8 Ways to Secure your Crypto Assets" article on Crypto Justin.
Generated: DETERMINISTIC_4fa0ca99ef3b58ce
Batch ID: 20250612_155557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for securing crypto assets
import os
import hashlib
import json
from cryptography.fernet import Fernet

class CryptoAssetSecurity:
    """
    This class provides methods to secure crypto assets using best practices.
    """

    def __init__(self, key=None):
        """
        Initializes the CryptoAssetSecurity class with an optional key.
        If no key is provided, a new key will be generated.
        """
        if key is None:
            self.key = Fernet.generate_key()
            self.cipher = Fernet(self.key)
        else:
            self.key = key
            self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        """
        Encrypts the given data using the Fernet symmetric encryption.

        :param data: The data to encrypt (string).
        :return: Encrypted data (bytes).
        """
        try:
            if isinstance(data, str):
                data = data.encode('utf-8')  # Convert string to bytes
            encrypted_data = self.cipher.encrypt(data)
            return encrypted_data
        except Exception as e:
            print(f"Error encrypting data: {e}")

    def decrypt_data(self, encrypted_data):
        """
        Decrypts the given encrypted data using the Fernet symmetric encryption.

        :param encrypted_data: The data to decrypt (bytes).
        :return: Decrypted data (string).
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data)
            return decrypted_data.decode('utf-8')  # Convert bytes back to string
        except Exception as e:
            print(f"Error decrypting data: {e}")

    @staticmethod
    def hash_data(data):
        """
        Generates a SHA-256 hash of the given data.

        :param data: The data to hash (string).
        :return: Hashed data (string).
        """
        try:
            sha256_hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
            return sha256_hash
        except Exception as e:
            print(f"Error hashing data: {e}")
    
    @staticmethod
    def save_key_to_file(key, filename):
        """
        Saves the encryption key to a file.

        :param key: The key to save (bytes).
        :param filename: The filename to save the key.
        """
        try:
            with open(filename, 'wb') as key_file:
                key_file.write(key)
                print(f"Key saved to {filename}.")
        except Exception as e:
            print(f"Error saving key to file: {e}")

    @staticmethod
    def load_key_from_file(filename):
        """
        Loads an encryption key from a file.

        :param filename: The filename to load the key from.
        :return: Loaded key (bytes).
        """
        try:
            with open(filename, 'rb') as key_file:
                key = key_file.read()
            return key
        except Exception as e:
            print(f"Error loading key from file: {e}")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the CryptoAssetSecurity class
    security = CryptoAssetSecurity()

    # Encrypting data
    data_to_encrypt = "MySecretCryptoAsset"
    encrypted_data = security.encrypt_data(data_to_encrypt)
    print(f"Encrypted Data: {encrypted_data}")

    # Decrypting data
    decrypted_data = security.decrypt_data(encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")

    # Hashing data
    hashed_data = security.hash_data(data_to_encrypt)
    print(f"Hashed Data: {hashed_data}")

    # Saving and loading key
    security.save_key_to_file(security.key, 'secret.key')
    loaded_key = security.load_key_from_file('secret.key')
    print(f"Loaded Key: {loaded_key}")
```
