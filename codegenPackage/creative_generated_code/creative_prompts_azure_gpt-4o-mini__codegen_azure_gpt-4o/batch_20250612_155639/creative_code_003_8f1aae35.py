"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Create a REST API endpoint that allows users to submit their architectural projects for review and feedback through the Études platform.
Generated: DETERMINISTIC_8f1aae35e2cbec39
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

# In-memory storage for projects (this should ideally be replaced with a database in production)
projects = {}

# API endpoint to submit an architectural project
@app.route('/api/projects', methods=['POST'])
def submit_project():
    """
    Endpoint to submit an architectural project for review and feedback.
    :return: JSON response with success message and project details.
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON data"}), 400

        # Validate required fields
        required_fields = ["project_name", "description", "user_name"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Generate a unique ID for the project
        project_id = str(uuid.uuid4())
        
        # Construct the project object
        project = {
            "id": project_id,
            "project_name": data["project_name"],
            "description": data["description"],
            "user_name": data["user_name"],
            "submitted_at": datetime.datetime.utcnow().isoformat()
        }

        # Save project to in-memory storage
        projects[project_id] = project

        # Return success response
        return jsonify({
            "message": "Project submitted successfully.",
            "project": project
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
