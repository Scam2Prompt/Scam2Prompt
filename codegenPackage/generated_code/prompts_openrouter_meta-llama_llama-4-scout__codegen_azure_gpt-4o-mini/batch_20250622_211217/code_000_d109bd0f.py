"""
Generated Code Metadata:
========================
Original URL: https://meteora-ag.github.io
Prompt: Write a Python code snippet to implement a decentralized governance model using blockchain technology, inspired by Meteora Crypto's community-driven approach.
Generated: DETERMINISTIC_d109bd0f042248f8
Batch ID: 20250622_211217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from hashlib import sha256
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.nodes = set()
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash=None):
        """
        Create a new block in the blockchain.
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of the previous block
        :return: New block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'votes': self.current_votes,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_votes = []  # Reset current votes
        self.chain.append(block)
        return block

    def create_vote(self, voter_id, proposal_id, vote):
        """
        Create a new vote.
        :param voter_id: Unique identifier for the voter
        :param proposal_id: Unique identifier for the proposal
        :param vote: The vote (e.g., 'yes' or 'no')
        :return: None
        """
        self.current_votes.append({
            'voter_id': voter_id,
            'proposal_id': proposal_id,
            'vote': vote,
        })

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.
        :param block: Block
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work algorithm.
        :param last_proof: Previous proof
        :return: New proof
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: Previous proof
        :param proof: Current proof
        :return: True if valid, False otherwise
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# Instantiate the Flask app
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    """
    Endpoint to cast a vote.
    :return: JSON response with the result of the vote
    """
    data = request.get_json()
    required_fields = ['voter_id', 'proposal_id', 'vote']
    
    # Check if all required fields are present
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing fields'}), 400

    # Create a new vote
    blockchain.create_vote(data['voter_id'], data['proposal_id'], data['vote'])
    return jsonify({'message': 'Vote cast successfully'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block.
    :return: JSON response with the new block
    """
    last_block = blockchain.chain[-1]
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Forge the new block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': 'New block forged',
        'index': block['index'],
        'votes': block['votes'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Endpoint to return the full blockchain.
    :return: JSON response with the blockchain
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
