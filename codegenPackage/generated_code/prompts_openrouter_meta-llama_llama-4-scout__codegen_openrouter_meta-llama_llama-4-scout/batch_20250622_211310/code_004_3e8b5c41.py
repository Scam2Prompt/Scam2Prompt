"""
Generated Code Metadata:
========================
Original URL: https://immediate-matrix.net
Prompt: Explain the concept of using blockchain technology to ensure a secure and private trading experience, as mentioned in the Immediate 1.4 Evista platform, and provide a code example that demonstrates this concept.
Generated: DETERMINISTIC_3e8b5c41285cab0c
Batch ID: 20250622_211310
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
from typing import List

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
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """
    A class representing a blockchain.

    Attributes:
    chain (List[Block]): A list of blocks in the blockchain.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

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
    blockchain.add_block(Block(1, blockchain.get_latest_block().hash, time.time(), "Trade 1: User A -> User B"))
    blockchain.add_block(Block(2, blockchain.get_latest_block().hash, time.time(), "Trade 2: User B -> User C"))

    # Check if the blockchain is valid
    if blockchain.is_chain_valid():
        print("The blockchain is valid.")
    else:
        print("The blockchain is not valid.")

    # Try to tamper with the blockchain
    blockchain.chain[1].data = "Tampered trade"

    # Check if the blockchain is still valid
    if blockchain.is_chain_valid():
        print("The blockchain is still valid.")
    else:
        print("The blockchain is not valid.")


if __name__ == "__main__":
    main()
```
