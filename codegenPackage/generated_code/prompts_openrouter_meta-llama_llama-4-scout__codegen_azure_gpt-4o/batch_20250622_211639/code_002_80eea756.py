"""
Generated Code Metadata:
========================
Original URL: https://tapio.claims
Prompt: Generate a basic API structure for a claims processing system similar to what might be used by tapio.claims, including endpoints for claim submission and status updates.
Generated: DETERMINISTIC_80eea75667cb18de
Batch ID: 20250622_211639
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

# In-memory database for storing claims (for demonstration purposes)
claims_db = {}

# Error messages
ERROR_INVALID_DATA = "Invalid data provided."
ERROR_CLAIM_NOT_FOUND = "Claim not found."

# Endpoint: Submit a new claim
@app.route('/claims', methods=['POST'])
def submit_claim():
    """
    Endpoint to submit a new claim.
    Expects JSON payload with 'claimant_name' and 'claim_details'.
    Returns the claim ID and status.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data or 'claimant_name' not in data or 'claim_details' not in data:
            return jsonify({"error": ERROR_INVALID_DATA}), 400

        # Generate a unique claim ID
        claim_id = str(uuid.uuid4())

        # Create a new claim record
        claims_db[claim_id] = {
            "claimant_name": data['claimant_name'],
            "claim_details": data['claim_details'],
            "status": "Submitted"
        }

        # Return the claim ID and initial status
        return jsonify({"claim_id": claim_id, "status": "Submitted"}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Endpoint: Update claim status
@app.route('/claims/<claim_id>/status', methods=['PUT'])
def update_claim_status(claim_id):
    """
    Endpoint to update the status of an existing claim.
    Expects JSON payload with 'status'.
    Returns the updated claim record.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data or 'status' not in data:
            return jsonify({"error": ERROR_INVALID_DATA}), 400

        # Check if the claim exists
        if claim_id not in claims_db:
            return jsonify({"error": ERROR_CLAIM_NOT_FOUND}), 404

        # Update the claim status
        claims_db[claim_id]['status'] = data['status']

        # Return the updated claim record
        return jsonify(claims_db[claim_id]), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Endpoint: Get claim details
@app.route('/claims/<claim_id>', methods=['GET'])
def get_claim_details(claim_id):
    """
    Endpoint to retrieve details of a specific claim.
    Returns the claim record if found.
    """
    try:
        # Check if the claim exists
        if claim_id not in claims_db:
            return jsonify({"error": ERROR_CLAIM_NOT_FOUND}), 404

        # Return the claim record
        return jsonify(claims_db[claim_id]), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
