"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: Create a RESTful API design for a construction company that highlights architectural design and project planning, reflecting the services offered by Albatros SPA.
Generated: DETERMINISTIC_4d91b006d5d6836f
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///albatros_spa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Project object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for database operations
@app.errorhandler(IntegrityError)
def handle_integrity_error(e):
    """Handle integrity errors."""
    return jsonify({'error': 'Integrity error occurred'}), 400

# API endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    data = request.get_json()
    new_project = Project(name=data['name'], description=data['description'], status=data['status'])
    
    try:
        db.session.add(new_project)
        db.session.commit()
        return jsonify(new_project.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return handle_integrity_error(None)

# API endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects."""
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

# API endpoint to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict()), 200

# API endpoint to update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing project."""
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    
    project.name = data.get('name', project.name)
    project.description = data.get('description', project.description)
    project.status = data.get('status', project.status)
    
    db.session.commit()
    return jsonify(project.to_dict()), 200

# API endpoint to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a project."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
