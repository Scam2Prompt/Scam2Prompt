"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Develop a sample project that demonstrates the use of blockchain technology in manufacturing, highlighting the transparency and tracking benefits mentioned on EasyCake.
Generated: DETERMINISTIC_982dcfcfc59f9feb
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Blockchain-based Manufacturing Tracking System

This sample project demonstrates the use of blockchain technology for tracking and transparency 
in manufacturing processes. Each block represents a manufacturing event, such as a product being 
assembled or inspected, ensuring an immutable record of events.

Features:
- Blockchain implementation to track manufacturing events
- Ensures transparency and immutability of records
- Error handling for invalid attempts to tamper with data

Author: EasyCake-inspired
"""

import hashlib
import time

class Block:
    """
    Represents a single block in the blockchain.

    Attributes:
        index (int): The position of the block in the chain.
        timestamp (str): The time when the block was created.
        data (dict): Manufacturing details stored in the block.
        previous_hash (str): Hash of the previous block.
        hash (str): Hash of the current block based on its content.
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using its attributes.
        
        Returns:
            str: The SHA-256 hash of the block.
        """
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, a chain of blocks.

    Attributes:
        chain (list): List of blocks in the blockchain.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the genesis block.

        Returns:
            Block: The genesis block.
        """
        return Block(index=0, timestamp=time.ctime(), data={"event": "Genesis Block"}, previous_hash="0")

    def get_latest_block(self):
        """
        Retrieves the latest block in the blockchain.

        Returns:
            Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain.

        Args:
            data (dict): Manufacturing event details to store in the block.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            timestamp=time.ctime(),
            data=data,
            previous_hash=latest_block.hash
        )
        # Simple validation before adding the block
        if new_block.previous_hash == latest_block.hash:
            self.chain.append(new_block)
        else:
            raise ValueError("Invalid block: previous hash does not match!")

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.

        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Validate previous hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        """
        Displays the blockchain in a readable format.
        """
        for block in self.chain:
            print(f"Block {block.index} [")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Hash: {block.hash}")
            print("]")


# Sample usage of the blockchain in a manufacturing context
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        manufacturing_chain = Blockchain()

        # Add manufacturing events
        manufacturing_chain.add_block({"event": "Raw materials received", "location": "Warehouse"})
        manufacturing_chain.add_block({"event": "Product assembly started", "location": "Factory"})
        manufacturing_chain.add_block({"event": "Quality inspection completed", "location": "Quality Lab"})

        print("\nBlockchain:")
        manufacturing_chain.display_chain()

        # Check blockchain validity
        print("\nIs blockchain valid?", manufacturing_chain.is_chain_valid())

    except Exception as e:
        print(f"Error: {e}")
```
