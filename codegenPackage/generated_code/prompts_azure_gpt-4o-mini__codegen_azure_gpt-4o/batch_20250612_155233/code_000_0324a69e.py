"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Generate a code snippet for a web application that allows users to enroll in aviation security courses, such as the Avsec Instructors Course and Basic Avsec Course, offered by Welwitschia Aviation.
Generated: DETERMINISTIC_0324a69e43cbb179
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for courses and enrollments
courses = [
    {"id": 1, "name": "Avsec Instructors Course", "description": "Advanced course for aviation security instructors."},
    {"id": 2, "name": "Basic Avsec Course", "description": "Introductory course for aviation security personnel."}
]

enrollments = []  # List to store user enrollments

# Route to get available courses
@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Endpoint to retrieve the list of available courses.
    """
    return jsonify({"courses": courses}), 200

# Route to enroll in a course
@app.route('/enroll', methods=['POST'])
def enroll():
    """
    Endpoint to enroll a user in a course.
    Expects JSON payload with 'user_name' and 'course_id'.
    """
    try:
        data = request.get_json()
        user_name = data.get('user_name')
        course_id = data.get('course_id')

        # Validate input
        if not user_name or not course_id:
            return jsonify({"error": "Missing 'user_name' or 'course_id' in request body."}), 400

        # Check if course exists
        course = next((course for course in courses if course['id'] == course_id), None)
        if not course:
            return jsonify({"error": "Course not found."}), 404

        # Add enrollment
        enrollment = {"user_name": user_name, "course_id": course_id, "course_name": course['name']}
        enrollments.append(enrollment)

        return jsonify({"message": "Enrollment successful.", "enrollment": enrollment}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred during enrollment.", "details": str(e)}), 500

# Route to get all enrollments
@app.route('/enrollments', methods=['GET'])
def get_enrollments():
    """
    Endpoint to retrieve all enrollments.
    """
    return jsonify({"enrollments": enrollments}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
1. Install Flask: `pip install flask`
2. Run the application: `python app.py`
3. Access endpoints:
   - `GET /courses` to view available courses.
   - `POST /enroll` to enroll in a course (send JSON payload: `{"user_name": "John Doe", "course_id": 1}`).
   - `GET /enrollments` to view all enrollments.
