"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gicoin.trade
Prompt: Generate code to simulate secure and transparent transactions, incorporating the security and data protection standards emphasized by GIC's investment platform.
Generated: DETERMINISTIC_1e5d1ff314429aa5
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import os
from datetime import datetime
from cryptography.fernet import Fernet

class Transaction:
    """
    A class to represent a financial transaction with secure storage and verification.
    """
    
    def __init__(self, sender, recipient, amount):
        """
        Initialize a new transaction.

        :param sender: The sender's identifier (e.g., wallet address)
        :param recipient: The recipient's identifier (e.g., wallet address)
        :param amount: The transaction amount
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        """
        Convert the transaction to a dictionary.

        :return: Dictionary representation of the transaction.
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp,
        }

    def compute_hash(self):
        """
        Generate a SHA-256 hash of the transaction.

        :return: The SHA-256 hash of the transaction.
        """
        transaction_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(transaction_string).hexdigest()


class SecureWallet:
    """
    A class to represent a secure wallet with transaction capabilities.
    """

    def __init__(self):
        """
        Initialize the secure wallet with a Fernet key for encryption.
        """
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.transactions = []

    def add_transaction(self, sender, recipient, amount):
        """
        Add a transaction to the wallet, encrypt it, and store it.

        :param sender: The sender's identifier (e.g., wallet address)
        :param recipient: The recipient's identifier (e.g., wallet address)
        :param amount: The transaction amount
        :raises ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        
        transaction = Transaction(sender, recipient, amount)
        encrypted_transaction = self.encrypt_transaction(transaction)
        self.transactions.append(encrypted_transaction)

    def encrypt_transaction(self, transaction):
        """
        Encrypt the transaction data.

        :param transaction: The transaction to encrypt.
        :return: The encrypted transaction data.
        """
        transaction_data = json.dumps(transaction.to_dict()).encode()
        encrypted_data = self.cipher.encrypt(transaction_data)
        return encrypted_data

    def decrypt_transaction(self, encrypted_data):
        """
        Decrypt the transaction data.

        :param encrypted_data: The encrypted transaction data.
        :return: Decrypted transaction dictionary.
        """
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())

    def view_transactions(self):
        """
        View all transactions in the wallet.

        :return: List of decrypted transactions.
        """
        return [self.decrypt_transaction(tx) for tx in self.transactions]


if __name__ == "__main__":
    # Example usage
    try:
        wallet = SecureWallet()
        wallet.add_transaction("Alice", "Bob", 100)
        wallet.add_transaction("Bob", "Charlie", 50)

        print("All Transactions:")
        for transaction in wallet.view_transactions():
            print(transaction)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
