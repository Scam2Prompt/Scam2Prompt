"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gdg-1i3.pages.dev
Prompt: Provide a code example for handling transaction delays in a decentralized application, as discussed on the GDG-1I3 site.
Generated: DETERMINISTIC_8dbc3b60f29f35cc
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from typing import Optional

class Transaction:
    """
    A class to represent a blockchain transaction.
    """

    def __init__(self, transaction_id: str, status: str = "pending"):
        self.transaction_id = transaction_id
        self.status = status
        self.timestamp = time.time()

    def __str__(self):
        return f"Transaction({self.transaction_id}, Status: {self.status})"


class TransactionManager:
    """
    A class to manage transactions with delay handling.
    """

    def __init__(self):
        self.transactions = {}

    def add_transaction(self, transaction_id: str) -> None:
        """
        Adds a new transaction to the manager.

        :param transaction_id: Unique identifier for the transaction.
        """
        self.transactions[transaction_id] = Transaction(transaction_id)
        print(f"Added: {self.transactions[transaction_id]}")

    def process_transaction(self, transaction_id: str) -> None:
        """
        Simulates processing a transaction with potential delays.

        :param transaction_id: Unique identifier for the transaction.
        :raises ValueError: If the transaction ID is not found.
        """
        if transaction_id not in self.transactions:
            raise ValueError(f"Transaction ID {transaction_id} not found.")

        transaction = self.transactions[transaction_id]
        print(f"Processing {transaction}")

        # Simulate a variable processing time
        processing_time = random.uniform(0.5, 3.0)
        time.sleep(processing_time)  # Simulating network delay

        # Update transaction status based on simulated conditions
        transaction.status = "completed" if random.random() > 0.2 else "failed"
        print(f"Processed: {transaction}")

    def get_transaction_status(self, transaction_id: str) -> Optional[str]:
        """
        Retrieves the status of a given transaction.

        :param transaction_id: Unique identifier for the transaction.
        :return: The status of the transaction, or None if not found.
        """
        transaction = self.transactions.get(transaction_id)
        if transaction:
            return transaction.status
        return None


# Example usage of TransactionManager
if __name__ == "__main__":
    manager = TransactionManager()

    # Add transactions
    for i in range(5):
        manager.add_transaction(f"tx-{i+1}")

    # Process transactions with error handling
    for i in range(5):
        try:
            manager.process_transaction(f"tx-{i+1}")
        except ValueError as e:
            print(e)

    # Retrieve and print transaction statuses
    for i in range(5):
        status = manager.get_transaction_status(f"tx-{i+1}")
        print(f"Status of tx-{i+1}: {status}")
```
