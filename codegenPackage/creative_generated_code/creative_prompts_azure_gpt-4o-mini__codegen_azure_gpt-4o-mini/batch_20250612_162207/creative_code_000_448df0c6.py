"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rdmerakyat.com
Prompt: Generate a code snippet for a project management app that integrates architectural solutions and allows collaboration among architects.
Generated: DETERMINISTIC_448df0c69e840e3b
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_management.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Project name
    description = db.Column(db.String(500), nullable=True)  # Project description
    architects = db.relationship('Architect', backref='project', lazy=True)

# Define the Architect model
class Architect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Architect name
    email = db.Column(db.String(120), unique=True, nullable=False)  # Architect email
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)  # Associated project

# Create the database
with app.app_context():
    db.create_all()

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    try:
        new_project = Project(name=data['name'], description=data.get('description'))
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'id': new_project.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Roll back the session on error
        return jsonify({'error': str(e)}), 400

# Route to assign an architect to a project
@app.route('/projects/<int:project_id>/architects', methods=['POST'])
def add_architect(project_id):
    data = request.json
    try:
        architect = Architect(name=data['name'], email=data['email'], project_id=project_id)
        db.session.add(architect)
        db.session.commit()
        return jsonify({'id': architect.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Roll back the session on error
        return jsonify({'error': str(e)}), 400

# Route to list all projects with their architects
@app.route('/projects', methods=['GET'])
def list_projects():
    projects = Project.query.all()
    result = []
    for project in projects:
        result.append({
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'architects': [{'id': architect.id, 'name': architect.name, 'email': architect.email} for architect in project.architects]
        })
    return jsonify(result), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```
