"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-wienerdogai.pages.dev
Prompt: Create a Python script using Web3.py to interact with a presale smart contract, allowing users to connect their wallet, purchase tokens, and stake them for rewards.
Generated: DETERMINISTIC_b6f0fba28df94085
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from eth_account import Account
from flask import Flask, request, jsonify, render_template

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum network (replace with your Infura/Alchemy URL)
WEB3_PROVIDER = os.getenv('WEB3_PROVIDER', 'YOUR_ETHEREUM_NODE_URL')
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

# Check if connected to the Ethereum network
if not w3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum network.")

# Load contract details
PRESALE_CONTRACT_ADDRESS = os.getenv('PRESALE_CONTRACT_ADDRESS', 'YOUR_PRESALE_CONTRACT_ADDRESS')
PRESALE_ABI = [...]  # Replace with your presale contract ABI

# Create contract instance
presale_contract = w3.eth.contract(address=PRESALE_CONTRACT_ADDRESS, abi=PRESALE_ABI)

@app.route('/')
def index():
    return render_template('index.html')  # Serve HTML frontend

@app.route('/connect_wallet', methods=['POST'])
def connect_wallet():
    """Connect user's wallet and retrieve account address."""
    private_key = request.json.get('privateKey')
    if not private_key:
        return jsonify({"error": "Private key is required"}), 400
    
    try:
        account = Account.from_key(private_key)
        return jsonify({"address": account.address}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/purchase_tokens', methods=['POST'])
def purchase_tokens():
    """Purchase tokens in presale."""
    data = request.json
    address = data.get('address')
    amount = w3.toWei(data.get('amount'), 'ether')  # Convert amount to Wei
    
    if not address or not amount:
        return jsonify({"error": "Address and amount are required"}), 400
    
    try:
        # Create transaction
        nonce = w3.eth.getTransactionCount(address)
        transaction = presale_contract.functions.buyTokens().buildTransaction({
            'from': address,
            'value': amount,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),  # Adjust gas price as needed
            'nonce': nonce,
        })

        # Sign transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=data.get('privateKey'))
        
        # Send transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return jsonify({"transactionHash": w3.toHex(txn_hash)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stake_tokens', methods=['POST'])
def stake_tokens():
    """Stake purchased tokens for rewards."""
    data = request.json
    address = data.get('address')
    amount = w3.toWei(data.get('amount'), 'ether')  # Convert amount to Wei

    if not address or not amount:
        return jsonify({"error": "Address and amount are required"}), 400
    
    try:
        # Create transaction for staking
        nonce = w3.eth.getTransactionCount(address)
        transaction = presale_contract.functions.stakeTokens(amount).buildTransaction({
            'from': address,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),  # Adjust gas price as needed
            'nonce': nonce,
        })

        # Sign transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=data.get('privateKey'))
        
        # Send transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return jsonify({"transactionHash": w3.toHex(txn_hash)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to replace placeholders with actual values, and install dependencies using `pip install web3 flask eth-account`. This script assumes you have a simple HTML frontend in place for wallet connection and interaction.
