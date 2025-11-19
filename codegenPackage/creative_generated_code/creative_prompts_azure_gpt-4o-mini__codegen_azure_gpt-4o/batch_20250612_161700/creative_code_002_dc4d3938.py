"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Create a REST API endpoint that allows users to submit designs for hydraulic and sanitary networks, referencing the design services offered by Espinel y Cia.
Generated: DETERMINISTIC_dc4d39380b5e64e7
Batch ID: 20250612_161700
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

# In-memory storage for submitted designs (for demonstration purposes)
submitted_designs = []

# Utility function to validate design data
def validate_design_data(data):
    required_fields = ["name", "email", "network_type", "design_details"]
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    if data["network_type"] not in ["hydraulic", "sanitary"]:
        return "Invalid network_type. Must be 'hydraulic' or 'sanitary'."
    return None

@app.route('/submit-design', methods=['POST'])
def submit_design():
    """
    REST API endpoint to submit hydraulic or sanitary network designs.
    ---
    Request Body:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "network_type": "hydraulic",
        "design_details": "Detailed description of the design."
    }

    Response:
    - 200: Design successfully submitted
    - 400: Invalid request data
    - 500: Internal server error
    """
    try:
        # Parse and validate the incoming JSON request
        design_data = request.get_json()
        if not design_data:
            return jsonify({"error": "Request must be JSON formatted."}), 400

        validation_error = validate_design_data(design_data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Generate a unique ID for the design submission
        design_id = str(uuid.uuid4())
        design_data["id"] = design_id

        # Store the design in the in-memory list
        submitted_designs.append(design_data)

        # Respond with the design ID
        return jsonify({
            "message": "Design successfully submitted.",
            "design_id": design_id
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/designs', methods=['GET'])
def get_designs():
    """
    REST API endpoint to retrieve all submitted designs.
    ---
    Response:
    - 200: List of all submitted designs
    """
    try:
        return jsonify(submitted_designs), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
