"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: Suggest best practices for implementing energy-efficient consensus mechanisms in a blockchain-based gaming platform like BetSwirl.
Generated: DETERMINISTIC_3fd63eca99cd318a
Batch ID: 20250612_152620
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
from typing import List, Dict, Any

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    @staticmethod
    def calculate_hash(index: int, previous_hash: str, timestamp: float, data: Any) -> str:
        """Calculate the hash of a block."""
        value = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(value).hexdigest()

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain."""
        genesis_block = Block(0, "0", time.time(), "Genesis Block", Block.calculate_hash(0, "0", time.time(), "Genesis Block"))
        self.chain.append(genesis_block)

    def add_block(self, data: Any):
        """Add a new block to the blockchain."""
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        hash = Block.calculate_hash(index, previous_block.hash, timestamp, data)
        new_block = Block(index, previous_block.hash, timestamp, data, hash)
        self.chain.append(new_block)

    def get_chain(self) -> List[Dict[str, Any]]:
        """Return the blockchain as a list of dictionaries."""
        return [{"index": block.index, "previous_hash": block.previous_hash, "timestamp": block.timestamp, "data": block.data, "hash": block.hash} for block in self.chain]

def main():
    """Main function to demonstrate blockchain functionality."""
    try:
        # Initialize the blockchain
        bet_swirl_blockchain = Blockchain()
        
        # Simulate adding blocks with game data
        bet_swirl_blockchain.add_block({"game": "Poker", "winner": "Player1"})
        bet_swirl_blockchain.add_block({"game": "Blackjack", "winner": "Player2"})
        
        # Output the blockchain
        for block in bet_swirl_blockchain.get_chain():
            print(block)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
