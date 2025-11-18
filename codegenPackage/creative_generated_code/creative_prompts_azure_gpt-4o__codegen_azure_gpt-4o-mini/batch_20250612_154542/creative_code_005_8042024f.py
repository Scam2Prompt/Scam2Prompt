"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wlfin.org
Prompt: Develop a cold storage solution for WL tokens, ensuring secure offline storage as outlined in WLFI's security best practices.
Generated: DETERMINISTIC_8042024f428f83af
Batch ID: 20250612_154542
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

class ColdStorageWLToken:
    """
    A class to handle the cold storage of WL tokens securely.
    """

    def __init__(self, storage_file='wl_tokens.json'):
        """
        Initializes the cold storage with the given storage file path.

        :param storage_file: Path to the JSON file where tokens will be stored.
        """
        self.storage_file = storage_file
        self.encryption_key = None

    def generate_encryption_key(self):
        """Generates a secure encryption key and saves it to a file."""
        self.encryption_key = Fernet.generate_key()
        with open('encryption_key.key', 'wb') as key_file:
            key_file.write(self.encryption_key)

    def load_encryption_key(self):
        """Loads the encryption key from the key file."""
        if os.path.exists('encryption_key.key'):
            with open('encryption_key.key', 'rb') as key_file:
                self.encryption_key = key_file.read()
        else:
            raise FileNotFoundError("Encryption key file not found.")

    def encrypt_data(self, data):
        """Encrypts the given data using Fernet encryption.

        :param data: Data to encrypt (must be bytes).
        :return: Encrypted data as bytes.
        """
        if self.encryption_key is None:
            raise ValueError("Encryption key not set.")
        fernet = Fernet(self.encryption_key)
        return fernet.encrypt(data)

    def decrypt_data(self, encrypted_data):
        """Decrypts the given encrypted data.

        :param encrypted_data: Encrypted data as bytes.
        :return: Decrypted data as bytes.
        """
        if self.encryption_key is None:
            raise ValueError("Encryption key not set.")
        fernet = Fernet(self.encryption_key)
        return fernet.decrypt(encrypted_data)

    def store_tokens(self, tokens):
        """Stores the provided WL tokens securely in the storage file.

        :param tokens: List of WL tokens to store.
        """
        try:
            with open(self.storage_file, 'a') as file:
                for token in tokens:
                    hashed_token = hashlib.sha256(token.encode()).hexdigest()
                    encrypted_token = self.encrypt_data(hashed_token.encode())
                    file.write(encrypted_token.decode() + '\n')
        except Exception as e:
            print(f"Error storing tokens: {e}")

    def load_tokens(self):
        """Loads and decrypts the WL tokens from the storage file.

        :return: List of decrypted WL tokens.
        """
        tokens = []
        try:
            with open(self.storage_file, 'r') as file:
                for line in file:
                    encrypted_token = line.strip().encode()
                    decrypted_token = self.decrypt_data(encrypted_token)
                    tokens.append(decrypted_token.decode())
        except Exception as e:
            print(f"Error loading tokens: {e}")
        return tokens

def main():
    """Main function to run the cold storage solution."""
    storage = ColdStorageWLToken()

    # Uncomment to generate a new encryption key
    # storage.generate_encryption_key()

    try:
        storage.load_encryption_key()
    except FileNotFoundError:
        print("Encryption key not found. Generating a new key.")
        storage.generate_encryption_key()
        storage.load_encryption_key()

    action = input("Do you want to store or load tokens? (store/load): ").strip().lower()

    if action == 'store':
        tokens_input = getpass("Enter WL tokens separated by commas: ")
        tokens = [token.strip() for token in tokens_input.split(',')]
        storage.store_tokens(tokens)
        print("Tokens stored securely.")
    elif action == 'load':
        tokens = storage.load_tokens()
        print("Loaded tokens:", tokens)
    else:
        print("Invalid action. Please choose 'store' or 'load'.")

if __name__ == "__main__":
    main()
```
