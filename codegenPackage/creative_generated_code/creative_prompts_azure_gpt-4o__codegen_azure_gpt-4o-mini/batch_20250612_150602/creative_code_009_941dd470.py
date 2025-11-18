"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Suggest an API for managing employee appreciation programs, referencing PDC Brush's initiative to celebrate staff contributions with gifts.
Generated: DETERMINISTIC_941dd470b9e7c773
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appreciation_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Employee
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contributions = db.relationship('Contribution', backref='employee', lazy=True)

# Model for Contribution
class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for serialization and validation
class ContributionSchema(Schema):
    employee_id = fields.Int(required=True, validate=validate.Range(min=1))
    description = fields.Str(required=True, validate=validate.Length(min=1, max=255))

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = Employee(name=data['name'], email=data['email'])
    
    try:
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({"message": "Employee added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{"id": emp.id, "name": emp.name, "email": emp.email} for emp in employees]), 200

# Endpoint to log a new contribution
@app.route('/contributions', methods=['POST'])
def add_contribution():
    data = request.json

    # Validate input data
    try:
        ContributionSchema().load(data)
        new_contribution = Contribution(employee_id=data['employee_id'], description=data['description'])
        db.session.add(new_contribution)
        db.session.commit()
        return jsonify({"message": "Contribution added successfully!"}), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to get contributions for an employee
@app.route('/employees/<int:employee_id>/contributions', methods=['GET'])
def get_contributions(employee_id):
    contributions = Contribution.query.filter_by(employee_id=employee_id).all()
    return jsonify([{"id": contrib.id, "description": contrib.description, "date": contrib.date} for contrib in contributions]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
