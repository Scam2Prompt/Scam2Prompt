"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://midoin.com
Prompt: Develop a blockchain-based solution to track and verify eco-friendly mining efforts for Midoins, ensuring minimal environmental impact.
Generated: DETERMINISTIC_3d1345892989380d
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import time
from typing import List

# Define a class to represent each block in the blockchain
class Block:
    def __init__(self, index: int, timestamp: str, data: dict, previous_hash: str):
        """
        Initialize a block in the blockchain.

        :param index: Position of the block in the chain.
        :param timestamp: Time the block was created.
        :param data: Data stored in the block (e.g., mining effort details).
        :param previous_hash: Hash of the previous block in the chain.
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    def generate_hash(self) -> str:
        """
        Generate a SHA-256 hash for the block.

        :return: Hexadecimal representation of the block's hash.
        """
        block_content = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()


# Define a class to represent the blockchain itself
class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain: List[Block] = []  # List to store the chain of blocks
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first (genesis) block in the blockchain.
        """
        genesis_block = Block(index=0, timestamp=str(time.time()), data={'message': 'Genesis Block'}, previous_hash="0")
        self.chain.append(genesis_block)

    def add_block(self, data: dict):
        """
        Add a new block to the blockchain.

        :param data: Data to be stored in the new block (e.g., eco-friendly mining details).
        """
        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=str(time.time()),
            data=data,
            previous_hash=last_block.hash
        )
        if self.is_block_valid(new_block, last_block):
            self.chain.append(new_block)
        else:
            raise ValueError("Invalid block. Cannot add to the blockchain.")

    def is_block_valid(self, new_block: Block, previous_block: Block) -> bool:
        """
        Validate a new block before adding it to the blockchain.
        
        :param new_block: The block being added.
        :param previous_block: The last block in the chain.
        :return: True if the block is valid; False otherwise.
        """
        if new_block.previous_hash != previous_block.hash:
            return False
        if new_block.index != previous_block.index + 1:
            return False
        if new_block.generate_hash() != new_block.hash:
            return False
        return True

    def is_chain_valid(self) -> bool:
        """
        Verify the integrity of the entire blockchain.

        :return: True if the blockchain is valid; False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if not self.is_block_valid(current_block, previous_block):
                return False
        return True

    def print_chain(self):
        """
        Print the contents of the blockchain for debugging purposes.
        """
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("---------------------------")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        eco_chain = Blockchain()

        # Add eco-friendly mining data to the blockchain
        eco_chain.add_block({"miner": "John Doe", "method": "Solar-powered mining", "impact_score": 10})
        eco_chain.add_block({"miner": "Jane Smith", "method": "Wind-powered mining", "impact_score": 8})

        # Verify the blockchain
        if eco_chain.is_chain_valid():
            print("Blockchain is valid.")
        else:
            print("Blockchain integrity compromised.")

        # Print the blockchain
        eco_chain.print_chain()
    except Exception as e:
        print(f"An error occurred: {e}")
```
