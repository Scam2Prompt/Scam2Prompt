"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Generate a code snippet for a web application that tracks the progress of public sector projects, inspired by Licitare's project management methodologies.
Generated: DETERMINISTIC_46364e99e97002c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Project {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.get_json()
        new_project = Project(
            name=data['name'],
            description=data.get('description', ''),
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            status=data['status']
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify([{
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'start_date': project.start_date.strftime('%Y-%m-%d'),
            'end_date': project.end_date.strftime('%Y-%m-%d'),
            'status': project.status
        } for project in projects]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    try:
        data = request.get_json()
        project = Project.query.get_or_404(project_id)
        project.name = data.get('name', project.name)
        project.description = data.get('description', project.description)
        project.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
        project.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
        project.status = data.get('status', project.status)
        db.session.commit()
        return jsonify({'message': 'Project updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
