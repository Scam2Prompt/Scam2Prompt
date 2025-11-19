"""
Generated Code Metadata:
========================
Original URL: https://it-ledger.com
Prompt: What are the advantages of using a digital ledger in IT project management, and how can it be set up for a startup?
Generated: DETERMINISTIC_187662f965954fbf
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Ledger Setup for IT Project Management

This script outlines the advantages of using a digital ledger in IT project management
and provides a basic setup for a startup using a simple blockchain-like structure.
"""

import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class DigitalLedger:
    def __init__(self):
        """Initialize the ledger with an empty chain and a list of transactions."""
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash=None):
        """Create a new block in the ledger.

        Args:
            proof (int): The proof of work for the new block.
            previous_hash (str): Hash of the previous block.

        Returns:
            dict: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)  # Add the new block to the chain
        return block

    def new_transaction(self, sender, recipient, amount):
        """Add a new transaction to the list of transactions.

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
    def hash(block):
        """Create a SHA-256 hash of a block.

        Args:
            block (dict): The block to hash.

        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

# Flask web application to interact with the digital ledger
app = Flask(__name__)
ledger = DigitalLedger()

@app.route('/mine', methods=['GET'])
def mine():
    """Mine a new block and add it to the ledger."""
    last_block = ledger.last_block
    proof = 100  # Placeholder for proof of work
    previous_hash = ledger.hash(last_block)
    block = ledger.create_block(proof, previous_hash)
    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Create a new transaction.

    Returns:
        json: Response containing the index of the block that will hold the transaction.
    """
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = ledger.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """Return the full digital ledger."""
    response = {
        'chain': ledger.chain,
        'length': len(ledger.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred: {e}")
```
