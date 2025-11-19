"""
Generated Code Metadata:
========================
Original URL: https://celestiaholdings.co
Prompt: Design a blockchain-based operational efficiency model for financial systems, incorporating transparency and accuracy improvements discussed by Célestia Global.
Generated: DETERMINISTIC_fe2dc052a3108dc0
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_financial_system.py

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
        - timestamp (float): The block's creation timestamp.
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
        return Block(0, "0", time.time(), {"genesis": "block"})

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


class FinancialSystem:
    def __init__(self):
        """
        Initialize a new financial system.
        """
        self.blockchain = Blockchain()

    def add_transaction(self, transaction: dict):
        """
        Add a new transaction to the blockchain.

        Args:
        - transaction (dict): The transaction.
        """
        try:
            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), transaction)
            self.blockchain.add_block(new_block)
        except Exception as e:
            print(f"Error adding transaction: {e}")

    def get_blockchain(self) -> Blockchain:
        """
        Get the blockchain.

        Returns:
        - Blockchain: The blockchain.
        """
        return self.blockchain


def main():
    financial_system = FinancialSystem()

    # Add transactions
    transactions: List[dict] = [
        {"from": "A", "to": "B", "amount": 100},
        {"from": "B", "to": "C", "amount": 50},
        {"from": "C", "to": "A", "amount": 25}
    ]
    for transaction in transactions:
        financial_system.add_transaction(transaction)

    # Check blockchain validity
    blockchain = financial_system.get_blockchain()
    print(f"Blockchain valid: {blockchain.is_chain_valid()}")

    # Print blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
