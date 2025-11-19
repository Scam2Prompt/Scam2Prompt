"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: What are the best practices for securely storing IQRA tokens after purchasing them on a DEX?
Generated: DETERMINISTIC_ecc4300cd803f302
Batch ID: 20250612_163659
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

class TokenStorage:
    """
    A class to securely store IQRA tokens using symmetric encryption.
    """

    def __init__(self, storage_file='token_storage.json'):
        """
        Initializes the TokenStorage with a specified storage file.
        Creates a key if it doesn't exist.

        Args:
            storage_file (str): Path to the JSON file for storing tokens.
        """
        self.storage_file = storage_file
        self.key_file = 'secret.key'
        self.key = self.load_or_create_key()

    def load_or_create_key(self):
        """
        Loads an existing encryption key or generates a new one.

        Returns:
            bytes: The encryption key.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
            return key

    def encrypt_token(self, token):
        """
        Encrypts the provided token.

        Args:
            token (str): The token to be encrypted.

        Returns:
            str: The encrypted token.
        """
        fernet = Fernet(self.key)
        encrypted_token = fernet.encrypt(token.encode())
        return encrypted_token.decode()

    def decrypt_token(self, encrypted_token):
        """
        Decrypts the previously encrypted token.

        Args:
            encrypted_token (str): The encrypted token to be decrypted.

        Returns:
            str: The decrypted token.
        """
        fernet = Fernet(self.key)
        decrypted_token = fernet.decrypt(encrypted_token.encode())
        return decrypted_token.decode()

    def store_token(self, token):
        """
        Stores the encrypted token in the storage file.

        Args:
            token (str): The token to be stored.
        """
        encrypted_token = self.encrypt_token(token)
        try:
            with open(self.storage_file, 'r+') as file:
                # Load existing tokens
                data = json.load(file)
                data['tokens'].append(encrypted_token)
                file.seek(0)
                json.dump(data, file)
        except FileNotFoundError:
            with open(self.storage_file, 'w') as file:
                json.dump({'tokens': [encrypted_token]}, file)
        except Exception as e:
            print(f"An error occurred while storing the token: {e}")

    def retrieve_tokens(self):
        """
        Retrieves and decrypts all stored tokens.

        Returns:
            list: A list of decrypted tokens.
        """
        try:
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                return [self.decrypt_token(t) for t in data['tokens']]
        except FileNotFoundError:
            print("No tokens found. Please store a token first.")
            return []
        except Exception as e:
            print(f"An error occurred while retrieving tokens: {e}")
            return []

if __name__ == '__main__':
    # Main program execution
    storage = TokenStorage()

    # User interaction for storing and retrieving tokens
    while True:
        action = input("Choose an action (store/retrieve/exit): ").strip().lower()
        if action == 'store':
            token = getpass("Enter your IQRA token: ")
            storage.store_token(token)
            print("Token stored securely.")
        elif action == 'retrieve':
            tokens = storage.retrieve_tokens()
            if tokens:
                print("Retrieved Tokens:")
                for t in tokens:
                    print(t)
        elif action == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please choose 'store', 'retrieve', or 'exit'.")
```
