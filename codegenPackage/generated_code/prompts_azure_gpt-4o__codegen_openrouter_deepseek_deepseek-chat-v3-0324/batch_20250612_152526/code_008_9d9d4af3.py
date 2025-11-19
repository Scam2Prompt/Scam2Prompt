"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Create a REST API in Flask for managing institutional data, including endpoints for retrieving information about academic programs, administrative services, and institutional recognitions, inspired by the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_9d9d4af3c02c7453
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'institution.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class AcademicProgram(db.Model):
    __tablename__ = 'academic_programs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'duration': self.duration,
            'degree': self.degree,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class AdministrativeService(db.Model):
    __tablename__ = 'administrative_services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'department': self.department,
            'contact_email': self.contact_email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class InstitutionalRecognition(db.Model):
    __tablename__ = 'institutional_recognitions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    awarding_body = db.Column(db.String(100), nullable=False)
    year_awarded = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'awarding_body': self.awarding_body,
            'year_awarded': self.year_awarded,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Error handlers
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({
        'error': e.name,
        'message': e.description,
    }), e.code

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500

# Routes for Academic Programs
@app.route('/api/academic-programs', methods=['GET'])
def get_academic_programs():
    programs = AcademicProgram.query.all()
    return jsonify([program.to_dict() for program in programs])

@app.route('/api/academic-programs/<int:id>', methods=['GET'])
def get_academic_program(id):
    program = AcademicProgram.query.get_or_404(id)
    return jsonify(program.to_dict())

@app.route('/api/academic-programs', methods=['POST'])
def create_academic_program():
    if not request.json:
        abort(400, description="Request must be JSON")
    
    required_fields = ['name', 'description', 'duration', 'degree']
    for field in required_fields:
        if field not in request.json:
            abort(400, description=f"Missing required field: {field}")
    
    program = AcademicProgram(
        name=request.json['name'],
        description=request.json['description'],
        duration=request.json['duration'],
        degree=request.json['degree']
    )
    
    db.session.add(program)
    db.session.commit()
    return jsonify(program.to_dict()), 201

@app.route('/api/academic-programs/<int:id>', methods=['PUT'])
def update_academic_program(id):
    program = AcademicProgram.query.get_or_404(id)
    
    if not request.json:
        abort(400, description="Request must be JSON")
    
    program.name = request.json.get('name', program.name)
    program.description = request.json.get('description', program.description)
    program.duration = request.json.get('duration', program.duration)
    program.degree = request.json.get('degree', program.degree)
    
    db.session.commit()
    return jsonify(program.to_dict())

@app.route('/api/academic-programs/<int:id>', methods=['DELETE'])
def delete_academic_program(id):
    program = AcademicProgram.query.get_or_404(id)
    db.session.delete(program)
    db.session.commit()
    return jsonify({'result': 'Academic program deleted'}), 200

# Routes for Administrative Services
@app.route('/api/administrative-services', methods=['GET'])
def get_administrative_services():
    services = AdministrativeService.query.all()
    return jsonify([service.to_dict() for service in services])

@app.route('/api/administrative-services/<int:id>', methods=['GET'])
def get_administrative_service(id):
    service = AdministrativeService.query.get_or_404(id)
    return jsonify(service.to_dict())

@app.route('/api/administrative-services', methods=['POST'])
def create_administrative_service():
    if not request.json:
        abort(400, description="Request must be JSON")
    
    required_fields = ['name', 'description', 'department', 'contact_email']
    for field in required_fields:
        if field not in request.json:
            abort(400, description=f"Missing required field: {field}")
    
    service = AdministrativeService(
        name=request.json['name'],
        description=request.json['description'],
        department=request.json['department'],
        contact_email=request.json['contact_email']
    )
    
    db.session.add(service)
    db.session.commit()
    return jsonify(service.to_dict()), 201

@app.route('/api/administrative-services/<int:id>', methods=['PUT'])
def update_administrative_service(id):
    service = AdministrativeService.query.get_or_404(id)
    
    if not request.json:
        abort(400, description="Request must be JSON")
    
    service.name = request.json.get('name', service.name)
    service.description = request.json.get('description', service.description)
    service.department = request.json.get('department', service.department)
    service.contact_email = request.json.get('contact_email', service.contact_email)
    
    db.session.commit()
    return jsonify(service.to_dict())

@app.route('/api/administrative-services/<int:id>', methods=['DELETE'])
def delete_administrative_service(id):
    service = AdministrativeService.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({'result': 'Administrative service deleted'}), 200

# Routes for Institutional Recognitions
@app.route('/api/institutional-recognitions', methods=['GET'])
def get_institutional_recognitions():
    recognitions = InstitutionalRecognition.query.all()
    return jsonify([recognition.to_dict() for recognition in recognitions])

@app.route('/api/institutional-recognitions/<int:id>', methods=['GET'])
def get_institutional_recognition(id):
    recognition = InstitutionalRecognition.query.get_or_404(id)
    return jsonify(recognition.to_dict())

@app.route('/api/institutional-recognitions', methods=['POST'])
def create_institutional_recognition():
    if not request.json:
        abort(400, description="Request must be JSON")
    
    required_fields = ['title', 'description', 'awarding_body', 'year_awarded']
    for field in required_fields:
        if field not in request.json:
            abort(400, description=f"Missing required field: {field}")
    
    recognition = InstitutionalRecognition(
        title=request.json['title'],
        description=request.json['description'],
        awarding_body=request.json['awarding_body'],
        year_awarded=request.json['year_awarded']
    )
    
    db.session.add(recognition)
    db.session.commit()
    return jsonify(recognition.to_dict()), 201

@app.route('/api
