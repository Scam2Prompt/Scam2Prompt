"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlineinstantresolve.firebaseapp.com
Prompt: Create a solution for resolving transaction delay issues in blockchain systems, referencing the "Transaction Delay" section.
Generated: DETERMINISTIC_71baa2d58ce4b023
Batch ID: 20250612_154609
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
from queue import PriorityQueue

class Transaction:
    """
    Represents a blockchain transaction.
    """
    def __init__(self, transaction_id, priority, timestamp=None):
        self.transaction_id = transaction_id
        self.priority = priority  # Higher number = higher priority
        self.timestamp = timestamp if timestamp else time.time()

    def __lt__(self, other):
        """
        Comparison method for priority, used by PriorityQueue.
        Transactions with higher priority are processed first.
        """
        return self.priority > other.priority

class TransactionPool:
    """
    Manages a pool of transactions to be processed in priority order.
    """
    def __init__(self):
        self.pool = PriorityQueue()

    def add_transaction(self, transaction):
        """
        Adds a transaction to the pool.
        """
        self.pool.put(transaction)

    def get_next_transaction(self):
        """
        Retrieves the highest priority transaction from the pool.
        """
        if self.pool.empty():
            raise Exception("Transaction pool is empty.")
        return self.pool.get()

    def is_empty(self):
        """
        Checks if the transaction pool is empty.
        """
        return self.pool.empty()

class BlockchainNode:
    """
    Represents a blockchain node responsible for processing transactions.
    """
    def __init__(self, processing_rate=1):
        self.processing_rate = processing_rate  # Transactions per second
        self.transaction_pool = TransactionPool()

    def add_transaction_to_pool(self, transaction):
        """
        Adds a transaction to the node's transaction pool.
        """
        self.transaction_pool.add_transaction(transaction)

    def process_transactions(self):
        """
        Processes transactions from the pool at the defined processing rate.
        """
        while not self.transaction_pool.is_empty():
            try:
                transaction = self.transaction_pool.get_next_transaction()
                self._process_single_transaction(transaction)
            except Exception as e:
                print(f"Error processing transaction: {e}")

    def _process_single_transaction(self, transaction):
        """
        Simulates processing a single transaction.
        """
        print(f"Processing transaction {transaction.transaction_id} "
              f"with priority {transaction.priority}")
        time.sleep(1 / self.processing_rate)  # Simulate processing time

def simulate_transaction_delay():
    """
    Simulates transaction delays by adding and processing transactions in a blockchain system.
    """
    # Create a blockchain node
    node = BlockchainNode(processing_rate=2)  # Processing 2 transactions per second

    # Simulate adding transactions with random priorities
    for i in range(1, 11):
        transaction = Transaction(
            transaction_id=f"TX-{i}",
            priority=random.randint(1, 10),
        )
        print(f"Added transaction {transaction.transaction_id} "
              f"with priority {transaction.priority}")
        node.add_transaction_to_pool(transaction)
    
    # Process transactions
    print("\nProcessing transactions based on priority:")
    node.process_transactions()

# Entry point for the solution
if __name__ == "__main__":
    simulate_transaction_delay()
```
