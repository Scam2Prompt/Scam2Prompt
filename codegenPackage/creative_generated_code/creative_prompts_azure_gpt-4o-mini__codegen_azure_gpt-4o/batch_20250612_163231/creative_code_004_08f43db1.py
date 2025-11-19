"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oasysgames.live
Prompt: Construct a code snippet that allows users to submit their NFTs to the in-game wallet for the "KAI: Battle of Three Kingdoms" campaign on OasysGames.
Generated: DETERMINISTIC_08f43db13dc92fea
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-game wallet storage (in production, use a secure database)
in_game_wallet = {}

# Helper function: Validate NFT submission
def validate_nft_submission(nft_data):
    required_fields = ["user_id", "nft_id", "nft_metadata"]
    for field in required_fields:
        if field not in nft_data:
            return False, f"Missing required field: {field}"
    return True, "Valid submission."

# Endpoint to submit NFT to the in-game wallet
@app.route('/submit-nft', methods=['POST'])
def submit_nft():
    try:
        # Parse incoming request data
        nft_data = request.get_json()
        if not nft_data:
            return jsonify({"error": "Invalid JSON payload."}), 400

        # Validate NFT submission data
        is_valid, message = validate_nft_submission(nft_data)
        if not is_valid:
            return jsonify({"error": message}), 400

        # Extract required fields from the request
        user_id = nft_data['user_id']
        nft_id = nft_data['nft_id']
        nft_metadata = nft_data['nft_metadata']

        # Add NFT to the in-game wallet (handle duplicates gracefully)
        if user_id not in in_game_wallet:
            in_game_wallet[user_id] = []
        
        # Check for duplicate NFT submissions
        if any(nft['nft_id'] == nft_id for nft in in_game_wallet[user_id]):
            return jsonify({"error": "NFT already submitted."}), 409

        # Store the NFT
        in_game_wallet[user_id].append({
            "nft_id": nft_id,
            "nft_metadata": nft_metadata
        })

        return jsonify({"message": "NFT successfully submitted!", "data": nft_data}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Endpoint to retrieve NFTs for a specific user
@app.route('/get-nfts/<user_id>', methods=['GET'])
def get_nfts(user_id):
    try:
        # Check if user has NFTs in the in-game wallet
        if user_id not in in_game_wallet:
            return jsonify({"error": "User not found or no NFTs available."}), 404

        return jsonify({"user_id": user_id, "nfts": in_game_wallet[user_id]}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Notes (in the code comments):
- This Flask-based Python API allows users to submit NFTs to the in-game wallet and retrieve them later. 
- The `/submit-nft` endpoint is designed for submission, while the `/get-nfts/<user_id>` endpoint retrieves a user's NFTs.
- Error handling and validation ensure the system is robust, and duplicate submissions are gracefully handled.
- In production, replace `in_game_wallet` with a database such as PostgreSQL or MongoDB for security and scalability.
