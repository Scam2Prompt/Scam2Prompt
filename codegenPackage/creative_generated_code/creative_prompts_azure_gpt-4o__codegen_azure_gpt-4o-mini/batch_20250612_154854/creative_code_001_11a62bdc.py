"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://turpymobileapps.com
Prompt: Recommend a web development library or framework that aligns with Turpy Mobile Apps' focus on delivering creative web solutions blended with the latest technologies.
Generated: DETERMINISTIC_11a62bdc17cde90d
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries
from flask import Flask, jsonify, request

# Create a Flask application
app = Flask(__name__)

# Sample data for demonstration purposes
projects = [
    {"id": 1, "name": "Creative Web Solution 1", "technology": "React"},
    {"id": 2, "name": "Creative Web Solution 2", "technology": "Vue.js"},
    {"id": 3, "name": "Creative Web Solution 3", "technology": "Angular"}
]

@app.route('/projects', methods=['GET'])
def get_projects():
    """
    GET endpoint to retrieve a list of creative web solutions.
    Returns a JSON response containing the project details.
    """
    return jsonify(projects), 200

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    GET endpoint to retrieve a specific project by its ID.
    :param project_id: The ID of the project to retrieve.
    :return: JSON response containing the project details or error message.
    """
    project = next((proj for proj in projects if proj['id'] == project_id), None)
    if project:
        return jsonify(project), 200
    else:
        return jsonify({'error': 'Project not found'}), 404

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    Returns a JSON response indicating the resource was not found.
    """
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 errors.
    Returns a JSON response for internal server errors.
    """
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```
