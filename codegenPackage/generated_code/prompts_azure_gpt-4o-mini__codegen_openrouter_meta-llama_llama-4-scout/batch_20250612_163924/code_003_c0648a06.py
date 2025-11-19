"""
Generated Code Metadata:
========================
Original URL: https://cryptolinknet.com
Prompt: Create a simple application that demonstrates how blockchain technology improves transparency in supply chains, as described on CryptoLinkNet.
Generated: DETERMINISTIC_c0648a06d078c652
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_supply_chain.py

import hashlib
import time
from typing import List

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initializes a new block.

        Args:
        index (int): The index of the block in the chain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        data (dict): The data stored in the block.
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
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """Represents a blockchain."""
    
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
        return Block(0, "0", time.time(), {"message": "Genesis Block"})

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
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Checks if the chain is valid.

        Returns:
        bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class SupplyChain:
    """Represents a supply chain."""
    
    def __init__(self):
        """
        Initializes a new supply chain with a blockchain.
        """
        self.blockchain = Blockchain()

    def add_transaction(self, data: dict):
        """
        Adds a new transaction to the supply chain.

        Args:
        data (dict): The transaction data.
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), data)
        self.blockchain.add_block(new_block)

    def is_supply_chain_valid(self) -> bool:
        """
        Checks if the supply chain is valid.

        Returns:
        bool: True if the supply chain is valid, False otherwise.
        """
        return self.blockchain.is_chain_valid()


def main():
    # Create a new supply chain
    supply_chain = SupplyChain()

    # Add transactions to the supply chain
    transactions: List[dict] = [
        {"product_id": "123", "supplier": "Supplier A", "quantity": 100},
        {"product_id": "123", "buyer": "Buyer B", "quantity": 50},
        {"product_id": "456", "supplier": "Supplier C", "quantity": 200},
    ]

    for transaction in transactions:
        supply_chain.add_transaction(transaction)

    # Check if the supply chain is valid
    if supply_chain.is_supply_chain_valid():
        print("The supply chain is valid.")
    else:
        print("The supply chain is not valid.")

    # Print the supply chain
    print("Supply Chain:")
    for i, block in enumerate(supply_chain.blockchain.chain):
        print(f"Block {i}:")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
