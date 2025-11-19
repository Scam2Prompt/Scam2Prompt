"""
Generated Code Metadata:
========================
Original URL: https://okexbit.com
Prompt: How can blockchain be used for supply chain management in the chemical industry?
Generated: DETERMINISTIC_2e4278660f9af45b
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Blockchain-based Supply Chain Management for the Chemical Industry

This script demonstrates how blockchain can be used to track and manage the supply chain
of chemicals. It uses a simplified blockchain model to record transactions and ensure
transparency and immutability in the supply chain.

Key Features:
- Add transactions to the blockchain (e.g., chemical production, transportation, storage).
- Verify the integrity of the blockchain.
- Query the blockchain for specific transactions.

Note: This is a simplified implementation for educational purposes and does not include
advanced features like consensus mechanisms or distributed nodes.
"""

import hashlib
import json
from datetime import datetime


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains:
    - Index: Position in the chain.
    - Timestamp: When the block was created.
    - Data: Transaction details (e.g., chemical production, transportation).
    - Previous Hash: Hash of the previous block for chain integrity.
    - Hash: Hash of the current block.
    """

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        Includes index, timestamp, data, and previous hash.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Provides methods to:
    - Add new blocks.
    - Verify the integrity of the chain.
    - Query transactions.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (Genesis Block).
        """
        return Block(0, str(datetime.now()), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        :param data: Transaction details (e.g., chemical production, transportation).
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.now()),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Verifies the integrity of the blockchain.
        Ensures that:
        - Each block's hash matches its calculated hash.
        - Each block's previous hash matches the hash of the previous block.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def query_transactions(self, filter_key, filter_value):
        """
        Queries the blockchain for transactions matching a specific filter.
        :param filter_key: Key to filter by (e.g., "chemical_name").
        :param filter_value: Value to filter by (e.g., "Acetone").
        :return: List of matching transactions.
        """
        matching_transactions = []
        for block in self.chain:
            if filter_key in block.data and block.data[filter_key] == filter_value:
                matching_transactions.append(block.data)
        return matching_transactions


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        chemical_supply_chain = Blockchain()

        # Add transactions to the blockchain
        chemical_supply_chain.add_block({
            "chemical_name": "Acetone",
            "quantity": "100 liters",
            "location": "Factory A",
            "timestamp": str(datetime.now()),
            "status": "Produced"
        })

        chemical_supply_chain.add_block({
            "chemical_name": "Acetone",
            "quantity": "100 liters",
            "location": "Warehouse B",
            "timestamp": str(datetime.now()),
            "status": "Transported"
        })

        chemical_supply_chain.add_block({
            "chemical_name": "Acetone",
            "quantity": "100 liters",
            "location": "Warehouse B",
            "timestamp": str(datetime.now()),
            "status": "Stored"
        })

        # Verify the integrity of the blockchain
        if chemical_supply_chain.is_chain_valid():
            print("Blockchain integrity verified.")
        else:
            print("Blockchain integrity compromised!")

        # Query transactions for a specific chemical
        acetone_transactions = chemical_supply_chain.query_transactions("chemical_name", "Acetone")
        print("Transactions for Acetone:")
        for transaction in acetone_transactions:
            print(transaction)

    except Exception as e:
        print(f"An error occurred: {e}")
```
