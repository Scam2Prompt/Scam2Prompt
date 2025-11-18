"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steemit-monadscore.blogspot.com
Prompt: Write code to implement a secure and transparent payment system for AI solutions in a blockchain-based marketplace like Anaphora AI.
Generated: DETERMINISTIC_74fe69dab2c43b39
Batch ID: 20250612_154115
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
from datetime import datetime
from typing import List, Dict, Any

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction data to a dictionary."""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

class Blockchain:
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Transaction] = []
        self.new_block(previous_hash='1')  # Creating the genesis block

    def new_block(self, previous_hash: str = None) -> Dict[str, Any]:
        """Create a new block in the blockchain."""
        block = {
            'index': len(self.chain) + 1,
            'transactions': [tx.to_dict() for tx in self.current_transactions],
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'timestamp': datetime.utcnow().isoformat()
        }
        self.current_transactions = []  # Reset current transactions
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """Create a SHA-256 hash of a block."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, transaction: Transaction) -> int:
        """Add a transaction to the list of transactions."""
        if self.validate_transaction(transaction):
            self.current_transactions.append(transaction)
            return self.last_block['index'] + 1
        else:
            raise ValueError("Invalid transaction")

    @property
    def last_block(self) -> Dict[str, Any]:
        """Return the last block in the blockchain."""
        return self.chain[-1]

    def validate_transaction(self, transaction: Transaction) -> bool:
        """Validate a transaction (basic checks)."""
        if transaction.amount <= 0:
            return False
        if not transaction.sender or not transaction.recipient:
            return False
        # Additional validations can be added here
        return True

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        blockchain = Blockchain()

        # Create a transaction
        tx1 = Transaction(sender="Alice", recipient="Bob", amount=50.0)
        blockchain.add_transaction(tx1)

        # Create a new block
        block = blockchain.new_block(previous_hash=blockchain.hash(blockchain.last_block))

        print("New Block:", block)
    except Exception as e:
        print(f"An error occurred: {e}")
```
