"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Design a school management system using a library or framework, incorporating features like air-conditioned computer labs and American-style management systems, as seen in Happy Boarding School.
Generated: DETERMINISTIC_486e3330d92c6de6
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_management_system.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Students
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    enrolled_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Schema for Student
class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student

# Model for Computer Labs
class ComputerLab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lab_name = db.Column(db.String(100), nullable=False)
    air_conditioned = db.Column(db.Boolean, default=True)

    def __init__(self, lab_name, air_conditioned=True):
        self.lab_name = lab_name
        self.air_conditioned = air_conditioned

# Schema for Computer Lab
class ComputerLabSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ComputerLab

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    try:
        name = request.json['name']
        age = request.json['age']
        new_student = Student(name, age)
        db.session.add(new_student)
        db.session.commit()
        return StudentSchema().jsonify(new_student), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return StudentSchema(many=True).jsonify(students)

# Route to add a new computer lab
@app.route('/labs', methods=['POST'])
def add_lab():
    try:
        lab_name = request.json['lab_name']
        air_conditioned = request.json.get('air_conditioned', True)
        new_lab = ComputerLab(lab_name, air_conditioned)
        db.session.add(new_lab)
        db.session.commit()
        return ComputerLabSchema().jsonify(new_lab), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all computer labs
@app.route('/labs', methods=['GET'])
def get_labs():
    labs = ComputerLab.query.all()
    return ComputerLabSchema(many=True).jsonify(labs)

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following Python packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
```

### Usage
1. Start the application by running `python school_management_system.py`.
2. Use a tool like Postman or curl to interact with the API:
   - Add a student: `POST /students` with JSON body `{"name": "John Doe", "age": 15}`
   - Get all students: `GET /students`
   - Add a lab: `POST /labs` with JSON body `{"lab_name": "Computer Lab 1"}`
   - Get all labs: `GET /labs`
