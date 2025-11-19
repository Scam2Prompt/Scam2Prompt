"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rfd.claims
Prompt: Provide an example of a RESTful API endpoint for claims retrieval inspired by rfd.claims.
Generated: DETERMINISTIC_29254788d5f7e33a
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data to simulate claims storage
claims_data = [
    {"claim_id": 1, "user_id": 101, "status": "approved", "amount": 150.00},
    {"claim_id": 2, "user_id": 102, "status": "pending", "amount": 200.50},
    {"claim_id": 3, "user_id": 101, "status": "rejected", "amount": 75.00},
]

# Custom error handler for API
@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({
            "error": {
                "code": e.code,
                "message": e.description
            }
        }).get_data()
        response.content_type = "application/json"
        return response
    else:
        # Handle non-HTTP exceptions
        return jsonify({
            "error": {
                "code": 500,
                "message": "An unexpected error occurred."
            }
        }), 500

# RESTful endpoint to retrieve claims
@app.route('/api/claims', methods=['GET'])
def get_claims():
    """
    Retrieve claims based on optional query parameters.
    Query Parameters:
        user_id (int): Filter claims by user ID.
        status (str): Filter claims by status (e.g., 'approved', 'pending', 'rejected').
    Returns:
        JSON response containing filtered claims or all claims if no filters are provided.
    """
    try:
        # Extract query parameters
        user_id = request.args.get('user_id', type=int)
        status = request.args.get('status', type=str)

        # Filter data based on query parameters
        filtered_claims = claims_data
        if user_id is not None:
            filtered_claims = [claim for claim in filtered_claims if claim['user_id'] == user_id]
        if status is not None:
            filtered_claims = [claim for claim in filtered_claims if claim['status'] == status]

        # Return filtered claims as JSON
        return jsonify({
            "success": True,
            "data": filtered_claims
        })
    except Exception as err:
        # Catch unexpected errors
        return jsonify({
            "success": False,
            "error": {
                "message": str(err)
            }
        }), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
