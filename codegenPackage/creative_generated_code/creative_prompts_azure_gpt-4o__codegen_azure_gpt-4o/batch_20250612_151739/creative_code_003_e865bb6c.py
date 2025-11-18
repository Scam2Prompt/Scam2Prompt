"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Develop a web-based application to manage admissions for aviation security courses, incorporating features for course selection such as "Basic Avsec Course" and "Avsec Management Course."
Generated: DETERMINISTIC_e865bb6c525fc4bd
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database to store course and student information
# In production, replace with a proper database like MySQL, PostgreSQL, or MongoDB
courses = [
    {"id": 1, "name": "Basic Avsec Course", "description": "Introduction to aviation security", "capacity": 30},
    {"id": 2, "name": "Avsec Management Course", "description": "Advanced aviation security management", "capacity": 20},
]

students = []  # List to store student enrollments

# Route: Fetch all available courses
@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Fetch all available aviation security courses
    :return: JSON list of courses
    """
    return jsonify({"status": "success", "data": courses}), 200

# Route: Enroll a student in a course
@app.route('/enroll', methods=['POST'])
def enroll_student():
    """
    Enroll a student in a course
    :return: Success or error message
    """
    try:
        # Validate request data
        data = request.json
        if not data or 'name' not in data or 'course_id' not in data:
            return jsonify({"status": "error", "message": "Invalid request. Name and course ID are required."}), 400

        # Check if course exists
        course = next((c for c in courses if c["id"] == data["course_id"]), None)
        if not course:
            return jsonify({"status": "error", "message": "Course not found."}), 404

        # Check course capacity
        enrolled_students = [s for s in students if s['course_id'] == course['id']]
        if len(enrolled_students) >= course['capacity']:
            return jsonify({"status": "error", "message": "Course is full."}), 400

        # Enroll the student
        student = {
            "id": len(students) + 1,
            "name": data["name"],
            "course_id": course["id"]
        }
        students.append(student)

        return jsonify({"status": "success", "message": f"{data['name']} successfully enrolled in {course['name']}."}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}), 500

# Route: View all enrolled students
@app.route('/students', methods=['GET'])
def get_students():
    """
    Fetch all enrolled students
    :return: JSON list of students
    """
    return jsonify({"status": "success", "data": students}), 200

# Error handler for 404 (not found)
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors
    :return: Error message
    """
    return jsonify({"status": "error", "message": "Resource not found."}), 404

# Error handler for 500 (internal server error)
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors
    :return: Error message
    """
    return jsonify({"status": "error", "message": "Internal server error."}), 500

# Main entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set to False for production
```
