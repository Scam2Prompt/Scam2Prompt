"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Create a RESTful API endpoint that allows users to submit requests for brick and stone restoration services, incorporating features like ventilation replacement and water repellant application mentioned on the Premier Pointing website.
Generated: DETERMINISTIC_068e41435907bd0f
Batch ID: 20250612_163423
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for restoration requests
class RestorationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    ventilation_replacement = db.Column(db.Boolean, default=False)
    water_repellant_application = db.Column(db.Boolean, default=False)

# Schema for validating input data
class RestorationRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    service_type = fields.Str(required=True)
    ventilation_replacement = fields.Bool(missing=False)
    water_repellant_application = fields.Bool(missing=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# RESTful API endpoint to submit restoration requests
@app.route('/api/restoration-request', methods=['POST'])
def submit_request():
    # Validate and deserialize input data
    schema = RestorationRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new restoration request
    new_request = RestorationRequest(
        name=data['name'],
        email=data['email'],
        service_type=data['service_type'],
        ventilation_replacement=data['ventilation_replacement'],
        water_repellant_application=data['water_repellant_application']
    )

    # Add the request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to save request", "details": str(e)}), 500

    # Return a success response
    return jsonify({"message": "Request submitted successfully", "id": new_request.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
