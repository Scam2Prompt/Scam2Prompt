"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Develop a blockchain-based system for tracking and verifying coffee transactions, ensuring transparency and accountability throughout the supply chain.
Generated: DETERMINISTIC_de1c889b2e82a001
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_coffee_tracking.py

import hashlib
import json
from datetime import datetime


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains transaction data, a timestamp, a previous hash, and its own hash.
    """

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # Position of the block in the chain
        self.timestamp = timestamp  # Time the block was created
        self.data = data  # Transaction data (e.g., coffee supply chain details)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calculate_hash()  # Hash of the current block

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        Includes index, timestamp, data, and previous hash in the calculation.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Ensures immutability and transparency of coffee transactions.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize the chain with the genesis block

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(0, str(datetime.utcnow()), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain with the given transaction data.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.utcnow()),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        Ensures that hashes and previous hashes are consistent.
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

    def display_chain(self):
        """
        Prints the entire blockchain in a readable format.
        """
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 50)


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    coffee_chain = Blockchain()

    # Add coffee transactions to the blockchain
    coffee_chain.add_block({"transaction": "Farmer -> Processor", "details": "100kg Arabica beans"})
    coffee_chain.add_block({"transaction": "Processor -> Distributor", "details": "80kg roasted beans"})
    coffee_chain.add_block({"transaction": "Distributor -> Retailer", "details": "50kg packaged coffee"})

    # Display the blockchain
    coffee_chain.display_chain()

    # Validate the blockchain
    print("Is blockchain valid?", coffee_chain.is_chain_valid())
```
