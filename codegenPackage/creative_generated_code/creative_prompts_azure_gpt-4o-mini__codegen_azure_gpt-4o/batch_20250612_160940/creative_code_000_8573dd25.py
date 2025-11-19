"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travaux.fr.fo
Prompt: Generate a code snippet for a web application that allows users to request estimates for home renovation projects like painting, roofing, or electrical work.
Generated: DETERMINISTIC_8573dd25ba1d9927
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
projects = [
    {"id": 1, "name": "Painting"},
    {"id": 2, "name": "Roofing"},
    {"id": 3, "name": "Electrical Work"}
]

# Endpoint: Get available project types
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Returns a list of available home renovation projects.
    """
    return jsonify({"success": True, "projects": projects})

# Endpoint: Request estimate for a project
@app.route('/estimate', methods=['POST'])
def request_estimate():
    """
    Handles user requests for project estimates.
    The user must specify:
    - 'project_id': The ID of the project type.
    - 'details': Any relevant information about the project.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Invalid JSON body"}), 400

        # Validate required fields
        project_id = data.get("project_id")
        details = data.get("details")
        if not project_id or not details:
            return jsonify({"success": False, "error": "Missing required fields: 'project_id' and/or 'details'"}), 400

        # Check if the project exists
        project = next((p for p in projects if p["id"] == project_id), None)
        if not project:
            return jsonify({"success": False, "error": "Invalid project_id"}), 400

        # Simulate estimate generation logic
        estimate = f"Estimate for {project['name']}: $5000 - $15000"

        # Respond with the estimate
        return jsonify({"success": True, "estimate": estimate, "details_received": details})
    except Exception as e:
        # Generic error handling
        return jsonify({"success": False, "error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
