"""
Generated Code Metadata:
========================
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Generate code to integrate blockchain-backed digital collectibles into a game platform, allowing users to own and earn rewards from their creations, as described in the Pixels ecosystem.
Generated: DETERMINISTIC_06d1e3b7b9dd3352
Batch ID: 20250612_150228
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
with open('CollectibleABI.json') as f:
    contract_abi = json.load(f)

contract_address = os.getenv('CONTRACT_ADDRESS')  # Set your contract address in environment variables
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# User wallet address (for demonstration purposes, should be securely managed)
user_wallet = os.getenv('USER_WALLET')  # Set your wallet address in environment variables

@app.route('/create_collectible', methods=['POST'])
def create_collectible():
    """
    Endpoint to create a new digital collectible.
    Expects JSON payload with 'name' and 'metadata'.
    """
    try:
        data = request.json
        name = data['name']
        metadata = data['metadata']

        # Create a transaction to mint a new collectible
        tx = contract.functions.mintCollectible(user_wallet, name, metadata).buildTransaction({
            'from': user_wallet,
            'nonce': web3.eth.getTransactionCount(user_wallet),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        })

        # Sign the transaction
        signed_tx = web3.eth.account.signTransaction(tx, private_key=os.getenv('PRIVATE_KEY'))

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return jsonify({'status': 'success', 'transaction_hash': tx_hash.hex()}), 201

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/collectibles', methods=['GET'])
def get_collectibles():
    """
    Endpoint to retrieve all collectibles owned by the user.
    """
    try:
        # Call the smart contract to get the list of collectibles
        collectibles = contract.functions.getCollectiblesByOwner(user_wallet).call()
        return jsonify({'status': 'success', 'collectibles': collectibles}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/reward', methods=['POST'])
def reward_user():
    """
    Endpoint to reward a user for their creations.
    Expects JSON payload with 'amount'.
    """
    try:
        data = request.json
        amount = data['amount']

        # Create a transaction to reward the user
        tx = contract.functions.rewardUser(user_wallet, amount).buildTransaction({
            'from': user_wallet,
            'nonce': web3.eth.getTransactionCount(user_wallet),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        })

        # Sign the transaction
        signed_tx = web3.eth.account.signTransaction(tx, private_key=os.getenv('PRIVATE_KEY'))

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return jsonify({'status': 'success', 'transaction_hash': tx_hash.hex()}), 201

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Ensure to set the environment variables `INFURA_URL`, `CONTRACT_ADDRESS`, `USER_WALLET`, and `PRIVATE_KEY` before running the application.
- The smart contract ABI should be saved in a file named `CollectibleABI.json`.
- This code assumes the existence of a smart contract with functions `mintCollectible`, `getCollectiblesByOwner`, and `rewardUser`. Adjust the function names and parameters as per your actual smart contract implementation.
