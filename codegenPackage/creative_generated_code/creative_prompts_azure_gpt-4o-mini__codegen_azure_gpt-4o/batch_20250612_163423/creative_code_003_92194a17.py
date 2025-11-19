"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Create an API endpoint for a virtual training platform that allows users to enroll in courses focused on personal and organizational change, as highlighted by Virtual5.
Generated: DETERMINISTIC_92194a17179dd69d
Batch ID: 20250612_163423
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
import uuid

app = Flask(__name__)

# In-memory storage for simplicity (use a database in production)
courses = [
    {"id": "course1", "name": "Personal Change Basics", "description": "Learn the fundamentals of personal change."},
    {"id": "course2", "name": "Organizational Change 101", "description": "Understand how to drive change in organizations."}
]
enrollments = []  # List to track user course enrollments

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Error handler to catch all exceptions and return clean JSON responses.
    """
    if isinstance(e, HTTPException):
        return jsonify(error=str(e), code=e.code), e.code
    return jsonify(error="An unexpected error occurred", code=500), 500

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    Endpoint to retrieve the list of available courses.
    """
    return jsonify(courses=courses), 200

@app.route('/api/enroll', methods=['POST'])
def enroll_in_course():
    """
    Endpoint to enroll a user in a course.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data:
            return jsonify(error="Missing JSON payload"), 400

        user_id = data.get('user_id')
        course_id = data.get('course_id')

        # Validate user_id and course_id
        if not user_id:
            return jsonify(error="Missing 'user_id'"), 400
        if not course_id:
            return jsonify(error="Missing 'course_id'"), 400

        # Check if the course exists
        course = next((c for c in courses if c['id'] == course_id), None)
        if not course:
            return jsonify(error="Invalid course ID"), 404

        # Check if the user is already enrolled
        existing_enrollment = next((e for e in enrollments if e['user_id'] == user_id and e['course_id'] == course_id), None)
        if existing_enrollment:
            return jsonify(error="User is already enrolled in this course"), 409

        # Create enrollment record
        enrollment = {
            "id": str(uuid.uuid4()),  # Unique enrollment ID
            "user_id": user_id,
            "course_id": course_id
        }
        enrollments.append(enrollment)

        return jsonify(message="Enrollment successful", enrollment=enrollment), 201

    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify(error="An unexpected error occurred", details=str(e)), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
