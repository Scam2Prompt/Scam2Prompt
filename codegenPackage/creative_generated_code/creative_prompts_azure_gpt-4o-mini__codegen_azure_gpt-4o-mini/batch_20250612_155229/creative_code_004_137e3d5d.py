"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.pages.dev
Prompt: Create a simple API to interact with a memecoin's smart contract, taking cues from the Owy project's community engagement features.
Generated: DETERMINISTIC_137e3d5d46aaf640
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from web3 import Web3
import json

# Initialize the Flask application
app = Flask(__name__)

# Connect to Ethereum node (e.g., Infura, Alchemy)
w3 = Web3(Web3.HTTPProvider('YOUR_INFURA_OR_ALCHEMY_URL'))

# Replace with your smart contract address and ABI
CONTRACT_ADDRESS = 'YOUR_SMART_CONTRACT_ADDRESS'
ABI = json.loads('YOUR_SMART_CONTRACT_ABI_JSON')

# Create contract instance
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    """
    Endpoint to get the balance of a specified address.
    :param address: The Ethereum address to check the balance for.
    :return: JSON response with the balance.
    """
    try:
        # Validate the address
        if not w3.isAddress(address):
            return jsonify({'error': 'Invalid address'}), 400
        
        # Get balance from the smart contract
        balance = contract.functions.balanceOf(address).call()
        return jsonify({'address': address, 'balance': balance}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/transfer', methods=['POST'])
def transfer():
    """
    Endpoint to transfer tokens from one address to another.
    :return: JSON response with transaction hash or error message.
    """
    data = request.json
    sender = data.get('sender')
    receiver = data.get('receiver')
    amount = data.get('amount')
    private_key = data.get('private_key')

    # Validate input data
    if not all([sender, receiver, amount, private_key]):
        return jsonify({'error': 'Missing parameters'}), 400
    
    if not w3.isAddress(sender) or not w3.isAddress(receiver):
        return jsonify({'error': 'Invalid address'}), 400

    try:
        # Prepare the transaction
        nonce = w3.eth.getTransactionCount(sender)
        txn = contract.functions.transfer(receiver, amount).buildTransaction({
            'chainId': 1,  # Mainnet ID; change for testnet
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = w3.eth.account.signTransaction(txn, private_key=private_key)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Return transaction hash
        return jsonify({'transaction_hash': txn_hash.hex()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app on the local development server
    app.run(host='0.0.0.0', port=5000)
```
