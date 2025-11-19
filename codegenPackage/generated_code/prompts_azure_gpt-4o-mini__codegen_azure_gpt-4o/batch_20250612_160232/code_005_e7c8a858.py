"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: How can I implement a decentralized funding model for small businesses inspired by the Viva La Libertad Project's mission?
Generated: DETERMINISTIC_e7c8a858826d606e
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a decentralized funding model for small businesses inspired by the Viva La Libertad Project's mission. The code uses blockchain principles to ensure transparency and decentralization.

```python
import hashlib
import json
from time import time
from typing import List, Dict, Any


class Blockchain:
    """
    A simple blockchain implementation for decentralized funding.
    Each block contains funding transactions for small businesses.
    """

    def __init__(self):
        self.chain: List[Dict[str, Any]] = []  # The blockchain (list of blocks)
        self.current_transactions: List[Dict[str, Any]] = []  # Pending transactions
        self.create_block(proof=1, previous_hash="0")  # Create the genesis block

    def create_block(self, proof: int, previous_hash: str) -> Dict[str, Any]:
        """
        Create a new block and add it to the blockchain.

        :param proof: The proof of work for the block.
        :param previous_hash: The hash of the previous block in the chain.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }

        # Reset the list of current transactions
        self.current_transactions = []

        # Add the new block to the chain
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Add a new transaction to the list of pending transactions.

        :param sender: The address of the sender.
        :param recipient: The address of the recipient (small business).
        :param amount: The funding amount.
        :return: The index of the block that will hold this transaction.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }

        self.current_transactions.append(transaction)
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """
        Create a SHA-256 hash of a block.

        :param block: The block to hash.
        :return: The hash of the block.
        """
        # Ensure the dictionary is ordered to produce consistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self) -> Dict[str, Any]:
        """
        Return the last block in the chain.

        :return: The last block.
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work algorithm:
        - Find a number p such that hash(p + last_proof) contains leading zeros.

        :param last_proof: The proof of the previous block.
        :return: The new proof.
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validate the proof: Does hash(last_proof + proof) contain leading zeros?

        :param last_proof: The proof of the previous block.
        :param proof: The current proof.
        :return: True if valid, False otherwise.
        """
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Adjust difficulty as needed


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add funding transactions
    try:
        blockchain.add_transaction(sender="Donor1", recipient="SmallBusiness1", amount=100.0)
        blockchain.add_transaction(sender="Donor2", recipient="SmallBusiness2", amount=200.0)
    except ValueError as e:
        print(f"Error adding transaction: {e}")

    # Perform proof of work and create a new block
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = blockchain.hash(blockchain.last_block)
    blockchain.create_block(proof, previous_hash)

    # Print the blockchain
    print(json.dumps(blockchain.chain, indent=4))
```

This code implements a basic blockchain for decentralized funding, allowing donors to send funds to small businesses. It includes error handling for invalid transactions and uses a simple proof-of-work mechanism for block validation.
