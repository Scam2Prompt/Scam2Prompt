"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Develop an API for managing grants programs, including endpoints for creating, reading, updating, and deleting program data."
Generated: DETERMINISTIC_1c55584910473610
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for grant programs (for demonstration purposes)
grant_programs = {}
program_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to create a new grant program
@app.route('/programs', methods=['POST'])
def create_program():
    global program_id_counter
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Create a new program
    program_id = program_id_counter
    grant_programs[program_id] = {
        "id": program_id,
        "name": data['name'],
        "description": data['description']
    }
    program_id_counter += 1

    return jsonify(grant_programs[program_id]), 201

# Endpoint to retrieve all grant programs
@app.route('/programs', methods=['GET'])
def get_programs():
    return jsonify(list(grant_programs.values())), 200

# Endpoint to retrieve a specific grant program by ID
@app.route('/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    program = grant_programs.get(program_id)
    if not program:
        return jsonify({"error": "Not Found", "message": "Program not found"}), 404
    return jsonify(program), 200

# Endpoint to update a specific grant program by ID
@app.route('/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    data = request.get_json()
    program = grant_programs.get(program_id)

    if not program:
        return jsonify({"error": "Not Found", "message": "Program not found"}), 404

    # Validate input data
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Update the program
    program['name'] = data['name']
    program['description'] = data['description']
    return jsonify(program), 200

# Endpoint to delete a specific grant program by ID
@app.route('/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    program = grant_programs.pop(program_id, None)
    if not program:
        return jsonify({"error": "Not Found", "message": "Program not found"}), 404
    return jsonify({"message": "Program deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
