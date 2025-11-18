"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genopets.eu
Prompt: Write code to integrate a blockchain-based rewards system for a gamified fitness app similar to Genopets.
Generated: DETERMINISTIC_7ec662c9a3e1fce6
Batch ID: 20250612_151513
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import json
import hashlib
from flask import Flask, request, jsonify
from web3 import Web3

# Initialize Flask app
app = Flask(__name__)

# Connect to the Ethereum blockchain (using Infura or a local node)
WEB3_PROVIDER = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

# Check if the connection is successful
if not web3.isConnected():
    raise Exception("Could not connect to Ethereum network")

# Simple blockchain structure
class Block:
    def __init__(self, index, previous_hash, transactions, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# In-memory blockchain and transaction pool
blockchain = []
transaction_pool = []

# Function to create a new transaction
def create_transaction(user_id, token_amount):
    transaction = {
        'user_id': user_id,
        'token_amount': token_amount
    }
    transaction_pool.append(transaction)
    return transaction

# Function to mine a block
def mine_block():
    if not transaction_pool:
        return None  # No transactions to mine

    last_block = blockchain[-1] if blockchain else None
    index = len(blockchain) + 1
    previous_hash = last_block.hash if last_block else '0'
    timestamp = web3.eth.getBlock('latest')['timestamp']
    
    block = Block(index, previous_hash, transaction_pool.copy(), timestamp)
    blockchain.append(block)

    # Clear the transaction pool after mining
    transaction_pool.clear()

    return block

# API endpoint to submit a transaction
@app.route('/transaction', methods=['POST'])
def submit_transaction():
    try:
        data = request.get_json()
        user_id = data['user_id']
        token_amount = data['token_amount']

        # Create a new transaction
        transaction = create_transaction(user_id, token_amount)
        
        return jsonify({'message': 'Transaction submitted successfully!', 'transaction': transaction}), 201
    except KeyError:
        return jsonify({'error': 'Invalid input, user_id and token_amount are required'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to mine a block
@app.route('/mine', methods=['POST'])
def mine():
    try:
        block = mine_block()
        if block is None:
            return jsonify({'message': 'No transactions to mine'}), 400
        
        return jsonify({'message': 'Block mined successfully!', 'block': block.__dict__}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get the current blockchain
@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify({'chain': [block.__dict__ for block in blockchain]}), 200

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

Before running this code, ensure that you have the required dependencies installed. You can install them using:
```bash
pip install Flask web3
```

Make sure to replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID to connect to the Ethereum network.
