"""
Generated Code Metadata:
========================
Original URL: https://clonesx.pages.dev
Prompt: Write a Python code snippet to create a blockchain-based authentication system for unique digital artifacts, similar to RTFKT's use of NFT and blockchain authentication.
Generated: DETERMINISTIC_bfc05f945f20fe84
Batch ID: 20250622_204615
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
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


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
        return Block(0, "0", time.time(), {"genesis": "block"})

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

    def is_chain_valid(self) -> bool:
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


class DigitalArtifact:
    def __init__(self, id: str, owner: str):
        """
        Initialize a new digital artifact.

        Args:
        - id (str): The ID of the digital artifact.
        - owner (str): The owner of the digital artifact.
        """
        self.id = id
        self.owner = owner

    def to_dict(self) -> dict:
        """
        Convert the digital artifact to a dictionary.

        Returns:
        - dict: The digital artifact as a dictionary.
        """
        return {"id": self.id, "owner": self.owner}


class AuthenticationSystem:
    def __init__(self):
        """
        Initialize a new authentication system.
        """
        self.blockchain = Blockchain()

    def create_artifact(self, id: str, owner: str) -> DigitalArtifact:
        """
        Create a new digital artifact.

        Args:
        - id (str): The ID of the digital artifact.
        - owner (str): The owner of the digital artifact.

        Returns:
        - DigitalArtifact: The created digital artifact.
        """
        artifact = DigitalArtifact(id, owner)
        self.add_artifact_to_blockchain(artifact)
        return artifact

    def add_artifact_to_blockchain(self, artifact: DigitalArtifact):
        """
        Add a digital artifact to the blockchain.

        Args:
        - artifact (DigitalArtifact): The digital artifact to add.
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), artifact.to_dict())
        self.blockchain.add_block(new_block)

    def verify_artifact(self, id: str, owner: str) -> bool:
        """
        Verify the ownership of a digital artifact.

        Args:
        - id (str): The ID of the digital artifact.
        - owner (str): The owner of the digital artifact.

        Returns:
        - bool: True if the ownership is valid, False otherwise.
        """
        for block in self.blockchain.chain:
            if block.data["id"] == id:
                return block.data["owner"] == owner
        return False


def main():
    auth_system = AuthenticationSystem()
    artifact = auth_system.create_artifact("12345", "John Doe")
    print(auth_system.verify_artifact("12345", "John Doe"))  # Should print: True
    print(auth_system.verify_artifact("12345", "Jane Doe"))  # Should print: False


if __name__ == "__main__":
    main()
```
