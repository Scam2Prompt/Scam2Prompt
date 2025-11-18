"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://midoin.com
Prompt: Develop a blockchain-based solution to track and verify eco-friendly mining efforts for Midoins, ensuring minimal environmental impact.
Generated: DETERMINISTIC_3d1345892989380d
Batch ID: 20250612_154609
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
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)  # Genesis block

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        :param proof: Proof provided by the Proof of Work algorithm
        :param previous_hash: Hash of the previous Block
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current list of transactions
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        :return: Hash of the Block
        """
        # Convert the block into a string and encode it to bytes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Returns the last block in the chain"""
        return self.chain[-1]

# Instantiate the Flask application
app = Flask(__name__)

# Create a Blockchain instance
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine():
    """
    Endpoint to mine a new block
    Expects JSON with 'proof' submitted via POST request
    """
    values = request.get_json()

    if not values or 'proof' not in values:
        return jsonify({'message': 'Missing proof'}), 400

    proof = values['proof']
    last_block = blockchain.last_block
    previous_hash = blockchain.hash(last_block)

    # Create a new block and reward the miner
    blockchain.new_transaction(sender="0", recipient=request.remote_addr, amount=1)  # Reward for mining
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 201

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Endpoint to create a new transaction
    Expects JSON with 'sender', 'recipient', and 'amount'
    """
    values = request.get_json()

    if not values or not all(k in values for k in ('sender', 'recipient', 'amount')):
        return jsonify({'message': 'Missing values'}), 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """Return the full blockchain"""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
