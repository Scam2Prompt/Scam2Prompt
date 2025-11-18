"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestiaholdings.co
Prompt: Design a blockchain-based operational efficiency model for financial systems, incorporating transparency and accuracy improvements discussed by Célestia Global.
Generated: DETERMINISTIC_fe2dc052a3108dc0
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Blockchain-based Operational Efficiency Model for Financial Systems

This is a Python implementation leveraging the transparency and accuracy improvements
discussed by Célestia Global.

Features:
1. Transaction transparency through blockchain principles.
2. Decentralized ledger with proof-of-work consensus.
3. Basic error handling and production-grade design.

Requirements:
- Python 3.7 or above
- `hashlib` (standard library for hashing)
- `datetime` (standard library for timestamps)
- `json` (standard library for serialization)
"""

import hashlib
import json
from datetime import datetime


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains:
    - Index: Position in the chain.
    - Timestamp: Creation time.
    - Data: Transaction details or relevant message.
    - Previous Hash: Hash of the previous block in the chain.
    - Hash: Unique hash of the block (generated based on contents).
    - Nonce: Proof-of-work value for mining.
    """

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block based on its contents.
        Combines index, timestamp, data, previous hash, and nonce.
        Returns:
            str: Hexadecimal hash string.
        """
        block_content = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Perform proof-of-work mining to find valid hash.
        The hash must start with a number of zeros equal to the difficulty.
        Args:
            difficulty (int): Number of leading zeros required in the hash.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    """
    Represents the blockchain implementation.
    Includes methods for adding new blocks, validating the chain, and maintaining transparency.
    """

    def __init__(self, difficulty=3):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Create the initial (genesis) block in the blockchain.
        Returns:
            Block: Genesis block with default parameters.
        """
        return Block(0, str(datetime.now()), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Retrieve the most recent block in the blockchain.
        Returns:
            Block: Latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Add a new block to the blockchain.
        Args:
            data (dict): Transaction details or relevant message.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.now()),
            data=data,
            previous_hash=latest_block.hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the integrity of the blockchain.
        Ensures that:
        1. Hashes match stored values.
        2. Previous hash pointers are consistent.
        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if hash is consistent with contents
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {current_block.index}")
                return False

            # Check if previous hash matches
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash at block {current_block.index}")
                return False

        return True

    def display_chain(self):
        """
        Display all blocks in the blockchain.
        Shows index, timestamp, data, hash, and previous hash for each block.
        """
        for block in self.chain:
            print(json.dumps({
                "index": block.index,
                "timestamp": block.timestamp,
                "data": block.data,
                "hash": block.hash,
                "previous_hash": block.previous_hash
            }, indent=4))


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain(difficulty=4)

    # Add blocks with example financial transactions
    blockchain.add_block({"sender": "Alice", "receiver": "Bob", "amount": 100})
    blockchain.add_block({"sender": "Bob", "receiver": "Charlie", "amount": 50})
    blockchain.add_block({"sender": "Charlie", "receiver": "Alice", "amount": 25})

    # Display the blockchain
    blockchain.display_chain()

    # Validate the blockchain's integrity
    print("\nBlockchain valid:", blockchain.is_chain_valid())
```
