"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Write a tutorial on how to create a blockchain-based identity verification system, inspired by the concepts presented at ETHBerlin04.
Generated: DETERMINISTIC_394804d47028b2b5
Batch ID: 20250612_162710
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
from typing import List

# Define a class for a block in the blockchain
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict, nonce: int = 0):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (dict): The data stored in the block.
        - nonce (int): A counter for proof-of-work. Defaults to 0.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """
        Mine the block using proof-of-work.

        Args:
        - difficulty (int): The difficulty level for mining.
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


# Define a class for the blockchain
class Blockchain:
    def __init__(self, difficulty: int = 2):
        """
        Initialize a new blockchain.

        Args:
        - difficulty (int): The difficulty level for mining. Defaults to 2.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, '0', time.time(), {'genesis': 'block'})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block) -> None:
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
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


# Define a class for identity verification
class IdentityVerifier:
    def __init__(self, blockchain: Blockchain):
        """
        Initialize a new identity verifier.

        Args:
        - blockchain (Blockchain): The blockchain to use.
        """
        self.blockchain = blockchain

    def verify_identity(self, identity_data: dict) -> bool:
        """
        Verify an identity.

        Args:
        - identity_data (dict): The identity data to verify.

        Returns:
        - bool: True if the identity is valid, False otherwise.
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), identity_data)
        self.blockchain.add_block(new_block)
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == '__main__':
    blockchain = Blockchain()
    verifier = IdentityVerifier(blockchain)

    identity_data = {'name': 'John Doe', 'age': 30}
    is_valid = verifier.verify_identity(identity_data)
    print(f'Is identity valid? {is_valid}')

    # Try to tamper with the blockchain
    blockchain.chain[1].data = {'tampered': 'data'}
    is_valid = blockchain.is_chain_valid()
    print(f'Is chain valid after tampering? {is_valid}')
```
