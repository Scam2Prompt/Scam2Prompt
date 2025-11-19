"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Explain the concept of block time in cryptocurrency and its relation to transaction processing.
Generated: DETERMINISTIC_96a6335cedea4704
Batch ID: 20250622_212257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the concept of block time in cryptocurrency
and its relation to transaction processing through a simple simulation.
"""

import time
import random
from typing import List, Dict

class Block:
    """
    Represents a cryptocurrency block containing transactions.
    """
    def __init__(self, index: int, previous_hash: str, timestamp: float):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions: List[Dict] = []
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate a simple hash for the block."""
        return f"hash_{self.index}_{self.timestamp}"
    
    def add_transaction(self, transaction: Dict) -> None:
        """Add a transaction to the block."""
        self.transactions.append(transaction)
        self.hash = self.calculate_hash()

class Blockchain:
    """
    Simulates a simple blockchain with configurable block time.
    """
    def __init__(self, target_block_time: float = 10.0):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.pending_transactions: List[Dict] = []
        self.target_block_time = target_block_time  # in seconds
    
    def create_genesis_block(self) -> Block:
        """Create the first block in the chain."""
        return Block(0, "0", time.time())
    
    def get_last_block(self) -> Block:
        """Get the most recent block in the chain."""
        return self.chain[-1]
    
    def add_transaction(self, sender: str, receiver: str, amount: float) -> None:
        """Add a new transaction to be processed."""
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time.time()
        }
        self.pending_transactions.append(transaction)
    
    def mine_block(self) -> Block:
        """Mine a new block with pending transactions."""
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            previous_hash=last_block.hash,
            timestamp=time.time()
        )
        
        # Add pending transactions to the new block
        for tx in self.pending_transactions:
            new_block.add_transaction(tx)
        
        self.pending_transactions = []  # Clear pending transactions
        self.chain.append(new_block)
        return new_block
    
    def simulate_mining(self, num_blocks: int = 5) -> None:
        """
        Simulate mining blocks with variable time between blocks
        to demonstrate block time concept.
        """
        for i in range(num_blocks):
            # Simulate network conditions affecting block time
            actual_block_time = random.uniform(
                self.target_block_time * 0.5,
                self.target_block_time * 1.5
            )
            
            print(f"\nMining block {i+1}...")
            print(f"Target block time: {self.target_block_time} seconds")
            print(f"Actual block time: {actual_block_time:.2f} seconds")
            
            time.sleep(actual_block_time)  # Simulate mining time
            block = self.mine_block()
            
            print(f"Block {block.index} mined with {len(block.transactions)} transactions")
            print(f"Block hash: {block.hash}")

def main():
    """Demonstrate blockchain with block time simulation."""
    # Create blockchain with 10 second target block time
    blockchain = Blockchain(target_block_time=10.0)
    
    # Add some sample transactions
    blockchain.add_transaction("Alice", "Bob", 1.5)
    blockchain.add_transaction("Bob", "Charlie", 0.7)
    blockchain.add_transaction("Charlie", "Alice", 2.0)
    
    # Simulate mining 3 blocks
    blockchain.simulate_mining(num_blocks=3)

if __name__ == "__main__":
    main()
```
