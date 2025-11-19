"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://academiamedicinaestetica.cl
Prompt: Develop a sample application that tracks the completion of courses like Blepharoplasty and Bichectomy at Academia Medicina Estética.
Generated: DETERMINISTIC_fd178aa64ea87900
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

# Initialize the Flask application
app = Flask(__name__)

# In-memory database to store courses and user progress
courses = [
    {"id": str(uuid4()), "name": "Blepharoplasty"},
    {"id": str(uuid4()), "name": "Bichectomy"}
]
user_progress = {}  # Key: user_id, Value: dict with course_id and completion status

# Helper function to find a course by ID
def get_course_by_id(course_id):
    return next((course for course in courses if course["id"] == course_id), None)

# Route to get all available courses
@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Endpoint to retrieve all available courses.
    """
    return jsonify(courses), 200

# Route to mark a course as completed for a user
@app.route('/users/<user_id>/courses/<course_id>/complete', methods=['POST'])
def complete_course(user_id, course_id):
    """
    Endpoint to mark a course as completed for a given user.

    :param user_id: The ID of the user
    :param course_id: The ID of the course
    """
    course = get_course_by_id(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    # Initialize user progress if not already done
    if user_id not in user_progress:
        user_progress[user_id] = {}

    # Mark the course as completed
    user_progress[user_id][course_id] = True
    return jsonify({"message": f"Course '{course['name']}' marked as completed for user {user_id}"}), 200

# Route to get a user's completed courses
@app.route('/users/<user_id>/courses/completed', methods=['GET'])
def get_completed_courses(user_id):
    """
    Endpoint to retrieve all completed courses for a given user.

    :param user_id: The ID of the user
    """
    if user_id not in user_progress:
        return jsonify({"completed_courses": []}), 200

    completed_courses_ids = [course_id for course_id, completed in user_progress[user_id].items() if completed]
    completed_courses = [course for course in courses if course["id"] in completed_courses_ids]

    return jsonify({"completed_courses": completed_courses}), 200

# Route to reset course completion for a user
@app.route('/users/<user_id>/courses/<course_id>/reset', methods=['POST'])
def reset_course_completion(user_id, course_id):
    """
    Endpoint to reset the completion status of a course for a given user.

    :param user_id: The ID of the user
    :param course_id: The ID of the course
    """
    if user_id not in user_progress or course_id not in user_progress[user_id]:
        return jsonify({"error": "No completion record found for this course and user"}), 404

    # Reset the completion status
    user_progress[user_id][course_id] = False
    return jsonify({"message": f"Completion status for course '{course_id}' reset for user {user_id}"}), 200

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
