"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Create a REST API in Flask for managing institutional data, including endpoints for retrieving information about academic programs, administrative services, and institutional recognitions, inspired by the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_9d9d4af3c02c7453
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data to simulate a database
data = {
    "academic_programs": [
        {"id": 1, "name": "Computer Science", "description": "Learn programming and data structures."},
        {"id": 2, "name": "Business Administration", "description": "Study management and organizational behavior."}
    ],
    "administrative_services": [
        {"id": 1, "name": "Admissions Office", "description": "Handles student applications and enrollments."},
        {"id": 2, "name": "Finance Office", "description": "Manages tuition payments and financial aid."}
    ],
    "institutional_recognitions": [
        {"id": 1, "title": "Best Technical Institute 2023", "details": "Awarded for excellence in technical education."},
        {"id": 2, "title": "Green Campus Award", "details": "Recognized for sustainable practices."}
    ]
}

# Error handling response format
def create_error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Route: Get all academic programs
@app.route('/api/academic-programs', methods=['GET'])
def get_academic_programs():
    return jsonify(data["academic_programs"])

# Route: Get a specific academic program by ID
@app.route('/api/academic-programs/<int:program_id>', methods=['GET'])
def get_academic_program(program_id):
    program = next((p for p in data["academic_programs"] if p["id"] == program_id), None)
    if not program:
        return create_error_response("Academic program not found.", 404)
    return jsonify(program)

# Route: Get all administrative services
@app.route('/api/administrative-services', methods=['GET'])
def get_administrative_services():
    return jsonify(data["administrative_services"])

# Route: Get a specific administrative service by ID
@app.route('/api/administrative-services/<int:service_id>', methods=['GET'])
def get_administrative_service(service_id):
    service = next((s for s in data["administrative_services"] if s["id"] == service_id), None)
    if not service:
        return create_error_response("Administrative service not found.", 404)
    return jsonify(service)

# Route: Get all institutional recognitions
@app.route('/api/institutional-recognitions', methods=['GET'])
def get_institutional_recognitions():
    return jsonify(data["institutional_recognitions"])

# Route: Get a specific institutional recognition by ID
@app.route('/api/institutional-recognitions/<int:recognition_id>', methods=['GET'])
def get_institutional_recognition(recognition_id):
    recognition = next((r for r in data["institutional_recognitions"] if r["id"] == recognition_id), None)
    if not recognition:
        return create_error_response("Institutional recognition not found.", 404)
    return jsonify(recognition)

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return create_error_response("Resource not found.", 404)

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return create_error_response("Internal server error.", 500)

# Main entry point to run the Flask app
if __name__ == '__main__':
    # Run the app in debug mode for development purposes
    app.run(debug=True)
```
