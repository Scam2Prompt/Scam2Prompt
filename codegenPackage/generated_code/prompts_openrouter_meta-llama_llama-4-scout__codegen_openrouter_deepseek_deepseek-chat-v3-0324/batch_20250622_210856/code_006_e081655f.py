"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Design a RESTful API for a child protection system, incorporating features for reporting and responding to child rights violations.
Generated: DETERMINISTIC_e081655f9a153dac
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import uuid
import jwt
import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///child_protection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.String(20))  # 'admin', 'case_worker', 'reporter'
    reports = db.relationship('Report', backref='user', lazy=True)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    status = db.Column(db.String(20), default='pending')  # 'pending', 'investigating', 'resolved'
    severity = db.Column(db.String(20))  # 'low', 'medium', 'high'
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    responses = db.relationship('Response', backref='report', lazy=True)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'name', 'email', 'role')

class ReportSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'title', 'description', 'location', 'status', 'severity', 'created_at', 'user_id')

class ResponseSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'content', 'created_at', 'report_id', 'user_id')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
report_schema = ReportSchema()
reports_schema = ReportSchema(many=True)
response_schema = ResponseSchema()
responses_schema = ResponseSchema(many=True)

# Decorator for token verification
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
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth['email'] or not auth['password']:
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(email=auth['email']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    
    return jsonify({'message': 'Wrong password'}), 401

@app.route('/api/reports', methods=['GET'])
@token_required
def get_all_reports(current_user):
    if current_user.role not in ['admin', 'case_worker']:
        return jsonify({'message': 'Unauthorized access!'}), 403
    
    reports = Report.query.all()
    return reports_schema.jsonify(reports)

@app.route('/api/reports/<public_id>', methods=['GET'])
@token_required
def get_one_report(current_user, public_id):
    report = Report.query.filter_by(public_id=public_id).first()
    if not report:
        return jsonify({'message': 'Report not found'}), 404
    
    if current_user.role not in ['admin', 'case_worker'] and report.user_id != current_user.id:
        return jsonify({'message': 'Unauthorized access!'}), 403
    
    return report_schema.jsonify(report)

@app.route('/api/reports', methods=['POST'])
@token_required
def create_report(current_user):
    data = request.get_json()
    new_report = Report(
        public_id=str(uuid.uuid4()),
        title=data['title'],
        description=data['description'],
        location=data['location'],
        severity=data['severity'],
        user_id=current_user.id
    )
    db.session.add(new_report)
    db.session.commit()
    return report_schema.jsonify(new_report), 201

@app.route('/api/reports/<public_id>', methods=['PUT'])
@token_required
def update_report(current_user, public_id):
    report = Report.query.filter_by(public_id=public_id).first()
    if not report:
        return jsonify({'message': 'Report not found'}), 404
    
    if current_user.role not in ['admin', 'case_worker'] and report.user_id != current_user.id:
        return jsonify({'message': 'Unauthorized access!'}), 403
    
    data = request.get_json()
    report.title = data.get('title', report.title)
    report.description = data.get('description', report.description)
    report.location = data.get('location', report.location)
    report.status = data.get('status', report.status)
    report.severity = data.get('severity', report.severity)
    
    db.session.commit()
    return report_schema.jsonify(report)

@app.route('/api/reports/<public_id>/responses', methods=['POST'])
@token_required
def create_response(current_user, public_id):
    if current_user.role not in ['admin', 'case_worker']:
        return jsonify({'message': 'Unauthorized access!'}), 403
    
    report = Report.query.filter_by(public_id=public_id).first()
    if not report:
        return jsonify({'message': 'Report not found'}), 404
    
    data = request.get_json()
    new_response = Response(
        public_id=str(uuid.uuid4()),
        content=data['content'],
        report_id=report.id,
        user_id=current_user.id
    )
    db.session.add(new_response)
    db.session.commit()
    return response_schema.jsonify(new_response), 201

@app.route('/api/reports/<public_id>/responses', methods=['GET'])
@token_required
def get_responses(current_user, public_id):
    report = Report.query.filter_by(public_id=public_id).first()
    if not report:
        return jsonify({'message': 'Report not found'}), 404
    
    if current_user.role not in ['admin', 'case_worker'] and report.user_id != current_user.id:
        return jsonify({'message': 'Unauthorized access!'}), 403
    
    responses = Response.query.filter_by(report_id=report.id).all()
    return responses_schema.jsonify(responses)

@app.route('/api/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized access!'}), 403
    
    users = User.query.all()
    return users_schema.jsonify(users)

# Main
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(
