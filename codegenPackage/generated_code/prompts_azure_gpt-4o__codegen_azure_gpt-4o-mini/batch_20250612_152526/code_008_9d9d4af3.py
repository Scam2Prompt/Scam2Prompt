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
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///institutional_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the AcademicProgram model
class AcademicProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

# Define the AdministrativeService model
class AdministrativeService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=True)

# Define the InstitutionalRecognition model
class InstitutionalRecognition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

# Define schemas for serialization
class AcademicProgramSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str()

class AdministrativeServiceSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    contact_info = fields.Str()

class InstitutionalRecognitionSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    year = fields.Int(required=True)

# Initialize schemas
academic_program_schema = AcademicProgramSchema()
academic_programs_schema = AcademicProgramSchema(many=True)
administrative_service_schema = AdministrativeServiceSchema()
administrative_services_schema = AdministrativeServiceSchema(many=True)
institutional_recognition_schema = InstitutionalRecognitionSchema()
institutional_recognitions_schema = InstitutionalRecognitionSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to retrieve all academic programs
@app.route('/api/programs', methods=['GET'])
def get_academic_programs():
    programs = AcademicProgram.query.all()
    return academic_programs_schema.dump(programs), 200

# Endpoint to retrieve a specific academic program by ID
@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_academic_program(program_id):
    program = AcademicProgram.query.get(program_id)
    if program is None:
        abort(404, description="Program not found")
    return academic_program_schema.dump(program), 200

# Endpoint to create a new academic program
@app.route('/api/programs', methods=['POST'])
def create_academic_program():
    try:
        data = request.get_json()
        program = academic_program_schema.load(data)
        new_program = AcademicProgram(**program)
        db.session.add(new_program)
        db.session.commit()
        return academic_program_schema.dump(new_program), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Endpoint to retrieve all administrative services
@app.route('/api/services', methods=['GET'])
def get_administrative_services():
    services = AdministrativeService.query.all()
    return administrative_services_schema.dump(services), 200

# Endpoint to retrieve a specific administrative service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_administrative_service(service_id):
    service = AdministrativeService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    return administrative_service_schema.dump(service), 200

# Endpoint to create a new administrative service
@app.route('/api/services', methods=['POST'])
def create_administrative_service():
    try:
        data = request.get_json()
        service = administrative_service_schema.load(data)
        new_service = AdministrativeService(**service)
        db.session.add(new_service)
        db.session.commit()
        return administrative_service_schema.dump(new_service), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Endpoint to retrieve all institutional recognitions
@app.route('/api/recognitions', methods=['GET'])
def get_institutional_recognitions():
    recognitions = InstitutionalRecognition.query.all()
    return institutional_recognitions_schema.dump(recognitions), 200

# Endpoint to retrieve a specific institutional recognition by ID
@app.route('/api/recognitions/<int:recognition_id>', methods=['GET'])
def get_institutional_recognition(recognition_id):
    recognition = InstitutionalRecognition.query.get(recognition_id)
    if recognition is None:
        abort(404, description="Recognition not found")
    return institutional_recognition_schema.dump(recognition), 200

# Endpoint to create a new institutional recognition
@app.route('/api/recognitions', methods=['POST'])
def create_institutional_recognition():
    try:
        data = request.get_json()
        recognition = institutional_recognition_schema.load(data)
        new_recognition = InstitutionalRecognition(**recognition)
        db.session.add(new_recognition)
        db.session.commit()
        return institutional_recognition_schema.dump(new_recognition), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
