"""
Generated Code Metadata:
========================
Original URL: https://spacecoin.online
Prompt: "Generate a basic blockchain structure using Python for a new cryptocurrency like Spacecoin."
Generated: DETERMINISTIC_e59f5eba7d2b7ba1
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from typing import List, Dict, Any

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return f"Block(index={self.index}, hash='{self.hash}', previous_hash='{self.previous_hash}', timestamp={self.timestamp}, data={self.data})"

class Blockchain:
    """
    Represents the entire blockchain.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the genesis block.
        """
        genesis_block = Block(0, "0", time.time(), "Genesis Block", self.hash_block(0, "0", time.time(), "Genesis Block"))
        self.chain.append(genesis_block)

    def hash_block(self, index: int, previous_hash: str, timestamp: float, data: Any) -> str:
        """
        Creates a SHA-256 hash of a block.
        """
        block_string = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_block(self, data: Any):
        """
        Adds a new block to the blockchain.
        """
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        hash = self.hash_block(index, previous_block.hash, timestamp, data)
        new_block = Block(index, previous_block.hash, timestamp, data, hash)
        self.chain.append(new_block)

    def get_chain(self) -> List[Dict[str, Any]]:
        """
        Returns the blockchain as a list of dictionaries for easier viewing.
        """
        return [block.__dict__ for block in self.chain]

# Example usage
if __name__ == "__main__":
    try:
        # Create a new blockchain
        spacecoin_chain = Blockchain()

        # Add some blocks to the blockchain
        spacecoin_chain.add_block("Transaction 1: Alice pays Bob 10 Spacecoins")
        spacecoin_chain.add_block("Transaction 2: Bob pays Charlie 5 Spacecoins")

        # Print the blockchain
        for block in spacecoin_chain.get_chain():
            print(block)

    except Exception as e:
        print(f"An error occurred: {e}")
```
