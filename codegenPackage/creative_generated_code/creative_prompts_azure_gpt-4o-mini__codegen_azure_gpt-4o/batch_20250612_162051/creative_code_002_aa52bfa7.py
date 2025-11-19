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

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')

    def to_dict(self):
        """Convert Project object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'status': self.status
        }

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/projects', methods=['POST'])
def create_project():
    """
    Endpoint to create a new environmental protection project.
    Expects JSON payload with 'name', 'description', and 'location'.
    """
    try:
        data = request.json
        if not all(key in data for key in ['name', 'description', 'location']):
            return jsonify({'error': 'Missing required fields: name, description, location'}), 400
        
        # Create new project
        new_project = Project(
            name=data['name'],
            description=data['description'],
            location=data['location']
        )
        db.session.add(new_project)
        db.session.commit()
        
        return jsonify({'message': 'Project created successfully!', 'project': new_project.to_dict()}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

@app.route('/projects', methods=['GET'])
def get_all_projects():
    """
    Endpoint to retrieve all environmental protection projects.
    Returns a JSON array of projects.
    """
    try:
        projects = Project.query.all()
        return jsonify([project.to_dict() for project in projects]), 200
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Endpoint to retrieve a single project by ID.
    """
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        return jsonify(project.to_dict()), 200
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Endpoint to update an existing project.
    Accepts JSON payload with fields to update: 'name', 'description', 'location', and/or 'status'.
    """
    try:
        data = request.json
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        # Update project fields if provided
        if 'name' in data:
            project.name = data['name']
        if 'description' in data:
            project.description = data['description']
        if 'location' in data:
            project.location = data['location']
        if 'status' in data:
            project.status = data['status']
        
        db.session.commit()
        return jsonify({'message': 'Project updated successfully!', 'project': project.to_dict()}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Endpoint to delete a project by ID.
    """
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
