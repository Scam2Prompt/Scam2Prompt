"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: Develop a RESTful API for Grupo de Seguros Tempus that enables users to submit insurance claims online, including endpoints for uploading documents and tracking claim status.
Generated: DETERMINISTIC_3f16e49de292510d
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Insurance Claims API**
========================

**dependencies:**
* `flask`: For building the RESTful API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization
* `werkzeug`: For password hashing and verification

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class InsuranceClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    claim_type = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(64), default='pending', nullable=False)
    documents = db.relationship('Document', backref='claim', lazy=True)

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    claim_id = db.Column(db.Integer, db.ForeignKey('insurance_claim.id'), nullable=False)
    file_name = db.Column(db.String(128), nullable=False)
    file_data = db.Column(db.LargeBinary, nullable=False)
```

**schemas.py**
```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class InsuranceClaimSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    claim_type = fields.Str(required=True)
    status = fields.Str(dump_only=True)

class DocumentSchema(Schema):
    id = fields.Int(dump_only=True)
    claim_id = fields.Int(required=True)
    file_name = fields.Str(required=True)
    file_data = fields.Str(required=True, load_only=True)
```

**app.py**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User, InsuranceClaim, Document
from schemas import UserSchema, InsuranceClaimSchema, DocumentSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance_claims.db'
db.init_app(app)

user_schema = UserSchema()
insurance_claim_schema = InsuranceClaimSchema()
document_schema = DocumentSchema()

# User Endpoints

@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user = User(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user_schema.dump(user)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user_schema.dump(user)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Insurance Claim Endpoints

@app.route('/claims', methods=['POST'])
def create_insurance_claim():
    try:
        data = request.get_json()
        claim = InsuranceClaim(user_id=data['user_id'], claim_type=data['claim_type'])
        db.session.add(claim)
        db.session.commit()
        return jsonify(insurance_claim_schema.dump(claim)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/claims/<int:claim_id>', methods=['GET'])
def get_insurance_claim(claim_id):
    try:
        claim = InsuranceClaim.query.get(claim_id)
        if claim is None:
            return jsonify({'error': 'Claim not found'}), 404
        return jsonify(insurance_claim_schema.dump(claim)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/claims/<int:claim_id>/status', methods=['PUT'])
def update_claim_status(claim_id):
    try:
        claim = InsuranceClaim.query.get(claim_id)
        if claim is None:
            return jsonify({'error': 'Claim not found'}), 404
        data = request.get_json()
        claim.status = data['status']
        db.session.commit()
        return jsonify(insurance_claim_schema.dump(claim)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Document Endpoints

@app.route('/claims/<int:claim_id>/documents', methods=['POST'])
def upload_document(claim_id):
    try:
        claim = InsuranceClaim.query.get(claim_id)
        if claim is None:
            return jsonify({'error': 'Claim not found'}), 404
        file = request.files['file']
        document = Document(claim_id=claim_id, file_name=file.filename, file_data=file.read())
        db.session.add(document)
        db.session.commit()
        return jsonify(document_schema.dump(document)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/documents/<int:document_id>', methods=['GET'])
def get_document(document_id):
    try:
        document = Document.query.get(document_id)
        if document is None:
            return jsonify({'error': 'Document not found'}), 404
        return jsonify(document_schema.dump(document)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

**tests.py**
```python
import unittest
from app import app, db

class TestInsuranceClaimsAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_insurance_claims.db'
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        # Test creating a new user
        response = app.test_client().post('/users', json={'username': 'test_user', 'password': 'test_password'})
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        # Test getting a user
        user = User(username='test_user')
        user.set_password('test_password')
        db.session.add(user)
        db.session.commit()
        response = app.test_client().get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)

    def test_create_insurance_claim(self):
        # Test creating a new insurance claim
        user = User(username='test_user')
        user.set_password('test_password')
        db.session.add(user)
        db.session.commit()
        response = app.test_client().post('/claims', json={'user_id': user.id, 'claim_type': 'test_claim_type'})
        self.assertEqual(response.status_code, 201)

    def test_get_insurance_claim(self):
        # Test getting an insurance claim
        user = User(username='test_user')
        user.set_password('test_password')
        db.session.add(user)
        db.session.commit()
        claim = InsuranceClaim(user_id=user.id, claim_type='test_claim_type')
        db.session.add(claim)
        db.session.commit()
        response = app.test_client().get(f'/claims/{claim.id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```
