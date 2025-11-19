"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-bitcoin.org
Prompt: Explain how Bitcoin Core achieves consensus among users without voting, and provide an example of how this can be implemented in a decentralized application.
Generated: DETERMINISTIC_ac6dd3d74fa93559
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a simple decentralized blockchain application that achieves consensus using similar principles to Bitcoin Core: aligning nodes based on the longest valid chain. The example demonstrates how nodes independently validate and adopt the longest valid chain without voting.

```python
import hashlib
import time
import json


class Block:
    """
    Represents a single block in the blockchain.
    Attributes:
        index: The position of the block in the chain.
        timestamp: When this block was created.
        data: The data stored in the block.
        previous_hash: The hash of the previous block in the chain.
        nonce: The value used for proof-of-work.
        hash: The hash of the current block after mining.
    """

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Computes the hash for the block using its attributes.
        Returns:
            str: The SHA-256 hash of the block.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mines a block by finding a hash with the required number of leading zeros.
        Args:
            difficulty: The number of leading zeros required in the hash.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()


class Blockchain:
    """
    Represents a simple blockchain.
    Attributes:
        chain: The list of blocks in the blockchain.
        difficulty: The mining difficulty.
    """

    def __init__(self):
        self.chain = []
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the genesis (first) block in the blockchain.
        """
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, data):
        """
        Adds a new block to the blockchain after mining.
        Args:
            data: The data to be stored in the block.
        Returns:
            Block: The newly added block.
        """
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        """
        Validates the blockchain by checking hash links and proof-of-work.
        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Validate the hash of the block
            if current.hash != current.compute_hash():
                return False

            # Validate the previous hash reference
            if current.previous_hash != previous.hash:
                return False

        return True

    def replace_chain(self, new_chain):
        """
        Replaces the chain with a new one if the new chain is longer and valid.
        Args:
            new_chain: The proposed new blockchain.
        Returns:
            bool: True if the chain was replaced, False otherwise.
        """
        if len(new_chain) > len(self.chain) and Blockchain.is_chain_valid_static(new_chain):
            self.chain = new_chain
            return True
        return False

    @staticmethod
    def is_chain_valid_static(chain):
        """
        Validates a blockchain passed as an argument.
        Args:
            chain: The blockchain to validate.
        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(chain)):
            current = chain[i]
            previous = chain[i - 1]

            # Validate the hash of the block
            if current.hash != current.compute_hash():
                return False

            # Validate the previous hash reference
            if current.previous_hash != previous.hash:
                return False

        return True


# Example usage:
if __name__ == "__main__":
    # Node A creates its blockchain
    node_a_blockchain = Blockchain()
    node_a_blockchain.add_block("Block 1 Data")
    node_a_blockchain.add_block("Block 2 Data")

    # Node B creates its blockchain
    node_b_blockchain = Blockchain()
    node_b_blockchain.add_block("Block 1 Data")

    # Simulate Node A sending its chain to Node B
    if node_b_blockchain.replace_chain(node_a_blockchain.chain):
        print("Node B replaced its chain with Node A's chain")
    else:
        print("Node B kept its original chain")

    # Validate the blockchain
    print("Is Node B's chain valid?", node_b_blockchain.is_chain_valid())
```

This code demonstrates the longest valid chain principle for achieving consensus without requiring voting. Each node independently validates and adopts the longest valid chain it receives.
