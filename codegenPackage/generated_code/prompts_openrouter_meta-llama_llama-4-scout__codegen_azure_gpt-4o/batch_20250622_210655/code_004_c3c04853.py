"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Design a RESTful API for managing Agile course enrollments, including endpoints for subscribing to courses and tracking student progress.
Generated: DETERMINISTIC_c3c04853b759cd34
Batch ID: 20250622_210655
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
courses = {
    1: {"name": "Agile Basics", "students": {}},
    2: {"name": "Advanced Agile Practices", "students": {}},
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": str(e)}), 500

# Endpoint to list all courses
@app.route('/courses', methods=['GET'])
def list_courses():
    return jsonify(courses)

# Endpoint to subscribe a student to a course
@app.route('/courses/<int:course_id>/subscribe', methods=['POST'])
def subscribe_to_course(course_id):
    if course_id not in courses:
        return jsonify({"error": "Course not found"}), 404

    data = request.json
    if not data or 'student_id' not in data or 'student_name' not in data:
        return jsonify({"error": "Invalid request payload"}), 400

    student_id = data['student_id']
    student_name = data['student_name']

    if student_id in courses[course_id]['students']:
        return jsonify({"error": "Student already subscribed"}), 400

    courses[course_id]['students'][student_id] = {
        "name": student_name,
        "progress": 0
    }

    return jsonify({"message": "Student subscribed successfully"}), 201

# Endpoint to update student progress
@app.route('/courses/<int:course_id>/students/<int:student_id>/progress', methods=['PUT'])
def update_progress(course_id, student_id):
    if course_id not in courses:
        return jsonify({"error": "Course not found"}), 404

    if student_id not in courses[course_id]['students']:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    if not data or 'progress' not in data:
        return jsonify({"error": "Invalid request payload"}), 400

    progress = data['progress']
    if not isinstance(progress, int) or progress < 0 or progress > 100:
        return jsonify({"error": "Progress must be an integer between 0 and 100"}), 400

    courses[course_id]['students'][student_id]['progress'] = progress

    return jsonify({"message": "Progress updated successfully"}), 200

# Endpoint to get student progress
@app.route('/courses/<int:course_id>/students/<int:student_id>/progress', methods=['GET'])
def get_progress(course_id, student_id):
    if course_id not in courses:
        return jsonify({"error": "Course not found"}), 404

    if student_id not in courses[course_id]['students']:
        return jsonify({"error": "Student not found"}), 404

    student_progress = courses[course_id]['students'][student_id]['progress']
    return jsonify({"progress": student_progress}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
