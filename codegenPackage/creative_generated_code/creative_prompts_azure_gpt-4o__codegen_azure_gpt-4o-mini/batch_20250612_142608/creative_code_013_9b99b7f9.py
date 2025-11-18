"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrvm.dev
Prompt: Generate code to track NFT assets using the BLOCKCHAIN app's dashboard and leaderboard features.
Generated: DETERMINISTIC_9b99b7f9a4e36ffa
Batch ID: 20250612_142608
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchain.com/v3/nft": {
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

# Constants
BLOCKCHAIN_API_URL = 'https://api.blockchain.com/v3/nft'
LEADERBOARD_CACHE = {}
CACHE_EXPIRATION_TIME = 60  # seconds

def fetch_nft_data(asset_id):
    """Fetch NFT data from the blockchain API.

    Args:
        asset_id (str): The ID of the NFT asset.

    Returns:
        dict: The NFT data if found, else None.
    """
    try:
        response = requests.get(f"{BLOCKCHAIN_API_URL}/assets/{asset_id}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        app.logger.error(f"Error fetching NFT data: {e}")
        return None

def update_leaderboard():
    """Update the leaderboard with the latest NFT assets."""
    global LEADERBOARD_CACHE
    try:
        response = requests.get(f"{BLOCKCHAIN_API_URL}/leaderboard")
        response.raise_for_status()
        LEADERBOARD_CACHE = response.json()
    except requests.RequestException as e:
        app.logger.error(f"Error updating leaderboard: {e}")

@app.route('/nft/<string:asset_id>', methods=['GET'])
def get_nft(asset_id):
    """Endpoint to get NFT details by asset ID.

    Args:
        asset_id (str): The ID of the NFT asset.

    Returns:
        JSON response with NFT data or error message.
    """
    nft_data = fetch_nft_data(asset_id)
    if nft_data:
        return jsonify(nft_data), 200
    else:
        return jsonify({"error": "NFT not found"}), 404

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Endpoint to get the current leaderboard of NFT assets.

    Returns:
        JSON response with leaderboard data.
    """
    global LEADERBOARD_CACHE
    # Check if the leaderboard cache is expired
    if not LEADERBOARD_CACHE:
        update_leaderboard()
    
    return jsonify(LEADERBOARD_CACHE), 200

@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error handler."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
