"""
Generated Code Metadata:
========================
Original URL: https://register-doublezero.com
Prompt: Write Python code to simulate a blockchain communication system using a dual-ring architecture, referencing the concepts described in DoubleZero's infrastructure model.
Generated: DETERMINISTIC_3d9eb21fd4e302f4
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from typing import List

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str):
        """
        Initializes a new block.

        Args:
        index (int): The index of the block in the chain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (str): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """Represents a blockchain."""
    
    def __init__(self):
        """Initializes a new blockchain."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Gets the latest block in the chain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Adds a new block to the chain.

        Args:
        new_block (Block): The new block to add.

        Raises:
        ValueError: If the new block is not valid.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


class DualRingArchitecture:
    """Simulates a dual-ring architecture for blockchain communication."""
    
    def __init__(self):
        """Initializes a new dual-ring architecture."""
        self.outer_ring = Blockchain()
        self.inner_ring = Blockchain()

    def add_block_to_outer_ring(self, data: str):
        """
        Adds a new block to the outer ring.

        Args:
        data (str): The data to store in the block.

        Raises:
        ValueError: If the block is not valid.
        """
        new_block = Block(len(self.outer_ring.chain), self.outer_ring.get_latest_block().hash, time.time(), data)
        self.outer_ring.add_block(new_block)

    def add_block_to_inner_ring(self, data: str):
        """
        Adds a new block to the inner ring.

        Args:
        data (str): The data to store in the block.

        Raises:
        ValueError: If the block is not valid.
        """
        new_block = Block(len(self.inner_ring.chain), self.inner_ring.get_latest_block().hash, time.time(), data)
        self.inner_ring.add_block(new_block)

    def validate_chains(self) -> bool:
        """
        Validates both chains.

        Returns:
        bool: True if both chains are valid, False otherwise.
        """
        # Validate outer ring
        for i in range(1, len(self.outer_ring.chain)):
            current_block = self.outer_ring.chain[i]
            previous_block = self.outer_ring.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        # Validate inner ring
        for i in range(1, len(self.inner_ring.chain)):
            current_block = self.inner_ring.chain[i]
            previous_block = self.inner_ring.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


def main():
    # Create a dual-ring architecture
    dual_ring = DualRingArchitecture()

    # Add blocks to outer ring
    dual_ring.add_block_to_outer_ring("Transaction 1")
    dual_ring.add_block_to_outer_ring("Transaction 2")

    # Add blocks to inner ring
    dual_ring.add_block_to_inner_ring("Inner transaction 1")
    dual_ring.add_block_to_inner_ring("Inner transaction 2")

    # Validate chains
    if dual_ring.validate_chains():
        print("Both chains are valid.")
    else:
        print("One or both chains are invalid.")

    # Print chain data
    print("Outer Ring:")
    for block in dual_ring.outer_ring.chain:
        print(f"Block {block.index} - Hash: {block.hash}")

    print("\nInner Ring:")
    for block in dual_ring.inner_ring.chain:
        print(f"Block {block.index} - Hash: {block.hash}")


if __name__ == "__main__":
    main()
```
