"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mansorytoken.xyz
Prompt: Develop a governance model for the Mansory Token community, allowing token holders to vote on future perks and research priorities.
Generated: DETERMINISTIC_8dc329015efce7f3
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Governance Model for Mansory Token Community
Language: Python
Purpose: Enable token holders to vote on future perks and research priorities.
Dependencies: web3.py, Flask
"""

from flask import Flask, request, jsonify
from web3 import Web3
import json

# Initialize Flask app
app = Flask(__name__)

# Blockchain Configuration
INFURA_URL = "<YOUR_INFURA_PROJECT_URL>"
PRIVATE_KEY = "<YOUR_PRIVATE_KEY>"
CONTRACT_ADDRESS = "<YOUR_SMART_CONTRACT_ADDRESS>"
TOKEN_HOLDERS = {}  # Mocked token holders dictionary; replace with actual blockchain data

# Connect to Ethereum blockchain
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum blockchain.")

# Load Smart Contract ABI
with open('governance_contract_abi.json', 'r') as abi_file:
    CONTRACT_ABI = json.load(abi_file)

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

@app.route('/vote', methods=['POST'])
def cast_vote():
    """
    Endpoint to allow token holders to cast votes on governance proposals.
    """
    try:
        data = request.json
        voter_address = data.get('voter_address')
        proposal_id = data.get('proposal_id')
        vote = data.get('vote')  # Accepts 'yes' or 'no'

        # Validate input
        if not voter_address or not web3.isAddress(voter_address):
            return jsonify({"error": "Invalid voter address."}), 400
        if not proposal_id or not isinstance(proposal_id, int):
            return jsonify({"error": "Invalid proposal ID."}), 400
        if vote not in ['yes', 'no']:
            return jsonify({"error": "Vote must be 'yes' or 'no'."}), 400

        # Check if voter is a token holder
        voter_tokens = TOKEN_HOLDERS.get(voter_address, 0)
        if voter_tokens <= 0:
            return jsonify({"error": "You must hold Mansory Tokens to vote."}), 403

        # Interact with blockchain to cast vote
        nonce = web3.eth.get_transaction_count(voter_address)
        txn = contract.functions.castVote(proposal_id, vote).build_transaction({
            'nonce': nonce,
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'from': voter_address
        })

        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return jsonify({"message": "Vote cast successfully!", "transaction_hash": web3.toHex(txn_hash)}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/proposals', methods=['GET'])
def get_proposals():
    """
    Endpoint to view current governance proposals.
    """
    try:
        proposals = contract.functions.getProposals().call()
        return jsonify({"proposals": proposals}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/results/<int:proposal_id>', methods=['GET'])
def get_results(proposal_id):
    """
    Endpoint to view results of a specific governance proposal.
    """
    try:
        results = contract.functions.getProposalResults(proposal_id).call()
        return jsonify({"proposal_id": proposal_id, "results": results}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
