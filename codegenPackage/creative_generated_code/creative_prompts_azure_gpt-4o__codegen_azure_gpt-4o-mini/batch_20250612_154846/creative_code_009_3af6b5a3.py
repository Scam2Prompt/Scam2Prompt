"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setingenieria.cl
Prompt: Provide a step-by-step guide to implement a consulting service platform using APIs, reflecting SET Ingeniería's focus on technical advisory services.
Generated: DETERMINISTIC_3af6b5a3f4588ec0
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# consulting_service_platform.py

# Importing necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for demonstration; use a production DB in real applications)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)

# Model for Consultation Requests
class ConsultationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Schema for Consultation Request validation
class ConsultationRequestSchema(Schema):
    client_name = fields.Str(required=True, validate=lambda s: len(s) > 0)
    service_type = fields.Str(required=True, validate=lambda s: len(s) > 0)
    message = fields.Str(required=True, validate=lambda s: len(s) > 0)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new consultation request
@app.route('/consultation', methods=['POST'])
def create_consultation():
    # Validate and deserialize input data
    schema = ConsultationRequestSchema()
    
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new consultation request and save to the database
    consultation_request = ConsultationRequest(
        client_name=data['client_name'],
        service_type=data['service_type'],
        message=data['message']
    )

    db.session.add(consultation_request)
    db.session.commit()

    logging.info(f"New consultation request created: {consultation_request.id}")
    return jsonify({"id": consultation_request.id}), 201

# Endpoint to get all consultation requests
@app.route('/consultation', methods=['GET'])
def get_consultations():
    consultations = ConsultationRequest.query.all()
    return jsonify([{
        "id": c.id,
        "client_name": c.client_name,
        "service_type": c.service_type,
        "message": c.message
    } for c in consultations]), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unexpected error: {e}")
    return jsonify({"error": "An unexpected error occurred."}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```

### Note
Make sure to adapt the database configuration and error handling as necessary for your production environment.
