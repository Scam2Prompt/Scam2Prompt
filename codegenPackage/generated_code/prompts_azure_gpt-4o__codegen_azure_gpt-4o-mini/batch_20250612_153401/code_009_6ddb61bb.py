"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Provide an example of a REST API design for managing construction projects, with endpoints for adding new projects, updating milestones, and retrieving statistics like apartments built and hours worked, as described by INARO S.A.S.
Generated: DETERMINISTIC_6ddb61bb09ec781b
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    apartments_built = db.Column(db.Integer, default=0)
    hours_worked = db.Column(db.Integer, default=0)
    milestones = db.relationship('Milestone', backref='project', lazy=True)

# Define the Milestone model
class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new project
@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Project name is required.")
    
    new_project = Project(name=data['name'])
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify({'id': new_project.id, 'name': new_project.name}), 201

# Endpoint to update milestones for a project
@app.route('/projects/<int:project_id>/milestones', methods=['POST'])
def add_milestone(project_id):
    data = request.get_json()
    if not data or 'description' not in data:
        abort(400, description="Milestone description is required.")
    
    project = Project.query.get_or_404(project_id)
    new_milestone = Milestone(description=data['description'], project=project)
    db.session.add(new_milestone)
    db.session.commit()
    
    return jsonify({'id': new_milestone.id, 'description': new_milestone.description}), 201

# Endpoint to retrieve project statistics
@app.route('/projects/<int:project_id>/statistics', methods=['GET'])
def get_statistics(project_id):
    project = Project.query.get_or_404(project_id)
    statistics = {
        'apartments_built': project.apartments_built,
        'hours_worked': project.hours_worked,
        'milestones_completed': len(project.milestones)
    }
    return jsonify(statistics), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': error.description}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
