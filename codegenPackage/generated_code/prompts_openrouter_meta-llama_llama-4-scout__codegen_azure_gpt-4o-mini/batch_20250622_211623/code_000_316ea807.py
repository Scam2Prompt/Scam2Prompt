"""
Generated Code Metadata:
========================
Original URL: https://lightchain.live-apps.com
Prompt: "Write a Python code snippet to implement a basic Proof of Intelligence (PoI) consensus mechanism as described in the Lightchain AI protocol."
Generated: DETERMINISTIC_316ea807ecfd85a6
Batch ID: 20250622_211623
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
import random
from typing import List, Dict, Any

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, data: Any, timestamp: float = None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the hash of the block using SHA-256."""
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}".encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain."""
        genesis_block = Block(0, "0", "Genesis Block")
        self.chain.append(genesis_block)

    def add_block(self, data: Any):
        """Add a new block to the blockchain."""
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.chain.append(new_block)

    def get_chain(self) -> List[Dict[str, Any]]:
        """Return the blockchain as a list of dictionaries."""
        return [vars(block) for block in self.chain]


class ProofOfIntelligence:
    """Class implementing the Proof of Intelligence consensus mechanism."""
    
    def __init__(self):
        self.blockchain = Blockchain()

    def generate_intelligence_proof(self) -> int:
        """Simulate the generation of a proof of intelligence."""
        # Simulate a random proof of intelligence
        return random.randint(1, 100)

    def validate_proof(self, proof: int) -> bool:
        """Validate the proof of intelligence."""
        # Simple validation: proof must be even
        return proof % 2 == 0

    def add_block_with_proof(self, data: Any):
        """Add a block to the blockchain after validating the proof of intelligence."""
        proof = self.generate_intelligence_proof()
        if self.validate_proof(proof):
            self.blockchain.add_block(data)
            print(f"Block added with proof: {proof}")
        else:
            raise ValueError("Invalid proof of intelligence.")


# Example usage
if __name__ == "__main__":
    try:
        poi = ProofOfIntelligence()
        poi.add_block_with_proof("First block data")
        poi.add_block_with_proof("Second block data")
        
        # Print the blockchain
        for block in poi.blockchain.get_chain():
            print(block)
    except Exception as e:
        print(f"An error occurred: {e}")
```
