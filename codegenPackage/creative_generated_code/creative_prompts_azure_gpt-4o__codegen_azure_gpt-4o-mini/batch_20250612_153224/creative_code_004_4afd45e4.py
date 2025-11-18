"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Develop a REST API in Flask that allows users to schedule consultations for foot and ankle conditions, including bunions, Achilles tendon injuries, and ankle arthritis.
Generated: DETERMINISTIC_4afd45e43ded9f2c
Batch ID: 20250612_153224
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for consultations
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    condition = db.Column(db.String(100), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Consultation {self.id} - {self.patient_name}>'

# Schema for validating input data
class ConsultationSchema(Schema):
    patient_name = fields.Str(required=True)
    condition = fields.Str(required=True, validate=lambda s: s in ["bunions", "Achilles tendon injuries", "ankle arthritis"])
    scheduled_time = fields.DateTime(required=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for scheduling a consultation
@app.route('/consultations', methods=['POST'])
def schedule_consultation():
    # Validate the incoming request data
    schema = ConsultationSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new consultation record
    new_consultation = Consultation(
        patient_name=data['patient_name'],
        condition=data['condition'],
        scheduled_time=data['scheduled_time']
    )

    # Save the record to the database
    try:
        db.session.add(new_consultation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to schedule consultation", "details": str(e)}), 500

    return jsonify({"message": "Consultation scheduled successfully", "consultation": data}), 201

# Route for fetching all consultations
@app.route('/consultations', methods=['GET'])
def get_consultations():
    consultations = Consultation.query.all()
    consultations_list = [
        {
            "id": con.id,
            "patient_name": con.patient_name,
            "condition": con.condition,
            "scheduled_time": con.scheduled_time.isoformat()
        } for con in consultations
    ]
    return jsonify(consultations_list), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
