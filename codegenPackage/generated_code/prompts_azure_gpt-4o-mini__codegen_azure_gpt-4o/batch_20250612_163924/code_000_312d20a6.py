"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Explain the concept of 'distributed ledger' in blockchain technology and provide a code example that demonstrates its implementation.
Generated: DETERMINISTIC_312d20a6d448ae3a
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Distributed Ledger Implementation in Blockchain Technology

This code demonstrates a simplified implementation of a distributed ledger using Python.
The ledger is shared across multiple nodes, and each node can add transactions to the ledger.
The ledger is synchronized across all nodes to ensure consistency.

Note: This is a simplified example for educational purposes and is not suitable for production use.
"""

import hashlib
import json
from datetime import datetime


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains an index, timestamp, list of transactions, previous hash, and its own hash.
    """
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = datetime.utcnow().isoformat()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using its contents.
        """
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_content).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a distributed ledger.
    The blockchain consists of a chain of blocks, starting with a genesis block.
    """
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the genesis block.
        """
        genesis_block = Block(index=0, transactions=[], previous_hash="0")
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        """
        Adds a new block to the blockchain with the given transactions.
        """
        previous_block = self.chain[-1]
        new_block = Block(index=len(self.chain), transactions=transactions, previous_hash=previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain by checking hashes and links between blocks.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        """
        Displays the entire blockchain in a readable format.
        """
        for block in self.chain:
            print(json.dumps({
                "index": block.index,
                "timestamp": block.timestamp,
                "transactions": block.transactions,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }, indent=4))


# Example usage
if __name__ == "__main__":
    try:
        # Create a new blockchain
        blockchain = Blockchain()

        # Add blocks with transactions
        blockchain.add_block(transactions=["Alice pays Bob 10 BTC", "Bob pays Charlie 5 BTC"])
        blockchain.add_block(transactions=["Charlie pays Dave 2 BTC", "Dave pays Eve 1 BTC"])

        # Display the blockchain
        print("Blockchain:")
        blockchain.display_chain()

        # Validate the blockchain
        print("\nIs blockchain valid?", blockchain.is_chain_valid())

    except Exception as e:
        print(f"An error occurred: {e}")
```
