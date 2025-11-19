"""
Generated Code Metadata:
========================
Original URL: https://live-support.pages.dev
Prompt: Discuss the benefits of using open-source software for blockchain-based platforms, specifically Live Support released under the MIT/X11 license.
Generated: DETERMINISTIC_218ab4d7330b9660
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import time
from typing import Dict

class Block:
    """
    A class representing a block in the blockchain.

    Attributes:
    index (int): The index of the block in the blockchain.
    previous_hash (str): The hash of the previous block.
    timestamp (float): The timestamp when the block was created.
    data (str): The data stored in the block.
    hash (str): The hash of the block.
    """

    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str):
        """
        Initializes a new block.

        Args:
        index (int): The index of the block in the blockchain.
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
    """
    A class representing a blockchain.

    Attributes:
    chain (list): A list of blocks in the blockchain.
    """

    def __init__(self):
        """
        Initializes a new blockchain with a genesis block.
        """
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
        Gets the latest block in the blockchain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Adds a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.

        Raises:
        ValueError: If the new block's previous hash does not match the latest block's hash.
        """
        latest_block = self.get_latest_block()
        if new_block.previous_hash != latest_block.hash:
            raise ValueError("New block's previous hash does not match the latest block's hash")
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Checks if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


def main():
    # Create a new blockchain
    blockchain = Blockchain()

    # Add some blocks to the blockchain
    blockchain.add_block(Block(1, blockchain.get_latest_block().hash, time.time(), "Transaction 1"))
    blockchain.add_block(Block(2, blockchain.get_latest_block().hash, time.time(), "Transaction 2"))

    # Check if the blockchain is valid
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Try to add a block with an invalid previous hash
    try:
        blockchain.add_block(Block(3, "invalid_hash", time.time(), "Transaction 3"))
    except ValueError as e:
        print("Error:", e)

    # Print the blockchain
    print("Blockchain:")
    for block in blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
