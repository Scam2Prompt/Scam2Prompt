"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phuketmedicalclinic.com
Prompt: Illustrate how to implement a secure API for managing vaccination records, focusing on user authentication and data privacy for a medical clinic.
Generated: DETERMINISTIC_1d70103c35e1f918
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask app, database, bcrypt, and JWT manager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vaccination_records.db'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_secret_key')  # Change this in production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Database model for Vaccination Record
class VaccinationRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vaccine_name = db.Column(db.String(120), nullable=False)
    vaccination_date = db.Column(db.Date, nullable=False)

# Schema for user registration
class UserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

# Schema for vaccination records
class VaccinationRecordSchema(Schema):
    vaccine_name = fields.String(required=True)
    vaccination_date = fields.Date(required=True)

user_schema = UserSchema()
record_schema = VaccinationRecordSchema()

@app.route('/register', methods=['POST'])
def register():
    """Endpoint for user registration."""
    try:
        data = user_schema.load(request.json)
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User registered successfully"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"msg": "Registration failed", "error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/records', methods=['POST'])
@jwt_required()
def add_record():
    """Endpoint to add a vaccination record."""
    user_id = get_jwt_identity()
    try:
        data = record_schema.load(request.json)
        new_record = VaccinationRecord(user_id=user_id, **data)
        db.session.add(new_record)
        db.session.commit()
        return jsonify({"msg": "Record added successfully"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"msg": "Failed to add record", "error": str(e)}), 500

@app.route('/records', methods=['GET'])
@jwt_required()
def get_records():
    """Endpoint to retrieve vaccination records for the logged-in user."""
    user_id = get_jwt_identity()
    records = VaccinationRecord.query.filter_by(user_id=user_id).all()
    return jsonify([{"vaccine_name": record.vaccine_name, "vaccination_date": record.vaccination_date.isoformat()} for record in records]), 200

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug to False in production
```
