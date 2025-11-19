"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Write a code snippet for a web application that allows parents to enroll their children in a daycare program like Kiddoo Playway, focusing on features such as activity-based curriculum and parental webinars.
Generated: DETERMINISTIC_3a5ec9b501a1361a
Batch ID: 20250612_162051
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

# In-memory database for demonstration purposes
daycare_programs = []
enrollments = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Route to list available daycare programs
@app.route('/programs', methods=['GET'])
def list_programs():
    """
    Endpoint to list all available daycare programs.
    """
    return jsonify(daycare_programs), 200

# Route to add a new daycare program
@app.route('/programs', methods=['POST'])
def add_program():
    """
    Endpoint to add a new daycare program.
    Expects JSON payload with 'name', 'activities', and 'webinars'.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'activities' not in data or 'webinars' not in data:
        return jsonify({"error": "Invalid input. 'name', 'activities', and 'webinars' are required."}), 400

    program = {
        "id": len(daycare_programs) + 1,
        "name": data['name'],
        "activities": data['activities'],
        "webinars": data['webinars']
    }
    daycare_programs.append(program)
    return jsonify(program), 201

# Route to enroll a child in a daycare program
@app.route('/enroll', methods=['POST'])
def enroll_child():
    """
    Endpoint to enroll a child in a daycare program.
    Expects JSON payload with 'child_name', 'parent_name', and 'program_id'.
    """
    data = request.get_json()
    if not data or 'child_name' not in data or 'parent_name' not in data or 'program_id' not in data:
        return jsonify({"error": "Invalid input. 'child_name', 'parent_name', and 'program_id' are required."}), 400

    # Check if the program exists
    program = next((p for p in daycare_programs if p['id'] == data['program_id']), None)
    if not program:
        return jsonify({"error": "Program not found."}), 404

    enrollment = {
        "id": len(enrollments) + 1,
        "child_name": data['child_name'],
        "parent_name": data['parent_name'],
        "program_id": data['program_id']
    }
    enrollments.append(enrollment)
    return jsonify(enrollment), 201

# Route to list all enrollments
@app.route('/enrollments', methods=['GET'])
def list_enrollments():
    """
    Endpoint to list all enrollments.
    """
    return jsonify(enrollments), 200

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
