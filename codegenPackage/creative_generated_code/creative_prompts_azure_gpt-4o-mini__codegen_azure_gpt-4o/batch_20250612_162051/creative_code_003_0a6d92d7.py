"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unimeleducacion.org
Prompt: Create a REST API that allows users to enroll in online courses like the "Máster Universitario en Educación Bilingüe" from Unimel Educación.
Generated: DETERMINISTIC_0a6d92d718f9e813
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import uuid

# Initialize Flask app
app = Flask(__name__)

# Mock database for courses and enrollments
courses = [
    {"id": "1", "name": "Máster Universitario en Educación Bilingüe", "provider": "Unimel Educación"}
]
enrollments = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions with structured JSON response."""
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).data
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle unexpected exceptions."""
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500

@app.route("/courses", methods=["GET"])
def get_courses():
    """
    GET /courses
    Returns a list of all available courses.
    """
    return jsonify({"courses": courses}), 200

@app.route("/enroll", methods=["POST"])
def enroll_in_course():
    """
    POST /enroll
    Enrolls a user in a course.
    Expects JSON data with 'course_id' and 'user_name'.
    """
    data = request.get_json()

    # Validate input data
    if not data or "course_id" not in data or "user_name" not in data:
        return jsonify({"error": "Bad Request", "message": "Missing 'course_id' or 'user_name'"}), 400

    course_id = data["course_id"]
    user_name = data["user_name"]

    # Check if the requested course exists
    course = next((course for course in courses if course["id"] == course_id), None)
    if not course:
        return jsonify({"error": "Not Found", "message": "Course not found"}), 404

    # Create enrollment record
    enrollment_id = str(uuid.uuid4())
    enrollment = {
        "id": enrollment_id,
        "course_id": course_id,
        "course_name": course["name"],
        "user_name": user_name
    }
    enrollments.append(enrollment)

    return jsonify({"message": "Enrollment successful", "enrollment": enrollment}), 201

@app.route("/enrollments", methods=["GET"])
def get_enrollments():
    """
    GET /enrollments
    Returns a list of all enrollments.
    """
    return jsonify({"enrollments": enrollments}), 200

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=False)  # Set debug to False for production
```
