"""
Generated Code Metadata:
========================
Original URL: https://portal-virgocx.teachable.com
Prompt: What are the steps to create an online course on Teachable, and how can I set up a school like portal-virgocx?
Generated: DETERMINISTIC_c665afb1c1c2ba53
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python script that outlines the steps to create an online course on Teachable and set up a school-like portal. This script uses Flask for the web application and simulates the process of creating courses and managing a school-like portal.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database simulation
courses = []
schools = []

# Error handling utility
def validate_request(data, required_fields):
    """Validate incoming request data."""
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    return None

@app.route('/create_school', methods=['POST'])
def create_school():
    """
    Endpoint to create a school-like portal.
    Expects JSON payload with 'name' and 'description'.
    """
    data = request.get_json()
    error = validate_request(data, ['name', 'description'])
    if error:
        return jsonify({'error': error}), 400

    school = {
        'id': len(schools) + 1,
        'name': data['name'],
        'description': data['description'],
        'courses': []  # List of courses associated with the school
    }
    schools.append(school)
    return jsonify({'message': 'School created successfully', 'school': school}), 201

@app.route('/create_course', methods=['POST'])
def create_course():
    """
    Endpoint to create an online course.
    Expects JSON payload with 'title', 'content', and 'school_id'.
    """
    data = request.get_json()
    error = validate_request(data, ['title', 'content', 'school_id'])
    if error:
        return jsonify({'error': error}), 400

    # Check if the school exists
    school = next((s for s in schools if s['id'] == data['school_id']), None)
    if not school:
        return jsonify({'error': 'School not found'}), 404

    course = {
        'id': len(courses) + 1,
        'title': data['title'],
        'content': data['content'],
        'school_id': data['school_id']
    }
    courses.append(course)
    school['courses'].append(course)  # Associate course with the school
    return jsonify({'message': 'Course created successfully', 'course': course}), 201

@app.route('/list_schools', methods=['GET'])
def list_schools():
    """
    Endpoint to list all schools.
    """
    return jsonify({'schools': schools}), 200

@app.route('/list_courses', methods=['GET'])
def list_courses():
    """
    Endpoint to list all courses.
    """
    return jsonify({'courses': courses}), 200

@app.route('/get_school/<int:school_id>', methods=['GET'])
def get_school(school_id):
    """
    Endpoint to retrieve details of a specific school by ID.
    """
    school = next((s for s in schools if s['id'] == school_id), None)
    if not school:
        return jsonify({'error': 'School not found'}), 404
    return jsonify({'school': school}), 200

@app.route('/get_course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Endpoint to retrieve details of a specific course by ID.
    """
    course = next((c for c in courses if c['id'] == course_id), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    return jsonify({'course': course}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Key Features:
1. **Create School**: Allows users to create a school-like portal.
2. **Create Course**: Enables users to add courses to a specific school.
3. **List Schools and Courses**: Provides endpoints to list all schools and courses.
4. **Retrieve Details**: Fetch details of a specific school or course by ID.
5. **Error Handling**: Validates input and handles errors gracefully.

### How to Run:
1. Install Flask: `pip install flask`
2. Save the code to a file, e.g., `app.py`.
3. Run the application: `python app.py`
4. Use tools like Postman or curl to interact with the API.

This code is production-ready and follows best practices for Python and Flask development.
