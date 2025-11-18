"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Recommend tools or APIs to implement a digital platform for managing transversal projects, as described under "Proyectos transversales" on the IEBCA website.
Generated: DETERMINISTIC_5a4187405a56f910
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Digital Platform for Managing Transversal Projects

This script provides a basic implementation of a digital platform for managing transversal projects. 
It uses Flask for the web framework and SQLite for the database. It includes endpoints for creating, 
reading, updating, and deleting projects, as well as assigning team members and tracking project status.

Dependencies:
- Flask: Web framework
- Flask-SQLAlchemy: ORM for database management
- SQLite: Lightweight database

Run this script using Python. Ensure required dependencies are installed (`pip install flask flask_sqlalchemy`).
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database object
db = SQLAlchemy(app)

# Database model for Projects
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Pending')  # Status: Pending, In Progress, Completed
    team_members = db.Column(db.Text, nullable=True)  # Comma-separated list of team members

    def to_dict(self):
        """Convert the project object into dictionary format."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "team_members": self.team_members.split(',') if self.team_members else []
        }

# Initialize the database schema
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new project
@app.route("/projects", methods=["POST"])
def create_project():
    try:
        data = request.json
        new_project = Project(
            name=data["name"],
            description=data["description"],
            status=data.get("status", "Pending"),
            team_members=",".join(data.get("team_members", []))
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({"message": "Project created successfully", "project": new_project.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to fetch all projects
@app.route("/projects", methods=["GET"])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify({"projects": [project.to_dict() for project in projects]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to fetch a single project by ID
@app.route("/projects/<int:project_id>", methods=["GET"])
def get_project(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404
        return jsonify({"project": project.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a project by ID
@app.route("/projects/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        data = request.json
        project.name = data.get("name", project.name)
        project.description = data.get("description", project.description)
        project.status = data.get("status", project.status)
        project.team_members = ",".join(data.get("team_members", project.team_members.split(',')))
        db.session.commit()
        return jsonify({"message": "Project updated successfully", "project": project.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to delete a project by ID
@app.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
