"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popcorn.claims
Prompt: What are the key features of the Popcorn Claims API for managing copyright information?
Generated: DETERMINISTIC_c56209e498777fd1
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Popcorn Claims API: Key Features
# This module provides functionality to manage copyright information for media assets.
# The API includes endpoints for registering, updating, retrieving, and verifying copyright claims.

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for copyright claims
copyright_claims = {}

# Error messages
ERRORS = {
    "not_found": "Claim not found.",
    "missing_fields": "Request is missing required fields.",
    "duplicate_claim": "A claim with this ID already exists."
}

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": ERRORS["not_found"]}), 404

@app.errorhandler(400)
def bad_request_error(error):
    """Handle 400 errors."""
    return jsonify({"error": ERRORS["missing_fields"]}), 400

@app.route('/claims', methods=['POST'])
def register_claim():
    """
    Endpoint: Register a new copyright claim
    Request Body: JSON with 'claim_id', 'title', and 'owner'
    Response: Success message or error
    """
    data = request.get_json()
    if not data or 'claim_id' not in data or 'title' not in data or 'owner' not in data:
        return bad_request_error(400)

    claim_id = data['claim_id']
    if claim_id in copyright_claims:
        return jsonify({"error": ERRORS["duplicate_claim"]}), 400

    copyright_claims[claim_id] = {
        "title": data["title"],
        "owner": data["owner"]
    }
    return jsonify({"message": f"Claim {claim_id} registered successfully."}), 201

@app.route('/claims/<claim_id>', methods=['GET'])
def retrieve_claim(claim_id):
    """
    Endpoint: Retrieve a copyright claim by ID
    Response: Claim details or error
    """
    claim = copyright_claims.get(claim_id)
    if not claim:
        return not_found_error(404)
    return jsonify(claim), 200

@app.route('/claims/<claim_id>', methods=['PUT'])
def update_claim(claim_id):
    """
    Endpoint: Update an existing copyright claim
    Request Body: JSON with 'title' and/or 'owner'
    Response: Success message or error
    """
    claim = copyright_claims.get(claim_id)
    if not claim:
        return not_found_error(404)

    data = request.get_json()
    if not data:
        return bad_request_error(400)

    title = data.get("title")
    owner = data.get("owner")

    if title:
        claim["title"] = title
    if owner:
        claim["owner"] = owner

    return jsonify({"message": f"Claim {claim_id} updated successfully."}), 200

@app.route('/claims/<claim_id>', methods=['DELETE'])
def delete_claim(claim_id):
    """
    Endpoint: Delete a copyright claim by ID
    Response: Success message or error
    """
    claim = copyright_claims.pop(claim_id, None)
    if not claim:
        return not_found_error(404)
    return jsonify({"message": f"Claim {claim_id} deleted successfully."}), 200

@app.route('/claims', methods=['GET'])
def list_claims():
    """
    Endpoint: List all copyright claims
    Response: JSON array of all claims
    """
    return jsonify(list(copyright_claims.values())), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
