"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Create a tutorial-style Python script for deploying a decentralized application (dApp) that addresses global systemic challenges, as discussed in the ETHBerlin04 manifesto.
Generated: DETERMINISTIC_fe6426729d2759e3
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from web3 import Web3
import json
import os

# Initialize Flask application
app = Flask(__name__)

# Connect to Ethereum network (using Infura as an example)
INFURA_URL = os.getenv('INFURA_URL')  # Set your Infura URL in environment variables
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Load smart contract ABI and address
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')  # Set your contract address in environment variables
with open('contract_abi.json') as f:
    contract_abi = json.load(f)

# Initialize contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

@app.route('/deploy', methods=['POST'])
def deploy_dapp():
    """
    Deploy a new instance of the dApp smart contract.
    Expects a JSON payload with the necessary parameters.
    """
    try:
        data = request.json
        # Validate input data
        if 'name' not in data or 'description' not in data:
            return jsonify({"error": "Missing required fields: name, description"}), 400
        
        # Prepare transaction
        transaction = contract.functions.createDApp(data['name'], data['description']).buildTransaction({
            'from': web3.eth.defaultAccount,
            'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        })

        # Sign the transaction
        private_key = os.getenv('PRIVATE_KEY')  # Set your private key in environment variables
        signed_txn = web3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction receipt
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)

        return jsonify({"transaction_hash": txn_hash.hex(), "receipt": txn_receipt}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/dapps', methods=['GET'])
def list_dapps():
    """
    List all deployed dApps.
    """
    try:
        # Fetch all dApps from the smart contract
        dapps = contract.functions.getAllDApps().call()
        return jsonify(dapps), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Set default account for transactions
    web3.eth.defaultAccount = web3.eth.account.from_key(os.getenv('PRIVATE_KEY')).address

    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Ensure you have the required libraries installed: `Flask`, `web3`, and any others you may need.
- Set the environment variables `INFURA_URL`, `CONTRACT_ADDRESS`, and `PRIVATE_KEY` before running the script.
- The smart contract should have the functions `createDApp` and `getAllDApps` implemented for this script to work correctly.
- The ABI file for the smart contract should be saved as `contract_abi.json` in the same directory as this script.
