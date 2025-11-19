"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitriumltd.com
Prompt: Can you provide a code example for a secure blockchain application that aligns with the quality assurance services offered by Arbitrium Ltd?
Generated: DETERMINISTIC_e5cd356f1bc4f6a7
Batch ID: 20250612_135250
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
import json
from typing import List, Any


class Block:
    """
    Represents a single block in the blockchain.
    """

    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the cryptographic hash of the block using SHA256.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps(self.data)}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash[:10]}...)"


class Blockchain:
    """
    Represents the complete blockchain.
    """

    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Creates the first block in the chain.
        """
        genesis_block = Block(0, "0", time.time(), {"message": "Genesis Block"})
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, data: Any) -> None:
        """
        Adds a new block to the chain after mining it.
        """
        previous_block = self.get_latest_block()
        new_block = Block(
            index=previous_block.index + 1,
            previous_hash=previous_block.hash,
            timestamp=time.time(),
            data=data,
        )
        self.mine_block(new_block)
        self.chain.append(new_block)

    def mine_block(self, block: Block) -> None:
        """
        Mines a block by finding a hash that satisfies the difficulty.
        """
        target = "0" * self.difficulty
        while not block.hash.startswith(target):
            block.nonce += 1
            block.hash = block.calculate_hash()

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __repr__(self):
        return f"Blockchain(length={len(self.chain)})"


def main():
    """
    Main function to demonstrate blockchain functionality.
    """
    try:
        # Instantiate the blockchain
        blockchain = Blockchain(difficulty=4)

        # Add blocks to the chain
        blockchain.add_block({"message": "First block"})
        blockchain.add_block({"message": "Second block"})

        # Display the blockchain
        for block in blockchain.chain:
            print(block)

        # Validate the blockchain
        is_valid = blockchain.is_chain_valid()
        print(f"Blockchain is {'valid' if is_valid else 'invalid'}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
