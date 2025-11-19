"""
Generated Code Metadata:
========================
Original URL: https://triasphase-claim.pages.dev
Prompt: Create a simple blockchain-based application that demonstrates the concept of trusted interactions, ensuring that machines perform deterministic actions based on given instructions.
Generated: DETERMINISTIC_d0d5c6e8414b0063
Batch ID: 20250622_212219
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
from typing import List, Optional

class Block:
    """
    A class representing a single block in the blockchain.
    """
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        self.index = index  # Position of the block in the chain
        self.previous_hash = previous_hash  # Hash of the previous block
        self.timestamp = timestamp  # Time of block creation
        self.data = data  # Data stored in the block
        self.nonce = nonce  # Nonce used for proof-of-work
        self.hash = self.calculate_hash()  # Hash of the current block

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block using its contents.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash}, previous_hash={self.previous_hash}, data={self.data})"


class Blockchain:
    """
    A class representing a simple blockchain.
    """
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]  # Initialize the chain with the genesis block
        self.difficulty = 4  # Number of leading zeros required in the hash for proof-of-work

    def create_genesis_block(self) -> Block:
        """
        Create the first block in the blockchain (genesis block).
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Retrieve the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain after validating and mining it.
        """
        new_block.previous_hash = self.get_latest_block().hash
        self.mine_block(new_block)
        self.chain.append(new_block)

    def mine_block(self, block: Block):
        """
        Perform proof-of-work to mine the block by finding a hash that meets the difficulty criteria.
        """
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {current_block.index}")
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash at block {current_block.index}")
                return False

        return True

    def __repr__(self):
        return f"Blockchain(chain={self.chain})"


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add some blocks
    blockchain.add_block(Block(1, "", time.time(), "Transaction 1: Alice pays Bob 10 BTC"))
    blockchain.add_block(Block(2, "", time.time(), "Transaction 2: Bob pays Charlie 5 BTC"))

    # Print the blockchain
    for block in blockchain.chain:
        print(block)

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())
```
