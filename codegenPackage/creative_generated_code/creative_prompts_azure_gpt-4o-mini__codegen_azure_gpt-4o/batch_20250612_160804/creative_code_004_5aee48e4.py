"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chain-dioneprotoclcom.pages.dev
Prompt: Provide an example of using the Dione Protocol's features to build a sustainable blockchain application.
Generated: DETERMINISTIC_5aee48e4feb219fa
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for blockchain development
import hashlib
import time

# Define the Block class for building the blockchain
class Block:
    """
    Represents a single block in the blockchain.
    Attributes:
        index (int): Position of the block in the blockchain.
        timestamp (str): Time when the block was created.
        data (str): Data stored in the block (e.g., transactions).
        previous_hash (str): Hash of the previous block in the chain.
        hash (str): Hash of the current block.
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        Returns:
            str: Generated hash for the block.
        """
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()

# Define the Blockchain class to manage the blockchain
class Blockchain:
    """
    Represents the blockchain, a chain of blocks.
    Attributes:
        chain (list[Block]): List containing all the blocks.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the genesis block, the first block in the blockchain.
        Returns:
            Block: The genesis block.
        """
        return Block(0, time.strftime("%Y-%m-%d %H:%M:%S"), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Retrieves the latest block in the blockchain.
        Returns:
            Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        Args:
            data (str): Data to store in the new block.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain to ensure data integrity.
        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the block is correct
            if current_block.hash != current_block.calculate_hash():
                print("Invalid block hash detected!")
                return False

            # Check if the previous hash matches the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash detected!")
                return False

        return True

# Instantiate the blockchain
blockchain = Blockchain()

# Add blocks to the blockchain with sample data
try:
    blockchain.add_block("Transaction 1: UserA pays UserB 10 DioneCoins")
    blockchain.add_block("Transaction 2: UserB pays UserC 5 DioneCoins")
    blockchain.add_block("Transaction 3: UserA pays UserC 2 DioneCoins")
except Exception as e:
    print(f"Error while adding block: {e}")

# Validate the blockchain
if blockchain.is_chain_valid():
    print("Blockchain is valid.")
else:
    print("Blockchain is invalid.")

# Display the blockchain
for block in blockchain.chain:
    print(f"Block {block.index}:")
    print(f"  Timestamp: {block.timestamp}")
    print(f"  Data: {block.data}")
    print(f"  Previous Hash: {block.previous_hash}")
    print(f"  Hash: {block.hash}")
    print()
```
