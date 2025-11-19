"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Generate a code snippet for a web application that allows users to request transportation services for bulk cargo, referencing the types of cargo offered by OPC, such as liquid and dry cargo.
Generated: DETERMINISTIC_471a2a5e10df39e0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define available cargo types
CARGO_TYPES = ["Liquid Cargo", "Dry Cargo"]

# Sample transportation services data (for demonstration purposes)
transport_services = []

@app.route('/cargo-types', methods=['GET'])
def get_cargo_types():
    """
    Endpoint to fetch available cargo types.
    Returns:
        JSON response with a list of cargo types offered.
    """
    return jsonify({"cargo_types": CARGO_TYPES}), 200

@app.route('/request-transport', methods=['POST'])
def request_transport():
    """
    Endpoint for users to request transportation services for bulk cargo.
    Expects JSON input with 'cargo_type', 'quantity', and 'pickup_location'.
    
    Returns:
        JSON response confirming the request or an error message.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        cargo_type = data.get("cargo_type")
        quantity = data.get("quantity")
        pickup_location = data.get("pickup_location")
        
        # Validate input
        if not cargo_type or not quantity or not pickup_location:
            return jsonify({"error": "Missing required fields: 'cargo_type', 'quantity', 'pickup_location'"}), 400
        
        if cargo_type not in CARGO_TYPES:
            return jsonify({"error": f"Invalid cargo type. Available types: {', '.join(CARGO_TYPES)}"}), 400

        # Create a new transportation request
        transport_request = {
            "cargo_type": cargo_type,
            "quantity": quantity,
            "pickup_location": pickup_location
        }
        transport_services.append(transport_request)

        # Return success response
        return jsonify({"message": "Transportation request created successfully", "request": transport_request}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing the request", "details": str(e)}), 500

@app.route('/transport-services', methods=['GET'])
def get_transport_services():
    """
    Endpoint to retrieve all transportation service requests.
    Returns:
        JSON response with a list of transportation service requests.
    """
    return jsonify({"transport_services": transport_services}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
