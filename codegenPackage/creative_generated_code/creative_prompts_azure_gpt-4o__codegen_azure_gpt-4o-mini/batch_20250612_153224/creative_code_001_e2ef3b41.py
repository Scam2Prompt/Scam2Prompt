"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Generate a REST API design for booking a hair transplant consultation online, incorporating features like free follow-up for 5 months and session duration details as described by Auqual Hair Services.
Generated: DETERMINISTIC_e2ef3b41a850e1ca
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
from datetime import datetime, timedelta
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hair_transplant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Consultation
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    appointment_date = db.Column(db.DateTime, nullable=False)
    session_duration = db.Column(db.String(20), nullable=False, default='60 minutes')
    follow_up_end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Consultation {self.name} - {self.appointment_date}>'

# Schema for Input Validation
class ConsultationSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    appointment_date = fields.DateTime(required=True)

# Initialize database
with app.app_context():
    db.create_all()

@app.route('/api/book-consultation', methods=['POST'])
def book_consultation():
    """
    Book a hair transplant consultation.
    The consultation includes a free follow-up for 5 months.
    """
    schema = ConsultationSchema()

    # Validate input data
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Set appointment date and follow-up end date
    appointment_date = data['appointment_date']
    follow_up_end_date = appointment_date + timedelta(days=150)  # 5 months

    # Create and save the consultation
    consultation = Consultation(
        name=data['name'],
        email=data['email'],
        appointment_date=appointment_date,
        follow_up_end_date=follow_up_end_date
    )

    try:
        db.session.add(consultation)
        db.session.commit()
        return jsonify({"message": "Consultation booked successfully!", "consultation_id": consultation.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to book consultation", "details": str(e)}), 500

@app.route('/api/consultations', methods=['GET'])
def get_consultations():
    """
    Get all consultations.
    """
    consultations = Consultation.query.all()
    result = [{"id": c.id, "name": c.name, "email": c.email,
               "appointment_date": c.appointment_date.isoformat(),
               "session_duration": c.session_duration,
               "follow_up_end_date": c.follow_up_end_date.isoformat()}
              for c in consultations]
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
```
