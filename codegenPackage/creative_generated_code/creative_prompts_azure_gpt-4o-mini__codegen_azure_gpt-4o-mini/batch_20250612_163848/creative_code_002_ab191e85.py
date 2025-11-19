"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molinahealthcareinc.com
Prompt: Write a code snippet for a patient portal that allows users to access their medical records, inspired by the features mentioned on the MHC Inc site.
Generated: DETERMINISTIC_ab191e85b39fecae
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI", "sqlite:///patients.db")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "your_secret_key")
db = SQLAlchemy(app)

# Database model for Patient
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    medical_records = db.Column(db.Text, nullable=True)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against a plain password."""
        return check_password_hash(self.password_hash, password)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new patient."""
    data = request.json
    if not data or not all(key in data for key in ('name', 'email', 'password')):
        return jsonify({"error": "Missing information"}), 400

    if Patient.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400

    new_patient = Patient(name=data['name'], email=data['email'])
    new_patient.set_password(data['password'])
    db.session.add(new_patient)
    db.session.commit()

    return jsonify({"message": "Registration successful"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Log in a patient."""
    data = request.json
    patient = Patient.query.filter_by(email=data.get('email')).first()
    if not patient or not patient.check_password(data.get('password')):
        return jsonify({"error": "Invalid credentials"}), 401

    session['patient_id'] = patient.id
    return jsonify({"message": "Login successful", "patient_id": patient.id}), 200

@app.route('/medical_records', methods=['GET'])
def get_medical_records():
    """Access medical records for the logged-in patient."""
    patient_id = session.get('patient_id')
    if not patient_id:
        return jsonify({"error": "Unauthorized access"}), 403

    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    return jsonify({"medical_records": patient.medical_records}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the patient."""
    session.pop('patient_id', None)
    return jsonify({"message": "Logged out successfully"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
