"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://planetserfi.pages.dev
Prompt: Create a blockchain-based voting system to allow users to prioritize sustainability projects, leveraging the principles of Planet ReFi.
Generated: DETERMINISTIC_589d589aa7ed89ec
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
from time import time
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

# Initialize Flask app and MongoDB connection
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/voting_db'
mongo = PyMongo(app)

class Vote:
    def __init__(self, voter_id, project_id, timestamp=None):
        self.voter_id = voter_id
        self.project_id = project_id
        self.timestamp = timestamp or time()
        self.vote_hash = self.hash_vote()

    def hash_vote(self):
        vote_string = f"{self.voter_id}{self.project_id}{self.timestamp}"
        return sha256(vote_string.encode()).hexdigest()

class Block:
    def __init__(self, index, timestamp, votes, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.votes = votes
        self.previous_hash = previous_hash
        self.block_hash = self.hash_block()

    def hash_block(self):
        block_string = f"{self.index}{self.timestamp}{self.votes}{self.previous_hash}"
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        # Create the genesis block
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = Block(len(self.chain) + 1, time(), self.current_votes, previous_hash)
        self.current_votes = []  # Reset the current votes list
        self.chain.append(block)
        return block

    def add_vote(self, vote):
        if not self.validate_vote(vote):
            return False
        self.current_votes.append(vote)
        return True

    def validate_vote(self, vote):
        # Simple validation to check if the voter has already voted for this project
        for v in self.current_votes:
            if v.voter_id == vote.voter_id and v.project_id == vote.project_id:
                return False
        return True

# Initialize blockchain
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    """Endpoint to cast a vote for a sustainability project."""
    voter_id = request.json.get('voter_id')
    project_id = request.json.get('project_id')

    if not voter_id or not project_id:
        return jsonify({'error': 'Voter ID and Project ID are required.'}), 400

    try:
        new_vote = Vote(voter_id, project_id)
        if blockchain.add_vote(new_vote):
            return jsonify({'message': 'Vote cast successfully!', 'vote_hash': new_vote.vote_hash}), 201
        else:
            return jsonify({'error': 'Vote already cast for this project by the voter.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/create_block', methods=['POST'])
def create_block():
    """Endpoint to manually create a new block from current votes."""
    try:
        previous_hash = blockchain.chain[-1].block_hash if blockchain.chain else '0'
        new_block = blockchain.create_block(previous_hash)
        return jsonify({
            'message': 'Block created successfully!',
            'block_index': new_block.index,
            'block_hash': new_block.block_hash,
            'votes': [vote.vote_hash for vote in new_block.votes]
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    """Endpoint to retrieve the current blockchain."""
    chain_data = [{
        'index': block.index,
        'timestamp': block.timestamp,
        'votes': [vote.vote_hash for vote in block.votes],
        'previous_hash': block.previous_hash,
        'block_hash': block.block_hash
    } for block in blockchain.chain]
    return jsonify(chain_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```
