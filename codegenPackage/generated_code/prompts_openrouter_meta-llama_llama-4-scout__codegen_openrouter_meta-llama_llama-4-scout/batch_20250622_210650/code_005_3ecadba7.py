"""
Generated Code Metadata:
========================
Original URL: https://powag.ch
Prompt: "Develop a proof-of-concept solution for a blockchain-based application, using innovative architecture and expert developer skills, for a private investor."
Generated: DETERMINISTIC_3ecadba7e226ba21
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_app.py

import hashlib
import time
from typing import List

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        """
        Initializes a new block.

        Args:
        index (int): The block's index in the chain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The block's timestamp.
        data (str): The block's data.
        nonce (int): The block's nonce (default is 0).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculates the block's hash."""
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """Mines the block."""
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    """Represents a blockchain."""
    
    def __init__(self, difficulty: int = 2):
        """
        Initializes a new blockchain.

        Args:
        difficulty (int): The blockchain's difficulty (default is 2).
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self) -> Block:
        """Creates the genesis block."""
        return Block(0, '0', time.time(), 'Genesis Block')

    def get_latest_block(self) -> Block:
        """Gets the latest block in the chain."""
        return self.chain[-1]

    def add_block(self, data: str) -> None:
        """Adds a new block to the chain."""
        previous_block = self.get_latest_block()
        new_block_index = previous_block.index + 1
        new_block_timestamp = time.time()
        new_block = Block(new_block_index, previous_block.hash, new_block_timestamp, data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Checks if the chain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


def main() -> None:
    try:
        # Create a new blockchain
        blockchain = Blockchain(difficulty=4)

        # Add blocks to the chain
        blockchain.add_block('Transaction 1')
        blockchain.add_block('Transaction 2')
        blockchain.add_block('Transaction 3')

        # Check if the chain is valid
        if blockchain.is_chain_valid():
            print('The blockchain is valid.')
        else:
            print('The blockchain is not valid.')

        # Print the blockchain
        for block in blockchain.chain:
            print(f'Block {block.index} - Hash: {block.hash}')
            print(f'Timestamp: {block.timestamp}, Data: {block.data}, Nonce: {block.nonce}')
            print('------------------------')

    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
```
