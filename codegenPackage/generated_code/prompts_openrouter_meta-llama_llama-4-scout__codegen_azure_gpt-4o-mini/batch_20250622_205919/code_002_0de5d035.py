"""
Generated Code Metadata:
========================
Original URL: https://leaconcapitalltd.com
Prompt: Generate a sample investment portfolio management system that uses blockchain technology and cryptocurrencies, inspired by Leacon Capital Ltd's investment solutions.
Generated: DETERMINISTIC_0de5d0351a50c8ee
Batch ID: 20250622_205919
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

# Connect to Ethereum blockchain (using Infura or local node)
infura_url = os.getenv('INFURA_URL')  # Set your Infura URL in environment variables
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected to the blockchain
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Sample smart contract ABI and address (replace with your own)
contract_address = '0xYourSmartContractAddress'
contract_abi = json.loads('''[
    {
        "constant": true,
        "inputs": [],
        "name": "getPortfolio",
        "outputs": [{"name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [{"name": "asset", "type": "string"}, {"name": "amount", "type": "uint256"}],
        "name": "addAsset",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]''')

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    """Fetch the investment portfolio from the smart contract."""
    try:
        portfolio = contract.functions.getPortfolio().call()
        return jsonify({'portfolio': portfolio}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/portfolio', methods=['POST'])
def add_asset():
    """Add an asset to the investment portfolio."""
    data = request.json
    asset = data.get('asset')
    amount = data.get('amount')

    if not asset or not isinstance(amount, (int, float)):
        return jsonify({'error': 'Invalid input. Asset and amount are required.'}), 400

    # Replace with your wallet address and private key
    wallet_address = os.getenv('WALLET_ADDRESS')
    private_key = os.getenv('PRIVATE_KEY')

    # Build transaction
    nonce = web3.eth.getTransactionCount(wallet_address)
    transaction = contract.functions.addAsset(asset, amount).buildTransaction({
        'chainId': 1,  # Mainnet
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    # Sign the transaction
    signed_txn = web3.eth.account.signTransaction(transaction, private_key)

    # Send the transaction
    try:
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return jsonify({'transaction_hash': web3.toHex(txn_hash)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
- Ensure to set the environment variables `INFURA_URL`, `WALLET_ADDRESS`, and `PRIVATE_KEY` before running the application.
- Replace the `contract_address` and `contract_abi` with your actual smart contract details.
- This code is a basic example and should be expanded with additional features and security measures for production use.
