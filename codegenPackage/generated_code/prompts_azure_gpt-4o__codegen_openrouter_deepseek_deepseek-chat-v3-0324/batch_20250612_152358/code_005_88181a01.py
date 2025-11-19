"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Write code to implement a role-based access control system for healthcare professionals in a SUS-inspired system, ensuring that general practitioners, nurses, and community health agents have access to relevant patient data.
Generated: DETERMINISTIC_88181a014dd5f0a6
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass
from functools import wraps
from flask import Flask, request, jsonify, abort
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # In production, use a proper secret key

# Enums for roles and permissions
class Role(Enum):
    GENERAL_PRACTITIONER = "general_practitioner"
    NURSE = "nurse"
    COMMUNITY_HEALTH_AGENT = "community_health_agent"

class Permission(Enum):
    VIEW_PATIENT_RECORDS = "view_patient_records"
    EDIT_PATIENT_RECORDS = "edit_patient_records"
    VIEW_SENSITIVE_DATA = "view_sensitive_data"
    CREATE_PATIENT_RECORDS = "create_patient_records"

# Data classes
@dataclass
class User:
    id: str
    name: str
    role: Role
    permissions: List[Permission]

@dataclass
class PatientRecord:
    id: str
    patient_id: str
    data: Dict
    sensitive: bool = False

# Mock database
users_db = {
    "doc1": User(id="doc1", name="Dr. Smith", role=Role.GENERAL_PRACTITIONER, 
                permissions=[Permission.VIEW_PATIENT_RECORDS, Permission.EDIT_PATIENT_RECORDS, 
                            Permission.VIEW_SENSITIVE_DATA, Permission.CREATE_PATIENT_RECORDS]),
    "nurse1": User(id="nurse1", name="Nurse Johnson", role=Role.NURSE,
                  permissions=[Permission.VIEW_PATIENT_RECORDS, Permission.CREATE_PATIENT_RECORDS]),
    "agent1": User(id="agent1", name="Agent Brown", role=Role.COMMUNITY_HEALTH_AGENT,
                  permissions=[Permission.VIEW_PATIENT_RECORDS])
}

patient_records_db = {
    "rec1": PatientRecord(id="rec1", patient_id="pat1", data={"diagnosis": "flu"}, sensitive=False),
    "rec2": PatientRecord(id="rec2", patient_id="pat2", data={"diagnosis": "HIV"}, sensitive=True)
}

# Authentication and authorization utilities
def generate_token(user_id: str) -> str:
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = {
        'user_id': user_id,
        'exp': expiration
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

def verify_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        abort(401, "Token expired")
    except jwt.InvalidTokenError:
        abort(401, "Invalid token")

def requires_permission(permission: Permission):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                abort(401, "Authorization token missing")
            
            user_id = verify_token(token.split()[1])
            user = users_db.get(user_id)
            if not user:
                abort(404, "User not found")
            
            if permission not in user.permissions:
                abort(403, "Insufficient permissions")
            
            return f(*args, **kwargs, current_user=user)
        return wrapped
    return decorator

# API endpoints
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('user_id')
    
    if not user_id or user_id not in users_db:
        abort(401, "Invalid credentials")
    
    token = generate_token(user_id)
    return jsonify({"token": token})

@app.route('/records/<record_id>', methods=['GET'])
@requires_permission(Permission.VIEW_PATIENT_RECORDS)
def get_record(record_id: str, current_user: User):
    record = patient_records_db.get(record_id)
    if not record:
        abort(404, "Record not found")
    
    if record.sensitive and Permission.VIEW_SENSITIVE_DATA not in current_user.permissions:
        abort(403, "Insufficient permissions to view sensitive data")
    
    return jsonify(record.data)

@app.route('/records', methods=['POST'])
@requires_permission(Permission.CREATE_PATIENT_RECORDS)
def create_record(current_user: User):
    data = request.get_json()
    if not data:
        abort(400, "No data provided")
    
    record_id = f"rec{len(patient_records_db) + 1}"
    sensitive = data.pop('sensitive', False)
    
    if sensitive and Permission.VIEW_SENSITIVE_DATA not in current_user.permissions:
        abort(403, "Insufficient permissions to create sensitive records")
    
    record = PatientRecord(
        id=record_id,
        patient_id=data.get('patient_id'),
        data=data,
        sensitive=sensitive
    )
    patient_records_db[record_id] = record
    return jsonify({"id": record_id}), 201

@app.route('/records/<record_id>', methods=['PUT'])
@requires_permission(Permission.EDIT_PATIENT_RECORDS)
def update_record(record_id: str, current_user: User):
    record = patient_records_db.get(record_id)
    if not record:
        abort(404, "Record not found")
    
    if record.sensitive and Permission.VIEW_SENSITIVE_DATA not in current_user.permissions:
        abort(403, "Insufficient permissions to edit sensitive data")
    
    data = request.get_json()
    if not data:
        abort(400, "No data provided")
    
    record.data.update(data)
    return jsonify(record.data)

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": str(error)}), 401

@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": str(error)}), 403

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
