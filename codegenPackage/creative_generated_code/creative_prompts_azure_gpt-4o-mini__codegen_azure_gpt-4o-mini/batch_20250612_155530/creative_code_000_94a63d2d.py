"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://voters4pepe.pages.dev
Prompt: Generate a code snippet to create a simple voting application that allows users to support President Pepe using a blockchain address.
Generated: DETERMINISTIC_94a63d2d148a35d5
Batch ID: 20250612_155530
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
from flask import Flask, request, jsonify
from urllib.parse import urlparse

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.nodes = set()
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        :param proof: Proof from the Proof of Work algorithm
        :param previous_hash: Hash of the previous block
        :return: New Block
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

    def new_vote(self, voter_address):
        """
        Add a new vote to the current votes
        :param voter_address: The blockchain address of the voter
        :return: Index of the block that will contain this vote
        """
        self.current_votes.append({'voter_address': voter_address})
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block
        :param block: Block
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

app = Flask(__name__)
node_identifier = str(uuid.uuid4()).replace('-', '')  # Unique node identifier
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    """
    Endpoint to cast a vote for President Pepe
    :return: JSON response with vote result
    """
    data = request.get_json()

    if not data or 'address' not in data:
        return jsonify({'message': 'Missing address'}), 400

    voter_address = data['address']

    # Add the new vote to the blockchain
    block_index = blockchain.new_vote(voter_address)
    response = {
        'message': 'Vote added!',
        'block_index': block_index,
    }
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Endpoint to return the full blockchain
    :return: JSON with the blockchain data
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
