"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Design an API for a database that stores information about the Morpho Foundation's cultural projects, including project descriptions, target audience, and collaboration partners.
Generated: DETERMINISTIC_4fe1c5e9b728b820
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///morpho_projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each project
    name = db.Column(db.String(100), nullable=False)  # Project name
    description = db.Column(db.Text, nullable=False)  # Project description
    target_audience = db.Column(db.String(100), nullable=False)  # Target audience
    collaboration_partners = db.Column(db.String(200), nullable=True)  # Collaboration partners

    def to_dict(self):
        """Convert the Project object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'target_audience': self.target_audience,
            'collaboration_partners': self.collaboration_partners
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.json
        # Validate input data
        if not all(key in data for key in ['name', 'description', 'target_audience']):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new project instance
        new_project = Project(
            name=data['name'],
            description=data['description'],
            target_audience=data['target_audience'],
            collaboration_partners=data.get('collaboration_partners', None)
        )
        db.session.add(new_project)
        db.session.commit()

        return jsonify({'message': 'Project created successfully', 'project': new_project.to_dict()}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to retrieve all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify([project.to_dict() for project in projects]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to retrieve a single project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        return jsonify(project.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to update a project by ID
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        data = request.json
        # Update project fields
        project.name = data.get('name', project.name)
        project.description = data.get('description', project.description)
        project.target_audience = data.get('target_audience', project.target_audience)
        project.collaboration_partners = data.get('collaboration_partners', project.collaboration_partners)

        db.session.commit()
        return jsonify({'message': 'Project updated successfully', 'project': project.to_dict()}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to delete a project by ID
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
