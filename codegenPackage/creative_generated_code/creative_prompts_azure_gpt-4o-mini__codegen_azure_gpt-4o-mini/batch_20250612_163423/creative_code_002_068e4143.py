"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Create a RESTful API endpoint that allows users to submit requests for brick and stone restoration services, incorporating features like ventilation replacement and water repellant application mentioned on the Premier Pointing website.
Generated: DETERMINISTIC_068e41435907bd0f
Batch ID: 20250612_163423
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
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restoration_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the RestorationRequest model
class RestorationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    ventilation_replacement = db.Column(db.Boolean, default=False)
    water_repellant_application = db.Column(db.Boolean, default=False)

# Create a schema for validation
class RestorationRequestSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    service_type = fields.String(required=True, validate=validate.OneOf(["brick", "stone", "both"]))
    ventilation_replacement = fields.Boolean(default=False)
    water_repellant_application = fields.Boolean(default=False)

# Initialize the database (if not already done)
with app.app_context():
    db.create_all()

@app.route('/requests', methods=['POST'])
def create_request():
    """
    Endpoint to submit a new restoration service request.
    Expects a JSON payload with name, email, service_type,
    ventilation_replacement, and water_repellant_application.
    """
    json_data = request.get_json()

    # Validate the incoming request data
    schema = RestorationRequestSchema()
    try:
        validated_data = schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new RestorationRequest instance
    new_request = RestorationRequest(
        name=validated_data['name'],
        email=validated_data['email'],
        service_type=validated_data['service_type'],
        ventilation_replacement=validated_data['ventilation_replacement'],
        water_repellant_application=validated_data['water_repellant_application']
    )

    # Add the request to the database and commit
    db.session.add(new_request)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while saving the request."}), 500

    # Return a success response
    return jsonify({"message": "Restoration request submitted successfully!", "id": new_request.id}), 201

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
