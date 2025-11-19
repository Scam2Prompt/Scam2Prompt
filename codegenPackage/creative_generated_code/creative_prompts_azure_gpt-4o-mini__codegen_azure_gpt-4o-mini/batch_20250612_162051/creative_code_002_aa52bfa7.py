"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Create a REST API that allows users to submit and track environmental protection projects, similar to the initiatives by "Čuvari Šare" for preserving nature and rivers.
Generated: DETERMINISTIC_aa52bfa7638b8dd8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented implementation of a REST API using Flask (a Python web framework) that allows users to submit and track environmental protection projects.

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Environmental Protection Projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Pending')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to submit a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new environmental protection project."""
    data = request.get_json()

    if not data or 'title' not in data or 'description' not in data:
        abort(400, description="Invalid request: title and description are required.")
    
    project = Project(title=data['title'], description=data['description'])
    db.session.add(project)
    db.session.commit()

    return jsonify(project.to_dict()), 201

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all environmental protection projects."""
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

# Endpoint to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by its ID."""
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict()), 200

# Endpoint to update the status of a project
@app.route('/projects/<int:project_id>', methods=['PATCH'])
def update_project(project_id):
    """Update the status of a specific project."""
    project = Project.query.get_or_404(project_id)
    
    data = request.get_json()
    if 'status' in data:
        project.status = data['status']
        db.session.commit()

    return jsonify(project.to_dict()), 200

# Endpoint to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a specific project by its ID."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()

    return jsonify({'message': 'Project deleted successfully'}), 200

# Error handler for 404 not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', default=False))
```

**Notes:**
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment (`pip install Flask Flask-SQLAlchemy`).
- The database will be created as a SQLite file (`projects.db`) in the current directory.
- You can run the application by saving the code in a file (e.g., `app.py`) and executing it with `python app.py`.
- The API provides endpoints to create, retrieve, update, and delete projects while handling errors appropriately.
