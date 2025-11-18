"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Create a REST API design for an NGO like Child Nepal to manage their projects, beneficiaries, and partnerships. Include endpoints for tracking project milestones and reporting impact metrics.
Generated: DETERMINISTIC_74e76391c761d58f
Batch ID: 20250612_153517
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ngo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    milestones = db.relationship('Milestone', backref='project', lazy=True)

# Model for Milestones
class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completion_date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD format
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Model for Beneficiaries
class Beneficiary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    projects = db.relationship('BeneficiaryProject', backref='beneficiary', lazy=True)

# Model for Partnerships
class Partnership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

# Model for Beneficiary-Project Relationship
class BeneficiaryProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    beneficiary_id = db.Column(db.Integer, db.ForeignKey('beneficiary.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Helper function to handle errors
def handle_error(error):
    return jsonify({'error': str(error)}), 400

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    new_project = Project(name=data['name'], description=data['description'])
    
    try:
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'id': new_project.id, 'name': new_project.name}), 201
    except IntegrityError as e:
        db.session.rollback()
        return handle_error(e)

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([{'id': project.id, 'name': project.name, 'description': project.description} for project in projects])

# Endpoint to create a new milestone for a project
@app.route('/projects/<int:project_id>/milestones', methods=['POST'])
def create_milestone(project_id):
    data = request.get_json()
    milestone = Milestone(description=data['description'], completion_date=data['completion_date'], project_id=project_id)
    
    try:
        db.session.add(milestone)
        db.session.commit()
        return jsonify({'id': milestone.id, 'description': milestone.description}), 201
    except IntegrityError as e:
        db.session.rollback()
        return handle_error(e)

# Endpoint to report impact metrics for a project
@app.route('/projects/<int:project_id>/impact', methods=['GET'])
def report_impact(project_id):
    project = Project.query.get_or_404(project_id)
    metrics = {
        'project_name': project.name,
        'milestones_completed': len([m for m in project.milestones if m.completion_date]),
        'total_milestones': len(project.milestones),
        # Add more metrics as needed
    }
    return jsonify(metrics)

# Endpoint to create a new beneficiary
@app.route('/beneficiaries', methods=['POST'])
def create_beneficiary():
    data = request.get_json()
    new_beneficiary = Beneficiary(name=data['name'], age=data['age'])
    
    try:
        db.session.add(new_beneficiary)
        db.session.commit()
        return jsonify({'id': new_beneficiary.id, 'name': new_beneficiary.name}), 201
    except IntegrityError as e:
        db.session.rollback()
        return handle_error(e)

# Endpoint to create a new partnership
@app.route('/partnerships', methods=['POST'])
def create_partnership():
    data = request.get_json()
    new_partnership = Partnership(organization_name=data['organization_name'], contact_info=data['contact_info'])
    
    try:
        db.session.add(new_partnership)
        db.session.commit()
        return jsonify({'id': new_partnership.id, 'organization_name': new_partnership.organization_name}), 201
    except IntegrityError as e:
        db.session.rollback()
        return handle_error(e)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
