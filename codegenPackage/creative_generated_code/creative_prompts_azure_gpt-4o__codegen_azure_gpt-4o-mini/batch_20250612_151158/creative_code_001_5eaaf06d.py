"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sundusartjrny.pages.dev
Prompt: Recommend APIs or libraries for implementing end-to-end encryption in a digital art gallery platform like JRNY Gallery to ensure user activity privacy.
Generated: DETERMINISTIC_5eaaf06d8d0293e7
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for encryption and secure communication
from cryptography.fernet import Fernet
import json
import os

# Utility class for encryption and decryption
class EncryptionService:
    """A service for encrypting and decrypting messages using symmetric encryption."""

    def __init__(self):
        """Initialize the EncryptionService and generate a key."""
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key():
        """Generate a new key for encryption."""
        return Fernet.generate_key()

    def encrypt(self, data: str) -> str:
        """
        Encrypt the provided data.
        
        Args:
            data (str): The plaintext data to encrypt.
        
        Returns:
            str: The encrypted data in bytes, encoded as a string.
        """
        try:
            return self.cipher.encrypt(data.encode()).decode()
        except Exception as e:
            raise RuntimeError(f"Encryption failed: {str(e)}")

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypt the provided encrypted data.
        
        Args:
            encrypted_data (str): The encrypted data to decrypt.

        Returns:
            str: The decrypted plaintext data.
        """
        try:
            return self.cipher.decrypt(encrypted_data.encode()).decode()
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {str(e)}")


# Sample usage of the EncryptionService
if __name__ == "__main__":
    # Initialize the encryption service
    encryption_service = EncryptionService()

    # Example data to encrypt
    user_activity_data = json.dumps({
        'user_id': '12345',
        'action': 'view_art',
        'art_id': '67890'
    })

    # Encrypt the user activity data
    encrypted_data = encryption_service.encrypt(user_activity_data)
    print(f"Encrypted Data: {encrypted_data}")

    # Decrypt the user activity data
    decrypted_data = encryption_service.decrypt(encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")

    # Optionally, save the key securely (in a real application)
    # Ensure the key is stored in a secure location, e.g., an environment variable or a secrets management service
    try:
        with open("encryption_key.key", "wb") as key_file:
            key_file.write(encryption_service.key)
    except IOError as e:
        print(f"Error saving key: {e}")
```
