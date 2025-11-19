"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudpremiumnfts.com
Prompt: What are the unique features of the Cloud Premium NFTs marketplace for auctioning NFTs?
Generated: DETERMINISTIC_d15b02f5b5e235ac
Batch ID: 20250612_162913
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

# In-memory storage for NFTs (simulating a database)
nft_marketplace = []

class NFT:
    """ Class representing an NFT. """

    def __init__(self, id, name, owner, price):
        self.id = id
        self.name = name
        self.owner = owner
        self.price = price

    def to_dict(self):
        """ Convert NFT instance to dictionary for JSON serialization. """
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner,
            'price': self.price
        }

@app.route('/api/nfts', methods=['POST'])
def create_nft():
    """ Endpoint for creating a new NFT. """
    try:
        data = request.json
        nft_id = len(nft_marketplace) + 1
        nft = NFT(nft_id, data['name'], data['owner'], data['price'])
        nft_marketplace.append(nft)
        return jsonify(nft.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nfts', methods=['GET'])
def get_nfts():
    """ Endpoint to retrieve all NFTs. """
    return jsonify([nft.to_dict() for nft in nft_marketplace]), 200

@app.route('/api/nfts/<int:nft_id>', methods=['GET'])
def get_nft(nft_id):
    """ Endpoint to retrieve a specific NFT by ID. """
    nft = next((nft for nft in nft_marketplace if nft.id == nft_id), None)
    if nft:
        return jsonify(nft.to_dict()), 200
    return jsonify({'error': 'NFT not found'}), 404

@app.route('/api/nfts/<int:nft_id>', methods=['PUT'])
def update_nft(nft_id):
    """ Endpoint for updating an existing NFT. """
    try:
        data = request.json
        nft = next((nft for nft in nft_marketplace if nft.id == nft_id), None)
        if not nft:
            return jsonify({'error': 'NFT not found'}), 404

        nft.name = data.get('name', nft.name)
        nft.owner = data.get('owner', nft.owner)
        nft.price = data.get('price', nft.price)
        return jsonify(nft.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nfts/<int:nft_id>', methods=['DELETE'])
def delete_nft(nft_id):
    """ Endpoint for deleting an NFT by ID. """
    global nft_marketplace
    nft_marketplace = [nft for nft in nft_marketplace if nft.id != nft_id]
    return jsonify({'message': 'NFT deleted successfully'}), 204

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This code defines a simple NFT marketplace using Flask, where you can create, retrieve, update, and delete NFTs. Error handling is included for missing fields and other exceptions.
