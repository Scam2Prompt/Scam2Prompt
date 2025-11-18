"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellydrop.web.app
Prompt: Develop a feature for tracking and displaying unique 1/1 NFTs, similar to the "Jelly 1/1" concept mentioned on the JellyDrop site.
Generated: DETERMINISTIC_8bd1fa08883556ba
Batch ID: 20250612_153648
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
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for the NFTs (This should be replaced with a persistent database in production)
nft_storage = {}


class NFT:
    """Class to represent a Non-Fungible Token (NFT)."""
    def __init__(self, token_id, name, description, owner):
        self.token_id = token_id
        self.name = name
        self.description = description
        self.owner = owner

    def to_dict(self):
        """Convert NFT properties to a dictionary."""
        return {
            'token_id': self.token_id,
            'name': self.name,
            'description': self.description,
            'owner': self.owner
        }


@app.route('/nft', methods=['POST'])
def create_nft():
    """Endpoint to create a new NFT."""
    try:
        data = request.json
        # Validate incoming data
        if not all(key in data for key in ('token_id', 'name', 'description', 'owner')):
            return jsonify({'error': 'Missing data'}), 400

        # Check for uniqueness
        if data['token_id'] in nft_storage:
            return jsonify({'error': 'NFT with this token_id already exists'}), 400

        # Create and store the NFT
        nft = NFT(data['token_id'], data['name'], data['description'], data['owner'])
        nft_storage[data['token_id']] = nft
        return jsonify(nft.to_dict()), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/nft/<token_id>', methods=['GET'])
def get_nft(token_id):
    """Endpoint to retrieve an NFT by its token_id."""
    try:
        nft = nft_storage.get(token_id)
        if nft is None:
            return jsonify({'error': 'NFT not found'}), 404
        return jsonify(nft.to_dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/nft/<token_id>', methods=['DELETE'])
def delete_nft(token_id):
    """Endpoint to delete an NFT by its token_id."""
    try:
        if token_id not in nft_storage:
            return jsonify({'error': 'NFT not found'}), 404
        
        del nft_storage[token_id]
        return jsonify({'message': 'NFT deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions globally."""
    return jsonify({'error': e.description}), e.code


if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
