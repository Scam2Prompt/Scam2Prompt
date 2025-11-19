"""
Generated Code Metadata:
========================
Original URL: https://paybackclaimltd.com
Prompt: Generate a sample code for a web application that helps users report financial fraud and request chargeback services, inspired by Payback Claim Ltd.'s offerings.
Generated: DETERMINISTIC_8cf040a0a8292c22
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///fraud_report.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class FraudReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    chargeback_requested = db.Column(db.Boolean, default=False)

    def __init__(self, user_id, description):
        self.user_id = user_id
        self.description = description

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 400
        new_user = User(email, password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401
        return jsonify({'message': 'Logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/report-fraud', methods=['POST'])
def report_fraud():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        user_id = data.get('user_id')
        description = data.get('description')
        if not user_id or not description:
            return jsonify({'error': 'User ID and description are required'}), 400
        new_report = FraudReport(user_id, description)
        db.session.add(new_report)
        db.session.commit()
        return jsonify({'message': 'Fraud report submitted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/request-chargeback', methods=['POST'])
def request_chargeback():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        report_id = data.get('report_id')
        if not report_id:
            return jsonify({'error': 'Report ID is required'}), 400
        report = FraudReport.query.get(report_id)
        if not report:
            return jsonify({'error': 'Report not found'}), 404
        report.chargeback_requested = True
        db.session.commit()
        return jsonify({'message': 'Chargeback requested successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask
Flask-SQLAlchemy
```

```python
# .env
DATABASE_URL=sqlite:///fraud_report.db
```
