"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to encrypt sensitive data for a growing business, following CyberConnect's cybersecurity guidelines.
Generated: DETERMINISTIC_abf913d4640980c5
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from cryptography.fernet import Fernet
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataEncryptor:
    def __init__(self, key=None):
        """
        Initializes the DataEncryptor with a given key.
        If no key is provided, a new one is generated.
        
        :param key: Optional; a bytes object to use as the encryption key.
        """
        if key:
            self.key = key
        else:
            self.key = self.generate_key()
        
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key():
        """
        Generates a new encryption key.
        
        :return: A bytes object representing the encryption key.
        """
        key = Fernet.generate_key()
        logging.info("Generated a new encryption key.")
        return key

    def encrypt(self, data):
        """
        Encrypts sensitive data using the provided key.
        
        :param data: The data to encrypt (string).
        :return: Encrypted data (bytes).
        """
        if not isinstance(data, str):
            raise ValueError("Data must be a string.")
        
        encrypted_data = self.cipher.encrypt(data.encode())
        logging.info("Data encrypted successfully.")
        return encrypted_data

    def decrypt(self, encrypted_data):
        """
        Decrypts previously encrypted data.
        
        :param encrypted_data: The encrypted data (bytes).
        :return: Decrypted data (string).
        """
        if not isinstance(encrypted_data, bytes):
            raise ValueError("Encrypted data must be bytes.")
        
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        logging.info("Data decrypted successfully.")
        return decrypted_data

    def save_key(self, file_path):
        """
        Saves the encryption key to a file.
        
        :param file_path: The file path to save the key.
        """
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(self.key)
            logging.info(f"Encryption key saved to {file_path}.")
        except IOError as e:
            logging.error(f"Failed to save the key: {e}")

    @staticmethod
    def load_key(file_path):
        """
        Loads the encryption key from a file.
        
        :param file_path: The file path to load the key from.
        :return: The loaded key (bytes).
        """
        try:
            with open(file_path, 'rb') as key_file:
                key = key_file.read()
            logging.info(f"Encryption key loaded from {file_path}.")
            return key
        except IOError as e:
            logging.error(f"Failed to load the key: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        # Initialize the DataEncryptor
        encryptor = DataEncryptor()

        # Save the key for future use
        encryptor.save_key("encryption_key.key")

        # Encrypt sensitive data
        sensitive_data = "This is a sensitive message."
        encrypted = encryptor.encrypt(sensitive_data)

        # Decrypt the data
        decrypted = encryptor.decrypt(encrypted)

        # Output results
        print(f"Original: {sensitive_data}")
        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
