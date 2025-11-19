"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-bitcoin.org
Prompt: Explain how Bitcoin Core achieves consensus among users without voting, and provide an example of how this can be implemented in a decentralized application.
Generated: DETERMINISTIC_ac6dd3d74fa93559
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Bitcoin Consensus Mechanism and Decentralized Application Example

This script demonstrates a simplified version of how Bitcoin achieves consensus 
among users in a decentralized manner without formal voting. It simulates a 
blockchain and the process of adding new blocks based on the longest chain rule.

This example doesn't implement actual mining or cryptographic verification, 
but serves as a basic illustration of how consensus can be achieved in a 
decentralized application (dApp).

Note: This code is for educational purposes only and should not be used in a 
production environment without significant enhancements and security measures.
"""

import hashlib
import time
from typing import List

class Block:
    """Class representing a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, hash: str):
        self.index = index                  # Block index
        self.previous_hash = previous_hash  # Hash of the previous block
        self.timestamp = timestamp          # Block creation time
        self.data = data                    # Data stored in the block
        self.hash = hash                    # Current block hash

    @staticmethod
    def calculate_hash(index: int, previous_hash: str, timestamp: float, data: str) -> str:
        """Calculates the hash of a block."""
        value = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(value).hexdigest()

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []       # List to store the blockchain
        self.create_block(previous_hash='0')  # Create the genesis block

    def create_block(self, data: str, previous_hash: str = '') -> Block:
        """Creates and adds a new block to the blockchain."""
        index = len(self.chain) + 1
        timestamp = time.time()
        hash = Block.calculate_hash(index, previous_hash, timestamp, data)
        new_block = Block(index, previous_hash, timestamp, data, hash)
        self.chain.append(new_block)
        return new_block

    def get_latest_block(self) -> Block:
        """Returns the latest block in the blockchain."""
        return self.chain[-1]

    def print_chain(self):
        """Prints the entire blockchain."""
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Hash: {block.hash}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}\n")

# Example usage

def main():
    """Main function to demonstrate blockchain creation and consensus."""
    try:
        # Create a new blockchain
        my_blockchain = Blockchain()
        
        # Add blocks to the blockchain
        my_blockchain.create_block(data="First block data")
        my_blockchain.create_block(data="Second block data")
        my_blockchain.create_block(data="Third block data")
        
        # Print the blockchain
        my_blockchain.print_chain()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
