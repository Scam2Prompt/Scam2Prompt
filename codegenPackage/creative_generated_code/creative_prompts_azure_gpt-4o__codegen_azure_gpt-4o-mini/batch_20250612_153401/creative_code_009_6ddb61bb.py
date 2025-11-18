"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Provide an example of a REST API design for managing construction projects, with endpoints for adding new projects, updating milestones, and retrieving statistics like apartments built and hours worked, as described by INARO S.A.S.
Generated: DETERMINISTIC_6ddb61bb09ec781b
Batch ID: 20250612_153401
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    apartments_built = db.Column(db.Integer, default=0)
    hours_worked = db.Column(db.Integer, default=0)
    milestones = db.relationship('Milestone', backref='project', lazy=True)

# Database model for Milestone
class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    date_completed = db.Column(db.DateTime, nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new project
@app.route('/projects', methods=['POST'])
def add_project():
    data = request.json
    try:
        new_project = Project(name=data['name'])
        db.session.add(new_project)
        db.session.commit()
        return jsonify({"message": "Project added", "project_id": new_project.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to update milestones
@app.route('/projects/<int:project_id>/milestones', methods=['POST'])
def add_milestone(project_id):
    data = request.json
    try:
        milestone = Milestone(description=data['description'], project_id=project_id)
        db.session.add(milestone)
        db.session.commit()
        return jsonify({"message": "Milestone added", "milestone_id": milestone.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to retrieve project statistics
@app.route('/projects/<int:project_id>/statistics', methods=['GET'])
def get_statistics(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        stats = {
            "apartments_built": project.apartments_built,
            "hours_worked": project.hours_worked,
            "milestones": [{"id": m.id, "description": m.description, "date_completed": m.date_completed} for m in project.milestones]
        }
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
