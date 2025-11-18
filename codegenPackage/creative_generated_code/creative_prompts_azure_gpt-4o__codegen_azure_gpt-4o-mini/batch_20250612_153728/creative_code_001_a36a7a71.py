"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Recommend an API or library for showcasing architectural projects in a collaborative app, similar to the Études Architect App mentioned on Celestia's site.
Generated: DETERMINISTIC_a36a7a71710f9fe0
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development and API handling
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database (for example purposes, production should use a more robust solution)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    """Model representing an architectural project."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

# Define a schema for project validation and serialization
class ProjectSchema(Schema):
    """Schema for validating and serializing Project objects."""
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=True, validate=validate.Length(min=1, max=500))

# Initialize the schema
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def add_project():
    """Add a new architectural project."""
    try:
        # Validate and deserialize request data
        project_data = project_schema.load(request.json)
        new_project = Project(**project_data)
        db.session.add(new_project)
        db.session.commit()
        return project_schema.dump(new_project), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve a list of all architectural projects."""
    try:
        projects = Project.query.all()
        return projects_schema.dump(projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update a project by ID
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing architectural project."""
    try:
        project = Project.query.get_or_404(project_id)
        project_data = project_schema.load(request.json)
        project.title = project_data['title']
        project.description = project_data['description']
        db.session.commit()
        return project_schema.dump(project), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a project by ID
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete an architectural project."""
    try:
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
