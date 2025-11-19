"""
Generated Code Metadata:
========================
Original URL: https://freebitcoinmining.website
Prompt: Design a blockchain-based system for secure and transparent free bitcoin mining, incorporating elements from Free Bitcoin Mining's platform.
Generated: DETERMINISTIC_cb6ee0c98ff4d036
Batch ID: 20250622_205523
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
import json
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict, nonce: int = 0):
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
        data_string = json.dumps(self.data)
        block_data = str(self.index) + self.previous_hash + str(self.timestamp) + data_string + str(self.nonce)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """
        Mine the block using proof-of-work.

        :param difficulty: The difficulty level of the blockchain.
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty: int = 2):
        """
        Initialize a new blockchain.

        :param difficulty: The difficulty level of the blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_data = []

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        :return: The genesis block.
        """
        return Block(0, '0', time.time(), {'genesis': 'block'})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        :return: The latest block.
        """
        return self.chain[-1]

    def add_data(self, data: dict) -> None:
        """
        Add data to the pending data.

        :param data: The data to add.
        """
        self.pending_data.append(data)

    def mine_pending_data(self) -> None:
        """
        Mine the pending data and add it to the blockchain.
        """
        if not self.pending_data:
            return

        new_block_index = self.get_latest_block().index + 1
        new_block_timestamp = time.time()
        new_block = Block(new_block_index, self.get_latest_block().hash, new_block_timestamp, self.pending_data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_data = []

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


class FreeBitcoinMining:
    def __init__(self):
        """
        Initialize a new Free Bitcoin Mining system.
        """
        self.blockchain = Blockchain()

    def start_mining(self, data: dict) -> None:
        """
        Start mining a new block.

        :param data: The data to mine.
        """
        try:
            self.blockchain.add_data(data)
            self.blockchain.mine_pending_data()
            if not self.blockchain.is_chain_valid():
                raise Exception("Invalid blockchain")
        except Exception as e:
            print(f"Error: {e}")

    def get_blockchain(self) -> List[Block]:
        """
        Get the blockchain.

        :return: The blockchain.
        """
        return self.blockchain.chain


if __name__ == "__main__":
    mining_system = FreeBitcoinMining()

    # Example usage:
    data1 = {'miner': 'John', 'reward': 10}
    data2 = {'miner': 'Alice', 'reward': 5}

    mining_system.start_mining(data1)
    mining_system.start_mining(data2)

    blockchain = mining_system.get_blockchain()
    for block in blockchain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("--------------------------------------------------")
```
