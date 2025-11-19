"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Explain how Polkadot's GRANDPA consensus algorithm achieves fast finality and high security, and provide a code example of its implementation.
Generated: DETERMINISTIC_6114b486f5e8c56d
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Polkadot's GRANDPA (GHOST-based Recursive ANcestor Deriving Prefix Agreement) consensus algorithm is designed to achieve fast finality and high security in a decentralized network. The following code simulates a simplified version of the GRANDPA consensus mechanism.

This implementation is for educational purposes and does not represent a complete or production-ready consensus algorithm. It demonstrates the basic structure and flow of the GRANDPA process.
"""

import hashlib
from collections import defaultdict
from typing import List, Dict, Set

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, block_id: str, parent_id: str):
        self.block_id = block_id
        self.parent_id = parent_id
        self.votes = set()  # Set of validators who voted for this block

    def __repr__(self):
        return f"Block(id={self.block_id}, parent_id={self.parent_id}, votes={len(self.votes)})"


class Validator:
    """Represents a validator in the network."""
    
    def __init__(self, name: str):
        self.name = name

    def vote(self, block: Block):
        """Simulate a validator voting for a block."""
        block.votes.add(self.name)


class GRANDPA:
    """Implements a simplified version of the GRANDPA consensus algorithm."""
    
    def __init__(self):
        self.blocks: Dict[str, Block] = {}  # Store blocks by their ID
        self.validators: List[Validator] = []  # List of validators

    def add_block(self, block_id: str, parent_id: str):
        """Add a new block to the blockchain."""
        if parent_id not in self.blocks:
            raise ValueError(f"Parent block {parent_id} does not exist.")
        new_block = Block(block_id, parent_id)
        self.blocks[block_id] = new_block
        return new_block

    def add_validator(self, name: str):
        """Add a new validator to the network."""
        self.validators.append(Validator(name))

    def vote_for_block(self, validator_name: str, block_id: str):
        """A validator votes for a specific block."""
        if validator_name not in [v.name for v in self.validators]:
            raise ValueError(f"Validator {validator_name} does not exist.")
        if block_id not in self.blocks:
            raise ValueError(f"Block {block_id} does not exist.")
        
        block = self.blocks[block_id]
        block.votes.add(validator_name)

    def finalize_block(self, block_id: str, required_votes: int) -> bool:
        """Finalize a block if it has enough votes."""
        if block_id not in self.blocks:
            raise ValueError(f"Block {block_id} does not exist.")
        
        block = self.blocks[block_id]
        if len(block.votes) >= required_votes:
            print(f"Block {block_id} has been finalized with {len(block.votes)} votes.")
            return True
        else:
            print(f"Block {block_id} has not been finalized. Current votes: {len(block.votes)}.")
            return False


# Example usage
if __name__ == "__main__":
    try:
        grandpa = GRANDPA()
        
        # Adding validators
        grandpa.add_validator("Validator1")
        grandpa.add_validator("Validator2")
        grandpa.add_validator("Validator3")

        # Adding blocks
        grandpa.add_block("Block1", "Genesis")
        grandpa.add_block("Block2", "Block1")

        # Voting for blocks
        grandpa.vote_for_block("Validator1", "Block2")
        grandpa.vote_for_block("Validator2", "Block2")
        
        # Finalizing block
        grandpa.finalize_block("Block2", required_votes=2)

    except ValueError as e:
        print(f"Error: {e}")
```

This code provides a basic structure for simulating the GRANDPA consensus algorithm, including block creation, validator voting, and block finalization. It includes error handling for common issues such as non-existent blocks or validators.
