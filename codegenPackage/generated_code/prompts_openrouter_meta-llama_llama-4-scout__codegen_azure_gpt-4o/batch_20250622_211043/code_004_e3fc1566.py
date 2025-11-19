"""
Generated Code Metadata:
========================
Original URL: https://celestiaholdings.co
Prompt: "Design a blockchain-based system for global trade and commerce to enhance data security and operational efficiency."
Generated: DETERMINISTIC_e3fc1566765c3a39
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a simplified blockchain-based system for global trade and commerce. It includes error handling, comments, and follows best practices.

```python
import hashlib
import time
import json


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains:
    - Index: Position in the chain
    - Timestamp: Time of creation
    - Data: Trade and commerce transaction details
    - Previous Hash: Hash of the previous block
    - Hash: Hash of the current block
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
        Combines index, timestamp, data, and previous hash for hashing.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Provides methods to add blocks, validate the chain, and retrieve data.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (Genesis Block).
        """
        return Block(0, time.time(), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        Validates the previous hash and calculates the hash for the new block.
        """
        try:
            latest_block = self.get_latest_block()
            new_block = Block(
                index=latest_block.index + 1,
                timestamp=time.time(),
                data=data,
                previous_hash=latest_block.hash,
            )
            self.chain.append(new_block)
        except Exception as e:
            print(f"Error adding block: {e}")

    def is_chain_valid(self):
        """
        Validates the blockchain by checking hashes and previous hashes.
        Ensures data integrity and security.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                print("Invalid block hash detected!")
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash detected!")
                return False

        return True

    def display_chain(self):
        """
        Displays the entire blockchain in a readable format.
        """
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {time.ctime(block.timestamp)}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 50)


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    trade_blockchain = Blockchain()

    # Add trade transactions to the blockchain
    trade_blockchain.add_block({"sender": "Country A", "receiver": "Country B", "goods": "Electronics", "value": 100000})
    trade_blockchain.add_block({"sender": "Country C", "receiver": "Country D", "goods": "Agriculture", "value": 50000})

    # Display the blockchain
    trade_blockchain.display_chain()

    # Validate the blockchain
    if trade_blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")
```

This code provides a basic blockchain implementation suitable for trade and commerce transactions. It includes error handling, comments, and adheres to best practices.
