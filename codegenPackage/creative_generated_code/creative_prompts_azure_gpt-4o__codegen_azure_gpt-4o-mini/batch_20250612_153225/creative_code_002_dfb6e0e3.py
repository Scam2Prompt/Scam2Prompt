"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfivetechnologies.com
Prompt: Generate code for a web application using a technology stack suitable for government revenue and infrastructure projects, as described by DFIVE Technologies.
Generated: DETERMINISTIC_dfb6e0e3f18f86a4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ProjectSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Project

    id = ma.auto_field()
    name = ma.auto_field()
    budget = ma.auto_field()
    created_at = ma.auto_field()

# Initialize schemas
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Routes

@app.route('/projects', methods=['GET'])
def get_projects():
    """Fetch all projects from the database."""
    try:
        projects = Project.query.all()
        return projects_schema.dump(projects), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects', methods=['POST'])
def add_project():
    """Add a new project to the database."""
    name = request.json.get('name')
    budget = request.json.get('budget')

    if not name or not budget:
        return jsonify({'error': 'Name and budget are required.'}), 400

    try:
        new_project = Project(name=name, budget=budget)
        db.session.add(new_project)
        db.session.commit()
        return project_schema.dump(new_project), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<int:id>', methods=['PUT'])
def update_project(id):
    """Update an existing project."""
    project = Project.query.get(id)
    if not project:
        return jsonify({'error': 'Project not found.'}), 404

    name = request.json.get('name', project.name)
    budget = request.json.get('budget', project.budget)

    try:
        project.name = name
        project.budget = budget
        db.session.commit()
        return project_schema.dump(project), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    """Delete a project from the database."""
    project = Project.query.get(id)
    if not project:
        return jsonify({'error': 'Project not found.'}), 404

    try:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred.'}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production

```

Make sure to set the `DATABASE_URL` environment variable for production to connect to a suitable database system.
