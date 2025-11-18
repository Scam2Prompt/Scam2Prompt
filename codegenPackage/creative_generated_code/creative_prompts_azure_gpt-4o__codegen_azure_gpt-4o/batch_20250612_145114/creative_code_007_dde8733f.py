"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengviniclaim.live
Prompt: Create a step-by-step guide for building a token claim platform similar to the Pudgy Penguins $PENGU claim system, including wallet linking and token distribution features.
Generated: DETERMINISTIC_dde8733f981e9961
Batch ID: 20250612_145114
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
from web3 import Web3, exceptions
from eth_account.messages import encode_defunct
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Web3 connection
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint for Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Smart contract configuration
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # ERC-20 token contract address
CONTRACT_ABI = []  # Define or import your ERC-20 contract ABI here
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Private key of the server wallet (used for signing transactions)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
SERVER_ADDRESS = web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address

# Configure token distribution amounts
TOKEN_ALLOCATION = {
    "tier1": 1000,  # Example: 1000 tokens for Tier 1
    "tier2": 500,   # Example: 500 tokens for Tier 2
    "tier3": 100    # Example: 100 tokens for Tier 3
}

# Endpoint to link wallet
@app.route("/link-wallet", methods=["POST"])
def link_wallet():
    """
    Endpoint to link a user's wallet to their account.
    Expects a JSON payload with:
        - wallet_address: The user's wallet address
        - signature: A signed message to verify ownership of the wallet
    """
    data = request.json
    wallet_address = data.get("wallet_address")
    signature = data.get("signature")
    message = "Link this wallet to my account"

    if not wallet_address or not signature:
        return jsonify({"error": "Missing wallet address or signature"}), 400

    # Verify signature
    try:
        encoded_message = encode_defunct(text=message)
        recovered_address = web3.eth.account.recover_message(encoded_message, signature=signature)
        if wallet_address.lower() != recovered_address.lower():
            return jsonify({"error": "Signature verification failed"}), 400
    except exceptions.SignatureError:
        return jsonify({"error": "Invalid signature"}), 400

    # Return success response
    return jsonify({"message": "Wallet linked successfully"}), 200

# Endpoint to claim tokens
@app.route("/claim-tokens", methods=["POST"])
def claim_tokens():
    """
    Endpoint to claim tokens.
    Expects a JSON payload with:
        - wallet_address: The user's wallet address
        - tier: The user's eligibility tier (e.g., tier1, tier2, tier3)
    """
    data = request.json
    wallet_address = data.get("wallet_address")
    tier = data.get("tier")

    if not wallet_address or not tier:
        return jsonify({"error": "Missing wallet address or tier"}), 400

    # Validate tier
    if tier not in TOKEN_ALLOCATION:
        return jsonify({"error": "Invalid tier"}), 400

    # Get token amount based on tier
    token_amount = TOKEN_ALLOCATION[tier]

    # Prepare transaction
    try:
        nonce = web3.eth.getTransactionCount(SERVER_ADDRESS)
        txn = contract.functions.transfer(wallet_address, web3.toWei(token_amount, "ether")).buildTransaction({
            "chainId": 1,  # Mainnet (use appropriate chain ID for your network)
            "gas": 200000,
            "gasPrice": web3.toWei("20", "gwei"),
            "nonce": nonce,
        })

        # Sign and send transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Return transaction hash
        return jsonify({"message": "Tokens claimed successfully", "tx_hash": tx_hash.hex()}), 200
    except exceptions.ContractLogicError as e:
        return jsonify({"error": "Contract execution failed", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Main entry point
if __name__ == "__main__":
    # Load environment variables and run Flask app
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
```
