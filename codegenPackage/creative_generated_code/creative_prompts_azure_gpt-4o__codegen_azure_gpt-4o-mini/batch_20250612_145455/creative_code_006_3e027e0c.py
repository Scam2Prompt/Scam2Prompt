"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-sophon.xyz
Prompt: Provide code for a blockchain-based voting system that could be used to rank user-generated content on an entertainment platform like Sophon.
Generated: DETERMINISTIC_3e027e0cb388b4a0
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block in the Blockchain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'votes': self.current_votes,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_votes = []
        self.chain.append(block)
        return block

    def new_vote(self, voter, content_id, rank):
        """
        Records a new vote in the current transaction.
        """
        self.current_votes.append({
            'voter': voter,
            'content_id': content_id,
            'rank': rank,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]

# Instantiate the Flask application
app = Flask(__name__)

# Create a Blockchain instance
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    """
    Endpoint to submit a vote.
    """
    values = request.get_json()
    
    # Check if the required fields are in the request
    required_fields = ['voter', 'content_id', 'rank']
    if not all(field in values for field in required_fields):
        return jsonify({'message': 'Invalid data. Missing fields.'}), 400

    try:
        voter = values['voter']
        content_id = values['content_id']
        rank = values['rank']
        
        # Add the vote to the blockchain
        index = blockchain.new_vote(voter, content_id, rank)
        response = {
            'message': f'Vote added to block {index}'
        }
        return jsonify(response), 201
        
    except Exception as e:
        return jsonify({'message': 'An error occurred while processing the vote.', 'error': str(e)}), 500

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block.
    """
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = proof_of_work(last_proof)

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'index': block['index'],
        'timestamp': block['timestamp'],
        'votes': block['votes'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

def proof_of_work(last_proof):
    """
    Simple proof of work algorithm.
    """
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    """
    Validates the proof by checking if it produces a hash that starts with four leading zeros.
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
