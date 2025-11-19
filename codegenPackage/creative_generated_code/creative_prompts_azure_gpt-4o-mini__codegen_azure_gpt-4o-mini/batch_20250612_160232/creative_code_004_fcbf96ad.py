"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sirixfinance.com
Prompt: Explain how to implement secure transactions for cryptocurrency investments using the security measures mentioned by Zirix Finance.
Generated: DETERMINISTIC_fcbf96ad0da5faa6
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import hmac
import json
from cryptography.fernet import Fernet
from typing import Dict, Any, Tuple

# Constants for encryption
ENCRYPTION_KEY = Fernet.generate_key()  # Generate a key for encryption
fernet = Fernet(ENCRYPTION_KEY)

# Transaction class to handle cryptocurrency transactions securely
class SecureTransaction:
    def __init__(self, user_id: str, transaction_details: Dict[str, Any]):
        """
        Initialize a secure transaction.

        :param user_id: Unique identifier for the user
        :param transaction_details: Details of the transaction
        """
        self.user_id = user_id
        self.transaction_details = transaction_details
        self.transaction_id = self.create_transaction_id()

    def create_transaction_id(self) -> str:
        """
        Create a unique transaction ID based on user ID and current timestamp.

        :return: A unique transaction ID
        """
        import time
        transaction_data = f"{self.user_id}{time.time()}"
        return hashlib.sha256(transaction_data.encode()).hexdigest()

    def encrypt_transaction_details(self) -> str:
        """
        Encrypt the transaction details for secure storage.

        :return: Encrypted transaction details as a string
        """
        json_data = json.dumps(self.transaction_details).encode()
        return fernet.encrypt(json_data).decode()

    def sign_transaction(self, secret: str) -> str:
        """
        Create a signature for the transaction to verify its authenticity.

        :param secret: Secret key for signing the transaction
        :return: Signature string
        """
        signature = hmac.new(secret.encode(), self.transaction_id.encode(), hashlib.sha256)
        return signature.hexdigest()

    def process_transaction(self, secret: str) -> Tuple[str, str]:
        """
        Process the transaction by encrypting details and signing it.

        :param secret: Secret key for signing the transaction
        :return: Tuple containing encrypted transaction details and signature
        """
        try:
            encrypted_details = self.encrypt_transaction_details()
            signature = self.sign_transaction(secret)
            return encrypted_details, signature
        except Exception as e:
            raise RuntimeError(f"Transaction processing failed: {e}")

# Example usage
if __name__ == "__main__":
    try:
        user_id = "user_123"
        transaction_details = {
            "amount": 0.5,
            "currency": "BTC",
            "recipient": "recipient_address",
            "timestamp": "2023-10-01T12:00:00Z"
        }
        secret_key = "very_secure_secret_key"

        # Create a secure transaction
        transaction = SecureTransaction(user_id, transaction_details)
        encrypted_details, signature = transaction.process_transaction(secret_key)

        print("Encrypted Transaction Details:", encrypted_details)
        print("Transaction Signature:", signature)
    except Exception as e:
        print(f"Error: {e}")
```
