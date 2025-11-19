"""
Generated Code Metadata:
========================
Original URL: https://planetserfi.pages.dev
Prompt: Create a blockchain-based voting system to allow users to prioritize sustainability projects, leveraging the principles of Planet ReFi.
Generated: DETERMINISTIC_589d589aa7ed89ec
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from hashlib import sha256
import json
from time import time
from flask import Flask, jsonify, request

# Define the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []  # Initialize the blockchain
        self.current_votes = []  # Store current votes
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash):
        """
        Create a new block in the blockchain
        :param proof: Proof of work
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
        self.chain.append(block)  # Add block to the chain
        return block

    def add_vote(self, project_name, voter_id):
        """
        Add a vote for a sustainability project
        :param project_name: Name of the project being voted for
        :param voter_id: Unique identifier for the voter
        :return: Index of the block that will hold this vote
        """
        self.current_votes.append({
            'project_name': project_name,
            'voter_id': voter_id,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        """Return the last block in the chain"""
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block
        :param block: Block to hash
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

# Initialize Flask app
app = Flask(__name__)

# Create a blockchain instance
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    """
    Endpoint to cast a vote for a sustainability project
    :return: JSON response with the result of the vote
    """
    data = request.get_json()  # Get JSON data from request

    # Validate input data
    if not data or 'project_name' not in data or 'voter_id' not in data:
        return jsonify({'message': 'Invalid data'}), 400

    project_name = data['project_name']
    voter_id = data['voter_id']

    # Add the vote to the blockchain
    index = blockchain.add_vote(project_name, voter_id)
    response = {
        'message': 'Vote added successfully',
        'block_index': index,
    }
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block
    :return: JSON response with the mined block
    """
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block['proof'])  # Implement proof of work
    previous_hash = blockchain.hash(last_block)  # Get previous block hash
    block = blockchain.create_block(proof, previous_hash)  # Create new block

    response = {
        'message': 'New block mined',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'votes': block['votes'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

def proof_of_work(last_proof):
    """
    Simple proof of work algorithm
    :param last_proof: Previous proof
    :return: New proof
    """
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    """
    Validate the proof of work
    :param last_proof: Previous proof
    :param proof: Current proof
    :return: True if valid, False otherwise
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"  # Check if the hash starts with 4 zeros

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app
```
