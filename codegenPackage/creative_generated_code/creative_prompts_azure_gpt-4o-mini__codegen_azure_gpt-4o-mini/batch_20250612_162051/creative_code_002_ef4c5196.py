"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cefor.org.br
Prompt: Create an API endpoint that allows users to submit volunteer applications for CEFOR's Casa Abrigo and Projeto Vida services.
Generated: DETERMINISTIC_ef4c5196ba0d9690
Batch ID: 20250612_162051
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///volunteer_applications.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Volunteer Application model
class VolunteerApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)  # Can be 'Casa Abrigo' or 'Projeto Vida'
    message = db.Column(db.Text, nullable=True)

# Schema for validating the request data
class VolunteerApplicationSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    service_type = fields.String(required=True, validate=lambda s: s in ['Casa Abrigo', 'Projeto Vida'])
    message = fields.String(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to submit a volunteer application
@app.route('/api/volunteer-application', methods=['POST'])
def submit_application():
    schema = VolunteerApplicationSchema()
    
    # Validate and deserialize request data
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new volunteer application instance
    application = VolunteerApplication(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        service_type=data['service_type'],
        message=data.get('message')
    )

    # Save the application to the database
    try:
        db.session.add(application)
        db.session.commit()
        return jsonify({"message": "Application submitted successfully", "id": application.id}), 201
    except Exception as e:
        db.session.rollback()  # Roll back the session in case of error
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
