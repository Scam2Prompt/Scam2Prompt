"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utkutantoglu.com
Prompt: Describe how to implement a consultation scheduling API for a clinic specializing in obesity and metabolic surgery, including features for multiple languages like Turkish and English.
Generated: DETERMINISTIC_59ca7c4d12ee95ce
Batch ID: 20250612_160853
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
from flask_babel import Babel, gettext as _
from datetime import datetime
from marshmallow import Schema, fields, ValidationError
import pytz

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Babel for multilingual support
babel = Babel(app)

# Define a simple model for consultations
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    consultation_time = db.Column(db.DateTime, nullable=False)

# Consultation schema for request validation
class ConsultationSchema(Schema):
    patient_name = fields.String(required=True)
    email = fields.String(required=True)
    consultation_time = fields.DateTime(required=True)

# Define the language selection function for Babel
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'tr'])

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/schedule', methods=['POST'])
def schedule_consultation():
    """Endpoint to schedule a consultation."""
    
    # Parse and validate the incoming JSON data
    schema = ConsultationSchema()
    
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Ensure consultation time is in the future
    if data['consultation_time'] < datetime.now(pytz.utc):
        return jsonify({"error": _("Consultation time must be in the future.")}), 400

    # Create a new consultation entry
    consultation = Consultation(
        patient_name=data['patient_name'],
        email=data['email'],
        consultation_time=data['consultation_time']
    )

    # Attempt to save the consultation to the database
    try:
        db.session.add(consultation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of any error
        return jsonify({"error": _("Failed to schedule consultation.")}), 500

    return jsonify({"message": _("Consultation scheduled successfully."), "consultation_id": consultation.id}), 201

@app.route('/consultations/<int:consultation_id>', methods=['GET'])
def get_consultation(consultation_id):
    """Endpoint to retrieve a consultation by ID."""
    consultation = Consultation.query.get(consultation_id)
    
    if consultation is None:
        return jsonify({"error": _("Consultation not found.")}), 404

    return jsonify({
        "id": consultation.id,
        "patient_name": consultation.patient_name,
        "email": consultation.email,
        "consultation_time": consultation.consultation_time.isoformat()
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```

Ensure you have the required packages installed by running:
```bash
pip install Flask Flask-SQLAlchemy Flask-Babel marshmallow pytz
```

This implementation provides a simple API for scheduling consultations, supporting both Turkish and English languages.
