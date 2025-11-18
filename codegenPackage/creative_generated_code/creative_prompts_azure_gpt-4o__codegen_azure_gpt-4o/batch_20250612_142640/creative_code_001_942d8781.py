"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Create a REST API for an asset finance brokerage service that allows users to submit proposals for financing assets such as HGVs, marine craft, or agricultural equipment, referencing the offerings on Rhino Asset Finance.
Generated: DETERMINISTIC_942d878179d046b8
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for demonstration purposes
# In a production environment, this would be a database
proposals = []

# Error handler for clean JSON responses
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=str(e), status_code=e.code), e.code
    return jsonify(error="Internal Server Error", status_code=500), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="API is up and running")

# Endpoint to submit a financing proposal
@app.route('/proposals', methods=['POST'])
def submit_proposal():
    """
    Endpoint to submit a financing proposal.
    Request body should include:
    - asset_type: The type of asset (e.g., "HGV", "marine craft", "agricultural equipment").
    - asset_description: Description of the asset.
    - financing_amount: Requested financing amount.
    - customer_name: Name of the customer submitting the proposal.
    - customer_contact: Contact details of the customer.
    """
    try:
        # Parse request JSON
        data = request.get_json()
        
        # Validate input
        required_fields = ['asset_type', 'asset_description', 'financing_amount', 'customer_name', 'customer_contact']
        for field in required_fields:
            if field not in data:
                return jsonify(error=f"Missing field: {field}"), 400
        
        # Create proposal object
        proposal = {
            "id": len(proposals) + 1,  # Auto-increment ID
            "asset_type": data['asset_type'],
            "asset_description": data['asset_description'],
            "financing_amount": data['financing_amount'],
            "customer_name": data['customer_name'],
            "customer_contact": data['customer_contact'],
            "status": "pending"  # Default status for new proposals
        }

        # Store proposal
        proposals.append(proposal)

        return jsonify(message="Proposal submitted successfully", proposal=proposal), 201
    except Exception as e:
        return jsonify(error="Failed to process the proposal", details=str(e)), 500

# Endpoint to list all proposals
@app.route('/proposals', methods=['GET'])
def list_proposals():
    """
    Endpoint to list all financing proposals.
    Supports optional query parameters:
    - status: Filter proposals by status (e.g., "pending", "approved", "rejected").
    """
    try:
        status_filter = request.args.get('status')
        if status_filter:
            filtered_proposals = [p for p in proposals if p['status'] == status_filter]
            return jsonify(proposals=filtered_proposals)
        return jsonify(proposals=proposals)
    except Exception as e:
        return jsonify(error="Failed to retrieve proposals", details=str(e)), 500

# Endpoint to update the status of a proposal
@app.route('/proposals/<int:proposal_id>', methods=['PATCH'])
def update_proposal_status(proposal_id):
    """
    Endpoint to update the status of a proposal.
    Request body should include:
    - status: The new status for the proposal (e.g., "approved", "rejected").
    """
    try:
        # Parse request JSON
        data = request.get_json()
        if 'status' not in data:
            return jsonify(error="Missing field: status"), 400
        
        # Find the proposal
        proposal = next((p for p in proposals if p['id'] == proposal_id), None)
        if not proposal:
            return jsonify(error="Proposal not found"), 404

        # Update proposal status
        proposal['status'] = data['status']

        return jsonify(message="Proposal status updated successfully", proposal=proposal)
    except Exception as e:
        return jsonify(error="Failed to update proposal status", details=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
