"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x1blockdag.pages.dev
Prompt: Write Python code to interact with the BlockDAG blockchain using its proof-of-work consensus mechanism and simulate mining BDAG coins.
Generated: DETERMINISTIC_d7c706426e552d76
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time

class Block:
    """
    Represents a single block in the BlockDAG blockchain.
    Each block contains the block data, parent block hash, and proof of work.
    """
    def __init__(self, index, parent_hash, data, difficulty):
        self.index = index  # Unique identifier for the block in BlockDAG
        self.parent_hash = parent_hash  # Hash of the parent block (or multiple parents in DAG)
        self.data = data  # Arbitrary data stored in the block
        self.difficulty = difficulty  # Mining difficulty (number of leading zeros required in hash)
        self.timestamp = time.time()  # Timestamp when the block is created
        self.nonce = 0  # Nonce value to adjust for proof-of-work
        self.hash = self.calculate_hash()  # Current hash of the block

    def calculate_hash(self):
        """
        Calculate the hash of the block using SHA256.
        Combines block properties into a single hash value.
        """
        block_contents = f"{self.index}{self.parent_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def mine_block(self):
        """
        Perform proof-of-work mining to find a valid hash.
        The hash must satisfy the difficulty requirement (leading zeros).
        """
        target = "0" * self.difficulty  # Target hash prefix
        while not self.hash.startswith(target):
            self.nonce += 1  # Increment the nonce to change the hash value
            self.hash = self.calculate_hash()  # Recalculate the hash
        print(f"Block mined: {self.hash} (Nonce: {self.nonce})")  # Mining success message


class BlockDAG:
    """
    Represents the BlockDAG blockchain.
    Contains methods to add and validate blocks while simulating mining.
    """
    def __init__(self, difficulty):
        self.blocks = []  # List of blocks in the DAG structure
        self.difficulty = difficulty  # Mining difficulty for all blocks
        self.genesis_block()  # Initialize the blockchain with a genesis block

    def genesis_block(self):
        """
        Create the genesis block (first block in the blockchain).
        """
        genesis = Block(index=0, parent_hash="0" * 64, data="Genesis Block", difficulty=self.difficulty)
        genesis.mine_block()  # Perform proof-of-work mining for the genesis block
        self.blocks.append(genesis)  # Add the genesis block to the DAG

    def add_block(self, data):
        """
        Add a new block to the blockchain.
        Perform proof-of-work mining before appending to the DAG.
        """
        parent_hash = self.blocks[-1].hash  # Use the most recent block as the parent
        new_block = Block(index=len(self.blocks), parent_hash=parent_hash, data=data, difficulty=self.difficulty)
        new_block.mine_block()  # Perform proof-of-work mining for the new block
        self.blocks.append(new_block)  # Add the new block to the DAG

    def display_chain(self):
        """
        Display all blocks in the DAG.
        """
        for block in self.blocks:
            print(f"Index: {block.index}")
            print(f"Parent Hash: {block.parent_hash}")
            print(f"Data: {block.data}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Nonce: {block.nonce}")
            print(f"Hash: {block.hash}")
            print("-" * 40)


# Driver Code
if __name__ == "__main__":
    try:
        difficulty = 4  # Set mining difficulty (number of leading zeros in hash)
        blockchain = BlockDAG(difficulty)  # Initialize the BlockDAG blockchain

        print("Mining blocks...")
        blockchain.add_block("Transaction Data: Alice pays Bob 5 BDAG")
        blockchain.add_block("Transaction Data: Bob pays Charlie 3 BDAG")
        blockchain.add_block("Transaction Data: Charlie pays Dana 2 BDAG")

        print("\nDisplaying the BlockDAG blockchain:")
        blockchain.display_chain()

    except Exception as e:
        print(f"An error occurred: {e}")
```
