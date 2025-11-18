"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playemberssssssssssssss.pages.dev
Prompt: Create a blockchain-based leaderboard system for mobile games, referencing Playember's ranking as the No.3 Blockchain Game on Dappradar.
Generated: DETERMINISTIC_6f76698d6d69f045
Batch ID: 20250612_152410
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
        self.chain = []
        self.current_rankings = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        :param proof: Proof of Work
        :param previous_hash: Hash of the previous block
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'rankings': self.current_rankings,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_rankings = []  # Reset current rankings
        self.chain.append(block)
        return block

    def new_ranking(self, player_id, score):
        """
        Add a new player's ranking to the current rankings
        :param player_id: Unique ID of the player
        :param score: Player's score
        """
        self.current_rankings.append({'player_id': player_id, 'score': score})

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block
        :param block: Block
        :return: Hash of the block
        """
        # Convert block to string and encode it
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm
        :param last_proof: Previous block's proof
        :return: New proof
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof
        :param last_proof: Previous block's proof
        :param proof: Current proof
        :return: True if valid, False otherwise
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# Initialize Flask app
app = Flask(__name__)

# Create blockchain instance
blockchain = Blockchain()

@app.route('/rankings/new', methods=['POST'])
def new_ranking():
    """
    Endpoint to add new player rankings
    :return: JSON response containing ranking details
    """
    data = request.get_json()
    if not data or 'player_id' not in data or 'score' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    player_id = data['player_id']
    score = data['score']

    # Add ranking to current rankings
    blockchain.new_ranking(player_id, score)
    return jsonify({'message': 'Ranking added successfully'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block
    :return: JSON response containing the new block
    """
    last_block = blockchain.chain[-1]
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Create a new block and add it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    return jsonify({
        'message': 'New block mined',
        'index': block['index'],
        'rankings': block['rankings'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Endpoint to return the entire blockchain
    :return: JSON response containing the blockchain
    """
    return jsonify({
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```
