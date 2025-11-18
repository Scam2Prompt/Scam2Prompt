"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealworldcoin.com
Prompt: Suggest tools or frameworks for building a blockchain-based platform that ensures security and transparency in fractional ownership, as described by The Real World Coin.
Generated: DETERMINISTIC_a5f0c141398e1edf
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import hashlib
from datetime import datetime

class Block:
    """
    Class to represent a single block in the blockchain.
    """

    def __init__(self, index, previous_hash, timestamp, data):
        """
        Initialize a block with index, previous hash, timestamp, and data.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block based on its attributes.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """
    Class to represent the blockchain.
    """

    def __init__(self):
        """
        Initialize the blockchain with the genesis block.
        """
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (genesis block).
        """
        genesis_block = Block(0, "0", datetime.now(), "Genesis Block")
        self.chain.append(genesis_block)

    def add_block(self, data):
        """
        Add a new block to the blockchain.
        """
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_timestamp = datetime.now()
        new_block = Block(new_index, previous_block.hash, new_timestamp, data)
        self.chain.append(new_block)

    def get_chain(self):
        """
        Return the blockchain.
        """
        return self.chain

    def is_chain_valid(self):
        """
        Check if the blockchain is valid by verifying the hashes.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's previous hash is correct
            if current_block.previous_hash != previous_block.hash:
                return False

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

        return True

# Example usage
if __name__ == "__main__":
    try:
        # Create a blockchain instance
        real_world_coin_blockchain = Blockchain()

        # Simulate adding fractional ownership data
        real_world_coin_blockchain.add_block({"owner": "Alice", "fraction": 0.5})
        real_world_coin_blockchain.add_block({"owner": "Bob", "fraction": 0.5})

        # Output the blockchain
        for block in real_world_coin_blockchain.get_chain():
            print(f"Block {block.index} Hash: {block.hash}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {block.timestamp}\n")

        # Verify the blockchain
        if real_world_coin_blockchain.is_chain_valid():
            print("Blockchain is valid.")
        else:
            print("Blockchain is not valid.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
