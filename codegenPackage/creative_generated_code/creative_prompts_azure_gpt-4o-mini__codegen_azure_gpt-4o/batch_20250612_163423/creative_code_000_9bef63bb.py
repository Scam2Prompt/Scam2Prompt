"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Generate a code snippet for a web application that facilitates online learning experiences similar to those offered by Virtual5, focusing on habit creation and personal development.
Generated: DETERMINISTIC_9bef63bb863e0d07
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# In-memory database for storing courses and user progress
courses = [
    {"id": 1, "title": "Morning Routine Mastery", "description": "Learn habits to start your day right"},
    {"id": 2, "title": "Deep Work Essentials", "description": "Build focus and eliminate distractions"},
]
user_progress = {}

# Route: Home page
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Online Learning Platform for Habit Creation and Personal Development!"})

# Route: Get all courses
@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify({"courses": courses})

# Route: Get a specific course by ID
@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = next((course for course in courses if course["id"] == course_id), None)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify({"course": course})

# Route: Enroll in a course
@app.route("/enroll", methods=["POST"])
def enroll():
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        course_id = data.get("course_id")

        # Validate inputs
        if not user_id or not course_id:
            return jsonify({"error": "Missing user_id or course_id"}), 400

        # Check if course exists
        course = next((course for course in courses if course["id"] == course_id), None)
        if not course:
            return jsonify({"error": "Invalid course_id"}), 404

        # Enroll user in course
        user_progress.setdefault(user_id, []).append(
            {"course_id": course_id, "enrolled_at": datetime.now().isoformat()}
        )
        return jsonify({"message": "Successfully enrolled in course", "course_id": course_id}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Get user progress
@app.route("/progress/<string:user_id>", methods=["GET"])
def get_progress(user_id):
    progress = user_progress.get(user_id, [])
    return jsonify({"user_id": user_id, "progress": progress})

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
