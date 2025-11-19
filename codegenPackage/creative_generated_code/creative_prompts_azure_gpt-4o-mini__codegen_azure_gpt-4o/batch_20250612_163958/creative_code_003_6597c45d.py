"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Provide an example of a web application that could manage student admissions for a school with facilities like those at Happy Boarding School.
Generated: DETERMINISTIC_6597c45dc69d4f35
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

# Initialize the Flask app
app = Flask(__name__)

# In-memory database (simulated)
students = []

# Error messages
ERROR_STUDENT_NOT_FOUND = "Student not found."

# Helper function to generate unique IDs
def generate_id():
    return str(uuid4())

# Route: Get all students
@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students."""
    return jsonify(students), 200

# Route: Get a single student by ID
@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve details of a single student by their ID."""
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': ERROR_STUDENT_NOT_FOUND}), 404
    return jsonify(student), 200

# Route: Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    """
    Add a new student to the system.
    JSON payload format:
    {
        "name": "John Doe",
        "age": 16,
        "grade": "10th"
    }
    """
    data = request.get_json()
    
    # Data validation
    if not data or 'name' not in data or 'age' not in data or 'grade' not in data:
        return jsonify({'error': 'Invalid data. Name, age, and grade are required.'}), 400
    
    # Create student record
    student = {
        'id': generate_id(),
        'name': data['name'],
        'age': data['age'],
        'grade': data['grade']
    }
    students.append(student)
    return jsonify(student), 201

# Route: Update an existing student
@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update details of an existing student.
    JSON payload format:
    {
        "name": "Jane Doe",
        "age": 17,
        "grade": "11th"
    }
    """
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': ERROR_STUDENT_NOT_FOUND}), 404
    
    data = request.get_json()
    
    # Data validation
    if not data or ('name' not in data and 'age' not in data and 'grade' not in data):
        return jsonify({'error': 'Invalid data. Provide at least one field to update.'}), 400
    
    # Update student record
    student.update({k: v for k, v in data.items() if k in ['name', 'age', 'grade']})
    return jsonify(student), 200

# Route: Delete a student
@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student from the system."""
    global students
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': ERROR_STUDENT_NOT_FOUND}), 404
    
    students = [s for s in students if s['id'] != student_id]
    return jsonify({'message': 'Student deleted successfully.'}), 200

# Error handler: Catch-all for server errors
@app.errorhandler(500)
def internal_server_error(e):
    """Handle unexpected server errors."""
    return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

# Entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
