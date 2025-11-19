"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Create a REST API specification for managing student records and performance tracking at an educational institution similar to Potencia Academy.
Generated: DETERMINISTIC_a2b37789953b7c96
Batch ID: 20250612_155654
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
student_id_counter = 1

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

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route: Get all students
@app.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve all student records.
    """
    return jsonify(list(students.values())), 200

# Route: Get a specific student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a specific student record by ID.
    """
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200

# Route: Create a new student record
@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.
    """
    global student_id_counter
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data or 'grade' not in data:
        return jsonify({"error": "Invalid input"}), 400

    student = {
        "id": student_id_counter,
        "name": data['name'],
        "age": data['age'],
        "grade": data['grade'],
        "performance": data.get('performance', {})
    }
    students[student_id_counter] = student
    student_id_counter += 1
    return jsonify(student), 201

# Route: Update an existing student record
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update an existing student record.
    """
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    student['name'] = data.get('name', student['name'])
    student['age'] = data.get('age', student['age'])
    student['grade'] = data.get('grade', student['grade'])
    student['performance'] = data.get('performance', student['performance'])
    return jsonify(student), 200

# Route: Delete a student record
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    Delete a student record.
    """
    student = students.pop(student_id, None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"message": "Student deleted successfully"}), 200

# Route: Add or update performance data for a student
@app.route('/students/<int:student_id>/performance', methods=['PUT'])
def update_performance(student_id):
    """
    Add or update performance data for a student.
    """
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    student['performance'].update(data)
    return jsonify(student), 200

# Route: Get performance data for a student
@app.route('/students/<int:student_id>/performance', methods=['GET'])
def get_performance(student_id):
    """
    Retrieve performance data for a student.
    """
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student.get('performance', {})), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
