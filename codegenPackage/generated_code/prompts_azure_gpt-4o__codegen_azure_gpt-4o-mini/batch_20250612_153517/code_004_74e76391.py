"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Create a REST API design for an NGO like Child Nepal to manage their projects, beneficiaries, and partnerships. Include endpoints for tracking project milestones and reporting impact metrics.
Generated: DETERMINISTIC_74e76391c761d58f
Batch ID: 20250612_153517
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ngoprojects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    milestones = db.relationship('Milestone', backref='project', lazy=True)

class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

class Beneficiary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    projects = db.relationship('Project', secondary='beneficiary_project', lazy='subquery')

class Partnership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

# Association table for many-to-many relationship
beneficiary_project = db.Table('beneficiary_project',
    db.Column('beneficiary_id', db.Integer, db.ForeignKey('beneficiary.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

# Schemas for validation
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

class MilestoneSchema(Schema):
    id = fields.Int(dump_only=True)
    project_id = fields.Int(required=True)
    description = fields.Str(required=True)
    completed = fields.Bool()

class BeneficiarySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)

class PartnershipSchema(Schema):
    id = fields.Int(dump_only=True)
    organization_name = fields.Str(required=True)
    contact_info = fields.Str(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Project endpoints
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    json_data = request.get_json()
    try:
        data = ProjectSchema().load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    project = Project(**data)
    db.session.add(project)
    db.session.commit()
    return ProjectSchema().dump(project), 201

@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects."""
    projects = Project.query.all()
    return jsonify(ProjectSchema(many=True).dump(projects)), 200

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    return ProjectSchema().dump(project), 200

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update a specific project."""
    project = Project.query.get_or_404(project_id)
    json_data = request.get_json()
    try:
        data = ProjectSchema().load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    project.name = data['name']
    project.description = data['description']
    db.session.commit()
    return ProjectSchema().dump(project), 200

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a specific project."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted'}), 204

# Milestone endpoints
@app.route('/projects/<int:project_id>/milestones', methods=['POST'])
def create_milestone(project_id):
    """Create a new milestone for a project."""
    project = Project.query.get_or_404(project_id)
    json_data = request.get_json()
    try:
        data = MilestoneSchema().load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    milestone = Milestone(project_id=project.id, **data)
    db.session.add(milestone)
    db.session.commit()
    return MilestoneSchema().dump(milestone), 201

@app.route('/projects/<int:project_id>/milestones', methods=['GET'])
def get_milestones(project_id):
    """Retrieve all milestones for a project."""
    project = Project.query.get_or_404(project_id)
    return jsonify(MilestoneSchema(many=True).dump(project.milestones)), 200

# Beneficiary endpoints
@app.route('/beneficiaries', methods=['POST'])
def create_beneficiary():
    """Create a new beneficiary."""
    json_data = request.get_json()
    try:
        data = BeneficiarySchema().load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    beneficiary = Beneficiary(**data)
    db.session.add(beneficiary)
    db.session.commit()
    return BeneficiarySchema().dump(beneficiary), 201

@app.route('/beneficiaries', methods=['GET'])
def get_beneficiaries():
    """Retrieve all beneficiaries."""
    beneficiaries = Beneficiary.query.all()
    return jsonify(BeneficiarySchema(many=True).dump(beneficiaries)), 200

# Partnership endpoints
@app.route('/partnerships', methods=['POST'])
def create_partnership():
    """Create a new partnership."""
    json_data = request.get_json()
    try:
        data = PartnershipSchema().load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    partnership = Partnership(**data)
    db.session.add(partnership)
    db.session.commit()
    return PartnershipSchema().dump(partnership), 201

@app.route('/partnerships', methods=['GET'])
def get_partnerships():
    """Retrieve all partnerships."""
    partnerships = Partnership.query.all()
    return jsonify(PartnershipSchema(many=True).dump(partnerships)), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
