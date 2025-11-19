"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Create a REST API endpoint that allows for the management of independent contractor transitions to full-time employees, inspired by Connext's offerings.
Generated: DETERMINISTIC_e5d08c33cdcd9685
Batch ID: 20250612_164005
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

# In-memory database (for demonstration purposes)
contractors = [
    {"id": 1, "name": "Alice", "status": "contractor"},
    {"id": 2, "name": "Bob", "status": "contractor"}
]

# Utility function to find a contractor by ID
def find_contractor(contractor_id):
    for contractor in contractors:
        if contractor["id"] == contractor_id:
            return contractor
    return None

@app.route('/transition/<int:contractor_id>', methods=['PUT'])
def transition_to_full_time(contractor_id):
    """
    REST API endpoint to transition a contractor to full-time employee.
    - contractor_id: ID of the contractor to transition
    """
    try:
        # Retrieve contractor record
        contractor = find_contractor(contractor_id)
        if not contractor:
            return jsonify({"error": "Contractor not found"}), 404

        # Check current status
        if contractor["status"] == "full-time":
            return jsonify({"message": "Contractor is already a full-time employee"}), 400

        # Transition contractor to full-time
        contractor["status"] = "full-time"
        return jsonify({"message": f"Contractor {contractor['name']} successfully transitioned to full-time", "contractor": contractor}), 200

    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    """
    return jsonify({"error": e.name, "details": e.description}), e.code

@app.route('/contractors', methods=['GET'])
def list_contractors():
    """
    REST API endpoint to list all contractors.
    """
    return jsonify(contractors), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
