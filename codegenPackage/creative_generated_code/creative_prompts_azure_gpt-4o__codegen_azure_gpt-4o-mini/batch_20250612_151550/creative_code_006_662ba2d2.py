"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fennextradingservices.com
Prompt: Design a blockchain-based solution to help clients understand and interact with a financial platform, incorporating features like perceptive analysis and business intelligence as described by Fennex Trading Services.
Generated: DETERMINISTIC_662ba2d241821ce0
Batch ID: 20250612_151550
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
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        """
        Creates a new block in the Blockchain
        :param proof: Proof of work
        :param previous_hash: Hash of the previous block
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions
        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount of the transaction
        :return: Index of the block that will hold this transaction
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
        Creates a SHA-256 hash of a block
        :param block: Block
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine():
    """
    Mints a new block by providing proof of work
    :return: Newly mined block
    """
    data = request.get_json()
    proof = data.get('proof')
    previous_hash = blockchain.hash(blockchain.last_block)

    # Basic error handling
    if proof is None:
        return jsonify({'message': 'Proof is required'}), 400

    block = blockchain.create_block(proof, previous_hash)
    return jsonify({
        'message': 'New block mined',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Creates a new transaction and adds it to the blockchain
    :return: Confirmation of the transaction
    """
    data = request.get_json()

    # Validate data
    required_fields = ['sender', 'recipient', 'amount']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Missing field: {field}'}), 400

    index = blockchain.new_transaction(data['sender'], data['recipient'], data['amount'])
    return jsonify({'message': f'Transaction will be added to block {index}'}), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Returns the full blockchain
    :return: The blockchain as JSON
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Make sure you have Flask installed to run this application. You can install it using pip:

```bash
pip install Flask
``` 

This implementation sets up a simple blockchain server with endpoints to mine blocks, create transactions, and view the full blockchain. It includes basic error handling, input validation, and follows best practices for structuring the code.
