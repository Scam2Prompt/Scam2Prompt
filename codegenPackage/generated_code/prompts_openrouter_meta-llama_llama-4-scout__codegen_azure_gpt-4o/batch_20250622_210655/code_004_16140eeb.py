"""
Generated Code Metadata:
========================
Original URL: https://www.efeotokurtarma.com.tr
Prompt: Create a RESTful API endpoint to request and manage towing services, inspired by the features and structure of Efem Oto Kurtarma's services in Ankara.
Generated: DETERMINISTIC_16140eeb04cc04ee
Batch ID: 20250622_210655
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

# In-memory database to store towing service requests
towing_requests = {}

# Helper function to validate request data
def validate_request_data(data):
    required_fields = ['name', 'phone', 'vehicle_type', 'location']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

@app.route('/api/towing-services', methods=['POST'])
def create_towing_request():
    """
    Create a new towing service request.
    Expected JSON payload:
    {
        "name": "John Doe",
        "phone": "1234567890",
        "vehicle_type": "Car",
        "location": "Ankara, Turkey"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate request data
        is_valid, error_message = validate_request_data(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Generate a unique ID for the request
        request_id = str(uuid.uuid4())
        towing_requests[request_id] = {
            "id": request_id,
            "name": data['name'],
            "phone": data['phone'],
            "vehicle_type": data['vehicle_type'],
            "location": data['location'],
            "status": "Pending"
        }

        return jsonify({"message": "Towing request created successfully", "request_id": request_id}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/towing-services/<request_id>', methods=['GET'])
def get_towing_request(request_id):
    """
    Retrieve a specific towing service request by ID.
    """
    try:
        towing_request = towing_requests.get(request_id)
        if not towing_request:
            return jsonify({"error": "Towing request not found"}), 404

        return jsonify(towing_request), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/towing-services/<request_id>', methods=['PUT'])
def update_towing_request(request_id):
    """
    Update the status of a towing service request.
    Expected JSON payload:
    {
        "status": "Completed"
    }
    """
    try:
        data = request.get_json()
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid JSON payload or missing 'status' field"}), 400

        towing_request = towing_requests.get(request_id)
        if not towing_request:
            return jsonify({"error": "Towing request not found"}), 404

        towing_request['status'] = data['status']
        return jsonify({"message": "Towing request updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/towing-services/<request_id>', methods=['DELETE'])
def delete_towing_request(request_id):
    """
    Delete a specific towing service request by ID.
    """
    try:
        if request_id not in towing_requests:
            return jsonify({"error": "Towing request not found"}), 404

        del towing_requests[request_id]
        return jsonify({"message": "Towing request deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/towing-services', methods=['GET'])
def list_towing_requests():
    """
    List all towing service requests.
    """
    try:
        return jsonify(list(towing_requests.values())), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
