"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Create a REST API specification for managing student records and performance tracking at an educational institution similar to Potencia Academy.
Generated: DETERMINISTIC_a2b37789953b7c96
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
students = {}
performance_records = {}

# Error messages
NOT_FOUND_ERROR = {"error": "Resource not found"}
BAD_REQUEST_ERROR = {"error": "Bad request"}

# Helper functions
def validate_student_data(data):
    """Validate student data provided in the request."""
    required_fields = ["id", "name", "age", "grade"]
    return all(field in data for field in required_fields)

def validate_performance_data(data):
    """Validate performance data provided in the request."""
    required_fields = ["student_id", "subject", "score"]
    return all(field in data for field in required_fields)

# Routes

@app.route('/students', methods=['GET'])
def get_all_students():
    """Retrieve all students."""
    return jsonify(list(students.values())), 200

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve details for a specific student."""
    student = students.get(student_id)
    if not student:
        return jsonify(NOT_FOUND_ERROR), 404
    return jsonify(student), 200

@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student."""
    data = request.get_json()
    if not validate_student_data(data):
        return jsonify(BAD_REQUEST_ERROR), 400
    student_id = data['id']
    if student_id in students:
        return jsonify({"error": "Student already exists"}), 409
    students[student_id] = data
    return jsonify(data), 201

@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    """Update details for an existing student."""
    data = request.get_json()
    if student_id not in students:
        return jsonify(NOT_FOUND_ERROR), 404
    if not validate_student_data(data):
        return jsonify(BAD_REQUEST_ERROR), 400
    students[student_id] = data
    return jsonify(data), 200

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student record."""
    if student_id not in students:
        return jsonify(NOT_FOUND_ERROR), 404
    del students[student_id]
    return jsonify({"message": "Student deleted"}), 200

@app.route('/performance', methods=['GET'])
def get_all_performance_records():
    """Retrieve all performance records."""
    return jsonify(list(performance_records.values())), 200

@app.route('/performance/<record_id>', methods=['GET'])
def get_performance_record(record_id):
    """Retrieve a specific performance record."""
    record = performance_records.get(record_id)
    if not record:
        return jsonify(NOT_FOUND_ERROR), 404
    return jsonify(record), 200

@app.route('/performance', methods=['POST'])
def add_performance_record():
    """Add a new performance record."""
    data = request.get_json()
    if not validate_performance_data(data):
        return jsonify(BAD_REQUEST_ERROR), 400
    record_id = f"{data['student_id']}-{data['subject']}"
    if record_id in performance_records:
        return jsonify({"error": "Performance record already exists"}), 409
    performance_records[record_id] = data
    return jsonify(data), 201

@app.route('/performance/<record_id>', methods=['PUT'])
def update_performance_record(record_id):
    """Update an existing performance record."""
    data = request.get_json()
    if record_id not in performance_records:
        return jsonify(NOT_FOUND_ERROR), 404
    if not validate_performance_data(data):
        return jsonify(BAD_REQUEST_ERROR), 400
    performance_records[record_id] = data
    return jsonify(data), 200

@app.route('/performance/<record_id>', methods=['DELETE'])
def delete_performance_record(record_id):
    """Delete a performance record."""
    if record_id not in performance_records:
        return jsonify(NOT_FOUND_ERROR), 404
    del performance_records[record_id]
    return jsonify({"message": "Performance record deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
