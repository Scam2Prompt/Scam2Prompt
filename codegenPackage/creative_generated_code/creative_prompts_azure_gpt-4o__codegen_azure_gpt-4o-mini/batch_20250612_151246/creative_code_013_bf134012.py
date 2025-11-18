"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x1blockdag.pages.dev
Prompt: Provide a step-by-step guide to integrate BlockDAG's proof-of-work consensus mechanism into an enterprise-grade DeFi protocol.
Generated: DETERMINISTIC_bf134012cf912944
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import json
from time import time
from typing import List, Dict, Any

# Define a class for a Block
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, hash: str):
        """
        Initialize a new block.

        :param index: Position of the block in the chain
        :param previous_hash: Hash of the previous block
        :param timestamp: Time the block was created
        :param data: Data contained in the block
        :param hash: Hash of the current block
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self) -> Dict[str, Any]:
        """Convert the block to a dictionary."""
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "hash": self.hash
        }

# Define a BlockDAG class
class BlockDAG:
    def __init__(self):
        """
        Initialize a BlockDAG structure with an empty list of blocks and a genesis block.
        """
        self.blocks: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self) -> Block:
        """Create the first block in the BlockDAG."""
        genesis_block = Block(0, "0", time(), "Genesis Block", self.hash_block(0, "0", time(), "Genesis Block"))
        self.blocks.append(genesis_block)

    def hash_block(self, index: int, previous_hash: str, timestamp: float, data: Any) -> str:
        """
        Create a SHA-256 hash of a block.

        :param index: Position of the block
        :param previous_hash: Hash of the previous block
        :param timestamp: Time the block was created
        :param data: Data contained in the block
        :return: Hash string of the block
        """
        block_string = f"{index}{previous_hash}{timestamp}{json.dumps(data)}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_block(self, data: Any) -> None:
        """
        Add a new block to the BlockDAG.

        :param data: The data to store in the new block
        :raises ValueError: If the data provided is invalid
        """
        if not self.is_valid_data(data):
            raise ValueError("Invalid data provided for the block.")
        
        # Get the previous block's hash
        previous_block = self.blocks[-1]
        new_index = previous_block.index + 1
        new_timestamp = time()
        new_hash = self.hash_block(new_index, previous_block.hash, new_timestamp, data)
        
        # Create and append the new block
        new_block = Block(new_index, previous_block.hash, new_timestamp, data, new_hash)
        self.blocks.append(new_block)

    def is_valid_data(self, data: Any) -> bool:
        """
        Validate the data being added to the block.

        :param data: The data to validate
        :return: True if valid, False otherwise
        """
        return isinstance(data, (str, dict))  # Adjust validation as necessary

    def get_chain(self) -> List[Dict[str, Any]]:
        """Return the entire BlockDAG as a list of dictionaries."""
        return [block.to_dict() for block in self.blocks]

# Example usage
if __name__ == "__main__":
    try:
        # Create a new BlockDAG
        block_dag = BlockDAG()
        
        # Add blocks with valid data
        block_dag.add_block({"transaction": "A to B", "amount": 50})
        block_dag.add_block({"transaction": "B to C", "amount": 30})

        # Retrieve and print the entire BlockDAG
        for block in block_dag.get_chain():
            print(block)
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
