"""
Generated Code Metadata:
========================
Original URL: https://dexmultichains.co
Prompt: "Design a blockchain architecture for a futuristic city like Utopos, including data storage and security features."
Generated: DETERMINISTIC_fdd92f9f5b1dbeb1
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain.py

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
        """Calculates the hash of the block."""
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """Represents the blockchain."""
    
    def __init__(self):
        """Initializes a new blockchain."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the genesis block."""
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """Gets the latest block in the chain."""
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """Adds a new block to the chain."""
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Checks if the chain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class UtoposBlockchain(Blockchain):
    """Represents the blockchain for the city of Utopos."""
    
    def __init__(self):
        """Initializes a new Utopos blockchain."""
        super().__init__()
        self.data_storage = {}

    def add_data(self, key: str, value: str):
        """Adds data to the blockchain."""
        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), {key: value})
        self.add_block(new_block)
        self.data_storage[key] = value

    def get_data(self, key: str) -> str:
        """Gets data from the blockchain."""
        return self.data_storage.get(key)

    def update_data(self, key: str, value: str):
        """Updates data in the blockchain."""
        if key in self.data_storage:
            self.data_storage[key] = value
            new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), {key: value})
            self.chain.pop()
            self.add_block(new_block)
        else:
            raise ValueError("Key not found")

    def delete_data(self, key: str):
        """Deletes data from the blockchain."""
        if key in self.data_storage:
            del self.data_storage[key]
            self.chain.pop()
        else:
            raise ValueError("Key not found")


def main():
    utopos_blockchain = UtoposBlockchain()
    utopos_blockchain.add_data("city_population", "1000000")
    utopos_blockchain.add_data("city_area", "1000 km^2")

    print("Blockchain valid:", utopos_blockchain.is_chain_valid())
    print("City population:", utopos_blockchain.get_data("city_population"))
    print("City area:", utopos_blockchain.get_data("city_area"))

    utopos_blockchain.update_data("city_population", "1500000")
    print("Updated city population:", utopos_blockchain.get_data("city_population"))

    utopos_blockchain.delete_data("city_area")
    try:
        print(utopos_blockchain.get_data("city_area"))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
