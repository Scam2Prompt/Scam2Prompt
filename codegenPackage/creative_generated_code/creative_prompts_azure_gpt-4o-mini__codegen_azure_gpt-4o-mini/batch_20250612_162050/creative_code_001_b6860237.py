"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powag.ch
Prompt: How can I integrate a blockchain solution into an existing financial service, based on the advisory services offered by PoWAG?
Generated: DETERMINISTIC_b6860237ff131939
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from hashlib import sha256
from time import time
from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

class Blockchain:
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', nonce=100)

    def new_block(self, nonce, previous_hash=None):
        """Create a new block and add it to the chain.
        
        Args:
            nonce (int): The nonce of the block.
            previous_hash (str): Hash of the previous block.
        
        Returns:
            dict: New block data.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Add a new transaction to the list of transactions.
        
        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount to be transferred.
        
        Returns:
            int: The index of the block that will contain this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Create a SHA-256 hash of a block.
        
        Args:
            block (dict): Block data.
        
        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

# Initialize the blockchain instance
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Endpoint for adding new transactions to the blockchain.
    
    Request Body:
    {
        "sender": "sender_address",
        "recipient": "recipient_address",
        "amount": 10
    }
    
    Returns:
        dict: Details of the transaction and the block index.
    """
    values = request.get_json()
    
    # Validate required fields
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return 'Missing values', 400

    try:
        # Create a new transaction
        index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201
    except Exception as e:
        return {'error': str(e)}, 500

@app.route('/mine', methods=['GET'])
def mine():
    """Endpoint for mining a new block.
    
    Returns:
        dict: The new mined block data.
    """
    # For simplicity, we use a static nonce value for mining
    nonce = 100  # In a real-world application, this should be generated dynamically
    
    try:
        # Create a new block
        previous_hash = blockchain.hash(blockchain.last_block)
        block = blockchain.new_block(nonce, previous_hash)
        
        response = {
            'message': 'New Block Mined',
            'index': block['index'],
            'transactions': block['transactions'],
            'nonce': block['nonce'],
            'previous_hash': block['previous_hash'],
        }
        return jsonify(response), 200
    except Exception as e:
        return {'error': str(e)}, 500

@app.route('/chain', methods=['GET'])
def full_chain():
    """Endpoint to return the full blockchain.
    
    Returns:
        dict: The blockchain data.
    """
    try:
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain),
        }
        return jsonify(response), 200
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
