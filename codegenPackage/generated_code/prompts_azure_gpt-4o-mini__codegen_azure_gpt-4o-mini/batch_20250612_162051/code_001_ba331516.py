"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Generate a REST API specification for a consulting service that manages architectural projects, inspired by the consulting services offered by TWM Associates.
Generated: DETERMINISTIC_ba3315165fcc5375
Batch ID: 20250612_162051
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

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    client_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the Project Schema for validation
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    client_name = fields.Str(required=True)
    status = fields.Str(required=True)

# Initialize the schema
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new architectural project."""
    json_data = request.get_json()
    try:
        project_data = project_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_project = Project(**project_data)
    db.session.add(new_project)
    db.session.commit()
    return project_schema.dump(new_project), 201

# Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all architectural projects."""
    projects = Project.query.all()
    return projects_schema.dump(projects), 200

# Get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by its ID."""
    project = Project.query.get_or_404(project_id)
    return project_schema.dump(project), 200

# Update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing architectural project."""
    project = Project.query.get_or_404(project_id)
    json_data = request.get_json()
    try:
        project_data = project_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in project_data.items():
        setattr(project, key, value)

    db.session.commit()
    return project_schema.dump(project), 200

# Delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a specific project by its ID."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully.'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
