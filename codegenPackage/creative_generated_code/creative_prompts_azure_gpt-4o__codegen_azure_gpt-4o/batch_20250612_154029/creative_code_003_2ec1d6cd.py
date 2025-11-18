"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quecko.com
Prompt: Create an API integration for a Web3 mobile app that connects to both L1 and L2 blockchain networks, as highlighted in Quecko's services.
Generated: DETERMINISTIC_2ec1d6cd0336ae83
Batch ID: 20250612_154029
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://optimism-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
from web3 import Web3
from flask import Flask, jsonify, request

# Flask app initialization
app = Flask(__name__)

# Configuration for blockchain networks
CONFIG = {
    "L1": {
        "rpc_url": "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
        "chain_name": "Ethereum Mainnet",
    },
    "L2": {
        "rpc_url": "https://optimism-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
        "chain_name": "Optimism L2",
    },
}

# Initialize Web3 instances for L1 and L2 networks
web3_l1 = Web3(Web3.HTTPProvider(CONFIG["L1"]["rpc_url"]))
web3_l2 = Web3(Web3.HTTPProvider(CONFIG["L2"]["rpc_url"]))

# Helper function to check connection to blockchain
def check_connection(web3_instance, chain_name):
    try:
        if web3_instance.isConnected():
            return {
                "status": "Connected",
                "chain_name": chain_name,
                "block_number": web3_instance.eth.block_number,
            }
        else:
            return {
                "status": "Not Connected",
                "chain_name": chain_name,
            }
    except Exception as e:
        return {
            "status": "Error",
            "chain_name": chain_name,
            "error_message": str(e),
        }

# Route to check L1 and L2 connections
@app.route("/api/v1/check_connections", methods=["GET"])
def check_connections():
    l1_status = check_connection(web3_l1, CONFIG["L1"]["chain_name"])
    l2_status = check_connection(web3_l2, CONFIG["L2"]["chain_name"])
    return jsonify({"L1": l1_status, "L2": l2_status})

# Route to get account balance on a given chain
@app.route("/api/v1/get_balance", methods=["POST"])
def get_balance():
    try:
        data = request.json
        address = data.get("address")
        chain = data.get("chain")

        if not address or not chain:
            return jsonify({"error": "Missing 'address' or 'chain' field"}), 400

        # Choose the appropriate Web3 instance based on the chain
        web3_instance = web3_l1 if chain == "L1" else web3_l2 if chain == "L2" else None
        if web3_instance is None:
            return jsonify({"error": "Invalid chain specified"}), 400

        # Validate Ethereum address
        if not web3_instance.isAddress(address):
            return jsonify({"error": "Invalid Ethereum address"}), 400

        # Fetch balance
        balance = web3_instance.eth.get_balance(address)
        human_readable_balance = web3_instance.fromWei(balance, "ether")

        return jsonify({"address": address, "balance": human_readable_balance, "chain": chain})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for undefined routes
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Start Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```
