"""
Generated Code Metadata:
========================
Original URL: https://dfivetechnologies.com
Prompt: Suggest a framework for a healthcare application that aligns with the project portfolio of DFIVE Technologies, focusing on quality and productivity.
Generated: DETERMINISTIC_e4c9f82219b25185
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# healthcare_app_framework.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import os
from datetime import timedelta
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///healthcare.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Configure logging
handler = RotatingFileHandler('healthcare_app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False, default='patient')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class PatientRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    diagnosis = db.Column(db.String(200))
    treatment = db.Column(db.String(200))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

# Marshmallow Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password_hash',)

class PatientRecordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PatientRecord

user_schema = UserSchema()
users_schema = UserSchema(many=True)
patient_record_schema = PatientRecordSchema()
patient_records_schema = PatientRecordSchema(many=True)

# API Routes
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'Username already exists'}), 400

        new_user = User(
            username=data['username'],
            email=data['email'],
            role=data.get('role', 'patient')
        )
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        app.logger.error(f"Registration error: {str(e)}")
        return jsonify({'message': 'Registration failed'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()

        if not user or not user.check_password(data['password']):
            return jsonify({'message': 'Invalid credentials'}), 401

        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    except Exception as e:
        app.logger.error(f"Login error: {str(e)}")
        return jsonify({'message': 'Login failed'}), 500

@app.route('/api/patient-records', methods=['GET'])
@jwt_required()
def get_patient_records():
    try:
        records = PatientRecord.query.all()
        return patient_records_schema.jsonify(records), 200
    except Exception as e:
        app.logger.error(f"Get records error: {str(e)}")
        return jsonify({'message': 'Failed to retrieve records'}), 500

@app.route('/api/patient-records', methods=['POST'])
@jwt_required()
def add_patient_record():
    try:
        data = request.get_json()
        new_record = PatientRecord(
            patient_id=data['patient_id'],
            diagnosis=data['diagnosis'],
            treatment=data['treatment'],
            notes=data.get('notes', '')
        )
        db.session.add(new_record)
        db.session.commit()
        return jsonify({'message': 'Record added successfully'}), 201
    except Exception as e:
        app.logger.error(f"Add record error: {str(e)}")
        db.session.rollback()
        return jsonify({'message': 'Failed to add record'}), 500

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Server error: {str(error)}")
    return jsonify({'message': 'Internal server error'}), 500

# Health Check
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
