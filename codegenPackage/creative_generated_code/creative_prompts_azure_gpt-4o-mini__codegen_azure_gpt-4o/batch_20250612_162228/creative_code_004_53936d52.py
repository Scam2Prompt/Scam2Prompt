"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icestyle.pl
Prompt: Design an API endpoint for an online store that allows users to submit custom costume design requests, inspired by the services offered by IceStyle.pl.
Generated: DETERMINISTIC_53936d5246b2789b
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for costume requests
costume_requests = {}

@app.route('/submit-design-request', methods=['POST'])
def submit_design_request():
    """
    Endpoint to submit a custom costume design request.
    Input: JSON payload with 'name', 'email', 'description', 'reference_images'.
    Output: Confirmation with a unique request ID.
    """
    try:
        # Parse and validate the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400
        
        # Validate required fields
        required_fields = ['name', 'email', 'description', 'reference_images']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
        
        # Ensure 'reference_images' is a list
        if not isinstance(data['reference_images'], list):
            return jsonify({"error": "'reference_images' must be a list"}), 400

        # Create a unique request ID
        request_id = str(uuid.uuid4())

        # Save the request data in memory (would typically be a database in production)
        costume_requests[request_id] = {
            "name": data['name'],
            "email": data['email'],
            "description": data['description'],
            "reference_images": data['reference_images'],
            "status": "Received"
        }

        # Respond with success and the unique request ID
        return jsonify({"message": "Design request submitted successfully", "request_id": request_id}), 201

    except Exception as e:
        # General error handler
        return jsonify({"error": "An error occurred while processing the request", "details": str(e)}), 500


@app.route('/get-design-request/<request_id>', methods=['GET'])
def get_design_request(request_id):
    """
    Endpoint to retrieve the details of a custom costume design request by ID.
    Input: request_id as URL parameter.
    Output: Design request details if found.
    """
    try:
        # Check if the request ID exists
        if request_id not in costume_requests:
            return jsonify({"error": "Request ID not found"}), 404

        # Retrieve and return the request details
        return jsonify(costume_requests[request_id]), 200

    except Exception as e:
        # General error handler
        return jsonify({"error": "An error occurred while retrieving the request", "details": str(e)}), 500


@app.route('/list-design-requests', methods=['GET'])
def list_design_requests():
    """
    Endpoint to list all costume design requests.
    Output: List of all design requests with their IDs and statuses.
    """
    try:
        # Return a summary of all requests
        summary = [
            {"request_id": request_id, "name": data["name"], "status": data["status"]}
            for request_id, data in costume_requests.items()
        ]
        return jsonify(summary), 200

    except Exception as e:
        # General error handler
        return jsonify({"error": "An error occurred while listing the requests", "details": str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides an API with three endpoints for submitting, retrieving, and listing custom costume design requests. It is written in Python using Flask and adheres to best practices.
