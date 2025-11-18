"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Create a web application that supports international vocational education programs, including features for micro-credentials and joint education programs, as detailed on the AVEA website.
Generated: DETERMINISTIC_6f66933131f8f472
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation using Python with the Flask framework for the requested functionality. It includes basic support for international vocational education programs, micro-credentials, and joint education programs.

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data for programs, micro-credentials, and joint programs
data = {
    "programs": [
        {"id": 1, "name": "International Business Management", "description": "Learn global business practices."},
        {"id": 2, "name": "Software Development", "description": "Master coding skills for global projects."}
    ],
    "micro_credentials": [
        {"id": 1, "name": "Data Analysis Basics", "program_id": 2, "description": "Understand data analysis fundamentals."},
        {"id": 2, "name": "Leadership Essentials", "program_id": 1, "description": "Build essential leadership skills."}
    ],
    "joint_programs": [
        {"id": 1, "name": "International Business + Leadership", "description": "Combine global business and leadership skills."},
        {"id": 2, "name": "Coding + Data Analysis", "description": "Master coding and data analysis together."}
    ]
}

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions with error messages"""
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).data
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle unexpected exceptions with a general error message"""
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Routes to manage vocational education programs
@app.route('/programs', methods=['GET'])
def get_programs():
    """Retrieve all vocational education programs"""
    return jsonify(data["programs"]), 200

@app.route('/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Retrieve a specific program by ID"""
    program = next((p for p in data["programs"] if p["id"] == program_id), None)
    if not program:
        return jsonify({"error": "Program not found"}), 404
    return jsonify(program), 200

# Routes to manage micro-credentials
@app.route('/micro_credentials', methods=['GET'])
def get_micro_credentials():
    """Retrieve all micro-credentials"""
    return jsonify(data["micro_credentials"]), 200

@app.route('/micro_credentials/<int:cred_id>', methods=['GET'])
def get_micro_credential(cred_id):
    """Retrieve a specific micro-credential by ID"""
    credential = next((mc for mc in data["micro_credentials"] if mc["id"] == cred_id), None)
    if not credential:
        return jsonify({"error": "Micro-credential not found"}), 404
    return jsonify(credential), 200

# Routes to manage joint programs
@app.route('/joint_programs', methods=['GET'])
def get_joint_programs():
    """Retrieve all joint programs"""
    return jsonify(data["joint_programs"]), 200

@app.route('/joint_programs/<int:joint_id>', methods=['GET'])
def get_joint_program(joint_id):
    """Retrieve a specific joint program by ID"""
    joint_program = next((jp for jp in data["joint_programs"] if jp["id"] == joint_id), None)
    if not joint_program:
        return jsonify({"error": "Joint program not found"}), 404
    return jsonify(joint_program), 200

# Main entry point
if __name__ == '__main__':
    # Run the application in debug mode for development; use production server for deployment
    app.run(debug=True)
```

This code provides RESTful endpoints to retrieve information about vocational programs, micro-credentials, and joint education programs. Proper error handling is implemented for robustness. In a real-world scenario, the `data` would be replaced with database queries, and authentication would be added for security.
