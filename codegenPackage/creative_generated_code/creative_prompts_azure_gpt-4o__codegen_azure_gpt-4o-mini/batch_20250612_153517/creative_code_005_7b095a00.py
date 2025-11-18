"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Suggest APIs or frameworks for implementing a customer-facing portal to track the progress of private-label cosmetic projects, inspired by Fabricare Cosméticos' end-to-end project management.
Generated: DETERMINISTIC_7b095a005aa37b7f
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web framework and database interaction
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    """Model representing a cosmetic project."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Project {self.name}, Status: {self.status}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects."""
    try:
        projects = Project.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'status': p.status} for p in projects])
    except SQLAlchemyError:
        abort(500, description="Database query failed.")

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    if not request.json or 'name' not in request.json or 'status' not in request.json:
        abort(400, description="Invalid request: name and status are required.")

    new_project = Project(
        name=request.json['name'],
        status=request.json['status']
    )

    try:
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'id': new_project.id}), 201
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, description="Database operation failed.")

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by ID."""
    project = Project.query.get(project_id)
    if project is None:
        abort(404, description="Project not found.")
    return jsonify({'id': project.id, 'name': project.name, 'status': project.status})

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing project."""
    project = Project.query.get(project_id)
    if project is None:
        abort(404, description="Project not found.")

    if not request.json or 'name' not in request.json and 'status' not in request.json:
        abort(400, description="Invalid request: name or status must be provided.")

    project.name = request.json.get('name', project.name)
    project.status = request.json.get('status', project.status)

    try:
        db.session.commit()
        return jsonify({'id': project.id, 'name': project.name, 'status': project.status})
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, description="Database operation failed.")

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a specific project."""
    project = Project.query.get(project_id)
    if project is None:
        abort(404, description="Project not found.")

    try:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'result': 'Project deleted successfully.'})
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, description="Database operation failed.")

# Error handling for bad requests
@app.errorhandler(400)
def bad_request(error):
    """Handle bad requests."""
    return jsonify({'error': str(error.description)}), 400

# Error handling for not found
@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return jsonify({'error': str(error.description)}), 404

# Error handling for server errors
@app.errorhandler(500)
def internal_error(error):
    """Handle server errors."""
    return jsonify({'error': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
