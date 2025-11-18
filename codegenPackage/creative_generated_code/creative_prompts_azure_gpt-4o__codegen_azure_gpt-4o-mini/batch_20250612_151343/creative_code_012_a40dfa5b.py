"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdag-8bz.pages.dev
Prompt: Generate code to integrate BlockDAG's cryptographic algorithms into a secure blockchain application.
Generated: DETERMINISTIC_a40dfa5b263feaab
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from time import time
from typing import List, Dict, Any

class Block:
    def __init__(self, index: int, transactions: List[Dict[str, Any]], timestamp: float, previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.
        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.create_block(transactions=[], previous_hash='0')  # Create genesis block

    def create_block(self, transactions: List[Dict[str, Any]], previous_hash: str) -> Block:
        """
        Create a new block and add it to the chain.
        Args:
            transactions (List[Dict[str, Any]]): List of transactions to include in the block.
            previous_hash (str): Hash of the previous block.
        Returns:
            Block: The newly created block.
        """
        index = len(self.chain) + 1
        timestamp = time()
        block = Block(index, transactions, timestamp, previous_hash)
        self.chain.append(block)
        return block

    def get_previous_block(self) -> Block:
        """
        Get the previous block in the chain.
        Returns:
            Block: The last block in the chain.
        """
        if not self.chain:
            raise Exception("Blockchain is empty. No previous block found.")
        return self.chain[-1]

    def add_transaction(self, transaction: Dict[str, Any]) -> None:
        """
        Add a transaction to the list of transactions.
        Args:
            transaction (Dict[str, Any]): The transaction to add.
        """
        if not isinstance(transaction, dict):
            raise ValueError("Transaction must be a dictionary.")
        self.get_previous_block().transactions.append(transaction)

    def mine_block(self) -> None:
        """
        Mine a new block by adding it to the blockchain with collected transactions.
        """
        previous_block = self.get_previous_block()
        new_block = self.create_block(previous_block.transactions, previous_block.hash)
        print(f"Block {new_block.index} mined!")
        print(f"Hash: {new_block.hash}")

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Adding transactions
    try:
        blockchain.add_transaction({"sender": "Alice", "recipient": "Bob", "amount": 10})
        blockchain.add_transaction({"sender": "Bob", "recipient": "Charlie", "amount": 15})

        # Mine the block
        blockchain.mine_block()
    except Exception as e:
        print(f"Error: {e}")
```

This code defines a basic blockchain structure using classes for blocks and the blockchain itself. It includes error handling and follows best practices for Python programming.
