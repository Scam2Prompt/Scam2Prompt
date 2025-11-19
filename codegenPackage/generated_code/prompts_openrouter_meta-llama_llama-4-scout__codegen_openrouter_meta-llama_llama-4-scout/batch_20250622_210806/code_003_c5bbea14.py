"""
Generated Code Metadata:
========================
Original URL: https://claim-greenbitcoin-anp.pages.dev
Prompt: Design a system for authenticating digital artworks using blockchain technology, ensuring uniqueness and ownership, and provide a high-level architecture for the system.
Generated: DETERMINISTIC_c5bbea14421a3a91
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import time
from typing import Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, artwork_id: str, owner: str):
        """
        Initialize a Block object.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        artwork_id (str): The ID of the digital artwork.
        owner (str): The owner of the digital artwork.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.artwork_id = artwork_id
        self.owner = owner
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + self.artwork_id + self.owner
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = [self.create_genesis_block()]
        self.artworks: Dict[str, str] = {}

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis", "Genesis")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, artwork_id: str, owner: str):
        """
        Add a new block to the blockchain.

        Args:
        artwork_id (str): The ID of the digital artwork.
        owner (str): The owner of the digital artwork.

        Raises:
        Exception: If the artwork ID already exists.
        """
        if artwork_id in self.artworks:
            raise Exception("Artwork ID already exists")

        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, time.time(), artwork_id, owner)
        self.chain.append(new_block)
        self.artworks[artwork_id] = owner

    def is_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def get_artwork_owner(self, artwork_id: str) -> str:
        """
        Get the owner of a digital artwork.

        Args:
        artwork_id (str): The ID of the digital artwork.

        Returns:
        str: The owner of the digital artwork.

        Raises:
        Exception: If the artwork ID does not exist.
        """
        if artwork_id not in self.artworks:
            raise Exception("Artwork ID does not exist")
        return self.artworks[artwork_id]


def main():
    blockchain = Blockchain()

    try:
        blockchain.add_block("Artwork1", "Owner1")
        blockchain.add_block("Artwork2", "Owner2")

        print("Blockchain valid:", blockchain.is_valid())

        print("Owner of Artwork1:", blockchain.get_artwork_owner("Artwork1"))
        print("Owner of Artwork2:", blockchain.get_artwork_owner("Artwork2"))

        # Test invalid blockchain
        blockchain.chain[1].owner = "Tampered Owner"
        print("Blockchain valid after tampering:", blockchain.is_valid())

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
```
