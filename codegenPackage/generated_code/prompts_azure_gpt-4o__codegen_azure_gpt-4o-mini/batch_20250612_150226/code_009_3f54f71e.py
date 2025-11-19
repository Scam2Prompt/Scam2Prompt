"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Generate code to simulate a blockchain-based voting system for transparent decision-making, inspired by the values of Innodapter ApS.
Generated: DETERMINISTIC_3f54f71efbd95b17
Batch ID: 20250612_150226
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
        self.current_votes = []
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
            'votes': self.current_votes,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_votes = []  # Reset the current votes
        self.chain.append(block)
        return block

    def new_vote(self, candidate):
        """Add a new vote to the current votes.

        Args:
            candidate (str): The candidate for whom the vote is cast.

        Returns:
            int: The index of the block that will hold this vote.
        """
        self.current_votes.append(candidate)
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

# Instantiate the Flask app
app = Flask(__name__)

# Create the blockchain
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    """Endpoint to cast a vote for a candidate.

    Returns:
        json: A response indicating the result of the vote.
    """
    data = request.get_json()
    candidate = data.get('candidate')

    if not candidate:
        return jsonify({'message': 'Candidate is required'}), 400

    # Add the vote to the blockchain
    index = blockchain.new_vote(candidate)
    response = {
        'message': f'Vote for {candidate} has been added to block {index}.'
    }
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    """Endpoint to mine a new block.

    Returns:
        json: The newly mined block.
    """
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'votes': block['votes'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

def proof_of_work(last_proof):
    """Simple proof of work algorithm.

    Args:
        last_proof (int): The previous proof.

    Returns:
        int: The new proof.
    """
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    """Validate the proof of work.

    Args:
        last_proof (int): The previous proof.
        proof (int): The current proof.

    Returns:
        bool: True if valid, False otherwise.
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
