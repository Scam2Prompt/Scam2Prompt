"""
Generated Code Metadata:
========================
Original URL: https://cryptoleads-inc.com
Prompt: "Explain the concept of Proof-of-Work (PoW) in cryptocurrency mining and how it ensures the security of the Bitcoin network."
Generated: DETERMINISTIC_a49c7d426c6397fb
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Proof-of-Work (PoW) Simulation for Cryptocurrency Mining

This script demonstrates a simplified version of how Proof-of-Work functions
in cryptocurrency mining and how it secures the Bitcoin network.
"""

import hashlib
import time
from typing import Tuple

class Block:
    """
    Represents a block in a blockchain with simplified attributes.
    """
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the SHA-256 hash of the block's contents.
        """
        block_contents = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

class Blockchain:
    """
    Simplified blockchain implementation demonstrating Proof-of-Work.
    """
    def __init__(self):
        self.difficulty = 4  # Number of leading zeros required in hash
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Returns the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block) -> None:
        """
        Adds a new block to the chain after validating it.
        """
        new_block.previous_hash = self.get_latest_block().hash
        self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block: Block) -> None:
        """
        Performs the proof-of-work algorithm to find a valid hash.
        """
        target = '0' * self.difficulty
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check hash integrity
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check block linkage
            if current_block.previous_hash != previous_block.hash:
                return False

            # Check proof-of-work
            if current_block.hash[:self.difficulty] != '0' * self.difficulty:
                return False

        return True

def mine_block(blockchain: Blockchain, data: str) -> Tuple[Block, float]:
    """
    Simulates mining a new block with the given data.
    Returns the new block and the time taken to mine it.
    """
    start_time = time.time()
    new_block = Block(
        len(blockchain.chain),
        blockchain.get_latest_block().hash,
        time.time(),
        data
    )
    blockchain.add_block(new_block)
    end_time = time.time()
    return new_block, end_time - start_time

def demonstrate_pow():
    """
    Demonstrates Proof-of-Work by creating a blockchain and mining blocks.
    """
    print("Creating blockchain...")
    blockchain = Blockchain()
    
    print("\nMining block 1...")
    block1, time1 = mine_block(blockchain, "Transaction Data 1")
    print(f"Block mined in {time1:.2f} seconds")
    print(f"Hash: {block1.hash}")
    
    print("\nMining block 2...")
    block2, time2 = mine_block(blockchain, "Transaction Data 2")
    print(f"Block mined in {time2:.2f} seconds")
    print(f"Hash: {block2.hash}")
    
    print("\nValidating blockchain...")
    is_valid = blockchain.is_chain_valid()
    print(f"Blockchain is {'valid' if is_valid else 'invalid'}")

if __name__ == "__main__":
    demonstrate_pow()
```
