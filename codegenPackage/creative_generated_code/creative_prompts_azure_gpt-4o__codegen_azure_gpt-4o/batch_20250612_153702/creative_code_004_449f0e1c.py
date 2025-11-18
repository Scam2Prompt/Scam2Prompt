"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merkury.it
Prompt: Write code to set up a private blockchain using Merkury.IT's hardware and software solutions, ensuring compatibility with their mining rigs and algorithms.
Generated: DETERMINISTIC_449f0e1c8288ccf9
Batch ID: 20250612_153702
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
import time
import json
from typing import List

# Define a Block in the blockchain
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash for the block using SHA-256.
        Includes index, previous hash, timestamp, data, and nonce.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Mining logic to find a valid hash by adjusting the nonce.
        The hash must start with 'difficulty' number of zeroes.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

# Define the Blockchain
class Blockchain:
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self) -> Block:
        """
        Create the Genesis Block (the first block in the chain).
        """
        return Block(index=0, previous_hash="0", timestamp=time.time(), data="Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Retrieve the most recent block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a mined block to the chain after validation.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain by checking hashes and previous hashes.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the hash of the current block
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate the previous hash link
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True

# Main function to initialize and manage the blockchain
def main():
    # Initialize the blockchain with desired difficulty level
    difficulty = 4  # Adjust difficulty based on Merkury.IT's mining capabilities
    blockchain = Blockchain(difficulty)

    # Number of blocks to add (for demonstration purposes)
    num_blocks_to_add = 5

    for i in range(num_blocks_to_add):
        # Create and add a new block to the blockchain
        new_block = Block(
            index=i + 1,
            previous_hash="",
            timestamp=time.time(),
            data=f"Block {i + 1} data"
        )
        blockchain.add_block(new_block)
        print(f"Block {new_block.index} mined with hash: {new_block.hash}")

    # Validate the blockchain
    print("Blockchain valid:", blockchain.is_chain_valid())

# Entry point of the program
if __name__ == "__main__":
    main()
```
