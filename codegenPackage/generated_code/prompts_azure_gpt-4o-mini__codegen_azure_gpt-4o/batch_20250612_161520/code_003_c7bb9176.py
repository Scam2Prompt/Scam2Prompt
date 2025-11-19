"""
Generated Code Metadata:
========================
Original URL: https://planetserfi.pages.dev
Prompt: Generate an example of how to implement blockchain technology to address one of the Sustainable Development Goals (SDGs) mentioned on the PLANET website.
Generated: DETERMINISTIC_c7bb917620b6626d
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Example implementation of blockchain technology to address SDG #12: Responsible Consumption and Production.
This code demonstrates a simplified blockchain-based system for tracking the provenance of sustainable products.
"""

import hashlib
import time


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains data, a timestamp, the hash of the previous block, and its own hash.
    """

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # Position of the block in the chain
        self.timestamp = timestamp  # Time when the block was created
        self.data = data  # Data stored in the block (e.g., product details)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calculate_hash()  # Hash of the current block

    def calculate_hash(self):
        """
        Calculates the hash of the block using its contents.
        """
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize the chain with the genesis block

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Returns the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain with the given data.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        Ensures that the hashes and previous hashes are consistent.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Example usage: Tracking sustainable product provenance
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        sustainable_chain = Blockchain()

        # Add blocks with product data
        sustainable_chain.add_block({
            "product_id": "12345",
            "name": "Organic Cotton T-Shirt",
            "manufacturer": "EcoWear Inc.",
            "certifications": ["Fair Trade", "GOTS"],
            "timestamp": time.time()
        })

        sustainable_chain.add_block({
            "product_id": "67890",
            "name": "Recycled Plastic Shoes",
            "manufacturer": "GreenSteps Co.",
            "certifications": ["Recycled Materials", "Carbon Neutral"],
            "timestamp": time.time()
        })

        # Validate the blockchain
        print("Blockchain valid:", sustainable_chain.is_chain_valid())

        # Print the blockchain
        for block in sustainable_chain.chain:
            print(f"Block {block.index}: {block.data}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
