"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-energy.com
Prompt: Create a REST API for Kraken Energy that allows sellers to submit mineral rights information and buyers to query available leases, based on the company's business model.
Generated: DETERMINISTIC_e494b31e1b4f10d6
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# REST API for Kraken Energy to handle mineral rights submissions and lease queries
# Framework: Flask (Python)

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import uuid

app = Flask(__name__)

# In-memory databases for demonstration purposes
mineral_rights = {}  # Dictionary to store submitted mineral rights
available_leases = {}  # Dictionary to store available leases

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler for clean responses
@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({"error": e.name, "message": e.description}).get_data()
        response.content_type = "application/json"
        return response
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint: Submit Mineral Rights (Seller)
@app.route('/submit-mineral-rights', methods=['POST'])
def submit_mineral_rights():
    """
    Sellers can use this endpoint to submit information about their mineral rights.
    Expected payload:
    {
        "owner_name": "John Doe",
        "contact_info": "john@example.com",
        "location": "Texas",
        "acreage": 100,
        "mineral_type": "oil"
    }
    """
    data = request.get_json()

    # Validate payload
    required_fields = ["owner_name", "contact_info", "location", "acreage", "mineral_type"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": "Bad Request", "message": f"Missing field: {field}"}), 400

    # Generate unique ID for the submission
    submission_id = generate_id()

    # Store submission in the database
    mineral_rights[submission_id] = {
        "owner_name": data["owner_name"],
        "contact_info": data["contact_info"],
        "location": data["location"],
        "acreage": data["acreage"],
        "mineral_type": data["mineral_type"]
    }

    return jsonify({"message": "Mineral rights submitted successfully", "submission_id": submission_id}), 201

# Endpoint: Query Available Leases (Buyer)
@app.route('/query-leases', methods=['GET'])
def query_leases():
    """
    Buyers can use this endpoint to query the available leases.
    Optional query parameters:
        location (str): Filter leases by location
        mineral_type (str): Filter leases by mineral type
    """
    location = request.args.get('location')
    mineral_type = request.args.get('mineral_type')

    # Filter leases based on query parameters
    filtered_leases = [
        {"lease_id": lease_id, **lease_info}
        for lease_id, lease_info in available_leases.items()
        if (not location or lease_info["location"] == location) and
           (not mineral_type or lease_info["mineral_type"] == mineral_type)
    ]

    return jsonify({"available_leases": filtered_leases}), 200

# Endpoint: Add Available Lease (Admin use or automation)
@app.route('/add-lease', methods=['POST'])
def add_lease():
    """
    Admins or automated processes can use this endpoint to add new leases.
    Expected payload:
    {
        "location": "Texas",
        "acreage": 100,
        "mineral_type": "oil",
        "price_per_acre": 500
    }
    """
    data = request.get_json()

    # Validate payload
    required_fields = ["location", "acreage", "mineral_type", "price_per_acre"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": "Bad Request", "message": f"Missing field: {field}"}), 400

    # Generate unique ID for the lease
    lease_id = generate_id()

    # Store lease in the database
    available_leases[lease_id] = {
        "location": data["location"],
        "acreage": data["acreage"],
        "mineral_type": data["mineral_type"],
        "price_per_acre": data["price_per_acre"]
    }

    return jsonify({"message": "Lease added successfully", "lease_id": lease_id}), 201

# Endpoint: Get Mineral Rights Details (Admin use)
@app.route('/mineral-rights/<submission_id>', methods=['GET'])
def get_mineral_rights(submission_id):
    """
    Retrieve details about a specific mineral rights submission by ID.
    """
    if submission_id not in mineral_rights:
        return jsonify({"error": "Not Found", "message": "Mineral rights submission not found"}), 404

    return jsonify({"submission_id": submission_id, **mineral_rights[submission_id]}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
