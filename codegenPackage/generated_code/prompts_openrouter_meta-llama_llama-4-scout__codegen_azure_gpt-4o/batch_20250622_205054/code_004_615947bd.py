"""
Generated Code Metadata:
========================
Original URL: https://racedata-fix.pages.dev
Prompt: Design a system to authenticate and verify digital artwork ownership using blockchain technology, similar to the approach described on the App Trust Fixed platform.
Generated: DETERMINISTIC_615947bd84db1862
Batch ID: 20250622_205054
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
import time
from typing import List, Dict, Any

class Blockchain:
    """
    A simple blockchain implementation for authenticating and verifying digital artwork ownership.
    """

    def __init__(self):
        self.chain: List[Dict[str, Any]] = []  # The blockchain (list of blocks)
        self.pending_transactions: List[Dict[str, Any]] = []  # Transactions waiting to be added to a block
        self.create_block(previous_hash="0")  # Create the genesis block

    def create_block(self, previous_hash: str) -> Dict[str, Any]:
        """
        Create a new block and add it to the blockchain.
        :param previous_hash: Hash of the previous block in the chain.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': self.hash_block(self.pending_transactions, previous_hash)
        }
        self.pending_transactions = []  # Clear pending transactions
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(transactions: List[Dict[str, Any]], previous_hash: str) -> str:
        """
        Generate a hash for a block.
        :param transactions: List of transactions in the block.
        :param previous_hash: Hash of the previous block.
        :return: The hash of the block.
        """
        block_string = json.dumps({'transactions': transactions, 'previous_hash': previous_hash}, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_transaction(self, artwork_id: str, owner: str) -> Dict[str, Any]:
        """
        Add a new transaction to the list of pending transactions.
        :param artwork_id: Unique identifier for the digital artwork.
        :param owner: Owner of the artwork.
        :return: The transaction added.
        """
        transaction = {
            'artwork_id': artwork_id,
            'owner': owner,
            'timestamp': time.time()
        }
        self.pending_transactions.append(transaction)
        return transaction

    def verify_ownership(self, artwork_id: str) -> str:
        """
        Verify the current owner of a digital artwork.
        :param artwork_id: Unique identifier for the digital artwork.
        :return: The current owner of the artwork or a message indicating no ownership found.
        """
        for block in reversed(self.chain):  # Traverse the chain in reverse order
            for transaction in block['transactions']:
                if transaction['artwork_id'] == artwork_id:
                    return transaction['owner']
        return "Ownership not found."

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the current block matches its calculated hash
            if current_block['hash'] != self.hash_block(current_block['transactions'], current_block['previous_hash']):
                return False

            # Check if the previous hash in the current block matches the hash of the previous block
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True


# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Add transactions
    blockchain.add_transaction(artwork_id="ART123", owner="Alice")
    blockchain.add_transaction(artwork_id="ART456", owner="Bob")

    # Create a new block
    blockchain.create_block(previous_hash=blockchain.chain[-1]['hash'])

    # Verify ownership
    print("Owner of ART123:", blockchain.verify_ownership("ART123"))
    print("Owner of ART456:", blockchain.verify_ownership("ART456"))

    # Validate blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())
```
