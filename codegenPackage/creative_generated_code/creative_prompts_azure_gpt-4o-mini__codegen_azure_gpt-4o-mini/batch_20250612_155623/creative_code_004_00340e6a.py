"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wildhorse-llc.com
Prompt: Explain how to implement secure data encryption for a trading application, referencing the security measures mentioned by Wildhorse LLC.
Generated: DETERMINISTIC_00340e6a05dd9f9e
Batch ID: 20250612_155623
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

# Set up logging for monitoring and debugging
logging.basicConfig(level=logging.INFO)

class EncryptionManager:
    """Class to manage encryption and decryption of sensitive data."""

    def __init__(self, key_file='secret.key'):
        """
        Initializes the EncryptionManager with a key.
        
        Args:
            key_file (str): The path to the key file. Default is 'secret.key'.
        """
        self.key_file = key_file
        self.key = self.load_key()

    def generate_key(self):
        """Generates a new key and saves it to a file."""
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)
        logging.info(f"Generated and saved encryption key to {self.key_file}")

    def load_key(self):
        """Loads the key from the current key file."""
        if not os.path.exists(self.key_file):
            logging.warning(f"{self.key_file} not found. Generating a new key.")
            self.generate_key()
        
        with open(self.key_file, 'rb') as key_file:
            return key_file.read()

    def encrypt_data(self, data: str) -> str:
        """
        Encrypts the provided data using the loaded key.
        
        Args:
            data (str): The plaintext data to encrypt.
        
        Returns:
            str: The encrypted data as a URL-safe base64 encoded string.
        """
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data.encode())
        logging.info("Data encrypted successfully.")
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypts the provided encrypted data using the loaded key.
        
        Args:
            encrypted_data (str): The encrypted data to decrypt.
        
        Returns:
            str: The decrypted plaintext data.
        """
        fernet = Fernet(self.key)
        try:
            decrypted_data = fernet.decrypt(encrypted_data.encode())
            logging.info("Data decrypted successfully.")
            return decrypted_data.decode()
        except Exception as e:
            logging.error("Decryption failed: %s", e)
            raise ValueError("Decryption failed. Please check the encrypted data.") from e

def main():
    """Main function to demonstrate encryption and decryption."""
    manager = EncryptionManager()
    
    # Sample data to be encrypted
    sensitive_data = "User's credit card information"
    
    # Encrypt the data
    encrypted = manager.encrypt_data(sensitive_data)
    print(f"Encrypted data: {encrypted}")

    # Decrypt the data
    decrypted = manager.decrypt_data(encrypted)
    print(f"Decrypted data: {decrypted}")

if __name__ == "__main__":
    main()
```

This code provides a secure implementation for encrypting and decrypting sensitive data in a trading application, adhering to best practices and including error handling and logging.
