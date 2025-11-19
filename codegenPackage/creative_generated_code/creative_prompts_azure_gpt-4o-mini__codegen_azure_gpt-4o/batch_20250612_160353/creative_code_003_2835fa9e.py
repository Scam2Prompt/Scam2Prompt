"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgn-faucet.vercel.app
Prompt: What libraries or APIs are recommended for building a Gitcoin Passport Gated Faucet similar to the one at pgn-faucet.vercel.app?
Generated: DETERMINISTIC_2835fa9eb0920e74
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation that uses Flask and web3.py to create a Gitcoin Passport Gated Faucet:

```python
import os
import json
from flask import Flask, request, jsonify
from web3 import Web3
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# Load environment variables
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint for Ethereum network
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the faucet account
FAUCET_ADDRESS = os.getenv("FAUCET_ADDRESS")  # Faucet account address
TOKEN_ADDRESS = os.getenv("TOKEN_ADDRESS")  # ERC20 contract address
PASSPORT_API_URL = os.getenv("PASSPORT_API_URL")  # Gitcoin Passport API URL
PASSPORT_API_KEY = os.getenv("PASSPORT_API_KEY")  # Gitcoin Passport API Key
REQUIRED_SCORE = float(os.getenv("REQUIRED_SCORE", 15))  # Minimum trust score

# Web3 initialization
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum network")

# ERC20 ABI
ERC20_ABI = json.loads("""[
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {"name": "recipient", "type": "address"},
            {"name": "amount", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]""")

# Token contract initialization
token_contract = web3.eth.contract(address=Web3.to_checksum_address(TOKEN_ADDRESS), abi=ERC20_ABI)


def get_passport_score(wallet_address):
    """
    Fetch the Gitcoin Passport trust score for a given wallet address.
    """
    headers = {
        "Authorization": f"Bearer {PASSPORT_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        f"{PASSPORT_API_URL}/score",
        json={"address": wallet_address},
        headers=headers
    )
    if response.status_code != 200:
        return None, f"Error fetching passport score: {response.text}"

    data = response.json()
    score = data.get("score")
    return score, None


@app.route("/faucet", methods=["POST"])
def faucet():
    """
    Faucet endpoint to send tokens to users with a sufficient Gitcoin Passport trust score.
    """
    try:
        # Parse JSON payload
        payload = request.get_json()
        wallet_address = payload.get("wallet_address")

        # Validate wallet address
        if not web3.isAddress(wallet_address):
            return jsonify({"error": "Invalid wallet address"}), 400

        # Check Gitcoin Passport trust score
        score, error = get_passport_score(wallet_address)
        if error:
            return jsonify({"error": error}), 500

        if score < REQUIRED_SCORE:
            return jsonify({"error": "Insufficient trust score"}), 403

        # Set up transaction parameters
        faucet_balance = token_contract.functions.balanceOf(Web3.to_checksum_address(FAUCET_ADDRESS)).call()
        amount_to_send = web3.to_wei(0.01, "ether")  # Define the token amount to send (example: 0.01 tokens)

        if faucet_balance < amount_to_send:
            return jsonify({"error": "Faucet out of funds"}), 500

        nonce = web3.eth.get_transaction_count(Web3.to_checksum_address(FAUCET_ADDRESS))
        transaction = token_contract.functions.transfer(
            Web3.to_checksum_address(wallet_address),
            amount_to_send
        ).build_transaction({
            "chainId": web3.eth.chain_id,
            "gas": 200000,
            "gasPrice": web3.eth.gas_price,
            "nonce": nonce
        })

        # Sign and send the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return jsonify({"success": True, "txn_hash": web3.to_hex(txn_hash)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint to ensure the server is running.
    """
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # Run the Flask server
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
1. **Dependencies:** You need to install `Flask`, `web3`, `python-dotenv`, and `requests`. Use `pip install flask web3 python-dotenv requests`.
2. **Environment Variables:** Store sensitive information like `INFURA_URL`, `PRIVATE_KEY`, `TOKEN_ADDRESS`, etc., in a `.env` file.
3. **Passport Integration:** The code assumes you have access to the Gitcoin Passport API, and that the wallet address's score can be fetched via an API call.
4. **Error Handling:** Proper error handling is included for external API calls, transaction failures, and invalid inputs.
