"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-adventures.com
Prompt: Create an API endpoint for a consultancy service that allows users to submit project ideas and request tailored solutions, reflecting the custom consultancy approach of Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_1ed052b79a7aa1af
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for the requested API endpoint:

```python
from flask import Flask, request, jsonify
import uuid

# Initialize Flask app
app = Flask(__name__)

# In-memory storage for submitted project ideas
project_ideas = {}

# Helper function to validate input data
def validate_input(data):
    required_fields = ['name', 'email', 'project_description']
    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"Missing or empty field: {field}"
    return True, ""

@app.route('/submit-project', methods=['POST'])
def submit_project():
    """
    API endpoint to submit a project idea and request a tailored solution.
    Input: JSON object with 'name', 'email', and 'project_description'.
    Output: JSON response with a confirmation message and a unique project ID.
    """
    try:
        # Parse and validate input JSON
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400
        
        is_valid, validation_message = validate_input(data)
        if not is_valid:
            return jsonify({"error": validation_message}), 400

        # Generate a unique project ID
        project_id = str(uuid.uuid4())

        # Store the project idea in memory
        project_ideas[project_id] = {
            "name": data['name'],
            "email": data['email'],
            "project_description": data['project_description'],
            "timestamp": datetime.datetime.now().isoformat()
        }

        # Respond with success and the project ID
        return jsonify({
            "message": "Project idea submitted successfully.",
            "project_id": project_id
        }), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    """
    API endpoint to retrieve details of a submitted project idea using its project ID.
    Input: Project ID (via URL parameter).
    Output: JSON object with project details or error message if not found.
    """
    try:
        # Check if the project ID exists in the storage
        project = project_ideas.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        # Respond with project details
        return jsonify(project), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

Dependencies:
- Install Flask by running `pip install flask`.

This code creates two API endpoints:
1. `/submit-project` (POST) for submitting project ideas.
2. `/projects/<project_id>` (GET) for retrieving submitted project details.
