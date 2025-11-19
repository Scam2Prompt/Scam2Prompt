"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Create a code snippet that demonstrates how to build a user registration and login system for a job placement platform, inspired by the features on jobONE.
Generated: DETERMINISTIC_8fa92b23ea54b3ac
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_auth.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_placement.db'
app.config['SECRET_KEY'] = 'secret_key_here'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='applicant')

    def __init__(self, username, email, password, role='applicant'):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('employer', lazy=True))

    def __init__(self, company_name, user_id):
        self.company_name = company_name
        self.user_id = user_id

    def __repr__(self):
        return f"Employer('{self.company_name}', '{self.user_id}')"


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'applicant')

        if not username or not email or not password:
            return jsonify({'message': 'Please provide all required fields'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'Email already exists'}), 400

        new_user = User(username, email, password, role)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Please provide all required fields'}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({'message': 'Invalid credentials'}), 401

        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': user.id,
            'role': user.role
        }

        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route('/employer/register', methods=['POST'])
def employer_register():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        user_id = data.get('user_id')
        company_name = data.get('company_name')

        if not user_id or not company_name:
            return jsonify({'message': 'Please provide all required fields'}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        existing_employer = Employer.query.filter_by(user_id=user_id).first()
        if existing_employer:
            return jsonify({'message': 'Employer already exists for this user'}), 400

        new_employer = Employer(company_name, user_id)
        db.session.add(new_employer)
        db.session.commit()

        return jsonify({'message': 'Employer created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
