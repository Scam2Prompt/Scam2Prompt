"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediaterevolution360.co
Prompt: Write a script to simulate the creation and detection of zero-confirmation transactions in a blockchain environment, based on the explanation provided by Omega Blockitex.
Generated: DETERMINISTIC_0f7cc3bbd4ed0925
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import hashlib
import json

class Transaction:
    """Class to represent a blockchain transaction."""
    
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.tx_id = self.generate_tx_id()

    def generate_tx_id(self):
        """Generates a unique transaction ID using SHA256 hash."""
        tx_data = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}".encode('utf-8')
        return hashlib.sha256(tx_data).hexdigest()

    def to_dict(self):
        """Converts the transaction to a dictionary for easy serialization."""
        return {
            'tx_id': self.tx_id,
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

class Blockchain:
    """Class to represent a simple blockchain."""
    
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        
    def add_transaction(self, transaction):
        """Adds a transaction to the pending list."""
        if isinstance(transaction, Transaction):
            self.pending_transactions.append(transaction)
        else:
            raise ValueError("Only Transaction instances can be added.")

    def mine_block(self):
        """Simulates mining a block by moving pending transactions to the blockchain."""
        if not self.pending_transactions:
            raise Exception("No transactions to mine.")
        
        block = {
            'block_number': len(self.chain) + 1,
            'transactions': [tx.to_dict() for tx in self.pending_transactions],
            'timestamp': time.time(),
            'block_id': hashlib.sha256(json.dumps(self.pending_transactions).encode('utf-8')).hexdigest()
        }
        
        self.chain.append(block)
        self.pending_transactions = []  # Clear pending transactions after mining
        return block

    def detect_zero_confirmation(self):
        """Detects zero-confirmation transactions which are in the pending pool."""
        return [tx.to_dict() for tx in self.pending_transactions]

def main():
    # Initialize the blockchain
    blockchain = Blockchain()
    
    # Create and add transactions
    try:
        tx1 = Transaction('Alice', 'Bob', 10)
        tx2 = Transaction('Bob', 'Charlie', 5)
        tx3 = Transaction('Alice', 'Charlie', 7)
        
        blockchain.add_transaction(tx1)
        blockchain.add_transaction(tx2)
        blockchain.add_transaction(tx3)

        # Print zero-confirmation transactions
        print("Zero-confirmation transactions:")
        print(blockchain.detect_zero_confirmation())

        # Mine a block
        mined_block = blockchain.mine_block()
        print("Mined Block:")
        print(mined_block)

        # Check for zero-confirmation transactions post mining
        print("Zero-confirmation transactions after mining:")
        print(blockchain.detect_zero_confirmation())

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
