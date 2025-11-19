"""
Generated Code Metadata:
========================
Original URL: https://fennextradingservices.com
Prompt: Design a blockchain-based solution to help clients understand and interact with a financial platform, incorporating features like perceptive analysis and business intelligence as described by Fennex Trading Services.
Generated: DETERMINISTIC_662ba2d241821ce0
Batch ID: 20250612_151550
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
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of the previous block
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
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
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Returns the last Block in the chain
        :return: Last Block
        """
        return self.chain[-1]

app = Flask(__name__)
node_identifier = "FennexTradingService"

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """
    Mine a new block and add it to the blockchain
    :return: JSON response with the new block
    """
    last_block = blockchain.last_block
    proof = proof_of_work(last_block)
    blockchain.new_transaction(sender="0", recipient=node_identifier, amount=1)
    block = blockchain.create_block(proof, blockchain.hash(last_block))
    response = {
        'message': 'New Block Mined',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

def proof_of_work(last_block):
    """
    Simple Proof of Work Algorithm
    :param last_block: Last Block in the chain
    :return: Proof
    """
    proof = 0
    while not valid_proof(last_block['proof'], proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    """
    Validates the Proof
    :param last_proof: Previous Proof
    :param proof: Current Proof
    :return: True if valid, False otherwise
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Create a new transaction
    :return: JSON response with the transaction index
    """
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Returns the full blockchain
    :return: JSON response with the blockchain
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
