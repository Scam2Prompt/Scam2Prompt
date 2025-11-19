"""
Generated Code Metadata:
========================
Original URL: https://en-bitcoin.org
Prompt: Explain the concept of consensus in Bitcoin Core and how it ensures the integrity of the blockchain.
Generated: DETERMINISTIC_fbaf1a941b76574f
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the concept of consensus in Bitcoin Core by simulating
how nodes validate and agree on new blocks being added to the blockchain.
"""

import hashlib
import json
from typing import List, Dict, Optional

class Block:
    """
    Represents a block in the blockchain with basic validation rules.
    """
    def __init__(self, index: int, previous_hash: str, transactions: List[Dict], timestamp: float, nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the SHA-256 hash of the block's contents.
        """
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def is_valid(self, previous_block: Optional['Block']) -> bool:
        """
        Validates the block against consensus rules:
        1. Correct index follows previous block
        2. Previous hash matches
        3. Valid hash meets difficulty requirement (simplified)
        4. Valid transactions (not implemented in this example)
        """
        if previous_block is None:
            return self.index == 0  # Genesis block
        
        if self.previous_hash != previous_block.hash:
            return False
        
        if self.index != previous_block.index + 1:
            return False
        
        # Simplified proof-of-work check (in real Bitcoin this would check leading zeros)
        if not self.hash.startswith("00"):
            return False
            
        return True

class Blockchain:
    """
    Represents the blockchain with consensus validation logic.
    """
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.difficulty = 2  # Number of leading zeros required for PoW

    @staticmethod
    def create_genesis_block() -> Block:
        """
        Creates the genesis block (first block in the chain).
        """
        return Block(0, "0", [], 0)

    def get_latest_block(self) -> Block:
        """
        Returns the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block) -> bool:
        """
        Attempts to add a new block to the chain after validating it.
        Returns True if block was added successfully.
        """
        if not new_block.is_valid(self.get_latest_block()):
            return False
        
        self.chain.append(new_block)
        return True

    def is_chain_valid(self) -> bool:
        """
        Validates the entire blockchain's integrity.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if not current_block.is_valid(previous_block):
                return False
        
        return True

    def proof_of_work(self, block: Block) -> Block:
        """
        Simple proof-of-work algorithm that finds a valid hash.
        """
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block

def simulate_consensus():
    """
    Demonstrates how nodes reach consensus by validating and adding blocks.
    """
    blockchain = Blockchain()
    
    print("Creating blockchain...")
    print(f"Genesis block hash: {blockchain.chain[0].hash}")
    
    # Simulate adding new blocks
    for i in range(1, 4):
        new_block = Block(
            index=i,
            previous_hash=blockchain.get_latest_block().hash,
            transactions=[{"from": "Alice", "to": "Bob", "amount": i}],
            timestamp=i
        )
        
        # Perform proof-of-work
        new_block = blockchain.proof_of_work(new_block)
        
        # Attempt to add block
        if blockchain.add_block(new_block):
            print(f"Block {i} added successfully. Hash: {new_block.hash}")
        else:
            print(f"Block {i} rejected by consensus rules")
    
    # Validate chain integrity
    print("\nBlockchain valid:", blockchain.is_chain_valid())
    
    # Attempt to tamper with the chain
    print("\nAttempting to tamper with the chain...")
    blockchain.chain[1].transactions = [{"from": "Eve", "to": "Eve", "amount": 100}]
    blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()
    print("Blockchain valid after tampering:", blockchain.is_chain_valid())

if __name__ == "__main__":
    simulate_consensus()
```
