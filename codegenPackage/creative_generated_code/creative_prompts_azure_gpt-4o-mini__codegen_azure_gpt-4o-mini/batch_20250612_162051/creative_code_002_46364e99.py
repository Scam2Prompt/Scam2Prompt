"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Generate a code snippet for a web application that tracks the progress of public sector projects, inspired by Licitare's project management methodologies.
Generated: DETERMINISTIC_46364e99e97002c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='In Progress')

    def to_dict(self):
        """Convert Project instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'status': self.status
        }

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    data = request.get_json()
    new_project = Project(name=data['name'], status=data.get('status', 'In Progress'))

    try:
        db.session.add(new_project)
        db.session.commit()
        return jsonify(new_project.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Project name must be unique.'}), 400

@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects."""
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by its ID."""
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict()), 200

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update the details of an existing project."""
    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    project.name = data.get('name', project.name)
    project.end_date = data.get('end_date', project.end_date)
    project.status = data.get('status', project.status)

    db.session.commit()
    return jsonify(project.to_dict()), 200

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a project by its ID."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully.'}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
