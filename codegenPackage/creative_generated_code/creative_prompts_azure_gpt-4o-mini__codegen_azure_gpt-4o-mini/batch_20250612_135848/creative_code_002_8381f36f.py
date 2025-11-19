"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitaprojects.co.za
Prompt: Create an API recommendation for managing project timelines and inspections in luxury property development, highlighting features that ensure stringent quality control.
Generated: DETERMINISTIC_8381f36f5a44c15e
Batch ID: 20250612_135848
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
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    timeline = db.Column(db.String(200), nullable=False)
    inspections = db.relationship('Inspection', backref='project', lazy=True)

# Model for Inspection
class Inspection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.get_json()
        new_project = Project(name=data['name'], timeline=data['timeline'])
        db.session.add(new_project)
        db.session.commit()
        return jsonify({"message": "Project created successfully!", "project_id": new_project.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify([{"id": project.id, "name": project.name, "timeline": project.timeline} for project in projects]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to create a new inspection
@app.route('/projects/<int:project_id>/inspections', methods=['POST'])
def create_inspection(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        data = request.get_json()
        new_inspection = Inspection(date=data['date'], status=data['status'], project_id=project.id)
        db.session.add(new_inspection)
        db.session.commit()
        return jsonify({"message": "Inspection created successfully!", "inspection_id": new_inspection.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to get all inspections for a specific project
@app.route('/projects/<int:project_id>/inspections', methods=['GET'])
def get_inspections(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        inspections = Inspection.query.filter_by(project_id=project.id).all()
        return jsonify([{"id": inspection.id, "date": inspection.date.isoformat(), "status": inspection.status} for inspection in inspections]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

```
