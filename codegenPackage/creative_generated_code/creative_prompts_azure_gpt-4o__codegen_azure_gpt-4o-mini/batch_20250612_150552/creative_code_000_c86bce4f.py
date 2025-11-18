"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a Python script to interact with the Oracle Meme presale page using Web3, allowing users to connect their MetaMask wallet and purchase OMEME tokens with BNB or USDT.
Generated: DETERMINISTIC_c86bce4f25d2d46f
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Connect to the Ethereum network
def get_web3():
    infura_url = os.getenv('INFURA_URL')
    return Web3(Web3.HTTPProvider(infura_url))

# Load contract ABI and address
def load_contract():
    with open('contract_abi.json') as f:
        contract_abi = json.load(f)
    contract_address = os.getenv('CONTRACT_ADDRESS')
    return get_web3().eth.contract(address=contract_address, abi=contract_abi)

# Endpoint to connect MetaMask wallet
@app.route('/connect', methods=['POST'])
def connect_wallet():
    wallet_address = request.json.get('wallet_address')
    if not wallet_address:
        return jsonify({"error": "Wallet address is required"}), 400
    return jsonify({"message": "Wallet connected", "address": wallet_address}), 200

# Endpoint to purchase OMEME tokens
@app.route('/purchase', methods=['POST'])
def purchase_tokens():
    data = request.json
    wallet_address = data.get('wallet_address')
    amount = data.get('amount')  # Amount in BNB or USDT

    if not wallet_address or not amount:
        return jsonify({"error": "Wallet address and amount are required"}), 400

    # Initialize web3 and contract
    w3 = get_web3()
    contract = load_contract()

    # Check if wallet is connected and amount is valid
    if not w3.isConnected():
        return jsonify({"error": "Failed to connect to Ethereum network"}), 500

    try:
        # Create transaction dictionary
        tx = {
            'from': wallet_address,
            'value': w3.toWei(amount, 'ether'),  # Convert amount to Wei
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei')
        }

        # Estimate gas for the transaction
        estimated_gas = contract.functions.buyTokens().estimateGas(tx)

        # Send transaction
        tx_hash = contract.functions.buyTokens().transact({
            'from': wallet_address,
            'value': w3.toWei(amount, 'ether'),
            'gas': estimated_gas
        })

        # Wait for transaction to be mined
        w3.eth.waitForTransactionReceipt(tx_hash)

        return jsonify({"message": "Purchase successful", "transaction_hash": tx_hash.hex()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)
```

### Notes
- Ensure you have the following environment variables set in a `.env` file:
  - `INFURA_URL`: Your Infura project endpoint.
  - `CONTRACT_ADDRESS`: The address of the OMEME token contract.
- The `contract_abi.json` file should contain the ABI of the smart contract you are interacting with.
- This script assumes the `buyTokens` function is defined in the smart contract to handle the token purchase logic.
- Flask must be installed in your environment (`pip install Flask`), as well as `web3.py` and `python-dotenv`.
