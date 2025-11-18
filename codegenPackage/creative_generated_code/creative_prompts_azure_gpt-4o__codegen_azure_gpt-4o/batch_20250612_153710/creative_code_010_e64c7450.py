"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-chainbase.com
Prompt: Generate a code snippet to utilize Chainbase's API for building a real-time blockchain data explorer dashboard.
Generated: DETERMINISTIC_e64c745024329a6b
Batch ID: 20250612_153710
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainbase.online/v1/blockchain": {
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
from flask import Flask, jsonify, request

app = Flask(__name__)

# Replace with your Chainbase API key
CHAINBASE_API_KEY = "your_chainbase_api_key"
CHAINBASE_API_URL = "https://api.chainbase.online/v1/blockchain"

# Function to fetch blockchain data from the Chainbase API
def fetch_blockchain_data(endpoint, params=None):
    try:
        headers = {
            "Content-Type": "application/json",
            "x-api-key": CHAINBASE_API_KEY
        }
        response = requests.get(f"{CHAINBASE_API_URL}/{endpoint}", headers=headers, params=params)
        
        # Raise an exception if the request fails
        response.raise_for_status()
        
        # Parse JSON response and return data
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log error and return failure response
        app.logger.error(f"Error fetching data from Chainbase API: {e}")
        return {"error": str(e)}

@app.route('/block', methods=['GET'])
def get_latest_block():
    """
    Endpoint to fetch the latest block on the blockchain.
    """
    data = fetch_blockchain_data("latest_block")
    if "error" in data:
        return jsonify({"error": "Failed to fetch latest block data"}), 500
    return jsonify(data)

@app.route('/transaction', methods=['GET'])
def get_transaction():
    """
    Endpoint to fetch details of a transaction by its hash.
    Example request: /transaction?tx_hash=<hash>
    """
    tx_hash = request.args.get("tx_hash")
    if not tx_hash:
        return jsonify({"error": "Transaction hash is required"}), 400
    
    data = fetch_blockchain_data("transaction", {"tx_hash": tx_hash})
    if "error" in data:
        return jsonify({"error": "Failed to fetch transaction data"}), 500
    return jsonify(data)

@app.route('/address', methods=['GET'])
def get_address_info():
    """
    Endpoint to fetch details of an address.
    Example request: /address?address=<address>
    """
    address = request.args.get("address")
    if not address:
        return jsonify({"error": "Address is required"}), 400
    
    data = fetch_blockchain_data("address", {"address": address})
    if "error" in data:
        return jsonify({"error": "Failed to fetch address data"}), 500
    return jsonify(data)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- Replace `"your_chainbase_api_key"` with your actual Chainbase API key.
- Ensure you have the Flask and requests libraries installed (`pip install flask requests`).
- This code provides endpoints for fetching the latest block, transaction details, and address info. Adjust endpoints and parameters based on Chainbase API documentation.
