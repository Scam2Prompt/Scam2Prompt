"""
Generated Code Metadata:
========================
Original URL: https://immediate-gains.com
Prompt: Develop a simple e-learning platform using Python libraries, incorporating features for risk management and awareness in investment education.
Generated: DETERMINISTIC_241fadcacdfd37c5
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
E-Learning Platform for Investment Education with Risk Management Awareness
Author: Expert Programmer
Date: YYYY-MM-DD
"""

import os
import json
from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Load course data (mock data for demonstration purposes)
COURSES_FILE = "courses.json"
if not os.path.exists(COURSES_FILE):
    # Create a sample courses file if it doesn't exist
    sample_courses = [
        {
            "id": 1,
            "title": "Introduction to Investment",
            "description": "Learn the basics of investing and financial markets.",
            "risk_level": "Low",
            "content": "This course covers fundamental concepts of investing..."
        },
        {
            "id": 2,
            "title": "Risk Management Strategies",
            "description": "Understand how to manage risks in your investment portfolio.",
            "risk_level": "Medium",
            "content": "This course explores various risk management techniques..."
        },
        {
            "id": 3,
            "title": "Advanced Investment Techniques",
            "description": "Dive deep into advanced strategies for maximizing returns.",
            "risk_level": "High",
            "content": "This course focuses on high-risk, high-reward strategies..."
        }
    ]
    with open(COURSES_FILE, "w") as f:
        json.dump(sample_courses, f, indent=4)

# Helper function to load courses
def load_courses():
    try:
        with open(COURSES_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        app.logger.error(f"Error loading courses: {e}")
        return []

# Route: Home page
@app.route("/")
def home():
    return render_template("index.html", title="E-Learning Platform")

# Route: Get all courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = load_courses()
    return jsonify(courses), 200

# Route: Get course by ID
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    courses = load_courses()
    course = next((c for c in courses if c["id"] == course_id), None)
    if course:
        return jsonify(course), 200
    return jsonify({"error": "Course not found"}), 404

# Route: Add a new course
@app.route("/api/courses", methods=["POST"])
def add_course():
    try:
        new_course = request.json
        if not new_course.get("title") or not new_course.get("description"):
            return jsonify({"error": "Invalid course data"}), 400

        courses = load_courses()
        new_course["id"] = max(c["id"] for c in courses) + 1 if courses else 1
        courses.append(new_course)

        with open(COURSES_FILE, "w") as f:
            json.dump(courses, f, indent=4)

        return jsonify(new_course), 201
    except Exception as e:
        app.logger.error(f"Error adding course: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Route: Delete a course by ID
@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    try:
        courses = load_courses()
        course = next((c for c in courses if c["id"] == course_id), None)
        if not course:
            return jsonify({"error": "Course not found"}), 404

        courses = [c for c in courses if c["id"] != course_id]
        with open(COURSES_FILE, "w") as f:
            json.dump(courses, f, indent=4)

        return jsonify({"message": "Course deleted successfully"}), 200
    except Exception as e:
        app.logger.error(f"Error deleting course: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "error": e.name,
        "message": e.description
    })
    response.content_type = "application/json"
    return response

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Unexpected error: {e}")
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

**Note:** This code assumes the presence of a `templates/index.html` file for the home page. You can create this file with basic HTML content to display the platform's welcome message.
