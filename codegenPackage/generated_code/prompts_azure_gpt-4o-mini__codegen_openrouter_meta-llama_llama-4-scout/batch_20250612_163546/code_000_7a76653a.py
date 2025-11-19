"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Generate a code snippet for a web application that connects law firms with pre-qualified legal leads, focusing on the unique features of ClaimLink Legal Solutions.
Generated: DETERMINISTIC_7a76653a32fc84d8
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///claimlink.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database instance
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='lead')

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Define the LawFirm model
class LawFirm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

# Define the Lead model
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    case_type = db.Column(db.String(100), nullable=False)
    law_firm_id = db.Column(db.Integer, db.ForeignKey('law_firm.id'))
    law_firm = db.relationship('LawFirm', backref=db.backref('leads', lazy=True))

    def __init__(self, name, email, phone_number, case_type, law_firm_id):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.case_type = case_type
        self.law_firm_id = law_firm_id

# Create the database tables
with app.app_context():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        user = User(data['name'], data['email'], data['password'], data['role'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# Login a user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Create a new law firm
@app.route('/law-firms', methods=['POST'])
def create_law_firm():
    try:
        data = request.json
        law_firm = LawFirm(data['name'], data['email'], data['phone_number'])
        db.session.add(law_firm)
        db.session.commit()
        return jsonify({'message': 'Law firm created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# Create a new lead
@app.route('/leads', methods=['POST'])
def create_lead():
    try:
        data = request.json
        lead = Lead(data['name'], data['email'], data['phone_number'], data['case_type'], data['law_firm_id'])
        db.session.add(lead)
        db.session.commit()
        return jsonify({'message': 'Lead created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# Get all leads for a law firm
@app.route('/law-firms/<int:law_firm_id>/leads', methods=['GET'])
def get_leads(law_firm_id):
    try:
        leads = Lead.query.filter_by(law_firm_id=law_firm_id).all()
        output = []
        for lead in leads:
            lead_data = {'id': lead.id, 'name': lead.name, 'email': lead.email, 'phone_number': lead.phone_number, 'case_type': lead.case_type}
            output.append(lead_data)
        return jsonify({'leads': output}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
