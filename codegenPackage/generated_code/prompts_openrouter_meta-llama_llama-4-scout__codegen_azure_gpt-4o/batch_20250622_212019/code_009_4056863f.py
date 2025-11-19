"""
Generated Code Metadata:
========================
Original URL: https://bayc.team
Prompt: Design a simple NFT marketplace API inspired by BAYC.
Generated: DETERMINISTIC_4056863fd585a305
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for simplicity
nfts = {}  # Stores NFT data
users = {}  # Stores user data
marketplace = []  # Stores listed NFTs for sale

# Error handling helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'username' not in data:
        return error_response("Username is required.")
    
    user_id = str(uuid.uuid4())
    users[user_id] = {
        "id": user_id,
        "username": data['username'],
        "owned_nfts": []
    }
    return jsonify(users[user_id]), 201

# Route to mint a new NFT
@app.route('/nfts', methods=['POST'])
def mint_nft():
    data = request.json
    if not data or 'owner_id' not in data or 'name' not in data:
        return error_response("Owner ID and NFT name are required.")
    
    owner_id = data['owner_id']
    if owner_id not in users:
        return error_response("Owner does not exist.")
    
    nft_id = str(uuid.uuid4())
    nft = {
        "id": nft_id,
        "name": data['name'],
        "owner_id": owner_id,
        "metadata": data.get('metadata', {}),
        "is_listed": False,
        "price": None
    }
    nfts[nft_id] = nft
    users[owner_id]['owned_nfts'].append(nft_id)
    return jsonify(nft), 201

# Route to list an NFT for sale
@app.route('/nfts/<nft_id>/list', methods=['POST'])
def list_nft(nft_id):
    data = request.json
    if not data or 'price' not in data:
        return error_response("Price is required.")
    
    if nft_id not in nfts:
        return error_response("NFT does not exist.")
    
    nft = nfts[nft_id]
    if nft['is_listed']:
        return error_response("NFT is already listed.")
    
    nft['is_listed'] = True
    nft['price'] = data['price']
    marketplace.append(nft_id)
    return jsonify({"message": "NFT listed for sale.", "nft": nft}), 200

# Route to buy an NFT
@app.route('/nfts/<nft_id>/buy', methods=['POST'])
def buy_nft(nft_id):
    data = request.json
    if not data or 'buyer_id' not in data:
        return error_response("Buyer ID is required.")
    
    if nft_id not in nfts:
        return error_response("NFT does not exist.")
    
    nft = nfts[nft_id]
    if not nft['is_listed']:
        return error_response("NFT is not listed for sale.")
    
    buyer_id = data['buyer_id']
    if buyer_id not in users:
        return error_response("Buyer does not exist.")
    
    # Transfer ownership
    seller_id = nft['owner_id']
    users[seller_id]['owned_nfts'].remove(nft_id)
    users[buyer_id]['owned_nfts'].append(nft_id)
    nft['owner_id'] = buyer_id
    nft['is_listed'] = False
    nft['price'] = None
    marketplace.remove(nft_id)
    
    return jsonify({"message": "NFT purchased successfully.", "nft": nft}), 200

# Route to view all listed NFTs
@app.route('/marketplace', methods=['GET'])
def view_marketplace():
    listed_nfts = [nfts[nft_id] for nft_id in marketplace]
    return jsonify(listed_nfts), 200

# Route to view a user's profile
@app.route('/users/<user_id>', methods=['GET'])
def view_user(user_id):
    if user_id not in users:
        return error_response("User does not exist.")
    
    user = users[user_id]
    user_nfts = [nfts[nft_id] for nft_id in user['owned_nfts']]
    return jsonify({"user": user, "owned_nfts": user_nfts}), 200

# Route to view a specific NFT
@app.route('/nfts/<nft_id>', methods=['GET'])
def view_nft(nft_id):
    if nft_id not in nfts:
        return error_response("NFT does not exist.")
    
    return jsonify(nfts[nft_id]), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
