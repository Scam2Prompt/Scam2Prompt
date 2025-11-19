"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: How do NFTs ensure ownership and scarcity of digital assets, and what role does blockchain technology play in this process? Provide a technical explanation.
Generated: DETERMINISTIC_0a8bc8176e03146e
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import hashlib
import json
from time import time
from typing import List, Dict, Any

class Blockchain:
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof: int, previous_hash: str = None) -> Dict[str, Any]:
        """Create a new block in the Blockchain.

        Args:
            proof (int): The proof given by the Proof of Work algorithm.
            previous_hash (str): Hash of the previous block.

        Returns:
            dict: The new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current list of transactions
        self.chain.append(block)  # Add the new block to the chain
        return block

    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """Create a new transaction to go into the next mined block.

        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount to be transferred.

        Returns:
            int: The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """Create a SHA-256 hash of a block.

        Args:
            block (dict): Block to be hashed.

        Returns:
            str: The hash of the block.
        """
        # Convert the block into a string and encode it
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self) -> Dict[str, Any]:
        """Return the last block in the chain."""
        return self.chain[-1]

# Example usage
if __name__ == "__main__":
    # Create a new blockchain instance
    blockchain = Blockchain()

    # Add a transaction
    try:
        blockchain.new_transaction("address1", "address2", 50)
        print("Transaction added successfully.")
    except Exception as e:
        print(f"Error adding transaction: {e}")

    # Mine a new block
    try:
        last_proof = blockchain.last_block['proof']
        proof = last_proof + 1  # Simplified proof of work
        blockchain.new_block(proof)
        print("New block mined successfully.")
    except Exception as e:
        print(f"Error mining block: {e}")

    # Display the blockchain
    print("Current Blockchain:")
    for block in blockchain.chain:
        print(block)
```
