"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.com
Prompt: Implement a digital ownership experience using Reown's UX-first approach, focusing on usability and utility.
Generated: DETERMINISTIC_c6a3cabf16f90b92
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_ownership.py

import json
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory storage for digital assets (for demonstration purposes)
digital_assets = {}

class DigitalAsset:
    """Class representing a digital asset."""
    
    def __init__(self, asset_id, owner, metadata):
        self.asset_id = asset_id
        self.owner = owner
        self.metadata = metadata

    def to_dict(self):
        """Convert the asset to a dictionary for JSON serialization."""
        return {
            'asset_id': self.asset_id,
            'owner': self.owner,
            'metadata': self.metadata
        }

@app.route('/assets', methods=['POST'])
def create_asset():
    """Create a new digital asset."""
    data = request.json
    if not data or 'asset_id' not in data or 'owner' not in data:
        abort(400, description="Invalid input: 'asset_id' and 'owner' are required.")

    asset_id = data['asset_id']
    owner = data['owner']
    metadata = data.get('metadata', {})

    if asset_id in digital_assets:
        abort(400, description="Asset ID already exists.")

    # Create and store the new digital asset
    asset = DigitalAsset(asset_id, owner, metadata)
    digital_assets[asset_id] = asset
    return jsonify(asset.to_dict()), 201

@app.route('/assets/<asset_id>', methods=['GET'])
def get_asset(asset_id):
    """Retrieve a digital asset by its ID."""
    asset = digital_assets.get(asset_id)
    if not asset:
        abort(404, description="Asset not found.")
    return jsonify(asset.to_dict()), 200

@app.route('/assets/<asset_id>', methods=['PUT'])
def update_asset(asset_id):
    """Update an existing digital asset."""
    asset = digital_assets.get(asset_id)
    if not asset:
        abort(404, description="Asset not found.")

    data = request.json
    if not data:
        abort(400, description="Invalid input: No data provided.")

    # Update asset metadata
    asset.metadata.update(data.get('metadata', {}))
    return jsonify(asset.to_dict()), 200

@app.route('/assets/<asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    """Delete a digital asset."""
    if asset_id not in digital_assets:
        abort(404, description="Asset not found.")

    del digital_assets[asset_id]
    return jsonify({"message": "Asset deleted successfully."}), 204

@app.errorhandler(400)
def bad_request(error):
    """Handle bad request errors."""
    return jsonify({"error": str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have Flask installed. You can install it using pip:

```bash
pip install Flask
```

### Running the Application
1. Save the code in a file named `digital_ownership.py`.
2. Run the application using the command:

```bash
python digital_ownership.py
```

3. Use tools like Postman or curl to interact with the API endpoints.
