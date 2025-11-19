"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Develop an API endpoint specification for a roofing service that allows clients to submit requests for inspections and estimates, including necessary parameters and response formats.
Generated: DETERMINISTIC_59558a0b22af006d
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database for storing inspection requests
inspection_requests = []

@app.route('/api/roofing/inspection', methods=['POST'])
def submit_inspection_request():
    """
    Endpoint to submit a roofing inspection request.
    Accepts JSON payload with required parameters.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'address', 'roof_type']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Validate email format (basic validation)
        if '@' not in data['email']:
            return jsonify({"error": "Invalid email format"}), 400

        # Create a new inspection request
        inspection_request = {
            "id": len(inspection_requests) + 1,  # Auto-increment ID
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "address": data['address'],
            "roof_type": data['roof_type'],
            "comments": data.get('comments', ""),  # Optional field
            "status": "Pending"  # Default status
        }

        # Save the request to the in-memory database
        inspection_requests.append(inspection_request)

        # Return success response
        return jsonify({
            "message": "Inspection request submitted successfully",
            "request_id": inspection_request['id']
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/api/roofing/inspection/<int:request_id>', methods=['GET'])
def get_inspection_request(request_id):
    """
    Endpoint to retrieve a specific inspection request by ID.
    """
    try:
        # Find the request by ID
        request_data = next((req for req in inspection_requests if req['id'] == request_id), None)
        if not request_data:
            return jsonify({"error": "Inspection request not found"}), 404

        # Return the request data
        return jsonify(request_data), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/api/roofing/inspection', methods=['GET'])
def list_inspection_requests():
    """
    Endpoint to list all inspection requests.
    """
    try:
        # Return all inspection requests
        return jsonify(inspection_requests), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
