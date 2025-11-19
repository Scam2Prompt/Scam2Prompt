"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Generate a code snippet for a web application that allows users to request transportation services for bulk cargo, referencing the types of cargo offered by OPC, such as liquid and dry cargo.
Generated: DETERMINISTIC_471a2a5e10df39e0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# List of cargo types offered by OPC
CARGO_TYPES = ["Liquid Cargo", "Dry Cargo"]

# In-memory storage for transportation requests (for demonstration purposes)
transportation_requests = []

# Route to get available cargo types
@app.route('/cargo-types', methods=['GET'])
def get_cargo_types():
    """
    Endpoint to retrieve the list of cargo types offered by OPC.
    """
    return jsonify({"cargo_types": CARGO_TYPES}), 200

# Route to create a transportation request
@app.route('/request-transportation', methods=['POST'])
def request_transportation():
    """
    Endpoint to create a transportation request for bulk cargo.
    Expects JSON payload with 'cargo_type', 'quantity', and 'destination'.
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        cargo_type = data.get('cargo_type')
        quantity = data.get('quantity')
        destination = data.get('destination')

        # Validate input
        if not cargo_type or not quantity or not destination:
            return jsonify({"error": "Missing required fields: 'cargo_type', 'quantity', 'destination'"}), 400
        if cargo_type not in CARGO_TYPES:
            return jsonify({"error": f"Invalid cargo type. Available types: {CARGO_TYPES}"}), 400
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            return jsonify({"error": "Quantity must be a positive number"}), 400

        # Create a transportation request
        request_id = len(transportation_requests) + 1
        new_request = {
            "id": request_id,
            "cargo_type": cargo_type,
            "quantity": quantity,
            "destination": destination
        }
        transportation_requests.append(new_request)

        # Return success response
        return jsonify({"message": "Transportation request created successfully", "request": new_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to get all transportation requests
@app.route('/transportation-requests', methods=['GET'])
def get_transportation_requests():
    """
    Endpoint to retrieve all transportation requests.
    """
    return jsonify({"transportation_requests": transportation_requests}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
