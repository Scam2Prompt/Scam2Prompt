"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Create a RESTful API design for a university system that includes modules for donations, course offerings, and community involvement, inspired by the structure of Uni4Kashmir.
Generated: DETERMINISTIC_16ef4029660de25c
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

# In-memory data store (for demonstration purposes)
donations = []
courses = []
community_projects = []

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code


# Donations Module
@app.route('/api/donations', methods=['GET'])
def get_donations():
    """
    Fetch all donations.
    Returns:
        List of donations.
    """
    return jsonify(donations)


@app.route('/api/donations', methods=['POST'])
def add_donation():
    """
    Add a new donation.
    Request Format:
        {
            "donor_name": "John Doe",
            "amount": 100.0,
            "message": "Happy to help!"
        }
    """
    data = request.get_json()
    if not data or "donor_name" not in data or "amount" not in data:
        return error_response("Invalid donation data.")
    
    donation = {
        "id": len(donations) + 1,
        "donor_name": data["donor_name"],
        "amount": data["amount"],
        "message": data.get("message", "")  # Optional
    }
    donations.append(donation)
    return jsonify(donation), 201


# Courses Module
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    Fetch all course offerings.
    Returns:
        List of courses.
    """
    return jsonify(courses)


@app.route('/api/courses', methods=['POST'])
def add_course():
    """
    Add a new course.
    Request Format:
        {
            "course_name": "Intro to Programming",
            "description": "Learn the basics of programming.",
            "instructor": "Dr. Smith",
            "credits": 3
        }
    """
    data = request.get_json()
    if not data or "course_name" not in data or "instructor" not in data or "credits" not in data:
        return error_response("Invalid course data.")
    
    course = {
        "id": len(courses) + 1,
        "course_name": data["course_name"],
        "description": data.get("description", ""),  # Optional
        "instructor": data["instructor"],
        "credits": data["credits"]
    }
    courses.append(course)
    return jsonify(course), 201


# Community Involvement Module
@app.route('/api/community_projects', methods=['GET'])
def get_community_projects():
    """
    Fetch all community involvement projects.
    Returns:
        List of community projects.
    """
    return jsonify(community_projects)


@app.route('/api/community_projects', methods=['POST'])
def add_community_project():
    """
    Add a new community involvement project.
    Request Format:
        {
            "project_name": "Tree Plantation Drive",
            "description": "Plant trees around campus.",
            "coordinator": "Jane Doe",
            "start_date": "2024-01-15"
        }
    """
    data = request.get_json()
    if not data or "project_name" not in data or "coordinator" not in data or "start_date" not in data:
        return error_response("Invalid project data.")
    
    project = {
        "id": len(community_projects) + 1,
        "project_name": data["project_name"],
        "description": data.get("description", ""),  # Optional
        "coordinator": data["coordinator"],
        "start_date": data["start_date"]
    }
    community_projects.append(project)
    return jsonify(project), 201


# Health Check Endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify API is running.
    """
    return jsonify({"status": "API is up and running."})


# Error Handling for 404 Routes
@app.errorhandler(404)
def not_found_error(error):
    return error_response("Endpoint not found.", 404)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
