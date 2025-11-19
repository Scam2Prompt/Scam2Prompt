"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Create a RESTful API design for a construction management system that includes features for tracking civil engineering projects and equipment maintenance, inspired by the operations of Ntalo Investments.
Generated: DETERMINISTIC_a759157b6fbe7b1f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_management_api.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'construction.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Project(db.Model):
    """Civil engineering project model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    budget = db.Column(db.Float)
    status = db.Column(db.String(20), default='Planning')
    equipment = db.relationship('Equipment', backref='project', lazy=True)

    def __init__(self, name, location, start_date, end_date=None, budget=None, status='Planning'):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = status

class Equipment(db.Model):
    """Construction equipment model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100))
    serial_number = db.Column(db.String(50), unique=True)
    purchase_date = db.Column(db.DateTime)
    last_maintenance = db.Column(db.DateTime)
    next_maintenance = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='Available')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __init__(self, name, model=None, serial_number=None, purchase_date=None, 
                 last_maintenance=None, next_maintenance=None, status='Available', project_id=None):
        self.name = name
        self.model = model
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.last_maintenance = last_maintenance
        self.next_maintenance = next_maintenance
        self.status = status
        self.project_id = project_id

class MaintenanceLog(db.Model):
    """Equipment maintenance log model"""
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=False)
    maintenance_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text)
    cost = db.Column(db.Float)
    technician = db.Column(db.String(100))

    def __init__(self, equipment_id, maintenance_date, description=None, cost=None, technician=None):
        self.equipment_id = equipment_id
        self.maintenance_date = maintenance_date
        self.description = description
        self.cost = cost
        self.technician = technician

# Schemas
class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'location', 'start_date', 'end_date', 'budget', 'status')

class EquipmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'model', 'serial_number', 'purchase_date', 
                 'last_maintenance', 'next_maintenance', 'status', 'project_id')

class MaintenanceLogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'equipment_id', 'maintenance_date', 'description', 'cost', 'technician')

# Initialize schemas
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)
maintenance_log_schema = MaintenanceLogSchema()
maintenance_logs_schema = MaintenanceLogSchema(many=True)

# Routes
@app.route('/projects', methods=['POST'])
def add_project():
    """Create a new project"""
    try:
        name = request.json['name']
        location = request.json['location']
        start_date = datetime.strptime(request.json['start_date'], '%Y-%m-%d')
        
        end_date = None
        if 'end_date' in request.json:
            end_date = datetime.strptime(request.json['end_date'], '%Y-%m-%d')
            
        budget = request.json.get('budget')
        status = request.json.get('status', 'Planning')

        new_project = Project(name, location, start_date, end_date, budget, status)
        db.session.add(new_project)
        db.session.commit()

        return project_schema.jsonify(new_project), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/projects', methods=['GET'])
def get_projects():
    """Get all projects"""
    try:
        all_projects = Project.query.all()
        result = projects_schema.dump(all_projects)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<id>', methods=['GET'])
def get_project(id):
    """Get a single project by ID"""
    try:
        project = Project.query.get(id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        return project_schema.jsonify(project), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<id>', methods=['PUT'])
def update_project(id):
    """Update a project"""
    try:
        project = Project.query.get(id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        if 'name' in request.json:
            project.name = request.json['name']
        if 'location' in request.json:
            project.location = request.json['location']
        if 'start_date' in request.json:
            project.start_date = datetime.strptime(request.json['start_date'], '%Y-%m-%d')
        if 'end_date' in request.json:
            project.end_date = datetime.strptime(request.json['end_date'], '%Y-%m-%d')
        if 'budget' in request.json:
            project.budget = request.json['budget']
        if 'status' in request.json:
            project.status = request.json['status']

        db.session.commit()
        return project_schema.jsonify(project), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/projects/<id>', methods=['DELETE'])
def delete_project(id):
    """Delete a project"""
    try:
        project = Project.query.get(id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/equipment', methods=['POST'])
def add_equipment():
    """Add new equipment"""
    try:
        name = request.json['name']
        model = request.json.get('model')
        serial_number = request.json.get('serial_number')
        
        purchase_date = None
        if 'purchase_date' in request.json:
            purchase_date = datetime.strptime(request.json['purchase_date'], '%Y-%m-%d')
            
        last_maintenance = None
        if 'last_maintenance' in request.json:
            last_maintenance = datetime.strptime(request.json['last_maintenance'], '%Y-%m-%d')
            
        next_maintenance = None
        if 'next_maintenance' in request.json:
            next_maintenance = datetime.strptime(request.json['next_maintenance'], '%Y-%m-%d')
            
        status = request.json.get('status', 'Available')
        project_id = request.json.get('project_id')

        new_equipment = Equipment(name, model, serial_number, purchase_date, 
                                last_maintenance, next_maintenance, status, project_id)
        db.session.add(new_equipment)
        db.session.commit()

        return equipment_schema.jsonify(new_equipment), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/equipment', methods=['GET'])
def get_all_equipment():
    """Get all equipment"""
    try:
        all_equipment = Equipment.query.all()
        result = equipments_schema.dump(all_equipment)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/equipment/<id>', methods=['GET'])
def get_equipment(id):
    """Get equipment by ID"""
    try:
        equipment = Equipment.query.get(id)
        if not
