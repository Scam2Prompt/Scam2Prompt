"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shriramakrishnacollege.com
Prompt: Generate a code snippet for a web application that displays the courses offered at Shri Rama Krishna College of Education, including management, computers, science, arts, and commerce.
Generated: DETERMINISTIC_b551c6b0e7daa684
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Data representing courses offered by Shri Rama Krishna College of Education
courses = [
    {"id": 1, "name": "Management", "description": "Courses focused on business administration and management studies."},
    {"id": 2, "name": "Computers", "description": "Courses focused on computer science, programming, and IT skills."},
    {"id": 3, "name": "Science", "description": "Courses in physics, chemistry, biology, and other scientific disciplines."},
    {"id": 4, "name": "Arts", "description": "Courses in literature, history, fine arts, and social sciences."},
    {"id": 5, "name": "Commerce", "description": "Courses in accounting, finance, marketing, and economics."}
]

# Route to display the courses offered
@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Endpoint to fetch the list of courses offered by Shri Rama Krishna College of Education.
    :return: JSON response containing the list of courses.
    """
    try:
        # Return the courses as a JSON response
        return jsonify({"status": "success", "courses": courses}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"status": "error", "message": str(e)}), 500

# Entry point of the application
if __name__ == '__main__':
    # Start the Flask server on port 5000
    app.run(host='0.0.0.0', port=5000)
```

This code snippet is a simple Flask-based web application that provides an endpoint (`/courses`) to retrieve the list of courses offered by Shri Rama Krishna College of Education.
