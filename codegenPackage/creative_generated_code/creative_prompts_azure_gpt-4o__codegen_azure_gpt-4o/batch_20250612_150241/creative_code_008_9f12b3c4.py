"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amlwd.com
Prompt: Explain how blockchain technology can be used to create trust and value representation in cross-industry collaborations, as highlighted on https://amlwd.com.
Generated: DETERMINISTIC_9f12b3c4a4abbad5
Batch ID: 20250612_150241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how blockchain technology can be used to create trust
and value representation in cross-industry collaborations. It utilizes a simple
blockchain implementation to record transactions shared between industries,
ensuring transparency, immutability, and trust.

Requirements:
- Python 3.x
"""

import hashlib
import json
import time
from typing import List, Dict, Any


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains:
    - Index: Position of the block in the chain
    - Timestamp: Time when the block was created
    - Data: Transaction details (cross-industry collaboration)
    - Previous Hash: Hash of the previous block for chaining
    - Current Hash: Hash of the current block
    """

    def __init__(self, index: int, data: Any, previous_hash: str = "0"):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash for the current block using SHA-256.
        Hash includes the index, timestamp, data, and previous hash.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the block to a dictionary for easier serialization and debugging.
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "current_hash": self.current_hash,
        }


class Blockchain:
    """
    Represents the blockchain as a whole.
    Contains methods for adding blocks, validating the chain, and inspecting data.
    """

    def __init__(self):
        # Initialize the blockchain with a genesis block (first block)
        self.chain: List[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the first block in the blockchain (Genesis block).
        The genesis block contains no previous hash or meaningful data.
        """
        return Block(index=0, data="Genesis Block", previous_hash="0")

    def add_block(self, data: Any):
        """
        Add a new block to the blockchain with the given data.
        """
        previous_block = self.chain[-1]
        new_block = Block(index=len(self.chain), data=data, previous_hash=previous_block.current_hash)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validate the blockchain to ensure data integrity.
        Each block should have a correctly calculated hash and match the previous block's hash.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if current block's hash is valid
            if current_block.current_hash != current_block.calculate_hash():
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.current_hash:
                return False

        return True

    def display_chain(self) -> None:
        """
        Print the blockchain to the console for inspection.
        """
        for block in self.chain:
            print(json.dumps(block.to_dict(), indent=4))


# Example Usage
if __name__ == "__main__":
    try:
        # Instantiate the blockchain
        blockchain = Blockchain()

        # Example cross-industry transactions to add
        blockchain.add_block({"industry_a": "Manufacturing", "industry_b": "Healthcare", "value": "Data Sharing Agreement"})
        blockchain.add_block({"industry_a": "Finance", "industry_b": "Retail", "value": "Loyalty Program Integration"})
        blockchain.add_block({"industry_a": "Energy", "industry_b": "Tech", "value": "Renewable Energy Credits"})

        # Display the blockchain
        print("Blockchain:")
        blockchain.display_chain()

        # Validate the blockchain
        if blockchain.is_chain_valid():
            print("\nBlockchain is valid.")
        else:
            print("\nBlockchain is invalid.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
