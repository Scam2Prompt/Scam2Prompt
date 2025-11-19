"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Create a RESTful API endpoint for a volunteer registration system that aligns with the community engagement initiatives of the NICER Foundation.
Generated: DETERMINISTIC_c6ed794a04652095
Batch ID: 20250612_160507
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

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///volunteers.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Volunteer model representing the volunteers table
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    skills = db.Column(db.String(255), nullable=True)

# Schema for validating volunteer input
class VolunteerSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    skills = fields.Str(required=False)

# Create the volunteers table
with app.app_context():
    db.create_all()

# Endpoint for registering a new volunteer
@app.route('/api/volunteers', methods=['POST'])
def register_volunteer():
    schema = VolunteerSchema()
    
    # Validate and deserialize the input
    try:
        volunteer_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new volunteer instance
    new_volunteer = Volunteer(**volunteer_data)
    
    # Add the new volunteer to the database
    try:
        db.session.add(new_volunteer)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to register volunteer", "details": str(e)}), 500

    return jsonify({"message": "Volunteer registered successfully", "volunteer": volunteer_data}), 201

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
