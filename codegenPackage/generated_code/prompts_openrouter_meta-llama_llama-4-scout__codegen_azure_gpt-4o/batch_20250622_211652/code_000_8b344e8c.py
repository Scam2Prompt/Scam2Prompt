"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Explain the concept of a distributed ledger in the context of blockchain, including its benefits and how it works.
Generated: DETERMINISTIC_8b344e8ce6b81963
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script explains the concept of a distributed ledger in the context of blockchain.
It simulates a simple blockchain-based distributed ledger system, demonstrating how data is stored,
shared, and verified across multiple nodes in a decentralized network.

Key Features:
- Simulates a blockchain with blocks containing transactions.
- Demonstrates the immutability and verification of data.
- Highlights the benefits of distributed ledgers, such as transparency and security.
"""

import hashlib
import json
from datetime import datetime


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains:
    - Index: Position of the block in the chain.
    - Timestamp: Time when the block was created.
    - Transactions: List of transactions stored in the block.
    - Previous Hash: Hash of the previous block in the chain.
    - Hash: Unique hash of the current block.
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
        Ensures immutability of the block's data.
        """
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_content.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a distributed ledger.
    The blockchain consists of a chain of blocks, starting with a genesis block.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the genesis block.
        """
        return Block(index=0, transactions=[], previous_hash="0")

    def add_block(self, transactions):
        """
        Adds a new block to the blockchain with the given transactions.
        """
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            transactions=transactions,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain by checking:
        - The hash of each block matches its contents.
        - The previous hash of each block matches the hash of the preceding block.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate previous hash reference
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


def main():
    """
    Main function to demonstrate the distributed ledger concept.
    """
    try:
        # Initialize the blockchain
        blockchain = Blockchain()

        # Add blocks with sample transactions
        blockchain.add_block(transactions=["Alice pays Bob 10 BTC", "Bob pays Charlie 5 BTC"])
        blockchain.add_block(transactions=["Charlie pays Dave 2 BTC", "Dave pays Eve 1 BTC"])

        # Display the blockchain
        print("Blockchain:")
        for block in blockchain.chain:
            print(json.dumps({
                "index": block.index,
                "timestamp": block.timestamp,
                "transactions": block.transactions,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }, indent=4))

        # Validate the blockchain
        print("\nIs blockchain valid?", blockchain.is_chain_valid())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
