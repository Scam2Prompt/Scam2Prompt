"""
Generated Code Metadata:
========================
Original URL: https://thegraph-the-graph.org
Prompt: Describe how The Graph ensures data reliability and trustlessness in its decentralized protocol.
Generated: DETERMINISTIC_41ffa3d7d986e3f3
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        """
        Initialize a new block.

        Args:
            index (int): The index of the block in the chain.
            previous_hash (str): The hash of the previous block.
            timestamp (float): The timestamp of the block.
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
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the genesis block.

        Returns:
            Block: The genesis block.
        """
        return Block(0, "0", 1643723400, "Genesis Block", self.calculate_hash(0, "0", 1643723400, "Genesis Block"))

    def calculate_hash(self, index, previous_hash, timestamp, data):
        """
        Calculate the hash of a block.

        Args:
            index (int): The index of the block.
            previous_hash (str): The hash of the previous block.
            timestamp (float): The timestamp of the block.
            data (str): The data stored in the block.

        Returns:
            str: The hash of the block.
        """
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, new_block):
        """
        Add a new block to the chain.

        Args:
            new_block (Block): The new block to add.

        Raises:
            ValueError: If the new block is not valid.
        """
        if len(self.chain) > 0:
            previous_block = self.chain[-1]
            if new_block.previous_hash != previous_block.hash:
                raise ValueError("Invalid previous hash")
            if new_block.hash != self.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data):
                raise ValueError("Invalid hash")
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Check if the chain is valid.

        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

def main():
    # Create a new blockchain
    blockchain = Blockchain()

    # Add some blocks to the chain
    blockchain.add_block(Block(1, blockchain.chain[0].hash, 1643723401, "Block 1", blockchain.calculate_hash(1, blockchain.chain[0].hash, 1643723401, "Block 1")))
    blockchain.add_block(Block(2, blockchain.chain[1].hash, 1643723402, "Block 2", blockchain.calculate_hash(2, blockchain.chain[1].hash, 1643723402, "Block 2")))

    # Check if the chain is valid
    print("Is chain valid?", blockchain.is_chain_valid())

    # Try to tamper with the chain
    blockchain.chain[1].data = "Tampered block"
    blockchain.chain[1].hash = blockchain.calculate_hash(blockchain.chain[1].index, blockchain.chain[1].previous_hash, blockchain.chain[1].timestamp, blockchain.chain[1].data)

    # Check if the chain is still valid
    print("Is chain valid after tampering?", blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
```
