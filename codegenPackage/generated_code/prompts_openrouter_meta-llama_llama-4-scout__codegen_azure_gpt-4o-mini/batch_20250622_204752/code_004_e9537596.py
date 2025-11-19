"""
Generated Code Metadata:
========================
Original URL: https://claim-vow.pages.dev
Prompt: What are the key considerations for creating a digital asset claiming platform like Claim VOW, and how can they be implemented technically?
Generated: DETERMINISTIC_e9537596acd64f4a
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_asset_claiming_platform.py

import json
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for digital assets and claims
assets = {}
claims = {}

class Asset:
    """Class representing a digital asset."""
    def __init__(self, asset_id, owner, metadata):
        self.asset_id = asset_id
        self.owner = owner
        self.metadata = metadata

class Claim:
    """Class representing a claim on a digital asset."""
    def __init__(self, claim_id, asset_id, claimant):
        self.claim_id = claim_id
        self.asset_id = asset_id
        self.claimant = claimant

@app.route('/assets', methods=['POST'])
def create_asset():
    """Endpoint to create a new digital asset."""
    try:
        data = request.json
        asset_id = data['asset_id']
        owner = data['owner']
        metadata = data['metadata']

        if asset_id in assets:
            return jsonify({"error": "Asset already exists."}), 400

        assets[asset_id] = Asset(asset_id, owner, metadata)
        return jsonify({"message": "Asset created successfully."}), 201

    except KeyError as e:
        raise BadRequest(f"Missing required field: {str(e)}")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/claims', methods=['POST'])
def create_claim():
    """Endpoint to create a claim on a digital asset."""
    try:
        data = request.json
        claim_id = data['claim_id']
        asset_id = data['asset_id']
        claimant = data['claimant']

        if asset_id not in assets:
            return jsonify({"error": "Asset does not exist."}), 404

        if claim_id in claims:
            return jsonify({"error": "Claim already exists."}), 400

        claims[claim_id] = Claim(claim_id, asset_id, claimant)
        return jsonify({"message": "Claim created successfully."}), 201

    except KeyError as e:
        raise BadRequest(f"Missing required field: {str(e)}")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/assets/<asset_id>', methods=['GET'])
def get_asset(asset_id):
    """Endpoint to retrieve a digital asset by its ID."""
    asset = assets.get(asset_id)
    if asset:
        return jsonify({
            "asset_id": asset.asset_id,
            "owner": asset.owner,
            "metadata": asset.metadata
        }), 200
    return jsonify({"error": "Asset not found."}), 404

@app.route('/claims/<claim_id>', methods=['GET'])
def get_claim(claim_id):
    """Endpoint to retrieve a claim by its ID."""
    claim = claims.get(claim_id)
    if claim:
        return jsonify({
            "claim_id": claim.claim_id,
            "asset_id": claim.asset_id,
            "claimant": claim.claimant
        }), 200
    return jsonify({"error": "Claim not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Install Flask: `pip install Flask`
- Run the application: `python digital_asset_claiming_platform.py`
- Use a tool like Postman or curl to interact with the API.
