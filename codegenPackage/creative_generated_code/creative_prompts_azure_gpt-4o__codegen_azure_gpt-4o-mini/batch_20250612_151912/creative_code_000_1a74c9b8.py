"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eosgas.io
Prompt: Write a Python script that simulates the integration of a Waste-to-Energy (WTE) power plant as a master node in a blockchain network, following the eosGAS model described on the website.
Generated: DETERMINISTIC_1a74c9b8283df673
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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
        self.create_block(previous_hash='1', miner_id='0')  # Genesis block

    def create_block(self, nonce, previous_hash):
        """
        Creates a new block in the Blockchain.

        :param nonce: The nonce used for mining the block
        :param previous_hash: Hash of the previous block
        :return: Newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []  # Reset current transactions
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions.

        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount of energy exchanged
        :return: Index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, last_nonce):
        """
        Simple proof of work algorithm.

        :param last_nonce: The nonce from the last block
        :return: Valid nonce
        """
        nonce = 0
        while not self.valid_proof(last_nonce, nonce):
            nonce += 1
        return nonce

    @staticmethod
    def valid_proof(last_nonce, nonce):
        """
        Validates the proof of work.

        :param last_nonce: The nonce from the last block
        :param nonce: The current nonce
        :return: True if valid, False otherwise
        """
        guess = f'{last_nonce}{nonce}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Arbitrary difficulty level

app = Flask(__name__)

# Create a new instance of Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block.
    """
    last_block = blockchain.last_block
    last_nonce = last_block['nonce']
    nonce = blockchain.proof_of_work(last_nonce)
    previous_hash = hashlib.sha256(json.dumps(last_block, sort_keys=True).encode()).hexdigest()

    # Create a new block
    block = blockchain.create_block(nonce, previous_hash)

    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'transactions': block['transactions'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Endpoint to create a new transaction.
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
    Endpoint to return the full blockchain.
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Make sure to install Flask before running this script:
```bash
pip install Flask
```

To run the script, save it to a file called `wte_blockchain.py` and execute:
```bash
python wte_blockchain.py
``` 

You can interact with the blockchain using RESTful API calls made to `http://localhost:5000`.
