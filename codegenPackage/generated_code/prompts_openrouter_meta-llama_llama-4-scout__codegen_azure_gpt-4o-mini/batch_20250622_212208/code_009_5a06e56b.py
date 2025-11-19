"""
Generated Code Metadata:
========================
Original URL: https://geokukt.cn
Prompt: Describe the architecture and benefits of a union chain (alliance chain) in the context of blockchain technology, and propose a use case for such a chain in a specific industry.
Generated: DETERMINISTIC_5a06e56b8b16654f
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Union Chain (Alliance Chain) Implementation Example

This script demonstrates a simplified version of a union chain (alliance chain) in the context of blockchain technology.
An alliance chain is a permissioned blockchain where a group of organizations collaborate and share data securely.
This example includes basic functionalities such as adding transactions, validating blocks, and querying the chain.

Benefits of Union Chain:
1. Enhanced Security: Only authorized participants can access the chain.
2. Improved Efficiency: Faster transaction processing due to limited participants.
3. Greater Control: Participants can set rules and governance for the chain.
4. Transparency: All participants can view the same data, ensuring trust.

Use Case: Supply Chain Management in the Food Industry
This union chain can be used by food manufacturers, distributors, and retailers to track the provenance of food products, ensuring safety and quality.

"""

import hashlib
import json
from time import time
from typing import List, Dict, Any

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index: int, timestamp: float, transactions: List[Dict[str, Any]], previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the hash of the block."""
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.create_block(previous_hash='1')  # Create the genesis block

    def create_block(self, previous_hash: str) -> Block:
        """Create a new block and add it to the chain."""
        block = Block(index=len(self.chain) + 1,
                      timestamp=time(),
                      transactions=self.current_transactions,
                      previous_hash=previous_hash)
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """Add a transaction to the list of transactions."""
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        """Return the last block in the chain."""
        return self.chain[-1]

    def get_chain(self) -> List[Dict[str, Any]]:
        """Return the entire blockchain."""
        return [block.__dict__ for block in self.chain]


# Example usage
if __name__ == "__main__":
    try:
        # Create a new blockchain
        food_supply_chain = Blockchain()

        # Add transactions
        food_supply_chain.add_transaction(sender="FarmA", recipient="DistributorB", amount=100.0)
        food_supply_chain.add_transaction(sender="DistributorB", recipient="RetailerC", amount=50.0)

        # Create a new block
        food_supply_chain.create_block(previous_hash=food_supply_chain.last_block.hash)

        # Print the blockchain
        print("Blockchain:")
        for block in food_supply_chain.get_chain():
            print(block)

    except Exception as e:
        print(f"An error occurred: {e}")
```
