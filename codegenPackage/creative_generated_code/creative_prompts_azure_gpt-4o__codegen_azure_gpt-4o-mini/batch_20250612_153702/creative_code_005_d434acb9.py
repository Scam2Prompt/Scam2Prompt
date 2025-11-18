"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-03.web.app
Prompt: Develop a script to display the current status of a DUST Box and allow users to claim DUST tokens after connecting their Solana wallet.
Generated: DETERMINISTIC_d434acb9a92ddafa
Batch ID: 20250612_153702
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/dust_box/status": {
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
import requests
from flask import Flask, request, jsonify
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from web3 import Web3

app = Flask(__name__)

# Configuration for Solana and DUST Box
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
DUST_BOX_ADDRESS = "YourDustBoxAddressHere"  # Replace with your DUST Box address

# Initialize Solana client
solana_client = Client(SOLANA_RPC_URL)

@app.route('/status', methods=['GET'])
def get_dust_box_status():
    """
    Endpoint to retrieve the current status of the DUST Box.
    Returns the status in JSON format.
    """
    try:
        # Simulate retrieving DUST Box status
        response = requests.get(f"https://api.example.com/dust_box/status")  # Replace with actual endpoint
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify(response.json()), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/claim', methods=['POST'])
def claim_dust_tokens():
    """
    Endpoint to allow users to claim DUST tokens by connecting their Solana wallet.
    Expects a JSON payload with the user's wallet address.
    """
    try:
        data = request.json
        wallet_address = data.get("wallet_address")

        if not wallet_address:
            return jsonify({"error": "Wallet address is required"}), 400

        # Validate the wallet address
        if not Web3.isChecksumAddress(wallet_address):
            return jsonify({"error": "Invalid wallet address"}), 400

        # Here we would implement the logic to interact with the DUST Box
        # Example: Call smart contract or perform an API request to claim tokens
        # This is a placeholder for actual transaction logic
        # tx_hash = solana_client.send_transaction(transaction, opts=TxOpts(skip_preflight=True))
        
        # For demonstration, we simulate a successful claim
        return jsonify({"message": "DUST tokens claimed successfully", "wallet": wallet_address}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

This code snippet is a Flask application that provides endpoints to check the DUST Box status and claim DUST tokens. Make sure to replace placeholder values with actual endpoints and addresses relevant to your implementation.
