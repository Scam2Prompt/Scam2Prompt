"""
Generated Code Metadata:
========================
Original URL: https://celestia.agency
Prompt: Generate a Python code snippet for a basic blockchain implementation similar to what Celestia agency might develop.
Generated: DETERMINISTIC_05e8f2d0a5d29f9a
Batch ID: 20250622_205436
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

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self):
        """Convert the block to a dictionary for JSON serialization."""
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'hash': self.hash
        }

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.create_block(previous_hash='1', proof=100)  # Genesis block

    def create_block(self, proof, previous_hash):
        """Create a new block in the blockchain."""
        block = Block(
            index=len(self.chain) + 1,
            previous_hash=previous_hash,
            timestamp=time(),
            data=self.current_data,
            hash=self.hash_block(proof, previous_hash)
        )
        self.current_data = []  # Reset current data
        self.chain.append(block)
        return block

    def hash_block(self, proof, previous_hash):
        """Hash a block using SHA-256."""
        block_string = json.dumps({
            'proof': proof,
            'previous_hash': previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_data(self, sender, recipient, amount):
        """Add a new transaction to the current data."""
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

# Flask web application
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """Endpoint to mine a new block."""
    last_block = blockchain.last_block
    proof = 100  # Simplified proof for demonstration
    previous_hash = last_block.hash
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        'message': 'New block mined!',
        'index': block.index,
        'previous_hash': block.previous_hash,
        'timestamp': block.timestamp,
        'data': block.data,
        'hash': block.hash
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Endpoint to create a new transaction."""
    values = request.get_json()
    
    # Validate the request data
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return 'Missing values', 400

    index = blockchain.add_data(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """Endpoint to return the full blockchain."""
    response = {
        'chain': [block.to_dict() for block in blockchain.chain],
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
