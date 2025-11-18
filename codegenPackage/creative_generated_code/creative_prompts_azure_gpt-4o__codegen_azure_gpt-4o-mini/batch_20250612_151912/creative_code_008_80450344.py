"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eosgas.io
Prompt: Recommend APIs or libraries for creating a blockchain platform that supports decentralized transactions between energy producers and cryptocurrency miners, following eosGAS's model.
Generated: DETERMINISTIC_804503440c3bc979
Batch ID: 20250612_151912
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
# Import necessary libraries for blockchain development
from flask import Flask, jsonify, request
from web3 import Web3
import json
import os

app = Flask(__name__)

# Configuration for the Ethereum blockchain
WEB3_PROVIDER = os.getenv('WEB3_PROVIDER', 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID')
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

# Check if Web3 is connected
if not w3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Smart contract address and ABI (Application Binary Interface)
CONTRACT_ADDRESS = '0xYourContractAddress'
contract_abi = json.loads('[...]')  # Replace with your contract ABI

# Initialize the smart contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

@app.route('/transaction', methods=['POST'])
def create_transaction():
    """
    Endpoint to create a transaction between energy producers and cryptocurrency miners.
    """
    try:
        data = request.json
        producer_address = data.get('producer_address')
        miner_address = data.get('miner_address')
        amount = data.get('amount')

        # Validate input data
        if not all([producer_address, miner_address, amount]):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create the transaction
        transaction = contract.functions.createTransaction(producer_address, miner_address, amount).buildTransaction({
            'nonce': w3.eth.getTransactionCount(producer_address),
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
        })

        # Sign the transaction
        private_key = os.getenv('PRODUCER_PRIVATE_KEY')  # Use environment variable for security
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return jsonify({'transaction_hash': txn_hash.hex()}), 201
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

@app.route('/transaction/<txn_hash>', methods=['GET'])
def get_transaction_status(txn_hash):
    """
    Endpoint to get the status of a transaction on the blockchain.
    """
    try:
        receipt = w3.eth.getTransactionReceipt(txn_hash)

        if receipt is None:
            return jsonify({'status': 'pending'}), 202
        
        return jsonify({'status': 'confirmed', 'block_number': receipt.blockNumber}), 200
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Notes
- Ensure to replace `YOUR_INFURA_PROJECT_ID`, `0xYourContractAddress`, and `[...]` with your actual Infura project ID, contract address, and ABI respectively.
- Store sensitive information like private keys in environment variables for security.
- This code uses Flask for creating the API and Web3.py for interacting with the Ethereum blockchain.
