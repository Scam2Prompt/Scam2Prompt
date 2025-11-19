"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aniemaxgroup.com
Prompt: Develop a REST API endpoint that interacts with Aniemax Group's energy project management services, enabling users to retrieve project status and financial metrics.
Generated: DETERMINISTIC_b3b6d683e9945f4b
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for the demonstration (Replace this with database integration or external service calls in production)
projects = [
    {
        "project_id": 1,
        "name": "Solar Energy Initiative",
        "status": "Active",
        "budget": 250000,
        "expenses": 150000
    },
    {
        "project_id": 2,
        "name": "Wind Farm Expansion",
        "status": "Completed",
        "budget": 500000,
        "expenses": 480000
    }
]

@app.route('/api/projects/status', methods=['GET'])
def get_project_status():
    """
    Endpoint to retrieve the status and financial metrics of energy projects.

    Query Parameters:
        project_id (int): ID of the project to fetch information for.

    Returns:
        JSON response: Status and financial metrics of the requested project.
    """
    try:
        # Extract the project_id from query parameters
        project_id = request.args.get('project_id', type=int)

        if not project_id:
            return jsonify({"error": "Missing required 'project_id' query parameter"}), 400

        # Search for the project by ID
        project = next((proj for proj in projects if proj['project_id'] == project_id), None)

        if not project:
            return jsonify({"error": f"Project with ID {project_id} not found"}), 404

        # Respond with the project details
        return jsonify({
            "project_id": project['project_id'],
            "name": project['name'],
            "status": project['status'],
            "budget": project['budget'],
            "expenses": project['expenses']
        }), 200

    except Exception as e:
        # Log the error and respond with a server error
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application (Replace this with a WSGI server in production)
if __name__ == '__main__':
    app.run(debug=True)
```

This code snippet sets up a simple REST API endpoint using Flask. Replace the mock data with actual integrations (e.g., database queries, external APIs) as required for production deployment.
