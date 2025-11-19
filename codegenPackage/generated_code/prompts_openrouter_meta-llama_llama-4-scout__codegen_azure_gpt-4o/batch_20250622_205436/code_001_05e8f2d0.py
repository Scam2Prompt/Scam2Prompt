"""
Generated Code Metadata:
========================
Original URL: https://celestia.agency
Prompt: Generate a Python code snippet for a basic blockchain implementation similar to what Celestia agency might develop.
Generated: DETERMINISTIC_05e8f2d0a5d29f9a
Batch ID: 20250622_205436
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

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index  # Position of the block in the chain
        self.previous_hash = previous_hash  # Hash of the previous block
        self.timestamp = timestamp  # Time of block creation
        self.data = data  # Data stored in the block
        self.nonce = nonce  # Nonce used for proof-of-work
        self.hash = self.calculate_hash()  # Current block's hash

    def calculate_hash(self):
        """
        Calculates the hash of the block using its contents.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mines the block by finding a hash that satisfies the difficulty level.
        """
        target = "0" * difficulty  # Target hash prefix based on difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    """
    Represents the blockchain, a chain of blocks.
    """
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]  # Initialize the chain with the genesis block
        self.difficulty = difficulty  # Difficulty level for mining

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain after mining it.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            timestamp=time.time(),
            data=data
        )
        new_block.mine_block(self.difficulty)  # Mine the block to meet the difficulty
        self.chain.append(new_block)  # Append the mined block to the chain

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Example usage
if __name__ == "__main__":
    # Create a new blockchain
    my_blockchain = Blockchain(difficulty=4)

    # Add blocks to the blockchain
    print("Mining block 1...")
    my_blockchain.add_block("Block 1 Data")

    print("Mining block 2...")
    my_blockchain.add_block("Block 2 Data")

    print("Mining block 3...")
    my_blockchain.add_block("Block 3 Data")

    # Display the blockchain
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print("-" * 40)

    # Validate the blockchain
    print("Is blockchain valid?", my_blockchain.is_chain_valid())
```
