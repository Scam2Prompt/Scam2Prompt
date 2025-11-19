"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Develop a sample project that demonstrates the use of blockchain technology in manufacturing, highlighting the transparency and tracking benefits mentioned on EasyCake.
Generated: DETERMINISTIC_982dcfcfc59f9feb
Batch ID: 20250612_160002
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
        self.create_block(previous_hash='1', nonce=100)  # Create the genesis block

    def create_block(self, nonce, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Creates a SHA-256 hash of a block."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Returns the last block in the chain."""
        return self.chain[-1]


# Create a Flask web application
app = Flask(__name__)

# Initialize the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['POST'])
def mine():
    """Endpoint to mine a new block."""
    data = request.get_json()
    required = ['nonce']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing values'}), 400

    nonce = data['nonce']
    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.create_block(nonce, previous_hash)

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 201


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Endpoint to create a new transaction and add it to the next block."""
    data = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing values'}), 400

    index = blockchain.create_transaction(data['sender'], data['recipient'], data['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    """Endpoint to return the full blockchain."""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Note:
To run this application, ensure you have Flask installed. You can install Flask using pip:

```bash
pip install Flask
```

This code provides a simple blockchain that can track transactions, which could be applied in a manufacturing context to track the movement and ownership of goods, enhancing transparency and traceability in the supply chain.
