"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-shinja-claim-alienform.web.app
Prompt: What are the steps to create a decentralized token project like AlienForm that emphasizes community-led governance and accountability?
Generated: DETERMINISTIC_dd86c46b88a54084
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from web3 import Web3
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum network (Infura or local node)
w3 = Web3(Web3.HTTPProvider(os.getenv('ETH_NODE_URL')))

# Check connection to Ethereum node
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node.")

# Load contract ABI and address
with open('token_abi.json') as f:
    contract_abi = json.load(f)

contract_address = os.getenv('TOKEN_CONTRACT_ADDRESS')
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Define a route for getting the token balance of an address
@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    """
    Get the token balance of a specified address.
    :param address: Ethereum address to check balance for.
    :return: JSON response with the balance.
    """
    try:
        balance = contract.functions.balanceOf(address).call()
        return jsonify({'address': address, 'balance': balance}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Define a route for transferring tokens
@app.route('/transfer', methods=['POST'])
def transfer_tokens():
    """
    Transfer tokens from the sender's address to a specified address.
    Requires `private_key` for signing the transaction.
    """
    data = request.json
    sender_address = data.get('sender_address')
    recipient_address = data.get('recipient_address')
    amount = data.get('amount')
    private_key = data.get('private_key')

    # Validate input data
    if not all([sender_address, recipient_address, amount, private_key]):
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        # Build the transaction
        transaction = contract.functions.transfer(recipient_address, amount).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(sender_address),
        })
        
        # Sign the transaction
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction receipt
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
        
        return jsonify({'transaction_hash': txn_receipt.transactionHash.hex()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Define a route for governance voting
@app.route('/vote', methods=['POST'])
def vote():
    """
    Cast a vote for a governance proposal.
    :param proposal_id: ID of the proposal to vote for.
    :param voter_address: Address of the voter.
    :param vote_choice: Choice of the voter (e.g., 'yes' or 'no').
    :return: JSON response with voting status.
    """
    data = request.json
    proposal_id = data.get('proposal_id')
    voter_address = data.get('voter_address')
    vote_choice = data.get('vote_choice')
    private_key = data.get('private_key')

    if not all([proposal_id, voter_address, vote_choice, private_key]):
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        # Build the transaction for voting
        transaction = contract.functions.vote(proposal_id, vote_choice).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(voter_address),
        })
        
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
        
        return jsonify({'transaction_hash': txn_receipt.transactionHash.hex()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```
