"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Design a RESTful API for integrating safety and health coordination services with other construction management systems, following AFCO's guidelines and French regulations.
Generated: DETERMINISTIC_c4d53ecb0c7dd4da
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
api = Api(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safety_health.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Should be changed in production

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'coordinator', 'contractor'
    company = db.Column(db.String(100), nullable=False)

class SafetyDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    file_path = db.Column(db.String(200), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected'
    compliance_standard = db.Column(db.String(50), nullable=False)  # e.g., 'AFCO', 'French Regulation XYZ'

class IncidentReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_occurred = db.Column(db.DateTime, nullable=False)
    severity = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high', 'critical'
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='open')  # 'open', 'investigating', 'resolved'
    location = db.Column(db.String(100), nullable=False)

# Marshmallow Schemas for validation
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    role = fields.Str(required=True)
    company = fields.Str(required=True)

class SafetyDocumentSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    file_path = fields.Str(required=True)
    upload_date = fields.DateTime(dump_only=True)
    uploader_id = fields.Int(required=True)
    status = fields.Str()
    compliance_standard = fields.Str(required=True)

class IncidentReportSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    date_occurred = fields.DateTime(required=True)
    severity = fields.Str(required=True)
    reporter_id = fields.Int(required=True)
    status = fields.Str()
    location = fields.Str(required=True)

# Initialize schemas
user_schema = UserSchema()
safety_document_schema = SafetyDocumentSchema()
incident_report_schema = IncidentReportSchema()

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# API Resources
class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        
        try:
            data = user_schema.load(data)
        except ValidationError as err:
            return err.messages, 400
        
        hashed_password = generate_password_hash(data['password'], method='sha256')
        
        new_user = User(
            username=data['username'],
            password=hashed_password,
            role=data['role'],
            company=data['company']
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return {'message': 'New user created!'}, 201

class UserLogin(Resource):
    def post(self):
        auth = request.authorization
        
        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
        user = User.query.filter_by(username=auth.username).first()
        
        if not user:
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
        if check_password_hash(user.password, auth.password):
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, app.config['SECRET_KEY'])
            
            return jsonify({'token': token})
        
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

class SafetyDocumentResource(Resource):
    @token_required
    def get(self, current_user, document_id=None):
        if document_id:
            document = SafetyDocument.query.get(document_id)
            if not document:
                return {'message': 'Document not found'}, 404
            return safety_document_schema.dump(document)
        else:
            documents = SafetyDocument.query.all()
            return jsonify([safety_document_schema.dump(doc) for doc in documents])
    
    @token_required
    def post(self, current_user):
        data = request.get_json()
        
        try:
            data = safety_document_schema.load(data)
        except ValidationError as err:
            return err.messages, 400
        
        new_document = SafetyDocument(
            title=data['title'],
            description=data.get('description'),
            file_path=data['file_path'],
            uploader_id=current_user.id,
            compliance_standard=data['compliance_standard']
        )
        
        db.session.add(new_document)
        db.session.commit()
        
        return {'message': 'Safety document created!'}, 201
    
    @token_required
    def put(self, current_user, document_id):
        document = SafetyDocument.query.get(document_id)
        if not document:
            return {'message': 'Document not found'}, 404
        
        data = request.get_json()
        
        try:
            data = safety_document_schema.load(data, partial=True)
        except ValidationError as err:
            return err.messages, 400
        
        if 'title' in data:
            document.title = data['title']
        if 'description' in data:
            document.description = data['description']
        if 'status' in data and current_user.role == 'admin':
            document.status = data['status']
        
        db.session.commit()
        
        return {'message': 'Document updated successfully'}

class IncidentReportResource(Resource):
    @token_required
    def get(self, current_user, report_id=None):
        if report_id:
            report = IncidentReport.query.get(report_id)
            if not report:
                return {'message': 'Report not found'}, 404
            return incident_report_schema.dump(report)
        else:
            reports = IncidentReport.query.all()
            return jsonify([incident_report_schema.dump(rep) for rep in reports])
    
    @token_required
    def post(self, current_user):
        data = request.get_json()
        
        try:
            data = incident_report_schema.load(data)
        except ValidationError as err:
            return err.messages, 400
        
        new_report = IncidentReport(
            title=data['title'],
            description=data['description'],
            date_occurred=data['date_occurred'],
            severity=data['severity'],
            reporter_id=current_user.id,
            location=data['location']
        )
        
        db.session.add(new_report)
        db.session.commit()
        
        return {'message': 'Incident report created!'}, 201
    
    @token_required
    def put(self, current_user, report_id):
        report = IncidentReport.query.get(report_id)
        if not report:
            return {'message': 'Report not found'}, 404
        
        data = request.get_json()
        
        try:
