"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Explain the concept of 'distributed ledger' in blockchain technology and provide a code example that demonstrates its implementation.
Generated: DETERMINISTIC_312d20a6d448ae3a
Batch ID: 20250612_163924
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

class Block:
    """A block in the blockchain containing index, timestamp, transactions, previous hash, and nonce."""
    
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        """Computes the SHA-256 hash of the block."""
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """A simple implementation of a blockchain."""

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # Create the genesis block
        self.new_block(previous_hash='1', nonce=100)

    def new_block(self, previous_hash, nonce):
        """Creates a new block and adds it to the chain."""
        block = Block(index=len(self.chain) + 1,
                      transactions=self.current_transactions,
                      timestamp=time(),
                      previous_hash=previous_hash,
                      nonce=nonce)
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Adds a new transaction to the list of transactions."""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block.index + 1

    @property
    def last_block(self):
        """Returns the last block in the chain."""
        return self.chain[-1]

# Flask web application for interacting with the blockchain
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    """API endpoint to add a new transaction."""
    values = request.get_json()
    
    # Validate request data
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return 'Missing values', 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    """API endpoint to mine a new block."""
    last_block = blockchain.last_block
    previous_hash = last_block.compute_hash()
    
    blockchain.new_transaction(sender='0', recipient='miner_address', amount=1)  # Reward for mining
    block = blockchain.new_block(previous_hash, nonce=0)  # In a real case, you would implement proof-of-work
    
    response = {
        'message': 'New block forged',
        'index': block.index,
        'transactions': block.transactions,
        'previous_hash': block.previous_hash,
        'timestamp': block.timestamp,
        'nonce': block.nonce
    }
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """API endpoint to return the full blockchain."""
    response = {
        'chain': [block.__dict__ for block in blockchain.chain],
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

This code provides a simple implementation of a blockchain with endpoints for creating transactions and mining blocks. Each block contains a list of transactions, and the blockchain is represented as a list of blocks.
