"""
Generated Code Metadata:
========================
Original URL: https://powag.ch
Prompt: "Develop a proof-of-concept solution for a blockchain-based application, using innovative architecture and expert developer skills, for a private investor."
Generated: DETERMINISTIC_3ecadba7e226ba21
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Proof-of-Concept Blockchain Application
This code implements a simple blockchain-based application for a private investor.
The blockchain is designed to store transactions securely and immutably.
"""

import hashlib
import time


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains an index, timestamp, data, previous hash, and its own hash.
    """

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        Combines the block's attributes to ensure immutability.
        """
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Provides methods to add blocks and validate the chain.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        Ensures the new block links to the previous block.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain to ensure all blocks are correctly linked and hashes are intact.
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


# Proof-of-Concept Usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        investor_blockchain = Blockchain()

        # Add some blocks with sample data
        investor_blockchain.add_block("Investor Transaction 1: $1000")
        investor_blockchain.add_block("Investor Transaction 2: $5000")
        investor_blockchain.add_block("Investor Transaction 3: $2000")

        # Print the blockchain
        for block in investor_blockchain.chain:
            print(f"Block {block.index}:")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Hash: {block.hash}")
            print()

        # Validate the blockchain
        is_valid = investor_blockchain.is_chain_valid()
        print(f"Blockchain Valid: {is_valid}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
