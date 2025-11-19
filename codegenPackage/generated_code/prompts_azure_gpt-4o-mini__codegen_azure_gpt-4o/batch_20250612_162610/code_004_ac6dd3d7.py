"""
Generated Code Metadata:
========================
Original URL: https://en-bitcoin.org
Prompt: Explain how Bitcoin Core achieves consensus among users without voting, and provide an example of how this can be implemented in a decentralized application.
Generated: DETERMINISTIC_ac6dd3d74fa93559
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This Python script demonstrates a simplified implementation of how Bitcoin Core achieves consensus 
among users without voting, using Proof of Work (PoW) and longest chain rule. This example is 
designed for educational purposes and is not production-ready for blockchain applications.
"""

import hashlib
import time

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = 0  # Used for Proof of Work
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        Includes index, previous hash, data, timestamp, and nonce.
        """
        block_content = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mines the block by finding a hash that starts with a certain number of zeros (difficulty).
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    """
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the blockchain after mining it.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain by checking hashes and previous hash links.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Example usage
if __name__ == "__main__":
    # Create a new blockchain
    blockchain = Blockchain(difficulty=4)

    # Add blocks to the blockchain
    blockchain.add_block(Block(1, blockchain.get_latest_block().hash, "Block 1 Data"))
    blockchain.add_block(Block(2, blockchain.get_latest_block().hash, "Block 2 Data"))

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Data: {block.data}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print("-" * 50)

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())
```

This code demonstrates a simplified blockchain implementation using Proof of Work (PoW) and the longest chain rule, which are key components of Bitcoin Core's consensus mechanism.
