"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asfcsc.pages.dev
Prompt: Develop a blockchain-based application that supports Universal Health Coverage (UHC) and Universal Basic Income (UBI) principles, as described in BitDoctor's mission.
Generated: DETERMINISTIC_0cd6c013660ee241
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from hashlib import sha256
import json
import time
from flask import Flask, jsonify, request

# Define a blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []  # Initialize the blockchain
        self.current_transactions = []  # Current transactions list
        self.create_block(prev_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, prev_hash):
        """Create a new block and add it to the chain."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': prev_hash,
        }
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)  # Append block to the chain
        return block

    def create_transaction(self, sender, recipient, amount):
        """Add a transaction to the list of transactions."""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1  # Return the index of the block that will hold this transaction

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """Simple proof of work algorithm."""
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """Validate the proof of work."""
        guess = f"{last_proof}{proof}".encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Check if hash starts with four zeroes

# Create a Flask web application
app = Flask(__name__)

# Initialize the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """Mine a new block."""
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Reward for mining
    blockchain.create_transaction(sender="0", recipient="your_address", amount=1)

    # Create the new block
    block = blockchain.create_block(proof, prev_hash=sha256(json.dumps(last_block, sort_keys=True).encode()).hexdigest())
    
    response = {
        'message': 'New Block Mined!',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Create a new transaction."""
    values = request.get_json()

    # Check for required fields
    required_fields = ['sender', 'recipient', 'amount']
    for field in required_fields:
        if field not in values:
            return jsonify({'message': f'Missing field {field}'}), 400

    index = blockchain.create_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """Return the full blockchain."""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Note:
- Replace `"your_address"` with the actual address where the reward for mining should be sent.
- The code utilizes Flask for the web server and implements basic blockchain functionality for transactions, mining, and blocks.
- Proper error handling is included for missing fields in transactions.
