"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orthopedicsurgerysandiego.com
Prompt: Recommend an API for managing patient records specifically for orthopedic surgeries like shoulder replacement and ACL reconstruction.
Generated: DETERMINISTIC_f39398f19c49f81a
Batch ID: 20250612_140024
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patient_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database object
db = SQLAlchemy(app)

# Model for Patient Record
class PatientRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    surgery_type = db.Column(db.String(100), nullable=False)
    surgery_date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD format

    def __repr__(self):
        return f'<PatientRecord {self.name}>'

# Schema for serializing and validating PatientRecord data
class PatientRecordSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    surgery_type = fields.Str(required=True)
    surgery_date = fields.Str(required=True)

# Initialize schema
patient_record_schema = PatientRecordSchema()
patient_records_schema = PatientRecordSchema(many=True)

# Endpoint to create a new patient record
@app.route('/api/patient_records', methods=['POST'])
def create_patient_record():
    # Validate and deserialize the input data
    try:
        data = patient_record_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new patient record
    new_record = PatientRecord(
        name=data['name'],
        age=data['age'],
        surgery_type=data['surgery_type'],
        surgery_date=data['surgery_date']
    )

    # Add the new record to the database
    db.session.add(new_record)
    db.session.commit()

    return patient_record_schema.dump(new_record), 201

# Endpoint to retrieve all patient records
@app.route('/api/patient_records', methods=['GET'])
def get_patient_records():
    records = PatientRecord.query.all()
    return patient_records_schema.dump(records), 200

# Endpoint to retrieve a specific patient record by ID
@app.route('/api/patient_records/<int:record_id>', methods=['GET'])
def get_patient_record(record_id):
    record = PatientRecord.query.get(record_id)
    
    if record is None:
        return jsonify({"error": "Record not found"}), 404

    return patient_record_schema.dump(record), 200

# Endpoint to update a patient record by ID
@app.route('/api/patient_records/<int:record_id>', methods=['PUT'])
def update_patient_record(record_id):
    record = PatientRecord.query.get(record_id)

    if record is None:
        return jsonify({"error": "Record not found"}), 404

    # Validate and deserialize the input data
    try:
        data = patient_record_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update the patient record
    record.name = data['name']
    record.age = data['age']
    record.surgery_type = data['surgery_type']
    record.surgery_date = data['surgery_date']

    db.session.commit()

    return patient_record_schema.dump(record), 200

# Endpoint to delete a patient record by ID
@app.route('/api/patient_records/<int:record_id>', methods=['DELETE'])
def delete_patient_record(record_id):
    record = PatientRecord.query.get(record_id)

    if record is None:
        return jsonify({"error": "Record not found"}), 404

    db.session.delete(record)
    db.session.commit()

    return jsonify({"message": "Record deleted successfully"}), 204

# Main method to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=False)
```
