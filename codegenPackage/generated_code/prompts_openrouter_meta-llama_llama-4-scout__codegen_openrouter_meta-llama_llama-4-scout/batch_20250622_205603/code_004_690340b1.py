"""
Generated Code Metadata:
========================
Original URL: https://hex-protocol.net
Prompt: How does the Hex protocol ensure the security and integrity of its blockchain network?
Generated: DETERMINISTIC_690340b154ef30d9
Batch ID: 20250622_205603
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

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
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

    def calculate_hash(self):
        """
        Calculate the hash of the block.

        :return: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mine the block using proof-of-work.

        :param difficulty: The difficulty level of the proof-of-work.
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty=2):
        """
        Initialize a new blockchain.

        :param difficulty: The difficulty level of the proof-of-work.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Create the genesis block.

        :return: The genesis block.
        """
        return Block(0, '0', int(time.time()), 'Genesis Block')

    def get_latest_block(self):
        """
        Get the latest block in the blockchain.

        :return: The latest block.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Add a new block to the blockchain.

        :param data: The data to be stored in the new block.
        """
        previous_block = self.get_latest_block()
        index = previous_block.index + 1
        timestamp = int(time.time())
        new_block = Block(index, previous_block.hash, timestamp, data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
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


def main():
    # Create a new blockchain with a difficulty level of 4
    blockchain = Blockchain(4)

    # Add some blocks to the blockchain
    blockchain.add_block('Transaction 1')
    blockchain.add_block('Transaction 2')
    blockchain.add_block('Transaction 3')

    # Check if the blockchain is valid
    print('Is blockchain valid?', blockchain.is_chain_valid())

    # Print the blockchain
    for block in blockchain.chain:
        print(f'Block {block.index} - Hash: {block.hash}')
        print(f'Timestamp: {block.timestamp}, Data: {block.data}')
        print('------------------------')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'An error occurred: {e}')
```
