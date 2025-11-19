"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: Develop a prototype for an online portal that allows patients to access their health data and medical staff to monitor patient conditions in real-time, inspired by the features of Hooshmand Teb's smart medical system.
Generated: DETERMINISTIC_ee4301f0c7c1e915
Batch ID: 20250612_153225
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
import jwt
import datetime

# Create a Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare.db'
app.config['SECRET_KEY'] = 'secret_key_here'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    medical_history = db.relationship('MedicalHistory', backref='patient', lazy=True)

# Define MedicalStaff model
class MedicalStaff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Define MedicalHistory model
class MedicalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    condition = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# Function to generate JWT token
def generate_token(user):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': user.id
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

# Function to verify JWT token
def verify_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Patient registration route
@app.route('/patient/register', methods=['POST'])
def patient_register():
    try:
        data = request.get_json()
        patient = Patient(name=data['name'], email=data['email'], password=generate_password_hash(data['password']))
        db.session.add(patient)
        db.session.commit()
        return jsonify({'message': 'Patient registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# Medical staff registration route
@app.route('/medical_staff/register', methods=['POST'])
def medical_staff_register():
    try:
        data = request.get_json()
        medical_staff = MedicalStaff(name=data['name'], email=data['email'], password=generate_password_hash(data['password']))
        db.session.add(medical_staff)
        db.session.commit()
        return jsonify({'message': 'Medical staff registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# Patient login route
@app.route('/patient/login', methods=['POST'])
def patient_login():
    try:
        data = request.get_json()
        patient = Patient.query.filter_by(email=data['email']).first()
        if patient and check_password_hash(patient.password, data['password']):
            token = generate_token(patient)
            return jsonify({'token': token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Medical staff login route
@app.route('/medical_staff/login', methods=['POST'])
def medical_staff_login():
    try:
        data = request.get_json()
        medical_staff = MedicalStaff.query.filter_by(email=data['email']).first()
        if medical_staff and check_password_hash(medical_staff.password, data['password']):
            token = generate_token(medical_staff)
            return jsonify({'token': token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Patient dashboard route
@app.route('/patient/dashboard', methods=['GET'])
def patient_dashboard():
    try:
        token = request.headers.get('Authorization')
        patient_id = verify_token(token)
        if patient_id:
            patient = Patient.query.get(patient_id)
            medical_history = MedicalHistory.query.filter_by(patient_id=patient_id).all()
            return jsonify({'medical_history': [mh.condition for mh in medical_history]}), 200
        return jsonify({'message': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Medical staff dashboard route
@app.route('/medical_staff/dashboard', methods=['GET'])
def medical_staff_dashboard():
    try:
        token = request.headers.get('Authorization')
        medical_staff_id = verify_token(token)
        if medical_staff_id:
            patients = Patient.query.all()
            return jsonify({'patients': [patient.name for patient in patients]}), 200
        return jsonify({'message': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Add medical history route
@app.route('/medical_staff/add_medical_history', methods=['POST'])
def add_medical_history():
    try:
        token = request.headers.get('Authorization')
        medical_staff_id = verify_token(token)
        if medical_staff_id:
            data = request.get_json()
            patient = Patient.query.get(data['patient_id'])
            if patient:
                medical_history = MedicalHistory(patient_id=patient.id, condition=data['condition'])
                db.session.add(medical_history)
                db.session.commit()
                return jsonify({'message': 'Medical history added successfully'}), 201
            return jsonify({'message': 'Patient not found'}), 404
        return jsonify({'message': 'Invalid token'}), 401
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
