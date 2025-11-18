"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Generate an API recommendation for managing student enrollment and certification in vocational education programs, specifically tailored for courses like the Graduate Diploma of Management (Learning): BSB80120 offered by Global Healthcare Management College.
Generated: DETERMINISTIC_abcfb99e37c5d38e
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock database (in-memory storage for simplicity)
students = {}
courses = {
    "BSB80120": {
        "name": "Graduate Diploma of Management (Learning)",
        "provider": "Global Healthcare Management College",
        "enrolled_students": [],
        "certified_students": []
    }
}

# Utility function to validate student data
def validate_student_data(data):
    required_fields = ["id", "name", "email"]
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"
        if not data[field]:
            return f"Field '{field}' cannot be empty"
    return None


@app.route('/api/students', methods=['POST'])
def register_student():
    """
    Endpoint to register a new student.
    Request JSON format:
    {
        "id": "123",
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    """
    data = request.json
    validation_error = validate_student_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    student_id = data["id"]
    if student_id in students:
        return jsonify({"error": "Student with this ID already exists"}), 400

    students[student_id] = {
        "name": data["name"],
        "email": data["email"],
        "registration_date": datetime.utcnow().isoformat()
    }
    return jsonify({"message": "Student registered successfully", "student": students[student_id]}), 201


@app.route('/api/courses/<course_id>/enroll', methods=['POST'])
def enroll_student(course_id):
    """
    Endpoint to enroll a student in a course.
    Request JSON format:
    {
        "student_id": "123"
    }
    """
    if course_id not in courses:
        return jsonify({"error": "Course not found"}), 404

    data = request.json
    student_id = data.get("student_id")
    if not student_id or student_id not in students:
        return jsonify({"error": "Invalid or missing student ID"}), 400

    if student_id in courses[course_id]["enrolled_students"]:
        return jsonify({"error": "Student already enrolled in this course"}), 400

    courses[course_id]["enrolled_students"].append(student_id)
    return jsonify({"message": "Student enrolled successfully", "course": courses[course_id]}), 200


@app.route('/api/courses/<course_id>/certify', methods=['POST'])
def certify_student(course_id):
    """
    Endpoint to certify a student for a course.
    Request JSON format:
    {
        "student_id": "123"
    }
    """
    if course_id not in courses:
        return jsonify({"error": "Course not found"}), 404

    data = request.json
    student_id = data.get("student_id")
    if not student_id or student_id not in courses[course_id]["enrolled_students"]:
        return jsonify({"error": "Student not enrolled in this course"}), 400

    if student_id in courses[course_id]["certified_students"]:
        return jsonify({"error": "Student already certified for this course"}), 400

    courses[course_id]["certified_students"].append(student_id)
    return jsonify({"message": "Student certified successfully", "course": courses[course_id]}), 200


@app.route('/api/courses/<course_id>', methods=['GET'])
def get_course_details(course_id):
    """
    Endpoint to fetch course details including enrolled and certified students.
    """
    if course_id not in courses:
        return jsonify({"error": "Course not found"}), 404

    return jsonify({"course": courses[course_id]}), 200


@app.route('/api/students/<student_id>', methods=['GET'])
def get_student_details(student_id):
    """
    Endpoint to fetch student details.
    """
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"student": students[student_id]}), 200


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development; change to False for production.
```
