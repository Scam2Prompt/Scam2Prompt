"""
Generated Code Metadata:
========================
Original URL: https://en-bitcoin.org
Prompt: Explain the concept of consensus in Bitcoin Core and how it ensures the integrity of the blockchain.
Generated: DETERMINISTIC_fbaf1a941b76574f
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# No Python code is suitable for this task as it is a conceptual explanation.
# However, I can provide a simple Python script that simulates a basic consensus mechanism.

import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (str): The data stored in the block.
        - nonce (int): A counter for proof-of-work.
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
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data + str(self.nonce)
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


class Blockchain:
    def __init__(self) -> None:
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, '0', time.time(), 'Genesis Block')

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

        Raises:
        - ValueError: If the new block is not valid.
        """
        if new_block.previous_hash != self.get_latest_block().hash:
            raise ValueError('Invalid block')
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


def main() -> None:
    blockchain = Blockchain()
    block1 = Block(1, blockchain.get_latest_block().hash, time.time(), 'Transaction 1')
    blockchain.add_block(block1)
    block2 = Block(2, blockchain.get_latest_block().hash, time.time(), 'Transaction 2')
    blockchain.add_block(block2)

    # Print blockchain
    for block in blockchain.chain:
        print(f'Block {block.index} - Hash: {block.hash}')

    # Check if blockchain is valid
    print(f'Is blockchain valid? {blockchain.is_chain_valid()}')


if __name__ == '__main__':
    main()
```
