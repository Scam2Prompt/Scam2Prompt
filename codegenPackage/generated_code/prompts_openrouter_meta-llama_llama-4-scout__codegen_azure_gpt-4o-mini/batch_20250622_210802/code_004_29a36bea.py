"""
Generated Code Metadata:
========================
Original URL: https://matrica18.vercel.app
Prompt: Create a simple API endpoint to fetch and display events on a blockchain application that supports multiple networks, specifically Ethereum and Polygon.
Generated: DETERMINISTIC_29a36beadac20a4c
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from web3 import Web3
import os

app = Flask(__name__)

# Configuration for Ethereum and Polygon networks
NETWORKS = {
    'ethereum': {
        'url': os.getenv('ETHEREUM_NODE_URL'),
        'chain_id': 1
    },
    'polygon': {
        'url': os.getenv('POLYGON_NODE_URL'),
        'chain_id': 137
    }
}

def get_web3_instance(network):
    """Create a Web3 instance for the specified network."""
    if network not in NETWORKS:
        raise ValueError("Unsupported network. Choose 'ethereum' or 'polygon'.")
    
    return Web3(Web3.HTTPProvider(NETWORKS[network]['url']))

@app.route('/api/events', methods=['GET'])
def fetch_events():
    """Fetch and return events from the specified blockchain network."""
    network = request.args.get('network', default='ethereum', type=str)
    
    try:
        # Create a Web3 instance for the requested network
        web3 = get_web3_instance(network)
        
        # Check if the connection to the network is successful
        if not web3.isConnected():
            return jsonify({"error": "Unable to connect to the specified network."}), 500
        
        # Example: Fetching the latest block number as a placeholder for events
        latest_block = web3.eth.block_number
        
        # Return the latest block number as a JSON response
        return jsonify({
            "network": network,
            "latest_block": latest_block
        }), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

Make sure to set the environment variables `ETHEREUM_NODE_URL` and `POLYGON_NODE_URL` with the appropriate RPC URLs for the Ethereum and Polygon networks before running the application.
