"""
Generated Code Metadata:
========================
Original URL: https://popcorn.claims
Prompt: What are the key features of the Popcorn Claims API for managing copyright information?
Generated: DETERMINISTIC_c56209e498777fd1
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Popcorn Claims API - Key Features for Managing Copyright Information

This script outlines the key features of the Popcorn Claims API for managing copyright information.
The API provides endpoints for creating, retrieving, updating, and deleting copyright claims.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for copyright claims (for demonstration purposes)
copyright_claims = {}

# Error messages
ERROR_NOT_FOUND = {"error": "Claim not found"}
ERROR_BAD_REQUEST = {"error": "Invalid request data"}

@app.route('/claims', methods=['POST'])
def create_claim():
    """
    Create a new copyright claim.
    Request JSON should include 'id', 'title', 'owner', and 'description'.
    """
    try:
        data = request.json
        if not all(key in data for key in ('id', 'title', 'owner', 'description')):
            return jsonify(ERROR_BAD_REQUEST), 400
        
        claim_id = data['id']
        if claim_id in copyright_claims:
            return jsonify({"error": "Claim ID already exists"}), 400
        
        copyright_claims[claim_id] = {
            "title": data['title'],
            "owner": data['owner'],
            "description": data['description']
        }
        return jsonify({"message": "Claim created successfully", "claim": copyright_claims[claim_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/claims/<claim_id>', methods=['GET'])
def get_claim(claim_id):
    """
    Retrieve a copyright claim by its ID.
    """
    try:
        claim = copyright_claims.get(claim_id)
        if not claim:
            return jsonify(ERROR_NOT_FOUND), 404
        return jsonify({"claim": claim}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/claims/<claim_id>', methods=['PUT'])
def update_claim(claim_id):
    """
    Update an existing copyright claim.
    Request JSON should include 'title', 'owner', and/or 'description'.
    """
    try:
        data = request.json
        claim = copyright_claims.get(claim_id)
        if not claim:
            return jsonify(ERROR_NOT_FOUND), 404
        
        # Update fields if provided
        if 'title' in data:
            claim['title'] = data['title']
        if 'owner' in data:
            claim['owner'] = data['owner']
        if 'description' in data:
            claim['description'] = data['description']
        
        return jsonify({"message": "Claim updated successfully", "claim": claim}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/claims/<claim_id>', methods=['DELETE'])
def delete_claim(claim_id):
    """
    Delete a copyright claim by its ID.
    """
    try:
        claim = copyright_claims.pop(claim_id, None)
        if not claim:
            return jsonify(ERROR_NOT_FOUND), 404
        return jsonify({"message": "Claim deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/claims', methods=['GET'])
def list_claims():
    """
    List all copyright claims.
    """
    try:
        return jsonify({"claims": list(copyright_claims.values())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
