"""
Generated Code Metadata:
========================
Original URL: https://en-bitcoin.org
Prompt: Explain how Bitcoin Core achieves consensus among users without voting, and provide an example of how this can be implemented in a decentralized application.
Generated: DETERMINISTIC_ac6dd3d74fa93559
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bitcoin Core achieves consensus through a mechanism called Proof of Work (PoW), 
where miners compete to solve complex mathematical problems. The first miner to solve 
the problem gets to add a new block to the blockchain, and the rest of the network 
accepts this block as valid. This process does not involve voting but relies on 
cryptographic proofs and economic incentives.

The following code demonstrates a simplified version of a decentralized application 
that mimics the consensus mechanism of Bitcoin using a PoW-like approach.
"""

import hashlib
import time
import random

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    Represents the entire blockchain.
    """
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain.
        """
        genesis_block = Block(0, "0", time.time(), "Genesis Block")
        self.chain.append(genesis_block)

    def add_block(self, new_block):
        """
        Adds a new block to the blockchain after validating it.
        """
        if self.is_valid_new_block(new_block, self.chain[-1]):
            self.chain.append(new_block)

    def is_valid_new_block(self, new_block, previous_block):
        """
        Validates the new block against the previous block.
        """
        if previous_block.index + 1 != new_block.index:
            print("Invalid index")
            return False
        elif previous_block.hash != new_block.previous_hash:
            print("Invalid previous hash")
            return False
        elif new_block.hash != new_block.calculate_hash():
            print("Invalid hash")
            return False
        return True

    def mine_block(self, data):
        """
        Simulates the mining process by finding a valid nonce.
        """
        index = len(self.chain)
        previous_hash = self.chain[-1].hash
        nonce = 0
        timestamp = time.time()

        # Simulate a difficulty level
        difficulty = 4
        prefix_str = '0' * difficulty

        while True:
            block = Block(index, previous_hash, timestamp, data, nonce)
            if block.hash.startswith(prefix_str):
                print(f"Block mined: {block.hash}")
                self.add_block(block)
                break
            nonce += 1

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Simulate mining of new blocks
    for i in range(5):
        data = f"Block {i + 1} Data"
        blockchain.mine_block(data)

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Index: {block.index}, Hash: {block.hash}, Previous Hash: {block.previous_hash}, Nonce: {block.nonce}")
```
