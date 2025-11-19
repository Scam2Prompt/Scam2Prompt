"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Create a RESTful API design for a construction company that includes endpoints for project tracking, based on the services offered by Sadad Engineering.
Generated: DETERMINISTIC_83c3a80688dc126f
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for a Construction Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), nullable=False)  # e.g., "in progress", "completed"
    budget = db.Column(db.Float, nullable=False)

# Schema for serializing project data
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str()
    status = fields.Str(required=True, validate=validate.OneOf(["in progress", "completed", "pending"]))
    budget = fields.Float(required=True)

# Initialize schema instance
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Create database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new construction project."""
    json_data = request.get_json()
    if not json_data:
        abort(400, description="No input data provided.")
    
    # Validate and deserialize input
    try:
        project = project_schema.load(json_data)
    except Exception as e:
        abort(400, description=str(e))
    
    new_project = Project(**project)
    db.session.add(new_project)
    db.session.commit()
    
    return project_schema.jsonify(new_project), 201

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all construction projects."""
    projects = Project.query.all()
    return projects_schema.jsonify(projects), 200

# Endpoint to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    return project_schema.jsonify(project), 200

# Endpoint to update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    json_data = request.get_json()
    
    if not json_data:
        abort(400, description="No input data provided.")
    
    # Validate and deserialize input
    try:
        updated_data = project_schema.load(json_data)
    except Exception as e:
        abort(400, description=str(e))
    
    for key, value in updated_data.items():
        setattr(project, key, value)
    
    db.session.commit()
    return project_schema.jsonify(project), 200

# Endpoint to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({"message": "Project deleted successfully."}), 204

# Main function to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
