"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Generate a REST API design for booking a hair transplant consultation online, incorporating features like free follow-up for 5 months and session duration details as described by Auqual Hair Services.
Generated: DETERMINISTIC_e2ef3b41a850e1ca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hair_transplant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Consultation
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    follow_up_end_date = db.Column(db.DateTime, nullable=False)

# Schema for input validation
class ConsultationSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    date = fields.DateTime(required=True)
    duration = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to book a consultation
@app.route('/api/consultations', methods=['POST'])
def book_consultation():
    # Validate input data
    schema = ConsultationSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Calculate follow-up end date (5 months from the consultation date)
    follow_up_end_date = data['date'] + timedelta(days=150)

    # Create a new consultation record
    new_consultation = Consultation(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        date=data['date'],
        duration=data['duration'],
        follow_up_end_date=follow_up_end_date
    )

    # Add to the database
    try:
        db.session.add(new_consultation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Consultation booked successfully!", "id": new_consultation.id}), 201

# Endpoint to get all consultations
@app.route('/api/consultations', methods=['GET'])
def get_consultations():
    consultations = Consultation.query.all()
    result = [
        {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "phone": c.phone,
            "date": c.date.isoformat(),
            "duration": c.duration,
            "follow_up_end_date": c.follow_up_end_date.isoformat()
        } for c in consultations
    ]
    return jsonify(result), 200

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
    app.run(debug=False)
```
