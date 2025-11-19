"""
Generated Code Metadata:
========================
Original URL: https://celestia.agency
Prompt: Generate a Python code snippet for a basic blockchain implementation similar to what Celestia agency might develop.
Generated: DETERMINISTIC_05e8f2d0a5d29f9a
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from time import time
from typing import List, Dict, Any, Optional

class Block:
    """
    A single block in the blockchain.
    """
    def __init__(self, index: int, transactions: List[Dict], timestamp: float, previous_hash: str, nonce: int = 0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self) -> str:
        """
        Returns the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    The blockchain class containing the chain of blocks.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict] = []
        self.create_genesis_block()
        self.difficulty = 2  # Adjust difficulty for PoW

    def create_genesis_block(self) -> None:
        """
        Creates the genesis block and adds it to the chain.
        """
        genesis_block = Block(0, [], time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, block: Block, proof: str) -> bool:
        """
        Adds a new block to the blockchain after verification.
        """
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        """
        Validates the proof by checking if the hash meets difficulty criteria.
        """
        return (block_hash.startswith('0' * self.difficulty) and 
                block_hash == block.compute_hash())

    def proof_of_work(self, block: Block) -> str:
        """
        Simple Proof of Work algorithm.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_new_transaction(self, transaction: Dict) -> None:
        """
        Adds a new transaction to the list of transactions.
        """
        self.current_transactions.append(transaction)

    @property
    def last_block(self) -> Block:
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]

    def mine(self) -> Optional[int]:
        """
        Mines a new block and adds it to the chain.
        """
        if not self.current_transactions:
            return None

        last_block = self.last_block
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.current_transactions,
            timestamp=time(),
            previous_hash=last_block.hash
        )

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.current_transactions = []
        return new_block.index

    def is_chain_valid(self) -> bool:
        """
        Validates the entire blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
```
