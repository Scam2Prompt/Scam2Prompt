"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chain-dioneprotoclcom.pages.dev
Prompt: Develop a blockchain-based solution to track and validate energy transactions, similar to the Nebra project in the Dione Protocol.
Generated: DETERMINISTIC_8ea0ba1c1d6627a1
Batch ID: 20250612_152109
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
        """Initialize the blockchain and the list of transactions."""
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash=None):
        """Create a new block in the blockchain.
        
        Args:
            proof (int): Proof of work.
            previous_hash (str): Hash of the previous block.
        
        Returns:
            dict: A new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Create a new transaction to go into the next mined block.
        
        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount of energy to be transferred.
        
        Returns:
            int: The index of the block that will hold this transaction.
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
            block (dict): A block in the blockchain.
        
        Returns:
            str: SHA-256 hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the blockchain.
        
        Returns:
            dict: The last block.
        """
        return self.chain[-1]

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Endpoint to create a new transaction.
    
    Returns:
        json: Confirmation of the transaction.
    """
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    try:
        index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    except Exception as e:
        return str(e), 500
    
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    """Endpoint to mine a new block.
    
    Returns:
        json: The newly mined block.
    """
    last_block = blockchain.last_block
    proof = proof_of_work(last_block)
    
    blockchain.new_transaction(sender="0", recipient="your_address", amount=1)  # Mining reward
    
    block = blockchain.create_block(proof, previous_hash=blockchain.hash(last_block))
    return jsonify(block), 200

def proof_of_work(last_block):
    """Simple Proof of Work algorithm.
    
    Args:
        last_block (dict): The last block in the blockchain.
        
    Returns:
        int: A proof for the new block.
    """
    proof = 0
    while not is_valid_proof(last_block['proof'], proof):
        proof += 1
    return proof

def is_valid_proof(last_proof, proof):
    """Validates the Proof.
    
    Args:
        last_proof (int): The previous proof.
        proof (int): The current proof.
        
    Returns:
        bool: True if the proof is valid, False otherwise.
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"  # Adjust difficulty as needed

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
