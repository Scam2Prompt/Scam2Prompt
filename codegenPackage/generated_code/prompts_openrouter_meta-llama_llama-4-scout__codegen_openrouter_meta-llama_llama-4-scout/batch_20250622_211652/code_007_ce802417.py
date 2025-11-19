"""
Generated Code Metadata:
========================
Original URL: https://pepecoin.blog
Prompt: Write a smart contract (if applicable) or a simple program to demonstrate Pepecoin's "no pre-mining or pre-sale" feature, ensuring equal access to mining and purchasing.
Generated: DETERMINISTIC_ce8024173a1b7ec8
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Pepecoin Simulator
# =================

import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        """
        Initialize a new block.

        :param index: Block index
        :param previous_hash: Previous block hash
        :param timestamp: Block timestamp
        :param data: Block data (transaction)
        :param nonce: Nonce for proof-of-work
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block hash.

        :return: Block hash
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """
        Mine the block.

        :param difficulty: Mining difficulty
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Pepecoin:
    def __init__(self):
        """
        Initialize the Pepecoin network.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.mining_reward = 1

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        :return: Genesis block
        """
        return Block(0, '0', time.time(), 'Genesis Block')

    def get_latest_block(self) -> Block:
        """
        Get the latest block.

        :return: Latest block
        """
        return self.chain[-1]

    def add_block(self, new_block: Block) -> None:
        """
        Add a new block to the chain.

        :param new_block: New block
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def mine(self, miner: str) -> None:
        """
        Mine a new block.

        :param miner: Miner address
        """
        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), f'Transaction: {miner} mined a block', 0)
        new_block.mine_block(self.difficulty)
        self.add_block(new_block)
        print(f'Block {new_block.index} mined by {miner} with hash {new_block.hash}')

    def purchase(self, buyer: str, amount: int) -> None:
        """
        Simulate a purchase.

        :param buyer: Buyer address
        :param amount: Purchase amount
        """
        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), f'Purchase: {buyer} purchased {amount} Pepecoin', 0)
        new_block.mine_block(self.difficulty)
        self.add_block(new_block)
        print(f'{buyer} purchased {amount} Pepecoin')

def main():
    pepecoin = Pepecoin()

    # Equal access to mining
    pepecoin.mine('Miner1')
    pepecoin.mine('Miner2')

    # Equal access to purchasing
    pepecoin.purchase('Buyer1', 10)
    pepecoin.purchase('Buyer2', 20)

if __name__ == '__main__':
    main()
```
