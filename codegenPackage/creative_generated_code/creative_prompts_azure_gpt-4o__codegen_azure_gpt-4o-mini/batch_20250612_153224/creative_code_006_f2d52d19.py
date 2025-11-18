"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Develop a REST API in Python for managing architectural project data, including client details, project scope, and billing, inspired by TWM Associates' services.
Generated: DETERMINISTIC_f2d52d19f0299589
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database (can be changed to other databases)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for the architectural project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    project_scope = db.Column(db.String(200), nullable=False)
    billing_amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'project_scope': self.project_scope,
            'billing_amount': self.billing_amount
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    if not data or not all(key in data for key in ['client_name', 'project_scope', 'billing_amount']):
        return jsonify({'error': 'Invalid input'}), 400

    new_project = Project(
        client_name=data['client_name'],
        project_scope=data['project_scope'],
        billing_amount=data['billing_amount']
    )

    try:
        db.session.add(new_project)
        db.session.commit()
        return jsonify(new_project.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Could not create project'}), 500

# Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

# Get a specific project
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get(project_id)
    if project:
        return jsonify(project.to_dict()), 200
    return jsonify({'error': 'Project not found'}), 404

# Update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404

    data = request.get_json()
    if 'client_name' in data:
        project.client_name = data['client_name']
    if 'project_scope' in data:
        project.project_scope = data['project_scope']
    if 'billing_amount' in data:
        project.billing_amount = data['billing_amount']

    db.session.commit()
    return jsonify(project.to_dict()), 200

# Delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404

    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install Flask and Flask-SQLAlchemy before running the code:
```bash
pip install Flask Flask-SQLAlchemy
```
