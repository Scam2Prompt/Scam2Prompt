"""
Generated Code Metadata:
========================
Original URL: https://j-node.net
Prompt: Write code to simulate validator node interactions on a blockchain testnet, referencing J•Node's focus on community trust.
Generated: DETERMINISTIC_201f7a1c27b637c6
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# validator_node_simulation.py

import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, validator: str):
        """
        Initialize a Block.

        Args:
        - index (int): The block's index in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The block's creation timestamp.
        - data (str): The block's data.
        - validator (str): The validator node that created the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.validator = validator
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        Returns:
        - str: The block's hash.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data + self.validator
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.validators = set()

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis Block", "Genesis Validator")

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block to add.

        Raises:
        - ValueError: If the new block's previous hash does not match the last block's hash.
        """
        if new_block.previous_hash != self.chain[-1].hash:
            raise ValueError("Invalid previous hash")

        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def add_validator(self, validator: str):
        """
        Add a validator node to the set of validators.

        Args:
        - validator (str): The validator node to add.
        """
        self.validators.add(validator)

    def is_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        - bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


class ValidatorNode:
    def __init__(self, name: str, blockchain: Blockchain):
        """
        Initialize a Validator Node.

        Args:
        - name (str): The validator node's name.
        - blockchain (Blockchain): The blockchain the validator node is part of.
        """
        self.name = name
        self.blockchain = blockchain

    def create_block(self, data: str) -> Block:
        """
        Create a new block.

        Args:
        - data (str): The block's data.

        Returns:
        - Block: The new block.
        """
        previous_block = self.blockchain.chain[-1]
        new_block = Block(len(self.blockchain.chain), previous_block.hash, time.time(), data, self.name)
        return new_block

    def add_block_to_chain(self, block: Block):
        """
        Add a block to the blockchain.

        Args:
        - block (Block): The block to add.

        Raises:
        - ValueError: If the block's previous hash does not match the last block's hash.
        """
        try:
            self.blockchain.add_block(block)
        except ValueError as e:
            print(f"Error adding block: {e}")


def main():
    # Create a blockchain
    blockchain = Blockchain()

    # Add validator nodes
    validator_node1 = ValidatorNode("Validator Node 1", blockchain)
    validator_node2 = ValidatorNode("Validator Node 2", blockchain)

    blockchain.add_validator(validator_node1.name)
    blockchain.add_validator(validator_node2.name)

    # Create and add blocks to the blockchain
    block1 = validator_node1.create_block("Transaction 1")
    validator_node1.add_block_to_chain(block1)

    block2 = validator_node2.create_block("Transaction 2")
    validator_node2.add_block_to_chain(block2)

    # Check if the blockchain is valid
    if blockchain.is_valid():
        print("Blockchain is valid")
    else:
        print("Blockchain is not valid")

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Validator: {block.validator}")
        print(f"Data: {block.data}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
