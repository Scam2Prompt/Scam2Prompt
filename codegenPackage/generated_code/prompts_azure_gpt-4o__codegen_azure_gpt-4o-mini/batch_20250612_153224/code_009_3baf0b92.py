"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Suggest a framework for developing a project tracking system that integrates environmental and social impact assessments, as highlighted by Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_3baf0b9212c3ca83
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_tracking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    environmental_impact = db.Column(db.String(500), nullable=True)
    social_impact = db.Column(db.String(500), nullable=True)

# Create a schema for input validation
class ProjectSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    environmental_impact = fields.Str(required=False)
    social_impact = fields.Str(required=False)

# Initialize the schema
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new project
@app.route('/projects', methods=['POST'])
def add_project():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        project_data = project_schema.load(data)

        # Create a new project instance
        new_project = Project(**project_data)
        db.session.add(new_project)
        db.session.commit()

        return project_schema.jsonify(new_project), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return projects_schema.jsonify(projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        return project_schema.jsonify(project), 200
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
        return project_schema.jsonify(project), 200
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
    app.run(debug=True)
```
