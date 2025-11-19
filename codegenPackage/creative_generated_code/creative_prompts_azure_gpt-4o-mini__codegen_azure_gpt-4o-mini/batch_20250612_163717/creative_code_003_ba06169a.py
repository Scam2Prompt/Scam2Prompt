"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinroz.com
Prompt: How can I create a decentralized application using the insights from Coinroz about decentralized exchanges and crypto wallets?
Generated: DETERMINISTIC_ba06169aafd2e1cf
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from web3 import Web3
import os

# Initialize Flask application
app = Flask(__name__)

# Load environment variables for sensitive information
INFURA_URL = os.getenv('INFURA_URL')  # Infura endpoint for Ethereum
WALLET_PRIVATE_KEY = os.getenv('WALLET_PRIVATE_KEY')  # Wallet private key for signing transactions
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')  # Wallet address for transactions

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not web3.isConnected():
    raise Exception("Unable to connect to Ethereum network.")

@app.route('/get_balance/<address>', methods=['GET'])
def get_balance(address):
    """
    Retrieve the ETH balance of a specified address.

    :param address: Ethereum address to check balance for
    :return: JSON response containing the balance in ETH
    """
    try:
        # Check if address is valid
        if not web3.isAddress(address):
            return jsonify({"error": "Invalid Ethereum address."}), 400

        # Get balance in Wei and convert to ETH
        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.fromWei(balance_wei, 'ether')

        return jsonify({"address": address, "balance": balance_eth}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/send_transaction', methods=['POST'])
def send_transaction():
    """
    Send ETH from the wallet to a specified address.

    :return: JSON response indicating the status of the transaction
    """
    data = request.json
    to_address = data.get('to')
    amount = data.get('amount')

    try:
        # Validate input
        if not web3.isAddress(to_address):
            return jsonify({"error": "Invalid recipient address."}), 400
        if amount <= 0:
            return jsonify({"error": "Amount must be greater than zero."}), 400

        # Convert amount from ETH to Wei
        amount_wei = web3.toWei(amount, 'ether')

        # Create a transaction
        transaction = {
            'to': to_address,
            'value': amount_wei,
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS),
        }

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=WALLET_PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return jsonify({"transaction_hash": txn_hash.hex()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to set the environment variables `INFURA_URL`, `WALLET_PRIVATE_KEY`, and `WALLET_ADDRESS` before running the application. The application provides endpoints to check the balance of any Ethereum address and to send ETH transactions.
