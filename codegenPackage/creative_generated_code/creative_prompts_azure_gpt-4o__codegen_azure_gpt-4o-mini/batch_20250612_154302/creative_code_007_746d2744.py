"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsecure-3bc.pages.dev
Prompt: Generate code for a decentralized storage solution that safeguards user data and assets, leveraging encryption techniques as described in Chain Solution Center's safety and security features.
Generated: DETERMINISTIC_746d2744355a9bfd
Batch ID: 20250612_154302
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
from typing import Dict


class DecentralizedStorage:
    def __init__(self, storage_directory: str):
        """
        Initialize the decentralized storage system.

        :param storage_directory: Directory where encrypted data will be stored.
        """
        self.storage_directory = storage_directory
        os.makedirs(self.storage_directory, exist_ok=True)
        self.key = self.generate_key()

    @staticmethod
    def generate_key() -> bytes:
        """
        Generate a new encryption key.

        :return: A Fernet key for encryption.
        """
        return Fernet.generate_key()

    def encrypt_data(self, data: str) -> bytes:
        """
        Encrypt the given data using Fernet symmetric encryption.

        :param data: Data to be encrypted.
        :return: Encrypted data in bytes.
        """
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode())

    def decrypt_data(self, encrypted_data: bytes) -> str:
        """
        Decrypt the given encrypted data.

        :param encrypted_data: Encrypted data in bytes.
        :return: Decrypted data as a string.
        """
        fernet = Fernet(self.key)
        return fernet.decrypt(encrypted_data).decode()

    def save_data(self, filename: str, data: str) -> None:
        """
        Save encrypted data to a file.

        :param filename: The name of the file to save the data.
        :param data: The data to be encrypted and saved.
        """
        try:
            encrypted_data = self.encrypt_data(data)
            file_path = os.path.join(self.storage_directory, filename)
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)
            print(f"Data saved successfully to {file_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename: str) -> str:
        """
        Load and decrypt data from a file.

        :param filename: The name of the file to load the data from.
        :return: Decrypted data as a string.
        """
        try:
            file_path = os.path.join(self.storage_directory, filename)
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            return self.decrypt_data(encrypted_data)
        except FileNotFoundError:
            print(f"Error: The file {filename} does not exist.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def hash_data(self, data: str) -> str:
        """
        Generate a SHA-256 hash for the given data.

        :param data: The data to be hashed.
        :return: The SHA-256 hash of the data.
        """
        return hashlib.sha256(data.encode()).hexdigest()


if __name__ == "__main__":
    # Example usage
    storage = DecentralizedStorage("decentralized_storage")

    # Save data
    sample_data = "User's sensitive information"
    storage.save_data("user_data.json", json.dumps({"data": sample_data}))

    # Load data
    loaded_data = storage.load_data("user_data.json")
    print(f"Loaded Data: {loaded_data}")

    # Hash the original data
    data_hash = storage.hash_data(sample_data)
    print(f"Data Hash: {data_hash}")
```
