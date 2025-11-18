"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genopets.eu
Prompt: Write code to integrate a blockchain-based rewards system for a gamified fitness app similar to Genopets.
Generated: DETERMINISTIC_7ec662c9a3e1fce6
Batch ID: 20250612_151513
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

# Blockchain class for rewards system
class Blockchain:
    def __init__(self):
        # Initialize the chain and create the genesis block
        self.chain = []
        self.current_transactions = []
        self.create_block(proof=1, previous_hash="0")  # Genesis Block

    def create_block(self, proof, previous_hash):
        """
        Create a new block and add it to the blockchain.
        :param proof: Proof of work for the block
        :param previous_hash: Hash of the previous block
        :return: The newly created block
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash,
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        """
        Add a transaction to the list of current_transactions.
        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount to be transferred
        :return: Index of the block that will hold this transaction
        """
        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
        })
        return self.last_block["index"] + 1

    def proof_of_work(self, previous_proof):
        """
        Proof of work algorithm to find the next proof.
        :param previous_proof: Proof of the previous block
        :return: New proof
        """
        proof = 1
        while not self.valid_proof(previous_proof, proof):
            proof += 1
        return proof

    def valid_proof(self, previous_proof, proof):
        """
        Validates the proof by checking if hash meets criteria.
        :param previous_proof: Proof of the previous block
        :param proof: Current proof
        :return: Boolean indicating whether proof is valid
        """
        guess = f"{previous_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash(self, block):
        """
        Create a SHA-256 hash of a block.
        :param block: Block to hash
        :return: Hash string
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

# Flask application for API
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block.
    :return: JSON response with the new block details
    """
    previous_block = blockchain.last_block
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        "message": "New block mined successfully!",
        "index": block["index"],
        "transactions": block["transactions"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Endpoint to create a new transaction.
    :return: JSON response with the block index where transaction will be added
    """
    data = request.get_json()

    # Validate required fields
    required = ["sender", "recipient", "amount"]
    if not all(field in data for field in required):
        return jsonify({"message": "Missing values"}), 400

    index = blockchain.add_transaction(data["sender"], data["recipient"], data["amount"])
    response = {"message": f"Transaction will be added to Block {index}"}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    """
    Endpoint to retrieve the entire blockchain.
    :return: JSON response with the full chain and its length
    """
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/validate', methods=['GET'])
def validate_chain():
    """
    Endpoint to validate the current blockchain.
    :return: JSON response indicating whether the chain is valid
    """
    chain = blockchain.chain
    for i in range(1, len(chain)):
        previous_block = chain[i - 1]
        current_block = chain[i]

        # Validate hash of the previous block
        if current_block["previous_hash"] != blockchain.hash(previous_block):
            return jsonify({"message": "Blockchain is invalid!"}), 400

        # Validate proof of work
        if not blockchain.valid_proof(previous_block["proof"], current_block["proof"]):
            return jsonify({"message": "Blockchain is invalid!"}), 400

    return jsonify({"message": "Blockchain is valid!"}), 200

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
