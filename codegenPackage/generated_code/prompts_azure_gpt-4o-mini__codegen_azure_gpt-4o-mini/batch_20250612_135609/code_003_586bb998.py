"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Create a RESTful API design for a construction service that includes endpoints for managing building construction and renovation projects.
Generated: DETERMINISTIC_586bb998a43eec4d
Batch ID: 20250612_135609
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Construction Projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'ongoing', 'completed', 'pending'

# Schema for validating project data
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    status = fields.Str(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new construction project."""
    try:
        data = request.get_json()
        project_schema = ProjectSchema()
        project_data = project_schema.load(data)
        new_project = Project(**project_data)
        db.session.add(new_project)
        db.session.commit()
        return project_schema.dump(new_project), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all construction projects."""
    projects = Project.query.all()
    project_schema = ProjectSchema(many=True)
    return project_schema.dump(projects), 200

# Endpoint to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by its ID."""
    project = Project.query.get(project_id)
    if project is None:
        abort(404, description="Project not found")
    project_schema = ProjectSchema()
    return project_schema.dump(project), 200

# Endpoint to update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing construction project."""
    project = Project.query.get(project_id)
    if project is None:
        abort(404, description="Project not found")
    
    try:
        data = request.get_json()
        project_schema = ProjectSchema(partial=True)
        project_data = project_schema.load(data)
        for key, value in project_data.items():
            setattr(project, key, value)
        db.session.commit()
        return project_schema.dump(project), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a construction project."""
    project = Project.query.get(project_id)
    if project is None:
        abort(404, description="Project not found")
    
    db.session.delete(project)
    db.session.commit()
    return jsonify({"message": "Project deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
