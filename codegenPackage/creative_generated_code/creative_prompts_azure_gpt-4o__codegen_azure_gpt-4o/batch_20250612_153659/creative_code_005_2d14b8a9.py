"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappass.neocities.org
Prompt: Suggest tools or APIs for managing fair distribution of NFTs or passes in a blockchain application, referencing the Dapp Pass "first come, first serve" minting system.
Generated: DETERMINISTIC_2d14b8a948a61b1d
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a fair distribution system for NFTs or passes in a blockchain application. 
It uses a "first come, first serve" minting system approach.

Dependencies: 
- Web3.py (for interacting with Ethereum blockchain)
- Flask (for API server)
"""

from flask import Flask, request, jsonify
from web3 import Web3
import time

app = Flask(__name__)

# Blockchain configuration
INFURA_URL = "<YOUR_INFURA_PROJECT_URL>"  # Replace with your Infura endpoint
CONTRACT_ADDRESS = "<YOUR_CONTRACT_ADDRESS>"  # Replace with your NFT contract address
PRIVATE_KEY = "<YOUR_PRIVATE_KEY>"  # Replace with your wallet's private key
PUBLIC_ADDRESS = "<YOUR_PUBLIC_ADDRESS>"  # Replace with your wallet's public address

# Connect to Ethereum blockchain
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise Exception("Unable to connect to Ethereum blockchain")

# Load contract ABI (replace with your NFT contract ABI)
CONTRACT_ABI = [
    # Add your contract ABI here
]

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# In-memory store to track reservation requests
reservations = {}
MAX_SUPPLY = 1000  # Maximum NFTs/passes that can be minted
minted_count = 0  # Counter for minted NFTs/passes
MINT_PRICE = web3.toWei(0.05, 'ether')  # Price per NFT/pass

@app.route('/reserve', methods=['POST'])
def reserve_nft():
    """
    Endpoint to reserve an NFT or pass in the "first come, first serve" system.
    Request body should include a valid Ethereum address.
    """
    global minted_count

    data = request.json
    user_address = data.get('address')

    # Input validation
    if not user_address or not web3.isAddress(user_address):
        return jsonify({"error": "Invalid Ethereum address"}), 400

    if minted_count >= MAX_SUPPLY:
        return jsonify({"error": "Minting has ended. Maximum supply reached"}), 400

    # Check if address has already reserved
    if user_address in reservations:
        return jsonify({"error": "Address has already reserved"}), 400

    # Add to reservations with a timestamp for fairness
    reservations[user_address] = time.time()

    return jsonify({"message": "Reservation successful", "address": user_address}), 200

@app.route('/mint', methods=['POST'])
def mint_nft():
    """
    Endpoint for users to mint an NFT/pass after reserving.
    Request body should include the user's Ethereum address.
    """
    global minted_count

    data = request.json
    user_address = data.get('address')

    # Input validation
    if not user_address or not web3.isAddress(user_address):
        return jsonify({"error": "Invalid Ethereum address"}), 400

    # Ensure the user has made a reservation
    if user_address not in reservations:
        return jsonify({"error": "No reservation found for this address"}), 400

    # Get reservation timestamp and check fairness
    reservation_time = reservations[user_address]
    if time.time() - reservation_time > 600:  # 10-minute expiration
        del reservations[user_address]
        return jsonify({"error": "Reservation expired"}), 400

    if minted_count >= MAX_SUPPLY:
        return jsonify({"error": "Minting has ended. Maximum supply reached"}), 400

    # Generate transaction for minting
    try:
        transaction = contract.functions.mint(user_address).buildTransaction({
            'chainId': 1,  # Ethereum Mainnet
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(PUBLIC_ADDRESS),
            'value': MINT_PRICE,
        })

        # Sign and send the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        minted_count += 1

        # Remove reservation after successful mint
        del reservations[user_address]

        return jsonify({"message": "Minting successful", "transactionHash": web3.toHex(tx_hash)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/status', methods=['GET'])
def status():
    """
    Endpoint to check the status of the minting process.
    Returns the number of minted NFTs/passes and reservations count.
    """
    return jsonify({
        "minted_count": minted_count,
        "reservations_count": len(reservations),
        "max_supply": MAX_SUPPLY
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
```
