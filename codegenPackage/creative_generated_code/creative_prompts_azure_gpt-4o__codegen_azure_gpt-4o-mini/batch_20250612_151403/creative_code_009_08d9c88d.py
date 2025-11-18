"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.alphadogs.run
Prompt: Generate a code snippet to authenticate a user’s wallet and verify ownership of an Alphadogs NFT before allowing access to training features.
Generated: DETERMINISTIC_08d9c88dca89ac7b
Batch ID: 20250612_151403
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/nfts": {
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
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Constants for the NFT API and the Alphadogs contract address
NFT_API_URL = "https://api.example.com/nfts"  # Replace with actual NFT API URL
ALPHADOGS_CONTRACT_ADDRESS = "0xYourAlphadogsContractAddress"  # Replace with actual address

@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    """
    Endpoint to authenticate a user's wallet and verify ownership of an Alphadogs NFT.
    Expects a JSON payload with the user's wallet address.
    """
    try:
        # Retrieve wallet address from the request
        data = request.json
        wallet_address = data.get('wallet_address')

        if not wallet_address:
            return jsonify({"error": "Wallet address is required"}), 400

        # Fetch the NFTs owned by the user from the NFT API
        response = requests.get(f"{NFT_API_URL}/{wallet_address}")
        
        # Check if the response was successful
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch NFT data"}), response.status_code
        
        # Parse the JSON response
        nfts = response.json()

        # Check if the user owns an Alphadogs NFT
        has_alphadog = any(
            nft['contract_address'].lower() == ALPHADOGS_CONTRACT_ADDRESS.lower()
            for nft in nfts
        )

        if not has_alphadog:
            return jsonify({"error": "User does not own an Alphadogs NFT"}), 403

        # Return success message if ownership is verified
        return jsonify({"message": "Access granted to training features"}), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
