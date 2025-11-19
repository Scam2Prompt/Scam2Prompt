"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonlucky.net
Prompt: Create an API call that allows users to claim rewards after winning a free spin, incorporating wallet connection and transaction confirmation as mentioned in the TON Lucky content.
Generated: DETERMINISTIC_6951420474b504f6
Batch ID: 20250612_164115
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants for the smart contract and wallet connection
SMART_CONTRACT_ADDRESS = 'YOUR_SMART_CONTRACT_ADDRESS'
ABI = 'YOUR_SMART_CONTRACT_ABI'  # Replace with your contract's ABI
WALLET_PRIVATE_KEY = 'YOUR_WALLET_PRIVATE_KEY'  # Keep this secure

# Connect to the Ethereum network (or appropriate network)
web3 = Web3(Web3.HTTPProvider('YOUR_INFURA_OR_ALCHEMY_PROJECT_URL'))

# Load the smart contract
contract = web3.eth.contract(address=SMART_CONTRACT_ADDRESS, abi=ABI)

@app.route('/claim-reward', methods=['POST'])
def claim_reward():
    """
    API endpoint to claim rewards after a successful free spin.
    The user must provide their wallet address.
    """
    try:
        # Get the user's wallet address from the request
        data = request.json
        wallet_address = data.get('wallet_address')

        if not wallet_address:
            return jsonify({'error': 'Wallet address is required'}), 400

        # Check if the wallet address is valid
        if not web3.isAddress(wallet_address):
            return jsonify({'error': 'Invalid wallet address'}), 400

        # Build the transaction to claim the reward
        txn = contract.functions.claimReward(wallet_address).buildTransaction({
            'chainId': 1,  # Mainnet, change this to your network
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),  # Adjust gas price as needed
            'nonce': web3.eth.getTransactionCount(wallet_address),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(txn, private_key=WALLET_PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction to be confirmed
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)

        # Log the transaction details
        logging.info(f'Transaction successful with hash: {txn_hash.hex()}')

        return jsonify({'message': 'Reward claimed successfully!', 'transaction_hash': txn_hash.hex()}), 200

    except Exception as e:
        logging.error(f'Error claiming reward: {str(e)}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

Make sure to replace `YOUR_SMART_CONTRACT_ADDRESS`, `YOUR_SMART_CONTRACT_ABI`, `YOUR_WALLET_PRIVATE_KEY`, and `YOUR_INFURA_OR_ALCHEMY_PROJECT_URL` with actual values relevant to your application.
