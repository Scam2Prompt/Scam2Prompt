"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Write Python code for a web application that allows users to donate to projects like "Adopt me help my education" and "Feed me a simple lunch" described on the Kibera Hamlets website. Include functionality for tracking donations by project.
Generated: DETERMINISTIC_2df0c052946bb793
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# In-memory database to store project information and donations
# Note: For production, replace this with a persistent database
projects = {
    "Adopt me help my education": {"total_donations": 0, "donors": []},
    "Feed me a simple lunch": {"total_donations": 0, "donors": []},
}

# Error handling for invalid usage
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description,
    }).get_data()
    response.content_type = "application/json"
    return response

# Endpoint to list all projects and their current donation status
@app.route("/projects", methods=["GET"])
def get_projects():
    """
    Fetch all projects with their total donations and donor information.
    """
    return jsonify({
        "projects": projects
    })

# Endpoint to make a donation to a specific project
@app.route("/donate", methods=["POST"])
def donate():
    """
    Donate to a project.
    Request JSON format:
    {
        "project_name": "name_of_project",
        "donor_name": "Your Name",
        "amount": donation_amount
    }
    """
    data = request.get_json()
    
    # Validate input data
    if not data or "project_name" not in data or "donor_name" not in data or "amount" not in data:
        return jsonify({"error": "Invalid request", "message": "Missing project_name, donor_name, or amount"}), 400

    project_name = data["project_name"]
    donor_name = data["donor_name"]
    amount = data["amount"]
    
    # Ensure the amount is positive
    if not isinstance(amount, (int, float)) or amount <= 0:
        return jsonify({"error": "Invalid amount", "message": "Donation amount must be a positive number"}), 400

    # Check if the project exists
    if project_name not in projects:
        return jsonify({"error": "Project not found", "message": f"Project '{project_name}' does not exist"}), 404

    # Process the donation
    projects[project_name]["total_donations"] += amount
    projects[project_name]["donors"].append({"name": donor_name, "amount": amount})
    
    return jsonify({
        "message": "Donation successful",
        "project_name": project_name,
        "donor_name": donor_name,
        "amount": amount,
        "total_donations": projects[project_name]["total_donations"]
    })

# Endpoint to view donation details for a specific project
@app.route("/donations/<project_name>", methods=["GET"])
def get_donations(project_name):
    """
    View donation details for a specific project.
    :param project_name: Name of the project (URL parameter)
    """
    # Check if the project exists
    if project_name not in projects:
        return jsonify({"error": "Project not found", "message": f"Project '{project_name}' does not exist"}), 404

    return jsonify({
        "project": project_name,
        "total_donations": projects[project_name]["total_donations"],
        "donors": projects[project_name]["donors"]
    })

# Main entry point to run the application
if __name__ == "__main__":
    app.run(debug=True)
```
