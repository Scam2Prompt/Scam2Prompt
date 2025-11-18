"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outsource.s1soft.com
Prompt: Write a Python script for a custom web development project using outsourcing services, referencing the programming expertise offered by Special One Outsourcing in Jordan.
Generated: DETERMINISTIC_a78814a43f843ff4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Custom error handler for HTTP exceptions
@app.errorhandler(Exception)
def handle_error(e):
    response = {
        "message": str(e),
        "status": "error"
    }
    return jsonify(response), 500

# Route to create a new project request
@app.route('/api/projects', methods=['POST'])
def create_project():
    """Create a new project request for outsourcing."""
    # Get data from the request
    data = request.get_json()

    # Validate incoming data
    if not data or 'project_name' not in data or 'description' not in data:
        return jsonify({"message": "Invalid data"}), 400

    project_name = data['project_name']
    description = data['description']
    
    # Simulate saving to a database (placeholder for actual DB logic)
    # In a real application, you would connect to a database and save the project
    # db.save_project(project_name, description)
    
    # Create a response
    response = {
        "message": f"Project '{project_name}' created successfully.",
        "status": "success"
    }
    return jsonify(response), 201

# Route to fetch all project requests
@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Fetch all project requests."""
    # Simulate fetching from a database (placeholder for actual DB logic)
    projects = [
        {"project_name": "Web Development", "description": "Create a responsive website"},
        {"project_name": "Mobile App", "description": "Develop a cross-platform mobile application"}
    ]
    
    return jsonify({"projects": projects}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- To run this script, ensure you have Flask installed in your Python environment (`pip install Flask`).
- The script simulates project creation and retrieval. Replace the database simulation with actual database logic as needed.
- Ensure proper security measures are taken for production, such as input validation and authentication, which are not detailed here for brevity.
