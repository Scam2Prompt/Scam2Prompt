"""
Generated Code Metadata:
========================
Original URL: https://www-testnetzulunetwork-io.pages.dev
Prompt: Design a community engagement platform using blockchain and decentralized finance (DeFi) principles, inspired by Zulu Network's approach.
Generated: DETERMINISTIC_685a5a3403171816
Batch ID: 20250622_205751
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
with open('CommunityEngagement.json') as f:
    contract_data = json.load(f)
    contract_address = contract_data['address']
    contract_abi = contract_data['abi']

# Initialize contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Error handling for user input
def validate_user_input(data):
    if 'user_id' not in data or 'engagement_type' not in data:
        raise ValueError("Invalid input: 'user_id' and 'engagement_type' are required")

# Route to create a new engagement
@app.route('/engagement', methods=['POST'])
def create_engagement():
    try:
        # Get JSON data from request
        data = request.get_json()
        validate_user_input(data)

        user_id = data['user_id']
        engagement_type = data['engagement_type']

        # Prepare transaction
        tx = contract.functions.createEngagement(user_id, engagement_type).buildTransaction({
            'from': web3.eth.defaultAccount,
            'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        })

        # Sign and send transaction
        signed_tx = web3.eth.account.signTransaction(tx, private_key=os.getenv('PRIVATE_KEY'))
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Wait for transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        return jsonify({'status': 'success', 'transaction_hash': tx_receipt.transactionHash.hex()}), 201

    except ValueError as ve:
        return jsonify({'status': 'error', 'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An error occurred: ' + str(e)}), 500

# Route to get engagement details
@app.route('/engagement/<user_id>', methods=['GET'])
def get_engagement(user_id):
    try:
        # Call smart contract function to get engagement details
        engagement_details = contract.functions.getEngagement(user_id).call()
        return jsonify({'status': 'success', 'engagement_details': engagement_details}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An error occurred: ' + str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Set default account for transactions
    web3.eth.defaultAccount = web3.eth.accounts[0]  # Replace with your account
    app.run(host='0.0.0.0', port=5000)
```

### Note:
- Ensure you have the necessary environment variables set (`INFURA_URL` and `PRIVATE_KEY`).
- The smart contract ABI and address should be stored in a file named `CommunityEngagement.json`.
- This code assumes that the smart contract has functions `createEngagement` and `getEngagement` defined. Adjust the function names and parameters as per your contract's implementation.
