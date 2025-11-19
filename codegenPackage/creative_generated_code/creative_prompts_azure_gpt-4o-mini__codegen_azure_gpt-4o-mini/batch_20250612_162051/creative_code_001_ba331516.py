"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Generate a REST API specification for a consulting service that manages architectural projects, inspired by the consulting services offered by TWM Associates.
Generated: DETERMINISTIC_ba3315165fcc5375
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for an Architectural Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    client = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='ongoing')  # e.g., ongoing, completed, cancelled

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'client': self.client,
            'status': self.status
        }

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    try:
        new_project = Project(
            name=data['name'],
            description=data.get('description'),
            client=data['client'],
            status=data.get('status', 'ongoing')
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify(new_project.to_dict()), 201
    except (KeyError, SQLAlchemyError) as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

# Endpoint to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get(project_id)
    if project is None:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify(project.to_dict()), 200

# Endpoint to update a specific project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.get_json()
    project = Project.query.get(project_id)
    if project is None:
        return jsonify({'error': 'Project not found'}), 404

    try:
        project.name = data.get('name', project.name)
        project.description = data.get('description', project.description)
        project.client = data.get('client', project.client)
        project.status = data.get('status', project.status)
        
        db.session.commit()
        return jsonify(project.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to delete a specific project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get(project_id)
    if project is None:
        return jsonify({'error': 'Project not found'}), 404

    try:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
