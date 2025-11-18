"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Suggest an API for managing occupational health records and compliance with INPSASEL regulations, similar to the services offered by Grupo Clínico IDET.
Generated: DETERMINISTIC_61eadee99f58170d
Batch ID: 20250612_154251
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
import os

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///health_records.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Occupational Health Record
class OccupationalHealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), nullable=False)
    medical_history = db.Column(db.Text, nullable=True)
    compliance_status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Record {self.id} for Employee {self.employee_id}>'

# Schema for validation
class OccupationalHealthRecordSchema(Schema):
    employee_id = fields.Str(required=True)
    medical_history = fields.Str(allow_none=True)
    compliance_status = fields.Str(required=True)

# Initialize the schema
record_schema = OccupationalHealthRecordSchema()
records_schema = OccupationalHealthRecordSchema(many=True)

# Error handling
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Endpoint to create a new health record
@app.route('/records', methods=['POST'])
def create_record():
    """Create a new occupational health record."""
    json_data = request.get_json()
    try:
        data = record_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_record = OccupationalHealthRecord(**data)
    db.session.add(new_record)
    db.session.commit()
    return record_schema.jsonify(new_record), 201

# Endpoint to retrieve all health records
@app.route('/records', methods=['GET'])
def get_records():
    """Retrieve all occupational health records."""
    records = OccupationalHealthRecord.query.all()
    return records_schema.jsonify(records), 200

# Endpoint to retrieve a single health record by ID
@app.route('/records/<int:id>', methods=['GET'])
def get_record(id):
    """Retrieve a specific occupational health record by ID."""
    record = OccupationalHealthRecord.query.get_or_404(id)
    return record_schema.jsonify(record), 200

# Endpoint to update a health record
@app.route('/records/<int:id>', methods=['PUT'])
def update_record(id):
    """Update an existing occupational health record."""
    json_data = request.get_json()
    try:
        data = record_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    record = OccupationalHealthRecord.query.get_or_404(id)
    for key, value in data.items():
        setattr(record, key, value)
    
    db.session.commit()
    return record_schema.jsonify(record), 200

# Endpoint to delete a health record
@app.route('/records/<int:id>', methods=['DELETE'])
def delete_record(id):
    """Delete an occupational health record."""
    record = OccupationalHealthRecord.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({'message': 'Record deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```
