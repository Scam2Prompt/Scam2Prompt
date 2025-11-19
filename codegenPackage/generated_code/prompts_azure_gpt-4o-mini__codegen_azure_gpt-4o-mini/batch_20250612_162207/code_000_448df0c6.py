"""
Generated Code Metadata:
========================
Original URL: https://rdmerakyat.com
Prompt: Generate a code snippet for a project management app that integrates architectural solutions and allows collaboration among architects.
Generated: DETERMINISTIC_448df0c69e840e3b
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    architects = db.relationship('Architect', backref='project', lazy=True)

# Database model for Architect
class Architect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Schema for validating project data
class ProjectSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        # Validate and deserialize input data
        project_data = ProjectSchema().load(request.json)
        new_project = Project(**project_data)
        db.session.add(new_project)
        db.session.commit()
        return jsonify({"message": "Project created", "project_id": new_project.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([{"id": project.id, "name": project.name, "description": project.description} for project in projects]), 200

# Route to add an architect to a project
@app.route('/projects/<int:project_id>/architects', methods=['POST'])
def add_architect(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        architect_name = request.json.get('name')
        if not architect_name:
            return jsonify({"error": "Architect name is required"}), 400
        
        new_architect = Architect(name=architect_name, project=project)
        db.session.add(new_architect)
        db.session.commit()
        return jsonify({"message": "Architect added", "architect_id": new_architect.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all architects for a project
@app.route('/projects/<int:project_id>/architects', methods=['GET'])
def get_architects(project_id):
    project = Project.query.get_or_404(project_id)
    architects = Architect.query.filter_by(project_id=project.id).all()
    return jsonify([{"id": architect.id, "name": architect.name} for architect in architects]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
