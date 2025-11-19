"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgngaya.in
Prompt: Create a REST API for managing student records and academic results, incorporating features that reflect the mission and vision of Param Gyan Niketan.
Generated: DETERMINISTIC_54f0703e845666ca
Batch ID: 20250612_162511
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

# In-memory data storage for simplicity
students = {}
results = {}

# Mission and Vision: Deliver holistic education and empower students academically and morally.

# Error Handling Middleware
@app.errorhandler(Exception)
def handle_error(e):
    """Global error handler for the API"""
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# REST API for managing student records

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all student records"""
    return jsonify({"students": students}), 200

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve specific student record by ID"""
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"student": student}), 200

@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student record"""
    data = request.json
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    student_id = data['id']
    if student_id in students:
        return jsonify({"error": "Student ID already exists"}), 400

    students[student_id] = {"name": data['name'], "class": data.get('class', None)}
    return jsonify({"message": "Student added successfully"}), 201

@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    """Update an existing student record"""
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid data"}), 400

    students[student_id].update({"name": data['name'], "class": data.get('class', students[student_id]['class'])})
    return jsonify({"message": "Student updated successfully"}), 200

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student record"""
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    del students[student_id]
    return jsonify({"message": "Student deleted successfully"}), 200

# REST API for managing academic results

@app.route('/results/<student_id>', methods=['GET'])
def get_results(student_id):
    """Retrieve results for a specific student"""
    result = results.get(student_id)
    if not result:
        return jsonify({"error": "Results not found for this student"}), 404
    return jsonify({"results": result}), 200

@app.route('/results/<student_id>', methods=['POST'])
def add_results(student_id):
    """Add academic results for a student"""
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    if not data or 'subject' not in data or 'marks' not in data:
        return jsonify({"error": "Invalid data"}), 400

    if student_id not in results:
        results[student_id] = []

    results[student_id].append({"subject": data['subject'], "marks": data['marks']})
    return jsonify({"message": "Results added successfully"}), 201

@app.route('/results/<student_id>', methods=['PUT'])
def update_results(student_id):
    """Update academic results for a student"""
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    if not data or 'subject' not in data or 'marks' not in data:
        return jsonify({"error": "Invalid data"}), 400

    if student_id not in results:
        return jsonify({"error": "Results not found for this student"}), 404

    for result in results[student_id]:
        if result['subject'] == data['subject']:
            result['marks'] = data['marks']
            return jsonify({"message": "Results updated successfully"}), 200

    return jsonify({"error": "Subject not found"}), 404

@app.route('/results/<student_id>', methods=['DELETE'])
def delete_results(student_id):
    """Delete all results for a student"""
    if student_id not in results:
        return jsonify({"error": "Results not found for this student"}), 404

    del results[student_id]
    return jsonify({"message": "Results deleted successfully"}), 200

# Entry point to start the Flask app
if __name__ == "__main__":
    app.run(debug=False)  # Set debug to False for production
```
