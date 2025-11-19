"""
Generated Code Metadata:
========================
Original URL: https://ictea.edu.mx
Prompt: Develop a basic example of how to implement a course catalog using a RESTful API.
Generated: DETERMINISTIC_ab009d1dc75f06e2
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for courses
courses = [
    {"id": 1, "name": "Introduction to Programming", "description": "Learn the basics of programming.", "credits": 3},
    {"id": 2, "name": "Data Structures", "description": "Understand how data is organized and manipulated.", "credits": 4},
]

# Helper function to find a course by ID
def find_course(course_id):
    return next((course for course in courses if course["id"] == course_id), None)

# Route: Get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Returns a list of all courses.
    """
    return jsonify(courses), 200

# Route: Get a specific course by ID
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Returns a specific course by its ID.
    """
    course = find_course(course_id)
    if course:
        return jsonify(course), 200
    return jsonify({"error": "Course not found"}), 404

# Route: Add a new course
@app.route('/courses', methods=['POST'])
def add_course():
    """
    Adds a new course to the catalog.
    Expects JSON payload with 'name', 'description', and 'credits'.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "description", "credits")):
            return jsonify({"error": "Invalid input"}), 400

        new_course = {
            "id": max(course["id"] for course in courses) + 1 if courses else 1,
            "name": data["name"],
            "description": data["description"],
            "credits": data["credits"],
        }
        courses.append(new_course)
        return jsonify(new_course), 201
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Route: Update an existing course
@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Updates an existing course by its ID.
    Expects JSON payload with 'name', 'description', and 'credits'.
    """
    course = find_course(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "description", "credits")):
            return jsonify({"error": "Invalid input"}), 400

        course.update({
            "name": data["name"],
            "description": data["description"],
            "credits": data["credits"],
        })
        return jsonify(course), 200
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Route: Delete a course
@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Deletes a course by its ID.
    """
    course = find_course(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    courses.remove(course)
    return jsonify({"message": "Course deleted successfully"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
