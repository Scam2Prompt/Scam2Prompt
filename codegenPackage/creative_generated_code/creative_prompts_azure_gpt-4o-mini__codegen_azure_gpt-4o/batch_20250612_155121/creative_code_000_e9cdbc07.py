"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digital.free-zetachain.online
Prompt: Generate a code snippet to implement a blockchain solution using ZetaChain.
Generated: DETERMINISTIC_e9cdbc07c35a75c3
Batch ID: 20250612_155121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import json
import time


class ZetaBlock:
    """
    Represents a single block in the blockchain.
    """

    def __init__(self, index, timestamp, data, previous_hash):
        """
        Initialize the block with an index, timestamp, data, and previous hash.
        :param index: Index of the block in the blockchain
        :param timestamp: Timestamp when the block was created
        :param data: Data to store in the block
        :param previous_hash: Hash of the previous block
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the SHA-256 hash of the block content.
        :return: Hash string
        """
        block_content = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(block_content).hexdigest()


class ZetaChain:
    """
    Represents the ZetaChain blockchain.
    """

    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the genesis block for the blockchain.
        :return: Genesis block instance
        """
        return ZetaBlock(index=0, timestamp=time.time(), data="Genesis Block", previous_hash="0")

    def get_latest_block(self):
        """
        Retrieve the latest block in the blockchain.
        :return: Latest block instance
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Add a new block to the blockchain.
        :param data: Data to store in the new block
        """
        previous_block = self.get_latest_block()
        new_block = ZetaBlock(
            index=previous_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the blockchain integrity.
        :return: True if valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the block is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        """
        Print the blockchain in a human-readable format.
        """
        for block in self.chain:
            print("Block Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Current Hash:", block.hash)
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    # Initialize the ZetaChain blockchain
    zeta_chain = ZetaChain()

    # Add blocks to the blockchain
    zeta_chain.add_block("First transaction data")
    zeta_chain.add_block("Second transaction data")

    # Print the blockchain
    zeta_chain.print_chain()

    # Validate the blockchain's integrity
    print("Is blockchain valid?", zeta_chain.is_chain_valid())
```
