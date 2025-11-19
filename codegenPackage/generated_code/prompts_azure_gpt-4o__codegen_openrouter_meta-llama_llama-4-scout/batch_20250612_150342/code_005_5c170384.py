"""
Generated Code Metadata:
========================
Original URL: https://arbitriumltd.com
Prompt: Write a script to test the reliability of a blockchain application, incorporating QA techniques similar to those described by Arbitrium Ltd.
Generated: DETERMINISTIC_5c170384d0a170cf
Batch ID: 20250612_150342
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
import random
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        """
        Initialize a new block.

        :param index: The index of the block in the blockchain.
        :param previous_hash: The hash of the previous block.
        :param timestamp: The timestamp of the block.
        :param data: The data stored in the block.
        :param nonce: The nonce value for proof-of-work.
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

        :return: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """
        Mine the block using proof-of-work.

        :param difficulty: The difficulty level for mining.
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty: int = 2):
        """
        Initialize a new blockchain.

        :param difficulty: The difficulty level for mining.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        :return: The genesis block.
        """
        return Block(0, '0', time.time(), 'Genesis Block')

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        :return: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block) -> None:
        """
        Add a new block to the blockchain.

        :param new_block: The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


def test_blockchain_reliability() -> None:
    """
    Test the reliability of the blockchain application.
    """
    blockchain = Blockchain(difficulty=4)

    # Add 10 blocks to the blockchain
    for _ in range(10):
        new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, time.time(), f'Transaction {_}')
        blockchain.add_block(new_block)

    # Check if the blockchain is valid
    print(f'Is blockchain valid? {blockchain.is_chain_valid()}')

    # Test tampering with a block
    blockchain.chain[5].data = 'Tampered transaction'
    blockchain.chain[5].hash = blockchain.chain[5].calculate_hash()
    print(f'Is blockchain valid after tampering? {blockchain.is_chain_valid()}')


def simulate_network_attack(blockchain: Blockchain) -> None:
    """
    Simulate a network attack by creating a fork in the blockchain.

    :param blockchain: The blockchain to attack.
    """
    forked_blockchain = Blockchain(difficulty=blockchain.difficulty)
    forked_blockchain.chain = blockchain.chain[:]

    # Create a fork in the blockchain
    new_block = Block(len(forked_blockchain.chain), forked_blockchain.get_latest_block().hash, time.time(), f'Forked transaction {random.randint(0, 100)}')
    forked_blockchain.add_block(new_block)

    # Check if the forked blockchain is valid
    print(f'Is forked blockchain valid? {forked_blockchain.is_chain_valid()}')


if __name__ == '__main__':
    test_blockchain_reliability()
    blockchain = Blockchain(difficulty=4)
    for _ in range(10):
        new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, time.time(), f'Transaction {_}')
        blockchain.add_block(new_block)
    simulate_network_attack(blockchain)
```
