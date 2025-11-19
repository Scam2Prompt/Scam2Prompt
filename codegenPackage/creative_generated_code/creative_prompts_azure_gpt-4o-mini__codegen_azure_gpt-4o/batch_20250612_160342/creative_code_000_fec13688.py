"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain.netlify.app
Prompt: Write a code snippet that utilizes the PulseChain's environment-synchronized Proof of History (PoH) consensus for a blockchain application.
Generated: DETERMINISTIC_fec136882291343b
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# pulsechain_poh.py

import time
import hashlib
from typing import List, Dict, Optional

class Block:
    """
    Represents a block in the blockchain.
    Each block contains:
    - A timestamp synchronized with the PulseChain environment (Proof of History).
    - A list of transactions.
    - Hash of the previous block in the chain.
    - Hash of the current block for integrity validation.
    """
    def __init__(self, index: int, transactions: List[Dict[str, str]], previous_hash: str):
        self.index = index
        self.timestamp = self.get_poh_synchronized_timestamp()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def get_poh_synchronized_timestamp(self) -> str:
        """
        Returns a timestamp synchronized with the PulseChain environment.
        For simplicity, we simulate the PoH synchronization using system time.
        In production, you would interface with PulseChain's PoH API or protocol.
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    def compute_hash(self) -> str:
        """
        Computes the hash of the block using SHA-256.
        Includes all critical block attributes for integrity validation.
        """
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain itself, consisting of a sequence of blocks.
    - Initializes with the genesis block.
    - Provides methods to add new blocks.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the initial block in the blockchain (Genesis block).
        """
        genesis_block = Block(index=0, transactions=[], previous_hash="0")
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]

    def add_block(self, transactions: List[Dict[str, str]]) -> Optional[Block]:
        """
        Adds a new block to the blockchain.
        Handles errors gracefully, ensuring the blockchain remains intact.
        """
        try:
            previous_block = self.get_last_block()
            new_block = Block(
                index=previous_block.index + 1,
                transactions=transactions,
                previous_hash=previous_block.hash
            )
            self.chain.append(new_block)
            return new_block
        except Exception as e:
            print(f"Error adding block: {e}")
            return None

    def is_chain_valid(self) -> bool:
        """
        Validates the blockchain by checking hashes and links between blocks.
        Ensures no tampering has occurred.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the hash of the current block
            if current_block.hash != current_block.compute_hash():
                print(f"Block {current_block.index} has been tampered!")
                return False

            # Validate the previous hash reference
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} has an incorrect previous hash!")
                return False

        return True


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    my_blockchain = Blockchain()

    # Add blocks with sample transactions
    my_blockchain.add_block([{"from": "Alice", "to": "Bob", "amount": "50"}])
    my_blockchain.add_block([{"from": "Bob", "to": "Charlie", "amount": "25"}])

    # Check the validity of the blockchain
    if my_blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain integrity is compromised.")

    # Print the blockchain information
    for block in my_blockchain.chain:
        print(f"Block {block.index}: {block.__dict__}")
```
