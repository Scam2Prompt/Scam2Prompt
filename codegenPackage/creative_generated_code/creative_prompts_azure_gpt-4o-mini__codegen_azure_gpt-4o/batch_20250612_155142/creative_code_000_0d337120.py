"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Generate a code snippet for a web application that allows users to register for gliding courses at the AAVE club, including fields for personal information and course selection.
Generated: DETERMINISTIC_0d337120df47efb4
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for user registration at the AAVE Gliding Club

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data for available courses
AVAILABLE_COURSES = [
    {"id": 1, "name": "Beginner Gliding", "description": "Learn the basics of gliding."},
    {"id": 2, "name": "Intermediate Gliding", "description": "Enhance your gliding skills."},
    {"id": 3, "name": "Advanced Gliding", "description": "Master advanced gliding techniques."},
]

# Store registered users - In production, replace this with a database
registered_users = []


@app.route("/courses", methods=["GET"])
def get_courses():
    """
    Endpoint to fetch available gliding courses.
    Returns:
        JSON list of courses.
    """
    return jsonify({"courses": AVAILABLE_COURSES}), 200


@app.route("/register", methods=["POST"])
def register():
    """
    Endpoint to register a user for a gliding course.
    Expects JSON payload with name, email, phone, and course_id.
    """
    try:
        # Parse and validate request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        course_id = data.get("course_id")

        if not all([name, email, phone, course_id]):
            return jsonify({"error": "Missing required fields"}), 400

        # Ensure course_id is valid
        course = next((course for course in AVAILABLE_COURSES if course["id"] == course_id), None)
        if not course:
            return jsonify({"error": "Invalid course ID"}), 400

        # Register the user
        user = {
            "name": name,
            "email": email,
            "phone": phone,
            "course_id": course_id,
            "course_name": course["name"],
        }
        registered_users.append(user)

        return jsonify({"message": "User successfully registered", "user": user}), 201

    except HTTPException as e:
        # Handle HTTP exceptions
        return jsonify({"error": str(e)}), e.code
    except Exception as e:
        # Catch-all error handler
        return jsonify({"error": "An error occurred while registering the user"}), 500


@app.route("/registrations", methods=["GET"])
def view_registrations():
    """
    Endpoint to view all registered users.
    Returns:
        JSON list of registered users.
    """
    return jsonify({"registrations": registered_users}), 200


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
