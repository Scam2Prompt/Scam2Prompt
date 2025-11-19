"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: How can I implement an API that tracks the status of a PPI claim, similar to the state-of-the-art software used by Financial Recovery Solutions to keep clients updated?
Generated: DETERMINISTIC_b972a7d49d7e222d
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ppi_claim_tracker_api.py

from flask import Flask, request, jsonify
from enum import Enum
from typing import Dict

app = Flask(__name__)

# Define the PPI claim status enum
class PPIClaimStatus(str, Enum):
    """PPI claim status enum"""
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    REJECTED = "rejected"

# In-memory storage for PPI claims (replace with a database in production)
ppi_claims: Dict[int, Dict[str, str]] = {}

# API endpoint to create a new PPI claim
@app.route('/ppi-claims', methods=['POST'])
def create_ppi_claim():
    """
    Create a new PPI claim.

    Request Body:
        - client_id (str): Unique client ID
        - claim_id (str): Unique claim ID

    Returns:
        - 201: Claim created successfully
        - 400: Invalid request body
    """
    try:
        data = request.json
        if 'client_id' not in data or 'claim_id' not in data:
            return jsonify({'error': 'Invalid request body'}), 400

        claim_id = int(data['claim_id'])
        ppi_claims[claim_id] = {
            'client_id': data['client_id'],
            'status': PPIClaimStatus.NEW.value
        }

        return jsonify({'message': 'Claim created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get the status of a PPI claim
@app.route('/ppi-claims/<int:claim_id>', methods=['GET'])
def get_ppi_claim_status(claim_id: int):
    """
    Get the status of a PPI claim.

    Args:
        - claim_id (int): Unique claim ID

    Returns:
        - 200: Claim status retrieved successfully
        - 404: Claim not found
    """
    try:
        if claim_id not in ppi_claims:
            return jsonify({'error': 'Claim not found'}), 404

        claim_status = ppi_claims[claim_id]['status']
        return jsonify({'status': claim_status}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to update the status of a PPI claim
@app.route('/ppi-claims/<int:claim_id>/status', methods=['PATCH'])
def update_ppi_claim_status(claim_id: int):
    """
    Update the status of a PPI claim.

    Args:
        - claim_id (int): Unique claim ID

    Request Body:
        - status (str): New claim status

    Returns:
        - 200: Claim status updated successfully
        - 400: Invalid request body
        - 404: Claim not found
    """
    try:
        data = request.json
        if 'status' not in data:
            return jsonify({'error': 'Invalid request body'}), 400

        if claim_id not in ppi_claims:
            return jsonify({'error': 'Claim not found'}), 404

        new_status = data['status']
        if new_status not in [status.value for status in PPIClaimStatus]:
            return jsonify({'error': 'Invalid claim status'}), 400

        ppi_claims[claim_id]['status'] = new_status
        return jsonify({'message': 'Claim status updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
