"""
Generated Code Metadata:
========================
Original URL: https://starknet-website.pages.dev
Prompt: Design a full-node API service for Starknet, including security and audit considerations.
Generated: DETERMINISTIC_26d87646518d8399
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import logging
import os
import json
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import MAINNET
from starknet_py.net.models import StarknetChainId
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables for security
STARKNET_API_KEY = os.getenv("STARKNET_API_KEY")  # Ensure this is set securely
if not STARKNET_API_KEY:
    raise EnvironmentError("STARKNET_API_KEY environment variable is not set.")

# Starknet client initialization
client = GatewayClient(net=MAINNET)

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "error": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unexpected error: {str(e)}")
    return jsonify({"error": "Internal Server Error", "description": str(e)}), 500

# Route: Get block by block number
@app.route("/block/<int:block_number>", methods=["GET"])
def get_block(block_number):
    """
    Fetch block details by block number.
    """
    try:
        block = client.get_block(block_number=block_number)
        return jsonify(block), 200
    except Exception as e:
        logger.error(f"Error fetching block {block_number}: {str(e)}")
        return jsonify({"error": "Failed to fetch block", "description": str(e)}), 500

# Route: Get transaction by transaction hash
@app.route("/transaction/<string:tx_hash>", methods=["GET"])
def get_transaction(tx_hash):
    """
    Fetch transaction details by transaction hash.
    """
    try:
        transaction = client.get_transaction(tx_hash=tx_hash)
        return jsonify(transaction), 200
    except Exception as e:
        logger.error(f"Error fetching transaction {tx_hash}: {str(e)}")
        return jsonify({"error": "Failed to fetch transaction", "description": str(e)}), 500

# Route: Submit a transaction
@app.route("/submit_transaction", methods=["POST"])
def submit_transaction():
    """
    Submit a new transaction to Starknet.
    """
    try:
        data = request.json
        if not data or "transaction" not in data:
            return jsonify({"error": "Invalid request", "description": "Missing transaction data"}), 400

        transaction = data["transaction"]
        response = client.add_transaction(transaction=transaction)
        return jsonify(response), 200
    except Exception as e:
        logger.error(f"Error submitting transaction: {str(e)}")
        return jsonify({"error": "Failed to submit transaction", "description": str(e)}), 500

# Route: Get chain ID
@app.route("/chain_id", methods=["GET"])
def get_chain_id():
    """
    Fetch the chain ID of the Starknet network.
    """
    try:
        chain_id = StarknetChainId.MAINNET.value
        return jsonify({"chain_id": chain_id}), 200
    except Exception as e:
        logger.error(f"Error fetching chain ID: {str(e)}")
        return jsonify({"error": "Failed to fetch chain ID", "description": str(e)}), 500

# Security headers middleware
@app.after_request
def add_security_headers(response):
    """
    Add security headers to all responses.
    """
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

# Run the Flask app
if __name__ == "__main__":
    # Use a secure port and host configuration
    app.run(host="0.0.0.0", port=5000, debug=False)
```
