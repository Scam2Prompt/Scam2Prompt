"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simpleswap.financial
Prompt: Generate code to securely store and retrieve cryptocurrency transaction data using encryption methods described in SimpleSwap's security features.
Generated: DETERMINISTIC_b73032d7def6078a
Batch ID: 20250612_154942
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
import json
import base64
import hashlib

class CryptoTransactionStore:
    def __init__(self, key: bytes):
        """
        Initialize the CryptoTransactionStore with a given encryption key.
        
        :param key: A bytes object containing the encryption key.
        """
        self.key = key
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generate a new Fernet encryption key.
        
        :return: A bytes object containing the encryption key.
        """
        return Fernet.generate_key()

    @staticmethod
    def hash_key(key: bytes) -> str:
        """
        Create a SHA-256 hash of the key for storage purposes.
        
        :param key: A bytes object containing the encryption key.
        :return: A hex string representation of the key hash.
        """
        return hashlib.sha256(key).hexdigest()

    def encrypt_transaction(self, transaction_data: dict) -> str:
        """
        Encrypts transaction data using the Fernet cipher.
        
        :param transaction_data: A dictionary containing transaction details.
        :return: An encrypted string representation of the transaction data.
        """
        try:
            # Convert dictionary to JSON string
            json_data = json.dumps(transaction_data).encode('utf-8')
            # Encrypt JSON string
            encrypted_data = self.cipher.encrypt(json_data)
            return encrypted_data.decode('utf-8')
        except Exception as e:
            raise RuntimeError(f"Encryption failed: {str(e)}")

    def decrypt_transaction(self, encrypted_data: str) -> dict:
        """
        Decrypts transaction data using the Fernet cipher.
        
        :param encrypted_data: An encrypted string representation of the transaction data.
        :return: A dictionary containing the original transaction details.
        """
        try:
            # Decrypt the data
            decrypted_data = self.cipher.decrypt(encrypted_data.encode('utf-8'))
            # Convert JSON string back to dictionary
            return json.loads(decrypted_data.decode('utf-8'))
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Generate and store encryption key (in practice, store this securely)
    key = CryptoTransactionStore.generate_key()
    key_hash = CryptoTransactionStore.hash_key(key)
    print(f"Generated Key Hash: {key_hash}")

    # Create a transaction store instance
    transaction_store = CryptoTransactionStore(key)

    # Example transaction data
    transaction = {
        "id": "txn_123456",
        "amount": 0.01,
        "currency": "BTC",
        "timestamp": "2023-10-01T12:00:00Z"
    }

    # Encrypt the transaction data
    encrypted_transaction = transaction_store.encrypt_transaction(transaction)
    print(f"Encrypted Transaction: {encrypted_transaction}")

    # Decrypt the transaction data
    decrypted_transaction = transaction_store.decrypt_transaction(encrypted_transaction)
    print(f"Decrypted Transaction: {decrypted_transaction}")
```
