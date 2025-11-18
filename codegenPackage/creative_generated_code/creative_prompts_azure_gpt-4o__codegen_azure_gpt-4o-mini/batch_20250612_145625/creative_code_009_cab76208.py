"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Create a blockchain-based voting system for the DEKSA community to decide on future virtual kingdom features, using $MASA tokens as voting power.
Generated: DETERMINISTIC_cab762088661671e
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from hashlib import sha256
from time import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# Create a Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        # Create a new block in the blockchain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'votes': self.current_votes,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_votes = []  # Reset the current votes list
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        # Generate a SHA-256 hash of a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def new_vote(self, voter_id, feature):
        # Add a new vote to the current votes
        self.current_votes.append({
            'voter_id': voter_id,
            'feature': feature
        })
        return self.last_block['index'] + 1  # Return the index of the block that will hold this vote

    @property
    def last_block(self):
        # Return the last block in the chain
        return self.chain[-1]


# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    # API endpoint to cast a vote
    values = request.get_json()

    if not values or 'voter_id' not in values or 'feature' not in values:
        return jsonify({'message': 'Missing voter_id or feature'}), 400

    # Register the vote
    vote_index = blockchain.new_vote(values['voter_id'], values['feature'])
    response = {
        'message': f'Vote added to block {vote_index}',
    }
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    # API endpoint to mine a new block
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = blockchain.hash(last_block)

    # Create a new block and add it to the chain
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'New Block Mined',
        'index': block['index'],
        'votes': block['votes'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    # API endpoint to get the full blockchain
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Please ensure you have the required libraries installed for this code to run. You can install Flask and Flask-CORS using pip:

```bash
pip install Flask Flask-CORS
```
