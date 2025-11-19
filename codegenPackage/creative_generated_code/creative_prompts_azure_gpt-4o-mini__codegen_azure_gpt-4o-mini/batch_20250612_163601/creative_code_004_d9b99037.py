"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sundusartjrny.pages.dev
Prompt: Generate a guide on how to ensure end-to-end encryption while using JRNY GALLERY for digital art transactions.
Generated: DETERMINISTIC_d9b99037cc7f0957
Batch ID: 20250612_163601
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
import cryptography
from cryptography.fernet import Fernet

class JRNYPersistentStorage:
    """Class to handle persistent storage of sensitive data."""
    
    def __init__(self, storage_file='storage.json'):
        self.storage_file = storage_file
        self.data = {}
        self.load_data()

    def load_data(self):
        """Load data from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                self.data = json.load(file)

    def save_data(self):
        """Save data to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.data, file)

    def set(self, key, value):
        """Set a value in the storage."""
        self.data[key] = value
        self.save_data()

    def get(self, key):
        """Get a value from the storage."""
        return self.data.get(key)


class EncryptionManager:
    """Class to handle encryption and decryption of sensitive data."""
    
    def __init__(self, key=None):
        """Generate or load an encryption key."""
        self.key = key if key else Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext):
        """Encrypt a plaintext string."""
        return self.cipher.encrypt(plaintext.encode())

    def decrypt(self, ciphertext):
        """Decrypt a ciphertext string."""
        try:
            return self.cipher.decrypt(ciphertext).decode()
        except cryptography.exceptions.InvalidToken:
            raise ValueError("Invalid decryption token.")


def main():
    """Main function to demonstrate end-to-end encryption."""
    try:
        # Setup storage and encryption manager
        storage = JRNYPersistentStorage()
        encryption_manager = EncryptionManager()

        # Example data to encrypt
        sensitive_data = "User's credit card details"

        # Encrypt sensitive data
        encrypted_data = encryption_manager.encrypt(sensitive_data)
        print(f"Encrypted Data: {encrypted_data}")

        # Store encrypted data
        storage.set('credit_card_info', encrypted_data.decode())

        # Retrieve and decrypt the data
        stored_encrypted_data = storage.get('credit_card_info').encode()
        decrypted_data = encryption_manager.decrypt(stored_encrypted_data)
        print(f"Decrypted Data: {decrypted_data}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
