"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Design a grants program using a visual canvas, including steps for planning payout processes and setting clear criteria."
Generated: DETERMINISTIC_af14bed36ef24de8
Batch ID: 20250622_212142
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
from flask_cors import CORS
import uuid

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend integration

# In-memory storage for grants program data
grants_programs = {}

# Helper function to validate input data
def validate_grants_program(data):
    required_fields = ["name", "description", "criteria", "payout_steps"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data["payout_steps"], list):
        return False, "Payout steps must be a list"
    return True, None

# Route to create a new grants program
@app.route('/grants', methods=['POST'])
def create_grants_program():
    try:
        # Parse request data
        data = request.json
        is_valid, error_message = validate_grants_program(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Generate a unique ID for the grants program
        program_id = str(uuid.uuid4())
        grants_programs[program_id] = {
            "id": program_id,
            "name": data["name"],
            "description": data["description"],
            "criteria": data["criteria"],
            "payout_steps": data["payout_steps"]
        }

        return jsonify({"message": "Grants program created successfully", "id": program_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all grants programs
@app.route('/grants', methods=['GET'])
def get_all_grants_programs():
    try:
        return jsonify(list(grants_programs.values())), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve a specific grants program by ID
@app.route('/grants/<program_id>', methods=['GET'])
def get_grants_program(program_id):
    try:
        program = grants_programs.get(program_id)
        if not program:
            return jsonify({"error": "Grants program not found"}), 404
        return jsonify(program), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a specific grants program by ID
@app.route('/grants/<program_id>', methods=['PUT'])
def update_grants_program(program_id):
    try:
        # Parse request data
        data = request.json
        is_valid, error_message = validate_grants_program(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Check if the program exists
        if program_id not in grants_programs:
            return jsonify({"error": "Grants program not found"}), 404

        # Update the program
        grants_programs[program_id].update({
            "name": data["name"],
            "description": data["description"],
            "criteria": data["criteria"],
            "payout_steps": data["payout_steps"]
        })

        return jsonify({"message": "Grants program updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a specific grants program by ID
@app.route('/grants/<program_id>', methods=['DELETE'])
def delete_grants_program(program_id):
    try:
        # Check if the program exists
        if program_id not in grants_programs:
            return jsonify({"error": "Grants program not found"}), 404

        # Delete the program
        del grants_programs[program_id]
        return jsonify({"message": "Grants program deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True, port=5000)
```
