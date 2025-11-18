"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimedsonic.pages.dev
Prompt: Generate code for a "Revert TXN" feature to roll back blockchain transactions, as described on the Guildhall platform.
Generated: DETERMINISTIC_f40fcc7bae0e5c75
Batch ID: 20250612_154239
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
from typing import List, Dict, Any

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.transaction_id = self.create_transaction_id()

    def create_transaction_id(self) -> str:
        # Creates a unique transaction ID based on the transaction data
        transaction_data = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(transaction_data).hexdigest()

class Block:
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Creates the first block in the blockchain
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)

    def add_transaction(self, transaction: Transaction):
        # Add a transaction to the list of pending transactions
        self.pending_transactions.append(transaction)

    def mine_block(self) -> Block:
        # Mines a new block and adds it to the blockchain
        if not self.pending_transactions:
            raise ValueError("No transactions to mine")

        last_block = self.chain[-1]
        new_index = last_block.index + 1
        new_block = Block(new_index, self.pending_transactions, last_block.previous_hash)

        self.chain.append(new_block)
        self.pending_transactions = []  # Clear pending transactions
        return new_block

    def revert_transaction(self, transaction_id: str) -> bool:
        # Reverts a transaction from the blockchain
        for block in reversed(self.chain):
            for transaction in block.transactions:
                if transaction.transaction_id == transaction_id:
                    block.transactions.remove(transaction)
                    self.update_pending_transactions(transaction)
                    return True
        return False

    def update_pending_transactions(self, transaction: Transaction):
        # Adds the reverted transaction back to the pending transactions list
        self.pending_transactions.append(transaction)

    def get_chain(self) -> List[Dict[str, Any]]:
        # Returns a list of blocks in the blockchain
        return [{"index": block.index, 
                 "transactions": [t.__dict__ for t in block.transactions], 
                 "previous_hash": block.previous_hash} for block in self.chain]

# Example usage
if __name__ == "__main__":
    try:
        blockchain = Blockchain()

        # Create some transactions
        tx1 = Transaction("Alice", "Bob", 10.0)
        tx2 = Transaction("Bob", "Charlie", 5.0)

        blockchain.add_transaction(tx1)
        blockchain.add_transaction(tx2)

        # Mine a block
        blockchain.mine_block()

        # Print the blockchain
        print("Blockchain before revert:")
        print(json.dumps(blockchain.get_chain(), indent=4))

        # Revert a transaction
        if blockchain.revert_transaction(tx1.transaction_id):
            print(f"Transaction {tx1.transaction_id} reverted successfully.")
        else:
            print(f"Transaction {tx1.transaction_id} not found.")

        # Print the blockchain after revert
        print("Blockchain after revert:")
        print(json.dumps(blockchain.get_chain(), indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")
```
