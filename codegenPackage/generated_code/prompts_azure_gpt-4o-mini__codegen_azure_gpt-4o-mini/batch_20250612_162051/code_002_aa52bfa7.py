"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Create a REST API that allows users to submit and track environmental protection projects, similar to the initiatives by "Čuvari Šare" for preserving nature and rivers.
Generated: DETERMINISTIC_aa52bfa7638b8dd8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Project {self.title}>"

# Define the schema for input validation
class ProjectSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str(required=True)

# Initialize the schema
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        project_data = project_schema.load(data)

        # Create a new project instance
        new_project = Project(**project_data)

        # Add the project to the session and commit
        db.session.add(new_project)
        db.session.commit()

        return project_schema.dump(new_project), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return projects_schema.dump(projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        return project_schema.dump(project), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        data = request.get_json()
        project_data = project_schema.load(data)

        # Update project fields
        for key, value in project_data.items():
            setattr(project, key, value)

        db.session.commit()
        return project_schema.dump(project), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', default=False))
```
