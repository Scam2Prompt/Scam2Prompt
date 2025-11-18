"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Generate code using a blockchain-based solution to ensure transparency in donation tracking, similar to Dysnix's transparent reporting of funds used for vehicle purchases.
Generated: DETERMINISTIC_fb7288c07226bce6
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from hashlib import sha256
from datetime import datetime
import json
from typing import List, Dict

class Transaction:
    """Represents a single transaction in the blockchain."""
    
    def __init__(self, donor: str, amount: float, timestamp: str):
        self.donor = donor
        self.amount = amount
        self.timestamp = timestamp
    
    def to_dict(self) -> Dict:
        """Convert the transaction to a dictionary."""
        return {
            'donor': self.donor,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

class Block:
    """Represents a block in the blockchain containing multiple transactions."""
    
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.timestamp = str(datetime.utcnow())
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate the hash of the block using SHA-256."""
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return sha256(block_string).hexdigest()
    
    def to_dict(self) -> Dict:
        """Convert the block to a dictionary."""
        return {
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }

class Blockchain:
    """Represents the blockchain which holds all blocks and transactions."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        self.create_block(previous_hash='0')  # Genesis block
    
    def create_block(self, previous_hash: str) -> Block:
        """Create a new block and add it to the blockchain."""
        block = Block(index=len(self.chain) + 1, transactions=self.current_transactions, previous_hash=previous_hash)
        self.current_transactions = []  # Reset current transactions
        self.chain.append(block)
        return block
    
    def add_transaction(self, donor: str, amount: float) -> None:
        """Add a new transaction to the list of transactions."""
        timestamp = str(datetime.utcnow())
        transaction = Transaction(donor=donor, amount=amount, timestamp=timestamp)
        self.current_transactions.append(transaction)
    
    def get_chain(self) -> List[Dict]:
        """Return the entire blockchain."""
        return [block.to_dict() for block in self.chain]
    
    def validate_chain(self) -> bool:
        """Validate the blockchain to ensure integrity."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if the hash of the block is correct
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Check if the previous hash is correct
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True

# Example usage (this would normally be in a separate module or script)

if __name__ == "__main__":
    try:
        # Initialize the blockchain
        donation_chain = Blockchain()
        
        # Add transactions
        donation_chain.add_transaction("Alice", 100.0)
        donation_chain.add_transaction("Bob", 50.0)
        
        # Create a new block
        donation_chain.create_block(previous_hash=donation_chain.chain[-1].hash)
        
        # Validate the blockchain
        if donation_chain.validate_chain():
            print("Blockchain is valid.")
        else:
            print("Blockchain is invalid.")
        
        # Output the blockchain
        print(json.dumps(donation_chain.get_chain(), indent=4))
    
    except Exception as e:
        print("An error occurred:", str(e))
```
