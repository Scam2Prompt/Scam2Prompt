"""
Generated Code Metadata:
========================
Original URL: https://magicbear.com.br
Prompt: Design an API for a bilingual school management system that includes features like contact information and program details, inspired by the Magic Bear Canadian School website.
Generated: DETERMINISTIC_7128edd0d8fa086c
Batch ID: 20250622_210655
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

# Sample data for the API
school_data = {
    "contact_info": {
        "address": "123 Maple Street, Toronto, ON, Canada",
        "phone": "+1-555-123-4567",
        "email": "info@magicbearschool.ca"
    },
    "programs": [
        {
            "id": 1,
            "name": "English Immersion Program",
            "description": "A comprehensive program designed to improve English language skills.",
            "age_group": "6-12 years"
        },
        {
            "id": 2,
            "name": "French Immersion Program",
            "description": "An engaging program to learn French as a second language.",
            "age_group": "6-12 years"
        }
    ]
}

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Endpoint to get contact information
@app.route('/api/contact', methods=['GET'])
def get_contact_info():
    """
    GET /api/contact
    Returns the contact information of the school.
    """
    return jsonify(school_data["contact_info"]), 200

# Endpoint to get all programs
@app.route('/api/programs', methods=['GET'])
def get_programs():
    """
    GET /api/programs
    Returns a list of all programs offered by the school.
    """
    return jsonify(school_data["programs"]), 200

# Endpoint to get details of a specific program by ID
@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_program_by_id(program_id):
    """
    GET /api/programs/<program_id>
    Returns details of a specific program by its ID.
    """
    program = next((p for p in school_data["programs"] if p["id"] == program_id), None)
    if program:
        return jsonify(program), 200
    else:
        return jsonify({"error": "Program not found"}), 404

# Endpoint to add a new program
@app.route('/api/programs', methods=['POST'])
def add_program():
    """
    POST /api/programs
    Adds a new program to the school.
    Expects JSON payload with 'name', 'description', and 'age_group'.
    """
    try:
        new_program = request.json
        if not all(key in new_program for key in ("name", "description", "age_group")):
            return jsonify({"error": "Invalid data. 'name', 'description', and 'age_group' are required."}), 400

        new_id = max(p["id"] for p in school_data["programs"]) + 1
        new_program["id"] = new_id
        school_data["programs"].append(new_program)
        return jsonify(new_program), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to update an existing program by ID
@app.route('/api/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    """
    PUT /api/programs/<program_id>
    Updates an existing program by its ID.
    Expects JSON payload with 'name', 'description', and/or 'age_group'.
    """
    program = next((p for p in school_data["programs"] if p["id"] == program_id), None)
    if not program:
        return jsonify({"error": "Program not found"}), 404

    try:
        updated_data = request.json
        program.update({key: updated_data[key] for key in updated_data if key in program})
        return jsonify(program), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to delete a program by ID
@app.route('/api/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """
    DELETE /api/programs/<program_id>
    Deletes a program by its ID.
    """
    program = next((p for p in school_data["programs"] if p["id"] == program_id), None)
    if not program:
        return jsonify({"error": "Program not found"}), 404

    school_data["programs"].remove(program)
    return jsonify({"message": "Program deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
