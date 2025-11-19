"""
Generated Code Metadata:
========================
Original URL: https://efhenna.org
Prompt: Describe how to create an eco-friendly cryptocurrency initiative inspired by the sustainable practices of Ethena.fi.
Generated: DETERMINISTIC_c9903ee528542fb4
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# eco_friendly_crypto.py

"""
Eco-friendly cryptocurrency initiative inspired by Ethena.fi's sustainable practices.

This script simulates a basic eco-friendly cryptocurrency system, 
focusing on energy-efficient transactions and carbon offsetting.
"""

import hashlib
import time
from typing import Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 transactions: list, carbon_offset: float):
        """
        Initialize a new block.

        Args:
        - index (int): Block index.
        - previous_hash (str): Previous block's hash.
        - timestamp (float): Block creation timestamp.
        - transactions (list): List of transactions.
        - carbon_offset (float): Carbon offset for this block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.carbon_offset = carbon_offset
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        Returns:
        - str: Block hash.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.transactions) + str(self.carbon_offset)
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: Genesis block.
        """
        return Block(0, "0", time.time(), [], 0.0)

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the chain.

        Returns:
        - Block: Latest block.
        """
        return self.chain[-1]

    def add_transaction(self, transaction: str):
        """
        Add a transaction to the pending transactions.

        Args:
        - transaction (str): Transaction to add.
        """
        self.pending_transactions.append(transaction)

    def mine_block(self, miner: str, carbon_offset: float) -> Block:
        """
        Mine a new block.

        Args:
        - miner (str): Miner address.
        - carbon_offset (float): Carbon offset for this block.

        Returns:
        - Block: New block.
        """
        if not self.pending_transactions:
            raise Exception("No transactions to mine")

        new_block_index = self.get_latest_block().index + 1
        new_block_timestamp = time.time()
        new_block = Block(new_block_index, self.get_latest_block().hash, new_block_timestamp, 
                           self.pending_transactions, carbon_offset)
        self.chain.append(new_block)
        self.pending_transactions = []

        # Reward the miner
        self.add_transaction(f"Miner reward: {miner}")

        return new_block

    def is_chain_valid(self) -> bool:
        """
        Check if the chain is valid.

        Returns:
        - bool: Chain validity.
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
    eco_chain = Blockchain()

    # Add some transactions
    eco_chain.add_transaction("Transaction 1: Alice -> Bob")
    eco_chain.add_transaction("Transaction 2: Bob -> Charlie")

    # Mine a new block with carbon offset
    new_block = eco_chain.mine_block("Miner1", 10.0)

    # Print the block details
    print(f"Block {new_block.index} Hash: {new_block.hash}")
    print(f"Timestamp: {new_block.timestamp}")
    print(f"Transactions: {new_block.transactions}")
    print(f"Carbon Offset: {new_block.carbon_offset}")

    # Check chain validity
    print(f"Is chain valid? {eco_chain.is_chain_valid()}")


if __name__ == "__main__":
    main()
```
