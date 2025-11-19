"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Generate a code snippet for a secure cryptocurrency transaction system suitable for an online gaming platform like BaxBet.
Generated: DETERMINISTIC_23e331493f4c1fcb
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import os
import json
from typing import Dict

class CryptoTransactionSystem:
    """
    A secure cryptocurrency transaction system for an online gaming platform.
    """

    def __init__(self, secret_key: str):
        """
        Initialize the transaction system with a secret key.
        :param secret_key: A secure secret key for signing transactions.
        """
        self.secret_key = secret_key

    def generate_transaction_id(self) -> str:
        """
        Generates a unique transaction ID using a cryptographic random number.
        :return: A unique transaction ID.
        """
        return hashlib.sha256(os.urandom(32)).hexdigest()

    def sign_transaction(self, transaction_data: Dict[str, str]) -> str:
        """
        Generates a cryptographic signature for a transaction.
        :param transaction_data: Dictionary containing transaction details.
        :return: A hex-encoded HMAC signature.
        """
        transaction_json = json.dumps(transaction_data, sort_keys=True).encode('utf-8')
        return hmac.new(self.secret_key.encode('utf-8'), transaction_json, hashlib.sha256).hexdigest()

    def verify_signature(self, transaction_data: Dict[str, str], signature: str) -> bool:
        """
        Verifies the cryptographic signature of a transaction.
        :param transaction_data: Dictionary containing transaction details.
        :param signature: Hex-encoded HMAC signature.
        :return: True if the signature is valid, False otherwise.
        """
        expected_signature = self.sign_transaction(transaction_data)
        return hmac.compare_digest(expected_signature, signature)

    def create_transaction(self, sender: str, receiver: str, amount: float, currency: str) -> Dict[str, str]:
        """
        Creates a new transaction with a unique ID and cryptographic signature.
        :param sender: Sender's identifier.
        :param receiver: Receiver's identifier.
        :param amount: Transaction amount.
        :param currency: Cryptocurrency type (e.g., BTC, ETH).
        :return: A dictionary containing the transaction details.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        transaction_data = {
            "transaction_id": self.generate_transaction_id(),
            "sender": sender,
            "receiver": receiver,
            "amount": str(amount),
            "currency": currency
        }

        transaction_data["signature"] = self.sign_transaction(transaction_data)
        return transaction_data

# Example usage:

if __name__ == "__main__":
    try:
        # Initialize the system with a secure secret key
        secret_key = "super_secure_secret"
        crypto_system = CryptoTransactionSystem(secret_key)

        # Create a transaction
        transaction = crypto_system.create_transaction(
            sender="user123",
            receiver="game_platform",
            amount=100.50,
            currency="BTC"
        )
        print("Transaction created successfully:")
        print(json.dumps(transaction, indent=4))

        # Verify the signature of the transaction
        is_valid = crypto_system.verify_signature(transaction, transaction["signature"])
        if is_valid:
            print("Transaction signature is valid.")
        else:
            print("Transaction signature is invalid.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
