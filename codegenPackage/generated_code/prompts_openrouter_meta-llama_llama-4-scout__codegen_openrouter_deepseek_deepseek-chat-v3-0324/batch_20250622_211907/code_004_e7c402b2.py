"""
Generated Code Metadata:
========================
Original URL: https://metamausklogiixy.godaddysites.com
Prompt: What are the best practices for securely storing MetaMask API keys and user data in a backend application?
Generated: DETERMINISTIC_e7c402b2a3c9a94e
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from typing import Optional
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class SecureStorage:
    """
    A class to securely store and manage sensitive data like API keys and user data.
    Uses environment variables for configuration and Fernet encryption for data at rest.
    """
    
    def __init__(self):
        """
        Initialize the SecureStorage with encryption key from environment variables.
        Raises:
            ValueError: If ENCRYPTION_KEY is not set or invalid.
        """
        self.encryption_key = os.getenv('ENCRYPTION_KEY')
        if not self.encryption_key:
            raise ValueError("ENCRYPTION_KEY environment variable not set")
        try:
            self.cipher_suite = Fernet(self.encryption_key.encode())
        except Exception as e:
            logger.error(f"Failed to initialize encryption: {e}")
            raise

    def encrypt_data(self, data: str) -> str:
        """
        Encrypt the provided data.
        
        Args:
            data: The plaintext data to encrypt.
            
        Returns:
            Encrypted data as a string.
            
        Raises:
            ValueError: If data is empty or None.
        """
        if not data:
            raise ValueError("Data cannot be empty")
        try:
            encrypted_data = self.cipher_suite.encrypt(data.encode())
            return encrypted_data.decode()
        except Exception as e:
            logger.error(f"Encryption failed: {e}")
            raise

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypt the provided data.
        
        Args:
            encrypted_data: The encrypted data to decrypt.
            
        Returns:
            Decrypted data as a string.
            
        Raises:
            ValueError: If encrypted_data is empty or None.
            cryptography.fernet.InvalidToken: If the token is invalid.
        """
        if not encrypted_data:
            raise ValueError("Encrypted data cannot be empty")
        try:
            decrypted_data = self.cipher_suite.decrypt(encrypted_data.encode())
            return decrypted_data.decode()
        except Exception as e:
            logger.error(f"Decryption failed: {e}")
            raise

    @staticmethod
    def generate_key() -> str:
        """
        Generate a new Fernet encryption key.
        
        Returns:
            A new encryption key as a string.
        """
        return Fernet.generate_key().decode()


# Example usage
if __name__ == "__main__":
    try:
        # Generate a new key if needed (should be set as ENCRYPTION_KEY in .env)
        if not os.getenv('ENCRYPTION_KEY'):
            new_key = SecureStorage.generate_key()
            logger.info(f"New encryption key: {new_key}")
            # In production, set this as ENCRYPTION_KEY in your environment
            
        storage = SecureStorage()
        
        # Example data to encrypt
        sensitive_data = "metamask_api_key_12345"
        encrypted = storage.encrypt_data(sensitive_data)
        logger.info(f"Encrypted: {encrypted}")
        
        decrypted = storage.decrypt_data(encrypted)
        logger.info(f"Decrypted: {decrypted}")
        
    except Exception as e:
        logger.error(f"Error in secure storage example: {e}")
```
