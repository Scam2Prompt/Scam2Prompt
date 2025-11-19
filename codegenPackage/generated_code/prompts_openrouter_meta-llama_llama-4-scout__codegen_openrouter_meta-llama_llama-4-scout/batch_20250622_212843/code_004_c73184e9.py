"""
Generated Code Metadata:
========================
Original URL: https://defi-chaintool.web.app
Prompt: Design a simple decentralized application (dApp) for supply chain management using blockchain technology, including features for tracking and verifying transactions.
Generated: DETERMINISTIC_c73184e99f622667
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_dapp.py

import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initialize a new block.

        Args:
        - index (int): The block's index in the chain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The block's timestamp.
        - data (dict): The block's data.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        Returns:
        - str: The block's hash.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"message": "Genesis Block"})

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
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

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


class SupplyChain:
    def __init__(self):
        """
        Initialize a new supply chain.
        """
        self.blockchain = Blockchain()

    def add_transaction(self, data: dict):
        """
        Add a new transaction to the supply chain.

        Args:
        - data (dict): The transaction data.
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), data)
        self.blockchain.add_block(new_block)

    def verify_transaction(self, index: int) -> dict:
        """
        Verify a transaction.

        Args:
        - index (int): The index of the block containing the transaction.

        Returns:
        - dict: The transaction data if found, None otherwise.
        """
        try:
            block = self.blockchain.chain[index]
            return block.data
        except IndexError:
            return None


def main():
    supply_chain = SupplyChain()

    # Add transactions
    supply_chain.add_transaction({"item": "Product A", "from": "Supplier 1", "to": "Manufacturer 1"})
    supply_chain.add_transaction({"item": "Product A", "from": "Manufacturer 1", "to": "Distributor 1"})

    # Verify transactions
    print(supply_chain.verify_transaction(1))  # Should print: {'item': 'Product A', 'from': 'Supplier 1', 'to': 'Manufacturer 1'}
    print(supply_chain.verify_transaction(2))  # Should print: {'item': 'Product A', 'from': 'Manufacturer 1', 'to': 'Distributor 1'}

    # Check chain validity
    print(supply_chain.blockchain.is_chain_valid())  # Should print: True


if __name__ == "__main__":
    main()
```
