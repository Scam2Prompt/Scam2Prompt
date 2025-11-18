"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Write a REST API for handling student registration processes for "Matricula 2025," inspired by the admission procedures mentioned on the Instituto Pangoa site.
Generated: DETERMINISTIC_604e9686b5f8f611
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Database simulation
students = []

# Helper function to validate student data
def validate_student_data(data):
    if not data.get('name') or not isinstance(data['name'], str):
        return "Name is required and must be a string."
    if not data.get('email') or not isinstance(data['email'], str):
        return "Email is required and must be a string."
    if not data.get('course') or not isinstance(data['course'], str):
        return "Course is required and must be a string."
    return None

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({'error': e.description}), e.code
    return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/students', methods=['POST'])
def register_student():
    """
    Register a new student.
    Endpoint: POST /students
    Body: JSON object containing 'name', 'email', and 'course'.
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be JSON.'}), 400

    # Validate input data
    validation_error = validate_student_data(data)
    if validation_error:
        return jsonify({'error': validation_error}), 400

    # Simulate ID generation and store the new student
    student_id = len(students) + 1
    new_student = {
        'id': student_id,
        'name': data['name'],
        'email': data['email'],
        'course': data['course']
    }
    students.append(new_student)
    return jsonify({'message': 'Student registered successfully.', 'student': new_student}), 201

@app.route('/students', methods=['GET'])
def list_students():
    """
    Get a list of all registered students.
    Endpoint: GET /students
    """
    return jsonify({'students': students}), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Get details of a specific student by ID.
    Endpoint: GET /students/<student_id>
    """
    student = next((student for student in students if student['id'] == student_id), None)
    if not student:
        return jsonify({'error': 'Student not found.'}), 404
    return jsonify({'student': student}), 200

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update details of a specific student by ID.
    Endpoint: PUT /students/<student_id>
    Body: JSON object containing 'name', 'email', and/or 'course'.
    """
    student = next((student for student in students if student['id'] == student_id), None)
    if not student:
        return jsonify({'error': 'Student not found.'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be JSON.'}), 400

    # Validate input data
    validation_error = validate_student_data(data)
    if validation_error:
        return jsonify({'error': validation_error}), 400

    # Update student details
    student.update({
        'name': data.get('name', student['name']),
        'email': data.get('email', student['email']),
        'course': data.get('course', student['course'])
    })
    return jsonify({'message': 'Student updated successfully.', 'student': student}), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    Delete a student by ID.
    Endpoint: DELETE /students/<student_id>
    """
    student = next((student for student in students if student['id'] == student_id), None)
    if not student:
        return jsonify({'error': 'Student not found.'}), 404

    students.remove(student)
    return jsonify({'message': 'Student deleted successfully.'}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
