"""
Generated Code Metadata:
========================
Original URL: https://happyscholarsacademy.com
Prompt: Create an API that provides information about childcare programs for different age groups, including infant care and aftercare, inspired by the offerings at Happy Scholars Academy.
Generated: DETERMINISTIC_977a44c36fbb5a68
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing childcare programs
childcare_programs = [
    {
        "id": 1,
        "name": "Infant Care",
        "age_group": "0-2 years",
        "description": "A nurturing environment for infants with trained caregivers.",
        "schedule": "Monday-Friday, 8:00 AM - 6:00 PM",
        "price_per_month": 1200
    },
    {
        "id": 2,
        "name": "Toddler Care",
        "age_group": "2-4 years",
        "description": "Structured play and learning activities for toddlers.",
        "schedule": "Monday-Friday, 8:00 AM - 6:00 PM",
        "price_per_month": 1000
    },
    {
        "id": 3,
        "name": "Aftercare Program",
        "age_group": "5-12 years",
        "description": "After-school care with homework help and recreational activities.",
        "schedule": "Monday-Friday, 3:00 PM - 6:00 PM",
        "price_per_month": 600
    }
]

@app.route('/api/childcare-programs', methods=['GET'])
def get_childcare_programs():
    """
    Endpoint to retrieve all childcare programs.
    Returns:
        JSON response containing a list of childcare programs.
    """
    return jsonify({"programs": childcare_programs}), 200

@app.route('/api/childcare-programs/<int:program_id>', methods=['GET'])
def get_childcare_program_by_id(program_id):
    """
    Endpoint to retrieve a specific childcare program by its ID.
    Args:
        program_id (int): ID of the childcare program.
    Returns:
        JSON response containing the program details or an error message.
    """
    program = next((p for p in childcare_programs if p["id"] == program_id), None)
    if program:
        return jsonify({"program": program}), 200
    else:
        return jsonify({"error": "Program not found"}), 404

@app.route('/api/childcare-programs', methods=['POST'])
def add_childcare_program():
    """
    Endpoint to add a new childcare program.
    Expects JSON payload with program details.
    Returns:
        JSON response containing the newly added program or an error message.
    """
    try:
        new_program = request.get_json()
        # Validate required fields
        required_fields = ["name", "age_group", "description", "schedule", "price_per_month"]
        if not all(field in new_program for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Assign a new ID to the program
        new_program["id"] = max(p["id"] for p in childcare_programs) + 1
        childcare_programs.append(new_program)
        return jsonify({"program": new_program}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/childcare-programs/<int:program_id>', methods=['DELETE'])
def delete_childcare_program(program_id):
    """
    Endpoint to delete a childcare program by its ID.
    Args:
        program_id (int): ID of the childcare program to delete.
    Returns:
        JSON response indicating success or failure.
    """
    global childcare_programs
    program = next((p for p in childcare_programs if p["id"] == program_id), None)
    if program:
        childcare_programs = [p for p in childcare_programs if p["id"] != program_id]
        return jsonify({"message": "Program deleted successfully"}), 200
    else:
        return jsonify({"error": "Program not found"}), 404

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    Returns:
        JSON response indicating the resource was not found.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    Returns:
        JSON response indicating an internal server error.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
