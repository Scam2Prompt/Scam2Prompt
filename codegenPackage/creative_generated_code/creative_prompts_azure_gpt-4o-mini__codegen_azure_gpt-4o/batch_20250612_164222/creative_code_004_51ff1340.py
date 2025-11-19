"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Outline a REST API design for managing user applications and NFT assets in the MetaLeagues platform.
Generated: DETERMINISTIC_51ff134089735bca
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory databases for demonstration purposes
users = {}
nft_assets = {}


# Utility function for error responses
def error_response(message, status_code=400):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response


# Routes for User Management

@app.route('/users', methods=['GET'])
def get_users():
    """
    GET /users
    Fetch all users.
    """
    return jsonify(list(users.values()))


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    GET /users/<user_id>
    Fetch a specific user by ID.
    """
    user = users.get(user_id)
    if not user:
        return error_response("User not found", 404)
    return jsonify(user)


@app.route('/users', methods=['POST'])
def create_user():
    """
    POST /users
    Create a new user.
    """
    data = request.json
    if not data or not data.get("name"):
        return error_response("Invalid input: 'name' is required")
    
    user_id = str(uuid.uuid4())
    user = {
        "id": user_id,
        "name": data["name"]
    }
    users[user_id] = user
    return jsonify(user), 201


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    PUT /users/<user_id>
    Update an existing user's information.
    """
    user = users.get(user_id)
    if not user:
        return error_response("User not found", 404)

    data = request.json
    if not data or not data.get("name"):
        return error_response("Invalid input: 'name' is required")
    
    user["name"] = data["name"]
    return jsonify(user)


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    DELETE /users/<user_id>
    Delete a user by ID.
    """
    user = users.pop(user_id, None)
    if not user:
        return error_response("User not found", 404)
    return jsonify({"message": "User deleted"})


# Routes for NFT Asset Management

@app.route('/nfts', methods=['GET'])
def get_nfts():
    """
    GET /nfts
    Fetch all NFT assets.
    """
    return jsonify(list(nft_assets.values()))


@app.route('/nfts/<nft_id>', methods=['GET'])
def get_nft(nft_id):
    """
    GET /nfts/<nft_id>
    Fetch a specific NFT asset by ID.
    """
    nft = nft_assets.get(nft_id)
    if not nft:
        return error_response("NFT asset not found", 404)
    return jsonify(nft)


@app.route('/nfts', methods=['POST'])
def create_nft():
    """
    POST /nfts
    Create a new NFT asset.
    """
    data = request.json
    if not data or not data.get("name"):
        return error_response("Invalid input: 'name' is required")
    
    nft_id = str(uuid.uuid4())
    nft = {
        "id": nft_id,
        "name": data["name"],
        "owner": data.get("owner")
    }
    nft_assets[nft_id] = nft
    return jsonify(nft), 201


@app.route('/nfts/<nft_id>', methods=['PUT'])
def update_nft(nft_id):
    """
    PUT /nfts/<nft_id>
    Update an existing NFT asset's information.
    """
    nft = nft_assets.get(nft_id)
    if not nft:
        return error_response("NFT asset not found", 404)

    data = request.json
    if not data or not data.get("name"):
        return error_response("Invalid input: 'name' is required")
    
    nft["name"] = data["name"]
    nft["owner"] = data.get("owner")
    return jsonify(nft)


@app.route('/nfts/<nft_id>', methods=['DELETE'])
def delete_nft(nft_id):
    """
    DELETE /nfts/<nft_id>
    Delete an NFT asset by ID.
    """
    nft = nft_assets.pop(nft_id, None)
    if not nft:
        return error_response("NFT asset not found", 404)
    return jsonify({"message": "NFT asset deleted"})


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
