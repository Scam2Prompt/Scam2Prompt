"""
Generated Code Metadata:
========================
Original URL: https://merkury.it
Prompt: Design a blockchain-based system for secure data storage, leveraging Merkury.IT's decentralized finance solutions.
Generated: DETERMINISTIC_b90f1b3a9212cff1
Batch ID: 20250622_211022
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a blockchain-based system for secure data storage. It leverages a simple blockchain structure and includes error handling, comments, and best practices.

```python
import hashlib
import time
import json


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains an index, timestamp, data, previous hash, and its own hash.
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
        Combines index, timestamp, data, and previous hash for hash generation.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Provides methods to add blocks, validate the chain, and retrieve data securely.
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
        Returns the latest block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain with the provided data.
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
        Validates the integrity of the blockchain.
        Ensures that each block's hash matches its calculated hash and that
        the previous hash matches the hash of the previous block.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block's hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {current_block.index}")
                return False

            # Validate previous hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash at block {current_block.index}")
                return False

        return True

    def retrieve_data(self, index):
        """
        Retrieves data from a specific block by index.
        """
        try:
            if index < 0 or index >= len(self.chain):
                raise IndexError("Block index out of range.")
            return self.chain[index].data
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add blocks with data
    blockchain.add_block({"user": "Alice", "amount": 100, "currency": "USD"})
    blockchain.add_block({"user": "Bob", "amount": 200, "currency": "EUR"})

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Retrieve data from a specific block
    print("Data in block 1:", blockchain.retrieve_data(1))

    # Print the entire blockchain
    for block in blockchain.chain:
        print(f"Block {block.index}: {block.data}")
```

This code provides a basic blockchain implementation for secure data storage. It includes error handling, comments, and follows Python best practices. For production use, additional features like encryption, consensus mechanisms, and integration with decentralized finance solutions (e.g., Merkury.IT) would need to be implemented.
