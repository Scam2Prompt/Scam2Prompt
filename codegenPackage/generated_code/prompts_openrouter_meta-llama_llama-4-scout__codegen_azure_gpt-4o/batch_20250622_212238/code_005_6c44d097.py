"""
Generated Code Metadata:
========================
Original URL: https://monad.at
Prompt: "Explain how Monad's low hardware requirements and MonadDB enable scalable decentralization for a large-scale blockchain network."
Generated: DETERMINISTIC_6c44d09758866d8b
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python code snippet that simulates the concept of low hardware requirements and a lightweight database (MonadDB) enabling scalable decentralization for a large-scale blockchain network. The code is well-documented and adheres to best practices.

```python
import hashlib
import json
import time
from typing import List, Optional


class Block:
    """
    Represents a single block in the blockchain.
    """

    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict, nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using its contents.
        """
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash})"


class MonadDB:
    """
    A lightweight in-memory database to store blockchain data.
    Simulates low hardware requirements by keeping the database simple and efficient.
    """

    def __init__(self):
        self.storage = {}

    def save_block(self, block: Block):
        """
        Saves a block to the database.
        """
        self.storage[block.index] = block

    def get_block(self, index: int) -> Optional[Block]:
        """
        Retrieves a block by its index.
        """
        return self.storage.get(index)

    def get_latest_block(self) -> Optional[Block]:
        """
        Retrieves the latest block in the database.
        """
        if not self.storage:
            return None
        return self.storage[max(self.storage.keys())]


class Blockchain:
    """
    Represents the blockchain, enabling scalable decentralization.
    """

    def __init__(self):
        self.db = MonadDB()
        self.difficulty = 2  # Adjustable difficulty for proof-of-work
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain.
        """
        genesis_block = Block(0, "0", time.time(), {"message": "Genesis Block"})
        self.db.save_block(genesis_block)

    def get_latest_block(self) -> Block:
        """
        Retrieves the latest block in the blockchain.
        """
        return self.db.get_latest_block()

    def add_block(self, data: dict):
        """
        Adds a new block to the blockchain after mining it.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            timestamp=time.time(),
            data=data
        )
        self.mine_block(new_block)
        self.db.save_block(new_block)

    def mine_block(self, block: Block):
        """
        Mines a block by finding a hash that satisfies the difficulty level.
        """
        print(f"Mining block {block.index}...")
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Block {block.index} mined with hash: {block.hash}")

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for index in range(1, len(self.db.storage)):
            current_block = self.db.get_block(index)
            previous_block = self.db.get_block(index - 1)

            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has been tampered with!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} has an invalid previous hash!")
                return False

        return True


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add blocks to the blockchain
    blockchain.add_block({"transaction": "Alice pays Bob 10 tokens"})
    blockchain.add_block({"transaction": "Bob pays Charlie 5 tokens"})

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Print the blockchain
    for index in range(len(blockchain.db.storage)):
        print(blockchain.db.get_block(index))
```

This code demonstrates a lightweight blockchain implementation with a simple in-memory database (`MonadDB`) to simulate low hardware requirements. It includes features like block mining, chain validation, and block storage, all while adhering to best practices.
