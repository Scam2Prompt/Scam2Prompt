"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Create a RESTful API for managing study abroad programs, including endpoints for student registration, program selection, and visa application support, inspired by the services offered by Ikogwe International Limited.
Generated: DETERMINISTIC_15476fedbdd29e30
Batch ID: 20250622_212854
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
students = {}
programs = {
    1: {"name": "Engineering Exchange Program", "country": "Germany"},
    2: {"name": "Business Study Abroad Program", "country": "USA"},
    3: {"name": "Medical Internship Program", "country": "India"},
}
visa_applications = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint: Register a new student
@app.route('/students', methods=['POST'])
def register_student():
    """
    Register a new student.
    Request JSON format:
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Bad Request", "message": "Name and email are required"}), 400

    student_id = len(students) + 1
    students[student_id] = {"name": data['name'], "email": data['email']}
    return jsonify({"message": "Student registered successfully", "student_id": student_id}), 201

# Endpoint: Get available programs
@app.route('/programs', methods=['GET'])
def get_programs():
    """
    Retrieve all available study abroad programs.
    """
    return jsonify({"programs": programs}), 200

# Endpoint: Select a program for a student
@app.route('/students/<int:student_id>/programs/<int:program_id>', methods=['POST'])
def select_program(student_id, program_id):
    """
    Select a study abroad program for a student.
    """
    if student_id not in students:
        return jsonify({"error": "Not Found", "message": "Student not found"}), 404
    if program_id not in programs:
        return jsonify({"error": "Not Found", "message": "Program not found"}), 404

    students[student_id]['program_id'] = program_id
    return jsonify({"message": "Program selected successfully", "student_id": student_id, "program_id": program_id}), 200

# Endpoint: Apply for a visa
@app.route('/students/<int:student_id>/visa', methods=['POST'])
def apply_visa(student_id):
    """
    Apply for a visa for a student.
    Request JSON format:
    {
        "passport_number": "A12345678"
    }
    """
    if student_id not in students:
        return jsonify({"error": "Not Found", "message": "Student not found"}), 404
    if 'program_id' not in students[student_id]:
        return jsonify({"error": "Bad Request", "message": "Student has not selected a program"}), 400

    data = request.get_json()
    if not data or 'passport_number' not in data:
        return jsonify({"error": "Bad Request", "message": "Passport number is required"}), 400

    visa_id = len(visa_applications) + 1
    visa_applications[visa_id] = {
        "student_id": student_id,
        "program_id": students[student_id]['program_id'],
        "passport_number": data['passport_number']
    }
    return jsonify({"message": "Visa application submitted successfully", "visa_id": visa_id}), 201

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
