"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Suggest an API that could help track student progress in employability skills training, similar to SMART's approach.
Generated: DETERMINISTIC_c03cbbb56bef588e
Batch ID: 20250612_163958
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

# In-memory database to track student progress
students = {}  # Example format: {student_id: {"name": "John Doe", "skills": {"communication": 80, "teamwork": 70}}}

# Helper function to validate input data
def validate_student_data(data):
    if "name" not in data or not isinstance(data["name"], str):
        return "Missing or invalid 'name'."
    if "skills" not in data or not isinstance(data["skills"], dict):
        return "Missing or invalid 'skills'."
    for skill, value in data["skills"].items():
        if not isinstance(skill, str) or not isinstance(value, int) or value < 0 or value > 100:
            return f"Invalid skill data for '{skill}'. Ensure skill names are strings and values are integers (0-100)."
    return None

# Route to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        error = validate_student_data(data)
        if error:
            return jsonify({"error": error}), 400
        
        student_id = len(students) + 1
        students[student_id] = {"name": data["name"], "skills": data["skills"]}
        return jsonify({"message": "Student added successfully.", "student_id": student_id}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while adding a student.", "details": str(e)}), 500

# Route to retrieve all students
@app.route('/students', methods=['GET'])
def get_all_students():
    try:
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching students.", "details": str(e)}), 500

# Route to update a student's skill levels
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student_skills(student_id):
    try:
        if student_id not in students:
            return jsonify({"error": "Student not found."}), 404
        
        data = request.json
        if "skills" not in data or not isinstance(data["skills"], dict):
            return jsonify({"error": "Missing or invalid 'skills'."}), 400
        
        for skill, value in data["skills"].items():
            if not isinstance(skill, str) or not isinstance(value, int) or value < 0 or value > 100:
                return jsonify({"error": f"Invalid skill data for '{skill}'. Ensure skill names are strings and values are integers (0-100)."}), 400
            
            students[student_id]["skills"][skill] = value
        
        return jsonify({"message": "Student skills updated successfully."}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while updating student skills.", "details": str(e)}), 500

# Route to delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        if student_id not in students:
            return jsonify({"error": "Student not found."}), 404
        
        del students[student_id]
        return jsonify({"message": "Student deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while deleting the student.", "details": str(e)}), 500

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running."}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
