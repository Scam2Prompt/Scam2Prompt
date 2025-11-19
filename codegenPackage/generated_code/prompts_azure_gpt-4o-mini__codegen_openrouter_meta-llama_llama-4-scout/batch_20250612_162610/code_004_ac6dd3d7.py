"""
Generated Code Metadata:
========================
Original URL: https://en-bitcoin.org
Prompt: Explain how Bitcoin Core achieves consensus among users without voting, and provide an example of how this can be implemented in a decentralized application.
Generated: DETERMINISTIC_ac6dd3d74fa93559
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Bitcoin Core Consensus Mechanism Example**
=====================================================

Below is an example implementation in Python, demonstrating a simplified version of the Proof-of-Work (PoW) consensus mechanism used in Bitcoin Core.

```python
import hashlib
import time
import random

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        """
        Initialize a new block.

        :param index: Block index
        :param previous_hash: Hash of the previous block
        :param timestamp: Block timestamp
        :param data: Block data
        :param nonce: Nonce value for PoW
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the block hash.

        :return: Block hash
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mine the block using PoW.

        :param difficulty: Mining difficulty
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty):
        """
        Initialize a new blockchain.

        :param difficulty: Mining difficulty
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Create the genesis block.

        :return: Genesis block
        """
        return Block(0, '0', int(time.time()), 'Genesis Block')

    def get_latest_block(self):
        """
        Get the latest block in the chain.

        :return: Latest block
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the chain.

        :param new_block: New block
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Check if the chain is valid.

        :return: Chain validity
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


# Example usage
if __name__ == '__main__':
    difficulty = 2
    blockchain = Blockchain(difficulty)

    # Add blocks to the chain
    for i in range(5):
        new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, int(time.time()), f'Transaction {i}')
        blockchain.add_block(new_block)

    # Print the chain
    for block in blockchain.chain:
        print(f'Block {block.index} - Hash: {block.hash}')
        print(f'Previous Hash: {block.previous_hash}')
        print(f'Timestamp: {block.timestamp}')
        print(f'Data: {block.data}')
        print(f'Nonce: {block.nonce}')
        print('------------------------')

    # Check chain validity
    print(f'Is chain valid? {blockchain.is_chain_valid()}')
```

Commit message:
```
Implement Bitcoin Core consensus mechanism example

* Added Block and Blockchain classes to demonstrate Proof-of-Work (PoW) consensus mechanism
* Implemented block mining and chain validation
* Provided example usage and testing
```
