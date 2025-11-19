"""
Generated Code Metadata:
========================
Original URL: https://predelin.ru
Prompt: "How does Beethoven X ensure security and transparency in its transactions and asset management?"
Generated: DETERMINISTIC_8e9019d8f8c49334
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime

class Transaction:
    """
    A class to represent a transaction in the Beethoven X system.
    """

    def __init__(self, sender, recipient, amount):
        """
        Initializes a new transaction.

        :param sender: The address of the sender
        :param recipient: The address of the recipient
        :param amount: The amount to be transferred
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self):
        """
        Generates a unique transaction ID using SHA-256 hashing.

        :return: A unique transaction ID
        """
        transaction_string = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        return hashlib.sha256(transaction_string.encode()).hexdigest()

    def to_dict(self):
        """
        Converts the transaction to a dictionary format.

        :return: A dictionary representation of the transaction
        """
        return {
            'transaction_id': self.transaction_id,
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': str(self.timestamp)
        }


class Ledger:
    """
    A class to represent the ledger that records all transactions.
    """

    def __init__(self):
        """
        Initializes a new ledger with an empty list of transactions.
        """
        self.transactions = []

    def add_transaction(self, transaction):
        """
        Adds a transaction to the ledger.

        :param transaction: The transaction to be added
        :raises ValueError: If the transaction is invalid
        """
        if not isinstance(transaction, Transaction):
            raise ValueError("Invalid transaction. Must be an instance of Transaction.")
        self.transactions.append(transaction)

    def get_all_transactions(self):
        """
        Retrieves all transactions in the ledger.

        :return: A list of all transactions
        """
        return [transaction.to_dict() for transaction in self.transactions]

    def get_transaction_by_id(self, transaction_id):
        """
        Retrieves a transaction by its ID.

        :param transaction_id: The ID of the transaction to retrieve
        :return: The transaction if found, else None
        """
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction.to_dict()
        return None


# Example usage
if __name__ == "__main__":
    # Create a ledger instance
    ledger = Ledger()

    # Create a new transaction
    try:
        transaction1 = Transaction(sender="Alice", recipient="Bob", amount=100)
        ledger.add_transaction(transaction1)

        transaction2 = Transaction(sender="Bob", recipient="Charlie", amount=50)
        ledger.add_transaction(transaction2)

        # Retrieve all transactions
        all_transactions = ledger.get_all_transactions()
        print(json.dumps(all_transactions, indent=4))

        # Retrieve a specific transaction by ID
        transaction_id = transaction1.transaction_id
        specific_transaction = ledger.get_transaction_by_id(transaction_id)
        print(json.dumps(specific_transaction, indent=4))

    except ValueError as e:
        print(f"Error: {e}")
```
