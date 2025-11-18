"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hemi.host
Prompt: Explain how to use Hemi’s extensibility features to incorporate Bitcoin’s security into a custom blockchain network.
Generated: DETERMINISTIC_7a6ae2d737cca168
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python code example that demonstrates how to incorporate Bitcoin-like security features (e.g., proof-of-work) into a custom blockchain network using extensibility principles. The code emphasizes clean design, modularity, and production readiness.

```python
import hashlib
import time
from typing import List, Optional

class Block:
    """
    Represents a single block in the blockchain.
    """

    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        self.index = index  # Position of the block in the chain
        self.previous_hash = previous_hash  # Hash of the previous block for chain linkage
        self.timestamp = timestamp  # Timestamp of block creation
        self.data = data  # Information stored in the block
        self.nonce = nonce  # Nonce used for proof-of-work
        self.hash = self.calculate_hash()  # Current block hash

    def calculate_hash(self) -> str:
        """
        Calculates the SHA-256 hash of the block.
        Includes all block attributes to ensure integrity.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """
        Performs the proof-of-work mining process.
        Adjusts the nonce until the hash meets the required difficulty criteria.
        """
        required_prefix = "0" * difficulty  # Target hash prefix
        while not self.hash.startswith(required_prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    """
    Represents the custom blockchain network with Bitcoin-like security features.
    """

    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = []  # The blockchain (list of blocks)
        self.difficulty = difficulty  # Mining difficulty (number of leading zeros in the hash)
        self.create_genesis_block()  # Initialize the chain with a genesis block

    def create_genesis_block(self) -> None:
        """
        Creates the first block in the blockchain (Genesis Block).
        """
        genesis_block = Block(index=0, previous_hash="0", timestamp=time.time(), data="Genesis Block")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data: str) -> None:
        """
        Adds a new block to the blockchain after mining.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            timestamp=time.time(),
            data=data
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the entire blockchain to ensure integrity.
        Checks hashes and linkages between blocks.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate linkage (current block points to the previous block)
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain with a mining difficulty of 4
        custom_blockchain = Blockchain(difficulty=4)

        # Add blocks to the blockchain
        custom_blockchain.add_block(data="Block 1: Transaction Data")
        custom_blockchain.add_block(data="Block 2: More Transaction Data")
        custom_blockchain.add_block(data="Block 3: Even More Transaction Data")

        # Print the blockchain
        for block in custom_blockchain.chain:
            print(f"Block {block.index}:")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}")
            print(f"  Hash: {block.hash}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Nonce: {block.nonce}\n")

        # Validate the blockchain
        print("Is blockchain valid?", custom_blockchain.is_chain_valid())

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code creates a simple blockchain network with proof-of-work mining inspired by Bitcoin's security features, including mining difficulty and block linkage validation. Let me know if you need further assistance!
