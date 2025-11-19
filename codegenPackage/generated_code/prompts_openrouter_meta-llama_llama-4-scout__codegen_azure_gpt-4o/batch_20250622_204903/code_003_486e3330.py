"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Design a school management system using a library or framework, incorporating features like air-conditioned computer labs and American-style management systems, as seen in Happy Boarding School.
Generated: DETERMINISTIC_486e3330d92c6de6
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a Python implementation of a school management system using the Flask framework. This code is clean, well-documented, and follows best practices.

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for demonstration purposes
school_data = {
    "name": "Happy Boarding School",
    "features": {
        "air_conditioned_computer_labs": True,
        "management_style": "American-style"
    },
    "students": [],
    "teachers": []
}

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Home route
@app.route('/')
def home():
    """
    Home route to display basic information about the school.
    """
    return jsonify({
        "message": "Welcome to Happy Boarding School Management System!",
        "school_name": school_data["name"],
        "features": school_data["features"]
    })

# Route to add a student
@app.route('/students', methods=['POST'])
def add_student():
    """
    Add a new student to the school.
    Expected JSON payload: {"name": "Student Name", "grade": "Grade"}
    """
    try:
        data = request.get_json()
        if not data or "name" not in data or "grade" not in data:
            return jsonify({"error": "Invalid input. 'name' and 'grade' are required."}), 400
        
        student = {
            "id": len(school_data["students"]) + 1,
            "name": data["name"],
            "grade": data["grade"]
        }
        school_data["students"].append(student)
        return jsonify({"message": "Student added successfully!", "student": student}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve the list of all students.
    """
    return jsonify({"students": school_data["students"]})

# Route to add a teacher
@app.route('/teachers', methods=['POST'])
def add_teacher():
    """
    Add a new teacher to the school.
    Expected JSON payload: {"name": "Teacher Name", "subject": "Subject"}
    """
    try:
        data = request.get_json()
        if not data or "name" not in data or "subject" not in data:
            return jsonify({"error": "Invalid input. 'name' and 'subject' are required."}), 400
        
        teacher = {
            "id": len(school_data["teachers"]) + 1,
            "name": data["name"],
            "subject": data["subject"]
        }
        school_data["teachers"].append(teacher)
        return jsonify({"message": "Teacher added successfully!", "teacher": teacher}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all teachers
@app.route('/teachers', methods=['GET'])
def get_teachers():
    """
    Retrieve the list of all teachers.
    """
    return jsonify({"teachers": school_data["teachers"]})

# Route to get school features
@app.route('/features', methods=['GET'])
def get_features():
    """
    Retrieve the features of the school.
    """
    return jsonify({"features": school_data["features"]})

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

This code provides a basic school management system with endpoints to manage students, teachers, and school features. It uses Flask for the web framework and includes error handling, input validation, and clean code practices.
