"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimesa.pages.dev
Prompt: Recommend best practices for building a secure token airdrop portal, referencing Masa's eligibility check and wallet connection features.
Generated: DETERMINISTIC_c8e319225869a278
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script for a secure token airdrop portal leveraging Web3 and eligibility checks.
# This implementation utilizes Flask for the web portal, Web3.py for wallet connection,
# and includes best practices for security and error handling.

from flask import Flask, request, jsonify
from web3 import Web3, HTTPProvider
import os
import jwt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration variables
INFURA_URL = os.getenv('INFURA_URL')  # Infura endpoint for Ethereum network connection
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Private key of the admin wallet (store securely)
JWT_SECRET = os.getenv('JWT_SECRET')  # Secret for JWT token signing
TOKEN_CONTRACT_ADDRESS = os.getenv('TOKEN_CONTRACT_ADDRESS')  # Token contract address
ELIGIBILITY_CHECK_API = os.getenv('ELIGIBILITY_CHECK_API')  # External eligibility API URL

app = Flask(__name__)

# Initialize Web3 connection
web3 = Web3(HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Token contract ABI (simplified for this example)
TOKEN_CONTRACT_ABI = [
    {
        "constant": False,
        "inputs": [{"name": "to", "type": "address"}, {"name": "value", "type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]
contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=TOKEN_CONTRACT_ABI)

# Helper function: Validate wallet address
def is_valid_address(wallet_address):
    return web3.isAddress(wallet_address)

# Helper function: Check eligibility
def check_eligibility(wallet_address):
    try:
        response = requests.post(ELIGIBILITY_CHECK_API, json={"wallet_address": wallet_address})
        if response.status_code == 200:
            return response.json().get("eligible", False)
        return False
    except Exception as e:
        print(f"Eligibility check failed: {e}")
        return False

# Helper function: Generate JWT token
def generate_jwt(wallet_address):
    payload = {"wallet_address": wallet_address}
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

# Route: Connect wallet
@app.route('/connect-wallet', methods=['POST'])
def connect_wallet():
    try:
        data = request.json
        wallet_address = data.get("wallet_address")
        
        if not wallet_address or not is_valid_address(wallet_address):
            return jsonify({"error": "Invalid wallet address"}), 400
        
        eligibility = check_eligibility(wallet_address)
        if not eligibility:
            return jsonify({"error": "Wallet not eligible for airdrop"}), 403
        
        jwt_token = generate_jwt(wallet_address)
        return jsonify({"message": "Wallet connected successfully", "token": jwt_token}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Airdrop tokens
@app.route('/airdrop', methods=['POST'])
def airdrop():
    try:
        data = request.json
        wallet_address = data.get("wallet_address")
        jwt_token = data.get("token")
        amount = data.get("amount")
        
        # Validate wallet address
        if not wallet_address or not is_valid_address(wallet_address):
            return jsonify({"error": "Invalid wallet address"}), 400
        
        # Validate JWT token
        try:
            decoded_token = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"])
            if decoded_token.get("wallet_address") != wallet_address:
                return jsonify({"error": "Token verification failed"}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 403
        
        # Execute token transfer
        nonce = web3.eth.getTransactionCount(web3.eth.defaultAccount)
        tx = contract.functions.transfer(wallet_address, int(amount)).buildTransaction({
            'nonce': nonce,
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei')
        })
        signed_tx = web3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return jsonify({"message": "Airdrop successful", "tx_hash": web3.toHex(tx_hash)}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
