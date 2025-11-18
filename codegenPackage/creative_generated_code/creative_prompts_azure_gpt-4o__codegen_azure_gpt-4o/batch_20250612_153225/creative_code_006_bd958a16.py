"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Develop a REST API to manage donations for a platform like Perú Makers, including endpoints for creating, retrieving, updating, and deleting donation records.
Generated: DETERMINISTIC_bd958a164b9f300d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database for demonstration purposes
donations = {}

# Helper function to validate donation payload
def validate_donation(data):
    required_fields = ["name", "email", "amount"]
    for field in required_fields:
        if field not in data:
            return f"Field '{field}' is required."
        if field == "amount" and (not isinstance(data["amount"], (int, float)) or data["amount"] <= 0):
            return f"Field '{field}' must be a positive number."
    return None

# Endpoint to create a new donation
@app.route('/donations', methods=['POST'])
def create_donation():
    """
    Endpoint to create a new donation record.

    Payload:
    {
        "name": "Donor Name",
        "email": "donor@example.com",
        "amount": 50.0
    }
    """
    data = request.get_json()
    validation_error = validate_donation(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400
    
    donation_id = str(uuid4())
    donation_record = {
        "id": donation_id,
        "name": data["name"],
        "email": data["email"],
        "amount": data["amount"]
    }
    donations[donation_id] = donation_record
    return jsonify(donation_record), 201

# Endpoint to retrieve all donations
@app.route('/donations', methods=['GET'])
def get_donations():
    """
    Endpoint to retrieve all donation records.
    """
    return jsonify(list(donations.values())), 200

# Endpoint to retrieve a specific donation by ID
@app.route('/donations/<donation_id>', methods=['GET'])
def get_donation(donation_id):
    """
    Endpoint to retrieve a donation record by ID.
    """
    donation_record = donations.get(donation_id)
    if not donation_record:
        return jsonify({"error": "Donation not found"}), 404
    return jsonify(donation_record), 200

# Endpoint to update a donation record by ID
@app.route('/donations/<donation_id>', methods=['PUT'])
def update_donation(donation_id):
    """
    Endpoint to update an existing donation record.

    Payload:
    {
        "name": "Updated Name",
        "email": "updated@example.com",
        "amount": 100.0
    }
    """
    donation_record = donations.get(donation_id)
    if not donation_record:
        return jsonify({"error": "Donation not found"}), 404
    
    data = request.get_json()
    validation_error = validate_donation(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400
    
    donation_record.update({
        "name": data["name"],
        "email": data["email"],
        "amount": data["amount"]
    })
    donations[donation_id] = donation_record
    return jsonify(donation_record), 200

# Endpoint to delete a donation record by ID
@app.route('/donations/<donation_id>', methods=['DELETE'])
def delete_donation(donation_id):
    """
    Endpoint to delete a donation record by ID.
    """
    donation_record = donations.pop(donation_id, None)
    if not donation_record:
        return jsonify({"error": "Donation not found"}), 404
    return jsonify({"message": "Donation deleted successfully"}), 200

# Error handling for unexpected errors
@app.errorhandler(500)
def internal_error(error):
    """
    Generic error handler for unexpected errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)
```
