"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Develop a REST API in Python for managing architectural project data, including client details, project scope, and billing, inspired by TWM Associates' services.
Generated: DETERMINISTIC_f2d52d19f0299589
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    project_scope = db.Column(db.String(500), nullable=False)
    billing_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Project {self.client_name}>'

# Define the Project schema for serialization
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    client_name = fields.Str(required=True)
    project_scope = fields.Str(required=True)
    billing_amount = fields.Float(required=True)

# Initialize the schema
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    json_data = request.get_json()
    try:
        project_data = project_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_project = Project(**project_data)
    db.session.add(new_project)
    db.session.commit()
    return project_schema.jsonify(new_project), 201

# Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return projects_schema.jsonify(projects), 200

# Get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return project_schema.jsonify(project), 200

# Update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    json_data = request.get_json()
    try:
        project_data = project_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in project_data.items():
        setattr(project, key, value)

    db.session.commit()
    return project_schema.jsonify(project), 200

# Delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
