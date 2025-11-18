"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Create a REST API endpoint for retrieving information about music courses, such as jazz improvisation and composition, offered by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_325d374bfa742ebf
Batch ID: 20250612_154351
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

# Mock data representing music courses
courses = [
    {
        "id": 1,
        "name": "Jazz Improvisation",
        "description": "Learn the art of jazz improvisation from experienced musicians.",
        "duration": "12 weeks",
        "instructor": "Ivan Petrov"
    },
    {
        "id": 2,
        "name": "Composition",
        "description": "Master the fundamentals of music composition for various genres.",
        "duration": "10 weeks",
        "instructor": "Anna Ivanova"
    }
]

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    REST API endpoint to retrieve all music courses.
    Returns a JSON object containing course information.
    """
    return jsonify({
        "status": "success",
        "data": courses
    }), 200

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    """
    REST API endpoint to retrieve a specific course by its ID.
    :param course_id: The ID of the course to retrieve.
    :return: JSON object with course information or error message if course not found.
    """
    course = next((course for course in courses if course["id"] == course_id), None)
    
    if course:
        return jsonify({
            "status": "success",
            "data": course
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Course not found"
        }), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for the Flask application.
    Handles both HTTP exceptions and other unexpected errors.
    """
    if isinstance(e, HTTPException):
        return jsonify({
            "status": "error",
            "message": e.description
        }), e.code
    else:
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred"
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
```
