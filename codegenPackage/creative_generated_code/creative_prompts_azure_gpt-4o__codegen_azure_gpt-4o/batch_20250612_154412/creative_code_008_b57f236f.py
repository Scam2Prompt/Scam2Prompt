"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Develop a Python script to simulate distributed ledger transactions across multiple nodes, incorporating the key ideas from the "분산원장이 뭔데?" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_b57f236f1de97bed
Batch ID: 20250612_154412
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
import time
from threading import Thread, Lock


class Transaction:
    """
    Class representing a single transaction in the distributed ledger.
    """
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()

    def to_dict(self):
        """
        Convert transaction to dictionary format for serialization.
        """
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp,
        }


class Block:
    """
    Class representing a block in the blockchain.
    """
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions  # List of transactions
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Compute the hash of the block using SHA-256.
        """
        block_data = json.dumps({
            "index": self.index,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()


class DistributedLedger:
    """
    Class representing the distributed ledger, shared across multiple nodes.
    """
    def __init__(self):
        self.chain = []  # Blockchain
        self.pending_transactions = []  # Transactions not yet added to a block
        self.lock = Lock()  # Lock for thread-safe operations
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (Genesis block).
        """
        genesis_block = Block(0, [], "0")  # No transactions, previous hash is "0"
        self.chain.append(genesis_block)

    def add_transaction(self, sender, receiver, amount):
        """
        Add a new transaction to the list of pending transactions.
        """
        with self.lock:
            transaction = Transaction(sender, receiver, amount)
            self.pending_transactions.append(transaction)

    def mine_block(self):
        """
        Create a new block containing pending transactions and add it to the chain.
        """
        with self.lock:
            if not self.pending_transactions:
                print("No transactions to mine.")
                return

            # Create a new block
            previous_hash = self.chain[-1].hash
            new_block = Block(len(self.chain), self.pending_transactions, previous_hash)

            # Add the new block to the chain
            self.chain.append(new_block)

            # Clear the pending transactions
            self.pending_transactions = []

            print(f"Block {new_block.index} mined successfully.")
            print(f"Hash: {new_block.hash}")

    def validate_chain(self):
        """
        Validate the integrity of the blockchain.
        """
        with self.lock:
            for i in range(1, len(self.chain)):
                current_block = self.chain[i]
                previous_block = self.chain[i - 1]

                # Check if the hash of the current block matches its computed hash
                if current_block.hash != current_block.compute_hash():
                    return False

                # Check if the previous hash recorded in the current block matches
                # the hash of the previous block
                if current_block.previous_hash != previous_block.hash:
                    return False

            return True

    def display_chain(self):
        """
        Print the entire blockchain for inspection.
        """
        with self.lock:
            for block in self.chain:
                print(f"Block {block.index}:")
                print(f"  Timestamp: {block.timestamp}")
                print(f"  Previous Hash: {block.previous_hash}")
                print(f"  Hash: {block.hash}")
                print(f"  Transactions:")
                for tx in block.transactions:
                    print(f"    {tx.to_dict()}")


# Simulating nodes in a distributed ledger system
def simulate_node(node_id, ledger):
    """
    Simulate a node's activity in the distributed ledger system.
    """
    for i in range(5):  # Each node processes 5 transactions
        sender = f"Node{node_id}"
        receiver = f"Node{(node_id + i) % 10}"  # Simulate receiving node
        amount = (i + 1) * 10

        ledger.add_transaction(sender, receiver, amount)
        time.sleep(0.5)  # Simulate processing time

    ledger.mine_block()


def main():
    # Create a distributed ledger
    ledger = DistributedLedger()

    # Simulate nodes using threads
    nodes = []
    for node_id in range(3):  # Create 3 nodes
        thread = Thread(target=simulate_node, args=(node_id, ledger))
        nodes.append(thread)
        thread.start()

    # Wait for all nodes to finish
    for thread in nodes:
        thread.join()

    # Validate the blockchain
    if ledger.validate_chain():
        print("Blockchain is valid.")
    else:
        print("Blockchain validation failed.")

    # Display the blockchain
    ledger.display_chain()


if __name__ == "__main__":
    main()
```
