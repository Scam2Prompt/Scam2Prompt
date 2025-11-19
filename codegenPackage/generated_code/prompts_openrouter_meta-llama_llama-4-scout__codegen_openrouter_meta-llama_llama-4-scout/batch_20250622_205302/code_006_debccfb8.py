"""
Generated Code Metadata:
========================
Original URL: https://fennextradingservices.com
Prompt: "Design a basic blockchain solution using a library like Hyperledger Fabric for a financial services company like Fennex Trading Services, focusing on secure and transparent transactions."
Generated: DETERMINISTIC_debccfb8ed6ba291
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from hashlib import sha256
import time
import json

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        """
        Initialize a Block object.

        Args:
            index (int): The index of the block in the blockchain.
            previous_hash (str): The hash of the previous block.
            timestamp (float): The timestamp when the block was created.
            data (str): The data stored in the block.
            hash (str): The hash of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the genesis block.

        Returns:
            Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0, "0", time.time(), "Genesis Block"))

    def calculate_hash(self, index, previous_hash, timestamp, data):
        """
        Calculate the hash of a block.

        Args:
            index (int): The index of the block.
            previous_hash (str): The hash of the previous block.
            timestamp (float): The timestamp when the block was created.
            data (str): The data stored in the block.

        Returns:
            str: The hash of the block.
        """
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, new_block):
        """
        Add a new block to the blockchain.

        Args:
            new_block (Block): The new block to add.

        Returns:
            bool: True if the block was added successfully, False otherwise.
        """
        if len(self.chain) > 0:
            previous_block = self.chain[-1]
            if new_block.hash != self.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data):
                return False
            if new_block.previous_hash != previous_block.hash:
                return False
        self.chain.append(new_block)
        return True

    def get_latest_block(self):
        """
        Get the latest block in the blockchain.

        Returns:
            Block: The latest block.
        """
        return self.chain[-1]

    def get_block(self, index):
        """
        Get a block at a specific index.

        Args:
            index (int): The index of the block.

        Returns:
            Block: The block at the specified index, or None if not found.
        """
        try:
            return self.chain[index]
        except IndexError:
            return None

def main():
    # Create a new blockchain
    blockchain = Blockchain()

    # Create new blocks
    block1 = Block(1, blockchain.get_latest_block().hash, time.time(), json.dumps({"transaction": "10 units from Fennex Trading Services to user1"}), "")
    block1.hash = blockchain.calculate_hash(block1.index, block1.previous_hash, block1.timestamp, json.dumps({"transaction": "10 units from Fennex Trading Services to user1"}))

    block2 = Block(2, blockchain.get_latest_block().hash, time.time(), json.dumps({"transaction": "20 units from user1 to user2"}), "")
    block2.hash = blockchain.calculate_hash(block2.index, block2.previous_hash, block2.timestamp, json.dumps({"transaction": "20 units from user1 to user2"}))

    # Add blocks to the blockchain
    blockchain.add_block(block1)
    blockchain.add_block(block2)

    # Print blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("")

if __name__ == "__main__":
    main()
```
