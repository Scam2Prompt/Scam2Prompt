"""
Generated Code Metadata:
========================
Original URL: https://blockdag-8bz.pages.dev
Prompt: Generate code to test BlockDAG's high-speed transaction capabilities (10 blocks per second) using its hybrid consensus mechanism.
Generated: DETERMINISTIC_77cc7abae1b0d597
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import threading
from queue import Queue

class Block:
    """Represents a single block in the BlockDAG."""
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()

    def __repr__(self):
        return f"Block(index={self.index}, previous_hash={self.previous_hash}, transactions={self.transactions})"

class BlockDAG:
    """Represents a simple BlockDAG structure."""
    def __init__(self):
        self.blocks = []
        self.lock = threading.Lock()

    def add_block(self, transactions):
        """Adds a new block to the BlockDAG."""
        with self.lock:
            index = len(self.blocks)
            previous_hash = self.blocks[-1].previous_hash if self.blocks else '0'
            new_block = Block(index, previous_hash, transactions)
            self.blocks.append(new_block)
            return new_block

class Transaction:
    """Represents a transaction in the BlockDAG."""
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __repr__(self):
        return f"Transaction(sender={self.sender}, receiver={self.receiver}, amount={self.amount})"

def generate_random_transaction():
    """Generates a random transaction."""
    sender = f"User{random.randint(1, 100)}"
    receiver = f"User{random.randint(1, 100)}"
    amount = random.randint(1, 1000)
    return Transaction(sender, receiver, amount)

def simulate_block_creation(block_dag, transaction_queue):
    """Simulates the creation of blocks in the BlockDAG."""
    while True:
        transactions = [generate_random_transaction() for _ in range(5)]  # Create 5 random transactions
        block = block_dag.add_block(transactions)
        transaction_queue.put(block)
        print(f"Created: {block}")
        time.sleep(0.1)  # Simulate 10 blocks per second

def main():
    """Main function to run the BlockDAG simulation."""
    block_dag = BlockDAG()
    transaction_queue = Queue()

    # Start the block creation thread
    block_creation_thread = threading.Thread(target=simulate_block_creation, args=(block_dag, transaction_queue))
    block_creation_thread.daemon = True
    block_creation_thread.start()

    try:
        while True:
            # Process blocks from the queue
            if not transaction_queue.empty():
                block = transaction_queue.get()
                # Here you can add additional processing for the block if needed
                transaction_queue.task_done()
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
