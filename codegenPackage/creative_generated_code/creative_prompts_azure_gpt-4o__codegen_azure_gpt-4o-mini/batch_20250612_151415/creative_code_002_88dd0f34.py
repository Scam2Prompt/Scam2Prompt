"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypton-exchange.com
Prompt: Generate code to simulate high-performance cryptocurrency transactions with an average processing time of less than one second, as described by Crypton Exchange.
Generated: DETERMINISTIC_88dd0f34dc331d50
Batch ID: 20250612_151415
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
from typing import List, Dict

class Transaction:
    """
    A class to represent a cryptocurrency transaction.
    """

    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

    def __repr__(self):
        return f"Transaction({self.sender} -> {self.recipient}: {self.amount} at {self.timestamp})"


class CryptocurrencyExchange:
    """
    A class to simulate a cryptocurrency exchange facilitating transactions.
    """

    def __init__(self):
        self.transaction_pool: List[Transaction] = []

    def create_transaction(self, sender: str, recipient: str, amount: float) -> Transaction:
        """
        Create a new transaction and add it to the transaction pool.

        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param amount: Amount of cryptocurrency to transfer.
        :return: A Transaction object.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        transaction = Transaction(sender, recipient, amount)
        self.transaction_pool.append(transaction)
        return transaction

    def process_transactions(self) -> List[Transaction]:
        """
        Process all transactions in the transaction pool with a simulated average processing time.

        :return: A list of processed transactions.
        """
        processed_transactions = []
        start_time = time.time()

        for transaction in self.transaction_pool:
            # Simulate transaction processing time
            processing_time = random.uniform(0.1, 0.9)  # Simulating processing time between 100ms and 900ms
            time.sleep(processing_time)
            processed_transactions.append(transaction)

            # Report processing time for monitoring
            print(f"Processed: {transaction} in {processing_time:.2f} seconds")

        self.transaction_pool.clear()  # Clear the pool after processing
        total_time = time.time() - start_time
        print(f"Total processing time: {total_time:.2f} seconds")
        return processed_transactions


if __name__ == "__main__":
    exchange = CryptocurrencyExchange()

    # Example transaction inputs
    transactions_info = [
        ("Alice", "Bob", 0.5),
        ("Charlie", "Dave", 1.0),
        ("Eve", "Frank", 2.0),
    ]

    # Create and process transactions
    for sender, recipient, amount in transactions_info:
        try:
            exchange.create_transaction(sender, recipient, amount)
        except ValueError as e:
            print(f"Error creating transaction: {e}")

    processed = exchange.process_transactions()
    print(f"All processed transactions: {processed}")
```
