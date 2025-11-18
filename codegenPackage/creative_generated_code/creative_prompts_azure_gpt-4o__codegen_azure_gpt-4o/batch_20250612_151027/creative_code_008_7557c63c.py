"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyan-8iu.pages.dev
Prompt: Provide a sample implementation of a referral tracking system in a blockchain game that rewards users with $NYAN tokens for inviting friends.
Generated: DETERMINISTIC_7557c63c9a2c815c
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Referral Tracking System for Blockchain Game
# Reward users with $NYAN tokens for inviting friends
# Language: Python
# Frameworks/Libraries: Web3.py for blockchain interaction, Flask for API layer

from flask import Flask, request, jsonify
from web3 import Web3, HTTPProvider
import json
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
INFURA_URL = os.getenv("INFURA_URL")  # Ethereum network provider (Infura URL)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Admin wallet private key for signing transactions
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # $NYAN token smart contract address
ABI_PATH = os.getenv("ABI_PATH", "./abi.json")  # Path to the compiled ABI file

# Connect to Ethereum blockchain
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure connection is established
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum blockchain.")

# Load $NYAN token contract ABI
with open(ABI_PATH, 'r') as abi_file:
    contract_abi = json.load(abi_file)

# Initialize $NYAN token smart contract
nyan_contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# Referral storage (could be moved to a database in production)
referrals = {}  # Format: {"referrer_address": ["referred_address_1", "referred_address_2", ...]}

# Reward amount in $NYAN tokens
REWARD_AMOUNT = web3.toWei(10, 'ether')  # Adjust token decimals as needed

@app.route('/invite', methods=['POST'])
def invite_friend():
    """
    Endpoint for inviting a friend.
    :param referrer: Ethereum address of the referrer (string)
    :param referred: Ethereum address of the referred friend (string)
    :return: JSON response with success status
    """
    try:
        data = request.get_json()
        referrer = data['referrer']
        referred = data['referred']

        # Validate Ethereum addresses
        if not web3.isAddress(referrer) or not web3.isAddress(referred):
            return jsonify({"error": "Invalid Ethereum addresses."}), 400

        # Prevent duplicate referrals
        if referrer not in referrals:
            referrals[referrer] = []
        if referred in referrals[referrer]:
            return jsonify({"error": "Friend already referred."}), 400

        # Store referral relationship
        referrals[referrer].append(referred)

        return jsonify({"message": "Referral recorded successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/reward', methods=['POST'])
def distribute_reward():
    """
    Endpoint for rewarding referrers with $NYAN tokens.
    :param referrer: Ethereum address of the referrer (string)
    :return: JSON response with success status
    """
    try:
        data = request.get_json()
        referrer = data['referrer']

        # Validate Ethereum address
        if not web3.isAddress(referrer):
            return jsonify({"error": "Invalid Ethereum address."}), 400

        # Check if referrer has referrals
        if referrer not in referrals or len(referrals[referrer]) == 0:
            return jsonify({"error": "No referrals found for this referrer."}), 400

        # Build and sign transaction to transfer $NYAN tokens
        nonce = web3.eth.get_transaction_count(web3.toChecksumAddress(referrer))
        tx = nyan_contract.functions.transfer(
            referrer, REWARD_AMOUNT
        ).build_transaction({
            'chainId': 1,  # Ethereum Mainnet ID (adjust for testnets)
            'gas': 200000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce,
        })

        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        return jsonify({"message": "Reward distributed.", "tx_hash": receipt.transactionHash.hex()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/referrals/<address>', methods=['GET'])
def get_referrals(address):
    """
    Endpoint for retrieving referrals for a given address.
    :param address: Ethereum address of the referrer (string)
    :return: JSON response with list of referrals
    """
    try:
        # Validate Ethereum address
        if not web3.isAddress(address):
            return jsonify({"error": "Invalid Ethereum address."}), 400

        # Retrieve referrals
        address = web3.toChecksumAddress(address)
        user_referrals = referrals.get(address, [])

        return jsonify({"referrals": user_referrals}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
```
