"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-com.pages.dev
Prompt: What are the steps to integrate blockchain technology into a crude oil investment platform like Crudo Protocol?
Generated: DETERMINISTIC_8456e7bf7c49b4ee
Batch ID: 20250612_155159
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
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []  # Initialize the blockchain
        self.current_transactions = []  # Store transactions
        self.new_block(previous_hash='1', proof=100)  # Create genesis block

    def new_block(self, proof, previous_hash=None):
        """Creates a new block in the Blockchain."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current transactions list
        self.chain.append(block)  # Add new block to the chain
        return block

    def new_transaction(self, sender, recipient, amount):
        """Adds a new transaction to the list of transactions."""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1  # Return the index of the block that will contain this transaction

    @staticmethod
    def hash(block):
        """Creates a SHA-256 hash of a block."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Returns the last block in the blockchain."""
        return self.chain[-1]

# Initialize Flask web application
app = Flask(__name__)

# Create an instance of the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine():
    """Mining a new block and adding it to the blockchain."""
    # Get the last proof from the blockchain
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    
    # Here, implement a proof of work algorithm (simplified for demonstration)
    proof = last_proof + 1  # Simplified increment for proof
    
    # Create a new block
    blockchain.new_block(proof, previous_hash=blockchain.hash(last_block))
    
    response = {
        'message': 'New block mined!',
        'index': blockchain.last_block['index'],
        'transactions': blockchain.last_block['transactions'],
        'proof': blockchain.last_block['proof'],
        'previous_hash': blockchain.last_block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Create a new transaction."""
    values = request.get_json()  # Get JSON data from the request
    required_fields = ['sender', 'recipient', 'amount']
    
    # Validate data
    if not all(field in values for field in required_fields):
        return 'Missing values', 400  # Return error if data is invalid

    # Create the new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {
        'message': f'Transaction will be added to Block {index}'
    }
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """Return the full blockchain."""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)  # Run the Flask app
    except Exception as e:
        print(f"Error starting the application: {e}")  # Handle errors gracefully
```
