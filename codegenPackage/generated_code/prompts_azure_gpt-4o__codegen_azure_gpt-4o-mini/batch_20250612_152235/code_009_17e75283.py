"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Recommend tools or libraries for implementing secure packaging and storage solutions, considering Bin Qutab Logistics' focus on safety and security in warehousing.
Generated: DETERMINISTIC_17e7528375efcb42
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# secure_storage.py

import os
import json
import logging
from cryptography.fernet import Fernet
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecureStorage:
    """
    A class to handle secure packaging and storage solutions using encryption.
    """

    def __init__(self, storage_path: str):
        """
        Initializes the SecureStorage with a specified path.

        :param storage_path: The directory where encrypted files will be stored.
        """
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    def generate_key(self) -> bytes:
        """
        Generates a new encryption key.

        :return: A bytes object representing the encryption key.
        """
        return Fernet.generate_key()

    def save_key(self, key_file: str):
        """
        Saves the encryption key to a file.

        :param key_file: The filename where the key will be stored.
        """
        try:
            with open(key_file, 'wb') as f:
                f.write(self.key)
            logging.info(f"Encryption key saved to {key_file}.")
        except Exception as e:
            logging.error(f"Error saving key: {e}")

    def load_key(self, key_file: str):
        """
        Loads the encryption key from a file.

        :param key_file: The filename from which the key will be loaded.
        """
        try:
            with open(key_file, 'rb') as f:
                self.key = f.read()
            self.cipher = Fernet(self.key)
            logging.info(f"Encryption key loaded from {key_file}.")
        except Exception as e:
            logging.error(f"Error loading key: {e}")

    def encrypt_data(self, data: dict) -> bytes:
        """
        Encrypts the provided data.

        :param data: A dictionary containing the data to encrypt.
        :return: Encrypted data as bytes.
        """
        try:
            json_data = json.dumps(data).encode()
            encrypted_data = self.cipher.encrypt(json_data)
            logging.info("Data encrypted successfully.")
            return encrypted_data
        except Exception as e:
            logging.error(f"Error encrypting data: {e}")
            raise

    def decrypt_data(self, encrypted_data: bytes) -> dict:
        """
        Decrypts the provided encrypted data.

        :param encrypted_data: The encrypted data to decrypt.
        :return: Decrypted data as a dictionary.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data)
            data = json.loads(decrypted_data.decode())
            logging.info("Data decrypted successfully.")
            return data
        except Exception as e:
            logging.error(f"Error decrypting data: {e}")
            raise

    def store_data(self, filename: str, data: dict):
        """
        Stores encrypted data in a file.

        :param filename: The name of the file to store the data.
        :param data: The data to encrypt and store.
        """
        try:
            encrypted_data = self.encrypt_data(data)
            with open(self.storage_path / filename, 'wb') as f:
                f.write(encrypted_data)
            logging.info(f"Data stored successfully in {filename}.")
        except Exception as e:
            logging.error(f"Error storing data: {e}")

    def retrieve_data(self, filename: str) -> dict:
        """
        Retrieves and decrypts data from a file.

        :param filename: The name of the file to retrieve the data from.
        :return: The decrypted data as a dictionary.
        """
        try:
            with open(self.storage_path / filename, 'rb') as f:
                encrypted_data = f.read()
            return self.decrypt_data(encrypted_data)
        except Exception as e:
            logging.error(f"Error retrieving data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    storage = SecureStorage("secure_storage")
    storage.save_key("encryption_key.key")

    # Example data to store
    data_to_store = {
        "item": "Widget",
        "quantity": 100,
        "location": "Warehouse A"
    }

    storage.store_data("item_data.json", data_to_store)

    # Retrieve the data
    retrieved_data = storage.retrieve_data("item_data.json")
    print("Retrieved Data:", retrieved_data)
```
