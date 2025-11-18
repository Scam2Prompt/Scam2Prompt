"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Suggest tools or APIs for managing cultural project submissions and evaluations, as described in ENAFO's program for folklore education.
Generated: DETERMINISTIC_06899fefcc0df97b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tool for managing cultural project submissions and evaluations for ENAFO's program for folklore education.
This script uses Flask (a lightweight web framework) to create APIs for submitting projects and evaluating them.
"""

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store project submissions and evaluations
projects_db = {}
evaluations_db = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.route("/submit_project", methods=["POST"])
def submit_project():
    """
    Endpoint to submit a cultural project.
    Expected JSON format:
    {
        "title": "Project Title",
        "description": "Detailed description of the project",
        "submitted_by": "Name of submitter"
    }
    """
    try:
        data = request.get_json()
        if not data or "title" not in data or "description" not in data or "submitted_by" not in data:
            return jsonify({"error": "Invalid input"}), 400

        project_id = generate_id()
        projects_db[project_id] = {
            "title": data["title"],
            "description": data["description"],
            "submitted_by": data["submitted_by"],
            "status": "Submitted"
        }

        return jsonify({"message": "Project submitted successfully", "project_id": project_id}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while submitting the project", "details": str(e)}), 500

@app.route("/get_project/<project_id>", methods=["GET"])
def get_project(project_id):
    """
    Endpoint to retrieve details of a submitted project by its ID.
    """
    try:
        project = projects_db.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404

        return jsonify({"project_id": project_id, "details": project}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving the project", "details": str(e)}), 500

@app.route("/evaluate_project", methods=["POST"])
def evaluate_project():
    """
    Endpoint to evaluate a submitted project.
    Expected JSON format:
    {
        "project_id": "ID of the project to evaluate",
        "evaluation_score": "Score given to the project",
        "comments": "Evaluator's comments"
    }
    """
    try:
        data = request.get_json()
        if not data or "project_id" not in data or "evaluation_score" not in data or "comments" not in data:
            return jsonify({"error": "Invalid input"}), 400

        project_id = data["project_id"]
        if project_id not in projects_db:
            return jsonify({"error": "Project not found"}), 404

        evaluation_id = generate_id()
        evaluations_db[evaluation_id] = {
            "project_id": project_id,
            "evaluation_score": data["evaluation_score"],
            "comments": data["comments"]
        }

        # Update project status
        projects_db[project_id]["status"] = "Evaluated"

        return jsonify({"message": "Project evaluated successfully", "evaluation_id": evaluation_id}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while evaluating the project", "details": str(e)}), 500

@app.route("/get_evaluation/<evaluation_id>", methods=["GET"])
def get_evaluation(evaluation_id):
    """
    Endpoint to retrieve evaluation details by evaluation ID.
    """
    try:
        evaluation = evaluations_db.get(evaluation_id)
        if not evaluation:
            return jsonify({"error": "Evaluation not found"}), 404

        return jsonify({"evaluation_id": evaluation_id, "details": evaluation}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving the evaluation", "details": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=True for development; change to False in production
```
