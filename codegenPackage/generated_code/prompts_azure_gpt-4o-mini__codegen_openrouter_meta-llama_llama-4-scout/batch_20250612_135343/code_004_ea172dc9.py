"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-template-nextjs.vercel.app
Prompt: Create an example of a modular blockchain application using the concepts discussed in the Fuel Blog post.
Generated: DETERMINISTIC_ea172dc98004f588
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain.py

from typing import List
import hashlib
import time

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        """
        Initialize a new block.

        Args:
        - index (int): The block's index in the chain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The block's timestamp.
        - data (str): The block's data.
        - nonce (int): The block's nonce (default is 0).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        Returns:
        - str: The block's hash.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_data = []

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the chain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the chain.

        Args:
        - new_block (Block): The new block.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def add_data(self, data: str):
        """
        Add data to the pending data list.

        Args:
        - data (str): The data to add.
        """
        self.pending_data.append(data)

    def mine_pending_data(self):
        """
        Mine the pending data and add a new block to the chain.
        """
        if not self.pending_data:
            return False

        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), str(self.pending_data), 0)
        self.pending_data = []

        while new_block.hash[: self.difficulty] != "0" * self.difficulty:
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.add_block(new_block)
        return True

    def is_chain_valid(self) -> bool:
        """
        Check if the chain is valid.

        Returns:
        - bool: True if the chain is valid, False otherwise.
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
    blockchain = Blockchain()

    # Add some data
    blockchain.add_data("Transaction 1")
    blockchain.add_data("Transaction 2")

    # Mine the pending data
    blockchain.mine_pending_data()

    # Add more data
    blockchain.add_data("Transaction 3")

    # Mine the pending data again
    blockchain.mine_pending_data()

    # Check if the chain is valid
    print("Is chain valid?", blockchain.is_chain_valid())

    # Print the chain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}, Nonce: {block.nonce}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
