"""
Generated Code Metadata:
========================
Original URL: https://purchase-blockdag-in.pages.dev
Prompt: Explain the proof-of-work system used by BlockDAG and provide a high-level overview of its security features, using technical terms and concepts.
Generated: DETERMINISTIC_f6da61da059ca6e5
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
Proof-of-Work System for BlockDAG
This script provides a high-level implementation of a Proof-of-Work (PoW) system used in BlockDAGs.
The PoW system ensures security by requiring computational effort to add blocks to the DAG structure.
"""

import hashlib
import time

class Block:
    """
    Represents a single block in the BlockDAG structure.
    Each block contains a reference to its parent(s), a timestamp, and a nonce for PoW.
    """
    def __init__(self, data, parents):
        """
        Initialize a new block.

        :param data: The data to be stored in the block.
        :param parents: List of parent block hashes (references in the DAG).
        """
        self.data = data
        self.parents = parents  # List of parent block hashes
        self.timestamp = time.time()  # Current timestamp
        self.nonce = 0  # Nonce used for Proof-of-Work
        self.hash = None  # Block hash (computed during mining)

    def compute_hash(self):
        """
        Compute the hash of the block using SHA-256.

        :return: Hexadecimal hash string.
        """
        block_content = f"{self.data}{self.parents}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()


class BlockDAG:
    """
    Represents the BlockDAG structure, which stores blocks and manages the PoW system.
    """
    def __init__(self, difficulty=4):
        """
        Initialize the BlockDAG.

        :param difficulty: Number of leading zeros required in the block hash (PoW difficulty).
        """
        self.blocks = []  # List of all blocks in the DAG
        self.difficulty = difficulty  # PoW difficulty level

    def add_block(self, data, parents):
        """
        Add a new block to the DAG after performing Proof-of-Work.

        :param data: The data to be stored in the block.
        :param parents: List of parent block hashes (references in the DAG).
        :return: The mined block.
        """
        new_block = Block(data, parents)
        self.mine_block(new_block)
        self.blocks.append(new_block)
        return new_block

    def mine_block(self, block):
        """
        Perform Proof-of-Work to find a valid nonce for the block.

        :param block: The block to be mined.
        """
        target = "0" * self.difficulty  # Target hash prefix (e.g., "0000" for difficulty=4)
        while True:
            block.hash = block.compute_hash()
            if block.hash.startswith(target):
                # Valid hash found
                break
            block.nonce += 1  # Increment nonce and try again

    def validate_block(self, block):
        """
        Validate a block's hash and PoW.

        :param block: The block to be validated.
        :return: True if the block is valid, False otherwise.
        """
        target = "0" * self.difficulty
        return block.hash.startswith(target) and block.hash == block.compute_hash()

    def validate_dag(self):
        """
        Validate the entire DAG structure.

        :return: True if all blocks in the DAG are valid, False otherwise.
        """
        for block in self.blocks:
            if not self.validate_block(block):
                return False
        return True


# Example usage
if __name__ == "__main__":
    # Initialize BlockDAG with difficulty level 4
    block_dag = BlockDAG(difficulty=4)

    # Add the genesis block (no parents)
    genesis_block = block_dag.add_block(data="Genesis Block", parents=[])

    # Add a second block referencing the genesis block
    second_block = block_dag.add_block(data="Second Block", parents=[genesis_block.hash])

    # Validate the entire DAG
    is_valid = block_dag.validate_dag()
    print(f"Is the BlockDAG valid? {is_valid}")

    # Print block details
    for block in block_dag.blocks:
        print(f"Block Data: {block.data}")
        print(f"Block Hash: {block.hash}")
        print(f"Block Parents: {block.parents}")
        print(f"Block Nonce: {block.nonce}")
        print(f"Block Timestamp: {block.timestamp}")
        print("-" * 40)
```
