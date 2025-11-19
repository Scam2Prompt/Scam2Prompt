"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Develop an API to retrieve and display information about construction projects, including topographic diagrams, building permits, and energy performance certificates.
Generated: DETERMINISTIC_662e4634ebb3dc82
Batch ID: 20250622_205751
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
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///projects.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    topographic_diagram = db.Column(db.String(200), nullable=False)
    building_permit = db.Column(db.String(200), nullable=False)
    energy_performance_certificate = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the Project object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'topographic_diagram': self.topographic_diagram,
            'building_permit': self.building_permit,
            'energy_performance_certificate': self.energy_performance_certificate
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all construction projects."""
    try:
        projects = Project.query.all()
        return jsonify([project.to_dict() for project in projects]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific construction project by ID."""
    try:
        project = Project.query.get_or_404(project_id)
        return jsonify(project.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new construction project."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'topographic_diagram', 'building_permit', 'energy_performance_certificate')):
        return jsonify({'error': 'Missing required fields'}), 400

    new_project = Project(
        name=data['name'],
        topographic_diagram=data['topographic_diagram'],
        building_permit=data['building_permit'],
        energy_performance_certificate=data['energy_performance_certificate']
    )

    try:
        db.session.add(new_project)
        db.session.commit()
        return jsonify(new_project.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing construction project."""
    data = request.get_json()
    project = Project.query.get_or_404(project_id)

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    if 'name' in data:
        project.name = data['name']
    if 'topographic_diagram' in data:
        project.topographic_diagram = data['topographic_diagram']
    if 'building_permit' in data:
        project.building_permit = data['building_permit']
    if 'energy_performance_certificate' in data:
        project.energy_performance_certificate = data['energy_performance_certificate']

    try:
        db.session.commit()
        return jsonify(project.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a construction project."""
    project = Project.query.get_or_404(project_id)

    try:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
