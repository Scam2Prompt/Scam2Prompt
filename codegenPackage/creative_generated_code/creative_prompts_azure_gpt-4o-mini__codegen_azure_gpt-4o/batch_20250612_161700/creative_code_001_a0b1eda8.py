"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Generate a code snippet for an API that provides online security training courses, similar to those offered by Blue Training Academy.
Generated: DETERMINISTIC_a0b1eda8d47c9bfc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing online security training courses
courses = [
    {
        "id": 1,
        "title": "Introduction to Cybersecurity",
        "description": "A beginner-friendly guide to the fundamentals of cybersecurity.",
        "duration": "2 hours",
        "difficulty": "Beginner"
    },
    {
        "id": 2,
        "title": "Advanced Network Security",
        "description": "Learn how to secure complex networks and prevent advanced threats.",
        "duration": "4 hours",
        "difficulty": "Advanced"
    },
    {
        "id": 3,
        "title": "Application Security Basics",
        "description": "Understand how to secure web and mobile applications.",
        "duration": "3 hours",
        "difficulty": "Intermediate"
    }
]

@app.route("/api/courses", methods=["GET"])
def get_courses():
    """
    API endpoint to retrieve all security training courses.
    Returns:
        JSON object containing a list of all available courses.
    """
    return jsonify({"courses": courses}), 200


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course_by_id(course_id):
    """
    API endpoint to retrieve a single course by its ID.
    Args:
        course_id (int): ID of the course to retrieve.
    Returns:
        JSON object containing the course details if found, or a 404 error if not found.
    """
    course = next((course for course in courses if course["id"] == course_id), None)
    if course:
        return jsonify(course), 200
    else:
        return jsonify({"error": "Course not found"}), 404


@app.route("/api/courses", methods=["POST"])
def add_course():
    """
    API endpoint to add a new course.
    Request JSON body must include 'title', 'description', 'duration', and 'difficulty'.
    Returns:
        JSON object containing the newly created course details.
    """
    try:
        data = request.get_json()
        # Validate required fields
        required_fields = ["title", "description", "duration", "difficulty"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new course
        new_course = {
            "id": len(courses) + 1,
            "title": data["title"],
            "description": data["description"],
            "duration": data["duration"],
            "difficulty": data["difficulty"]
        }
        courses.append(new_course)
        return jsonify(new_course), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    """
    API endpoint to delete a course by its ID.
    Args:
        course_id (int): ID of the course to delete.
    Returns:
        JSON object confirming the deletion or a 404 error if not found.
    """
    global courses
    course = next((course for course in courses if course["id"] == course_id), None)
    if course:
        courses = [course for course in courses if course["id"] != course_id]
        return jsonify({"message": "Course deleted successfully"}), 200
    else:
        return jsonify({"error": "Course not found"}), 404


if __name__ == "__main__":
    # Start the Flask app
    app.run(debug=True)
```
