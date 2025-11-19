"""
Generated Code Metadata:
========================
Original URL: https://powag.ch
Prompt: "Create a blockchain-based solution for information security and internet technologies, ensuring decentralized and secure data management."
Generated: DETERMINISTIC_90e85a3914b0a344
Batch ID: 20250622_210650
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

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        """
        Initialize a new block.

        Args:
            index (int): The index of the block in the chain.
            previous_hash (str): The hash of the previous block.
            timestamp (float): The timestamp of the block.
            data (str): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block.

        Returns:
            str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + json.dumps(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


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
        return Block(0, "0", time.time(), {"message": "Genesis Block"})

    def get_latest_block(self):
        """
        Get the latest block in the chain.

        Returns:
            Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the chain.

        Args:
            new_block (Block): The new block to add.

        Raises:
            ValueError: If the new block is not valid.
        """
        if new_block.previous_hash != self.get_latest_block().hash:
            raise ValueError("Invalid previous hash")
        new_block.hash = new_block.calculate_hash()
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
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


def main():
    blockchain = Blockchain()

    # Add some blocks to the chain
    blockchain.add_block(Block(1, blockchain.get_latest_block().hash, time.time(), {"message": "Block 1"}))
    blockchain.add_block(Block(2, blockchain.get_latest_block().hash, time.time(), {"message": "Block 2"}))

    # Check if the chain is valid
    print("Is chain valid?", blockchain.is_chain_valid())

    # Try to tamper with the chain
    blockchain.chain[1].data = {"message": "Tampered block"}
    blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()

    # Check if the chain is still valid
    print("Is chain valid after tampering?", blockchain.is_chain_valid())

    # Try to add a block with an invalid previous hash
    try:
        blockchain.add_block(Block(3, "invalid_hash", time.time(), {"message": "Block 3"}))
    except ValueError as e:
        print("Error adding block:", e)


if __name__ == "__main__":
    main()
```
