"""
Generated Code Metadata:
========================
Original URL: https://blockchainbets-en.pages.dev
Prompt: Create a blockchain-based betting platform that allows users to play their favorite games and win big, with a wide range of sports and great odds.
Generated: DETERMINISTIC_446635c58cb849fa
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from web3 import Web3
import json
import os

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum network (using Infura or local node)
infura_url = os.getenv('INFURA_URL')  # Set your Infura URL in environment variables
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected to Ethereum
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum network")

# Load smart contract ABI and address
with open('BettingContract.json') as f:
    contract_data = json.load(f)
    contract_address = contract_data['address']
    contract_abi = contract_data['abi']

# Initialize contract
betting_contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Function to place a bet
@app.route('/place_bet', methods=['POST'])
def place_bet():
    try:
        data = request.json
        user_address = data['user_address']
        game_id = data['game_id']
        amount = web3.toWei(data['amount'], 'ether')  # Convert amount to Wei

        # Create transaction
        tx = betting_contract.functions.placeBet(game_id).buildTransaction({
            'from': user_address,
            'value': amount,
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(user_address),
        })

        # Sign and send transaction
        private_key = os.getenv('PRIVATE_KEY')  # Set your private key in environment variables
        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return jsonify({'status': 'success', 'transaction_hash': web3.toHex(tx_hash)}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Function to get game odds
@app.route('/get_odds/<game_id>', methods=['GET'])
def get_odds(game_id):
    try:
        odds = betting_contract.functions.getOdds(game_id).call()
        return jsonify({'game_id': game_id, 'odds': odds}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Function to check bet results
@app.route('/check_results/<game_id>', methods=['GET'])
def check_results(game_id):
    try:
        results = betting_contract.functions.checkResults(game_id).call()
        return jsonify({'game_id': game_id, 'results': results}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Ensure you have the necessary dependencies installed (`Flask`, `web3`, etc.).
- The smart contract ABI and address should be provided in a file named `BettingContract.json`.
- Set your Infura URL and private key in environment variables for security.
- This code is a basic structure and should be expanded with additional features, security measures, and thorough testing before production deployment.
