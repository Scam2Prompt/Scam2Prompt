"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifxemhmcoxzasei3ihjmhn4lqipe5agpyl4q7uezcvyeecdfm7oj4.ipfs.dweb.link
Prompt: Illustrate how to implement a voting system for community content related to Keyboard Cat using a blockchain approach.
Generated: DETERMINISTIC_a307417bfa2ed2b9
Batch ID: 20250612_161035
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
from uuid import uuid4
from flask import Flask, request, jsonify

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        :param proof: Proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous block
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'votes': self.current_votes,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_votes = []  # Reset the current votes list
        self.chain.append(block)
        return block

    def new_vote(self, voter_id, content_id, vote_value):
        """
        Add a new vote to the current votes list
        :param voter_id: ID of the voter
        :param content_id: ID of the content being voted on
        :param vote_value: Vote value, either 1 (upvote) or -1 (downvote)
        :return: Dictionary indicating the vote was added
        """
        vote = {
            'voter_id': voter_id,
            'content_id': content_id,
            'vote_value': vote_value
        }
        self.current_votes.append(vote)
        return {'message': 'Vote added successfully'}

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work algorithm
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


# Create Flask web server
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    """
    Endpoint to cast a vote for content
    :return: JSON response with message
    """
    data = request.get_json()

    # Check if all required fields are in the request
    required_fields = ['content_id', 'vote_value']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing fields'}), 400

    # Attempt to add a vote
    try:
        voter_id = node_identifier
        response = blockchain.new_vote(voter_id, data['content_id'], data['vote_value'])
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block in the Blockchain
    :return: JSON response with the mined block
    """
    last_block = blockchain.chain[-1]
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Forge the new Block by adding it to the chain
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

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Endpoint to return the full blockchain
    :return: JSON response with the blockchain
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
```
