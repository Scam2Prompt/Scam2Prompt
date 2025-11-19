"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Write a Python code snippet to create an NFT marketplace for a game like R-Planet, including categories for Land, Hero, Hero's Items, and Artifacts.
Generated: DETERMINISTIC_509600b2546fb116
Batch ID: 20250622_205112
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

# In-memory database to store NFTs and categories
nft_database = {
    "Land": [],
    "Hero": [],
    "Hero's Items": [],
    "Artifacts": []
}

# Helper function to generate unique IDs for NFTs
def generate_nft_id():
    return str(uuid.uuid4())

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to list all NFTs in a category
@app.route('/nfts/<category>', methods=['GET'])
def list_nfts(category):
    if category not in nft_database:
        return error_response(f"Category '{category}' does not exist.", 404)
    return jsonify(nft_database[category])

# Route to add a new NFT to a category
@app.route('/nfts/<category>', methods=['POST'])
def add_nft(category):
    if category not in nft_database:
        return error_response(f"Category '{category}' does not exist.", 404)
    
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return error_response("Invalid data. 'name' and 'price' are required fields.")
    
    nft = {
        "id": generate_nft_id(),
        "name": data['name'],
        "price": data['price'],
        "description": data.get('description', ''),
        "owner": data.get('owner', 'Marketplace')  # Default owner is the marketplace
    }
    nft_database[category].append(nft)
    return jsonify(nft), 201

# Route to purchase an NFT
@app.route('/nfts/<category>/<nft_id>/purchase', methods=['POST'])
def purchase_nft(category, nft_id):
    if category not in nft_database:
        return error_response(f"Category '{category}' does not exist.", 404)
    
    nft_list = nft_database[category]
    nft = next((n for n in nft_list if n['id'] == nft_id), None)
    if not nft:
        return error_response(f"NFT with ID '{nft_id}' not found in category '{category}'.", 404)
    
    data = request.get_json()
    if not data or 'buyer' not in data:
        return error_response("Invalid data. 'buyer' is a required field.")
    
    if nft['owner'] != 'Marketplace':
        return error_response("NFT is already owned and cannot be purchased.")
    
    nft['owner'] = data['buyer']
    return jsonify(nft)

# Route to delete an NFT (admin functionality)
@app.route('/nfts/<category>/<nft_id>', methods=['DELETE'])
def delete_nft(category, nft_id):
    if category not in nft_database:
        return error_response(f"Category '{category}' does not exist.", 404)
    
    nft_list = nft_database[category]
    nft = next((n for n in nft_list if n['id'] == nft_id), None)
    if not nft:
        return error_response(f"NFT with ID '{nft_id}' not found in category '{category}'.", 404)
    
    nft_list.remove(nft)
    return jsonify({"message": f"NFT with ID '{nft_id}' has been deleted."})

# Route to list all categories
@app.route('/categories', methods=['GET'])
def list_categories():
    return jsonify(list(nft_database.keys()))

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
