"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Write Python code to simulate a blockchain system using blocks and hashes, incorporating the principles explained on the "블록과 해시" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_d3046ee54b3c10fa
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
from typing import List, Dict, Any

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, hash_value: str):
        """
        Initialize a new Block.
        
        :param index: Block index in the chain
        :param previous_hash: Hash of the previous block
        :param timestamp: Time when the block was created
        :param data: Data stored in the block
        :param hash_value: Hash of this block
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash_value = hash_value

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash_value})"

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain (genesis block)."""
        genesis_block = Block(0, "0", time.time(), "Genesis Block", self.hash_block(0, "0", time.time(), "Genesis Block"))
        self.chain.append(genesis_block)

    def hash_block(self, index: int, previous_hash: str, timestamp: float, data: Any) -> str:
        """
        Generate a SHA-256 hash of a block.
        
        :param index: Block index in the chain
        :param previous_hash: Hash of the previous block
        :param timestamp: Time when the block was created
        :param data: Data stored in the block
        :return: SHA-256 hash of the block
        """
        block_string = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_block(self, data: Any) -> None:
        """
        Add a new block to the blockchain.
        
        :param data: Data to be stored in the new block
        """
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        previous_hash = previous_block.hash_value
        
        # Create the new block
        new_block = Block(index, previous_hash, timestamp, data, self.hash_block(index, previous_hash, timestamp, data))
        self.chain.append(new_block)

    def get_chain(self) -> List[Dict[str, Any]]:
        """
        Retrieve the blockchain as a list of dictionaries.
        
        :return: List of blocks represented as dictionaries
        """
        return [block.__dict__ for block in self.chain]

# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()
    
    # Add some blocks
    blockchain.add_block("First block data")
    blockchain.add_block("Second block data")
    
    # Print the blockchain
    for block in blockchain.get_chain():
        print(block)
```
