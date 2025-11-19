"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simpsons.claims
Prompt: What are the key features of the Simpsons Claims API for managing insurance claims?
Generated: DETERMINISTIC_fa788cf996047021
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simpsons Claims API - A Python Flask-based API for managing insurance claims.

Key Features:
- Create a new insurance claim
- Retrieve a list of all insurance claims
- Retrieve a specific claim by ID
- Update an existing claim
- Delete a claim
"""

from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory database for storing insurance claims
claims_db = {}

# Error messages
NOT_FOUND_ERROR = {"error": "Claim not found"}
BAD_REQUEST_ERROR = {"error": "Invalid request data"}

@app.route('/claims', methods=['POST'])
def create_claim():
    """
    Create a new insurance claim.
    Expected JSON payload:
    {
        "policy_holder_name": "John Doe",
        "policy_number": "12345ABC",
        "claim_amount": 1500.00,
        "description": "Car accident"
    }
    """
    try:
        data = request.get_json()
        # Validate required fields
        required_fields = ["policy_holder_name", "policy_number", "claim_amount", "description"]
        if not all(field in data for field in required_fields):
            return jsonify(BAD_REQUEST_ERROR), 400

        # Generate a unique identifier for the claim
        claim_id = str(uuid.uuid4())
        claims_db[claim_id] = {
            "id": claim_id,
            "policy_holder_name": data["policy_holder_name"],
            "policy_number": data["policy_number"],
            "claim_amount": data["claim_amount"],
            "description": data["description"]
        }
        return jsonify(claims_db[claim_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/claims', methods=['GET'])
def get_all_claims():
    """
    Retrieve a list of all insurance claims.
    """
    return jsonify(list(claims_db.values())), 200


@app.route('/claims/<claim_id>', methods=['GET'])
def get_claim_by_id(claim_id):
    """
    Retrieve a specific claim by ID.
    """
    claim = claims_db.get(claim_id)
    if not claim:
        return jsonify(NOT_FOUND_ERROR), 404
    return jsonify(claim), 200


@app.route('/claims/<claim_id>', methods=['PUT'])
def update_claim(claim_id):
    """
    Update an existing insurance claim.
    Expected JSON payload:
    {
        "policy_holder_name": "Jane Doe",
        "policy_number": "67890XYZ",
        "claim_amount": 2000.00,
        "description": "House fire"
    }
    """
    claim = claims_db.get(claim_id)
    if not claim:
        return jsonify(NOT_FOUND_ERROR), 404

    try:
        data = request.get_json()
        # Validate required fields
        required_fields = ["policy_holder_name", "policy_number", "claim_amount", "description"]
        if not all(field in data for field in required_fields):
            return jsonify(BAD_REQUEST_ERROR), 400

        # Update the claim
        claims_db[claim_id].update({
            "policy_holder_name": data["policy_holder_name"],
            "policy_number": data["policy_number"],
            "claim_amount": data["claim_amount"],
            "description": data["description"]
        })
        return jsonify(claims_db[claim_id]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/claims/<claim_id>', methods=['DELETE'])
def delete_claim(claim_id):
    """
    Delete an insurance claim by ID.
    """
    claim = claims_db.pop(claim_id, None)
    if not claim:
        return jsonify(NOT_FOUND_ERROR), 404
    return jsonify({"message": "Claim deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
```
