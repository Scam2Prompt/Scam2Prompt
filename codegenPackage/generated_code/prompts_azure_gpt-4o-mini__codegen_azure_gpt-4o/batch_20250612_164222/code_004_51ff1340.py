"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Outline a REST API design for managing user applications and NFT assets in the MetaLeagues platform.
Generated: DETERMINISTIC_51ff134089735bca
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for users and NFT assets
users = {}
nft_assets = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid4())

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.
    Request body: { "name": "John Doe", "email": "john@example.com" }
    Response: { "id": "unique_user_id", "name": "John Doe", "email": "john@example.com" }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_id = generate_id()
    users[user_id] = {
        "id": user_id,
        "name": data['name'],
        "email": data['email']
    }
    return jsonify(users[user_id]), 201

# Route: Get user details
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get details of a specific user.
    Response: { "id": "unique_user_id", "name": "John Doe", "email": "john@example.com" }
    """
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# Route: Create a new NFT asset
@app.route('/nfts', methods=['POST'])
def create_nft():
    """
    Create a new NFT asset.
    Request body: { "name": "Rare Sword", "owner_id": "user_id" }
    Response: { "id": "unique_nft_id", "name": "Rare Sword", "owner_id": "user_id" }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'owner_id' not in data:
        return jsonify({"error": "Invalid input"}), 400

    if data['owner_id'] not in users:
        return jsonify({"error": "Owner not found"}), 404

    nft_id = generate_id()
    nft_assets[nft_id] = {
        "id": nft_id,
        "name": data['name'],
        "owner_id": data['owner_id']
    }
    return jsonify(nft_assets[nft_id]), 201

# Route: Get NFT asset details
@app.route('/nfts/<nft_id>', methods=['GET'])
def get_nft(nft_id):
    """
    Get details of a specific NFT asset.
    Response: { "id": "unique_nft_id", "name": "Rare Sword", "owner_id": "user_id" }
    """
    nft = nft_assets.get(nft_id)
    if not nft:
        return jsonify({"error": "NFT not found"}), 404
    return jsonify(nft), 200

# Route: List all NFTs owned by a user
@app.route('/users/<user_id>/nfts', methods=['GET'])
def list_user_nfts(user_id):
    """
    List all NFTs owned by a specific user.
    Response: [ { "id": "unique_nft_id", "name": "Rare Sword", "owner_id": "user_id" } ]
    """
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    user_nfts = [nft for nft in nft_assets.values() if nft['owner_id'] == user_id]
    return jsonify(user_nfts), 200

# Route: Delete a user and their associated NFTs
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user and all their associated NFTs.
    Response: { "message": "User and associated NFTs deleted successfully" }
    """
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    # Delete user
    del users[user_id]

    # Delete associated NFTs
    global nft_assets
    nft_assets = {nft_id: nft for nft_id, nft in nft_assets.items() if nft['owner_id'] != user_id}

    return jsonify({"message": "User and associated NFTs deleted successfully"}), 200

# Route: Delete an NFT asset
@app.route('/nfts/<nft_id>', methods=['DELETE'])
def delete_nft(nft_id):
    """
    Delete a specific NFT asset.
    Response: { "message": "NFT deleted successfully" }
    """
    if nft_id not in nft_assets:
        return jsonify({"error": "NFT not found"}), 404

    del nft_assets[nft_id]
    return jsonify({"message": "NFT deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
