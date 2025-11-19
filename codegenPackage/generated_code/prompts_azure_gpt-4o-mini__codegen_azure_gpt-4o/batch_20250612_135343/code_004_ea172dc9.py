"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-template-nextjs.vercel.app
Prompt: Create an example of a modular blockchain application using the concepts discussed in the Fuel Blog post.
Generated: DETERMINISTIC_ea172dc98004f588
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Modular Blockchain Application Example
This code demonstrates a simple modular blockchain application using Python.
The application is designed to be extensible and follows best practices for modularity.
"""

import hashlib
import json
import time
from typing import List, Dict, Any


# Block class to represent a single block in the blockchain
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict[str, Any], nonce: int = 0):
        """
        Initialize a block in the blockchain.

        :param index: Position of the block in the chain
        :param previous_hash: Hash of the previous block
        :param timestamp: Time the block was created
        :param data: Transaction or other data stored in the block
        :param nonce: Proof-of-work nonce value
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block using its contents.

        :return: SHA-256 hash of the block
        """
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash})"


# Blockchain class to manage the chain of blocks
class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain: List[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the first block in the blockchain (genesis block).

        :return: Genesis block
        """
        return Block(index=0, previous_hash="0", timestamp=time.time(), data={"message": "Genesis Block"})

    def get_latest_block(self) -> Block:
        """
        Get the most recent block in the chain.

        :return: Latest block
        """
        return self.chain[-1]

    def add_block(self, data: Dict[str, Any]) -> None:
        """
        Add a new block to the blockchain.

        :param data: Data to store in the block
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            timestamp=time.time(),
            data=data
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.

        :return: True if the chain is valid, False otherwise
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

    def __repr__(self):
        return f"Blockchain(chain={self.chain})"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        blockchain = Blockchain()

        # Add blocks to the blockchain
        blockchain.add_block({"transaction": "Alice pays Bob 10 BTC"})
        blockchain.add_block({"transaction": "Bob pays Charlie 5 BTC"})

        # Print the blockchain
        for block in blockchain.chain:
            print(block)

        # Validate the blockchain
        print("Is blockchain valid?", blockchain.is_chain_valid())

    except Exception as e:
        print(f"An error occurred: {e}")
```
