"""
Generated Code Metadata:
========================
Original URL: https://www.art-blocks.site
Prompt: "Design a basic blockchain-based art ownership system inspired by art-blocks.site."
Generated: DETERMINISTIC_c1cc6d251fcedc1c
Batch ID: 20250622_211741
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
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 artwork_id: str, owner: str, artwork_data: str):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp when the block was created.
        - artwork_id (str): The ID of the artwork.
        - owner (str): The owner of the artwork.
        - artwork_data (str): The data of the artwork.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.artwork_id = artwork_id
        self.owner = owner
        self.artwork_data = artwork_data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + \
               self.artwork_id + self.owner + self.artwork_data
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), "0", "None", "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        - bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class Artwork:
    def __init__(self, artwork_id: str, data: str, owner: str):
        """
        Initialize a new artwork.

        Args:
        - artwork_id (str): The ID of the artwork.
        - data (str): The data of the artwork.
        - owner (str): The owner of the artwork.
        """
        self.artwork_id = artwork_id
        self.data = data
        self.owner = owner


class ArtOwnershipSystem:
    def __init__(self):
        """
        Initialize a new art ownership system.
        """
        self.blockchain = Blockchain()
        self.artworks = {}

    def add_artwork(self, artwork_id: str, data: str, owner: str):
        """
        Add a new artwork to the system.

        Args:
        - artwork_id (str): The ID of the artwork.
        - data (str): The data of the artwork.
        - owner (str): The owner of the artwork.
        """
        if artwork_id in self.artworks:
            raise ValueError("Artwork ID already exists")

        artwork = Artwork(artwork_id, data, owner)
        self.artworks[artwork_id] = artwork

        new_block = Block(len(self.blockchain.chain), 
                          self.blockchain.get_latest_block().hash, 
                          time.time(), artwork_id, owner, data)
        self.blockchain.add_block(new_block)

    def transfer_ownership(self, artwork_id: str, new_owner: str):
        """
        Transfer the ownership of an artwork.

        Args:
        - artwork_id (str): The ID of the artwork.
        - new_owner (str): The new owner of the artwork.

        Raises:
        - ValueError: If the artwork ID does not exist.
        """
        if artwork_id not in self.artworks:
            raise ValueError("Artwork ID does not exist")

        self.artworks[artwork_id].owner = new_owner

        new_block = Block(len(self.blockchain.chain), 
                          self.blockchain.get_latest_block().hash, 
                          time.time(), artwork_id, new_owner, 
                          self.artworks[artwork_id].data)
        self.blockchain.add_block(new_block)

    def get_artwork_owner(self, artwork_id: str) -> str:
        """
        Get the owner of an artwork.

        Args:
        - artwork_id (str): The ID of the artwork.

        Returns:
        - str: The owner of the artwork.

        Raises:
        - ValueError: If the artwork ID does not exist.
        """
        if artwork_id not in self.artworks:
            raise ValueError("Artwork ID does not exist")
        return self.artworks[artwork_id].owner


def main():
    system = ArtOwnershipSystem()
    system.add_artwork("art1", "artwork data", "owner1")
    print(system.get_artwork_owner("art1"))  # Output: owner1
    system.transfer_ownership("art1", "owner2")
    print(system.get_artwork_owner("art1"))  # Output: owner2


if __name__ == "__main__":
    main()
```
