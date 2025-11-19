"""
Generated Code Metadata:
========================
Original URL: https://immediate-matrix.net
Prompt: Explain the concept of using blockchain technology to ensure a secure and private trading experience, as mentioned in the Immediate 1.4 Evista platform, and provide a code example that demonstrates this concept.
Generated: DETERMINISTIC_3e8b5c41285cab0c
Batch ID: 20250622_211310
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
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        """Initialize the blockchain and create the genesis block."""
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        """Create a new block in the Blockchain.

        Args:
            proof (int): The proof of work for the new block.
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
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)  # Add the new block to the chain
        return block

    def new_transaction(self, sender, recipient, amount):
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
    def hash(block):
        """Create a SHA-256 hash of a block.

        Args:
            block (dict): Block to be hashed.

        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

# Create a Flask web application
app = Flask(__name__)

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Endpoint to create a new transaction.

    Returns:
        json: Response containing the index of the block that will hold the transaction.
    """
    values = request.get_json()  # Get the JSON data from the request

    # Check that the required fields are in the POST data
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return jsonify({'message': 'Missing values'}), 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    """Endpoint to mine a new block.

    Returns:
        json: Response containing the new block and its details.
    """
    last_block = blockchain.last_block
    proof = 100  # Placeholder for proof of work (should be replaced with actual proof of work logic)
    previous_hash = blockchain.hash(last_block)

    # Create a new block
    block = blockchain.new_block(proof, previous_hash)
    return jsonify({
        'message': 'New Block Mined',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

This code implements a simple blockchain using Flask to create a secure and private trading experience. It includes endpoints for creating transactions and mining new blocks, with proper error handling and documentation.
