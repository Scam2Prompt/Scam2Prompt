"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: How can I develop an API that provides information on the legal requirements and costs for temporary registration in Adygea?
Generated: DETERMINISTIC_fc98823783f444fd
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adygea_registration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for the registration information
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requirement = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Float, nullable=False)

# Create a schema for input validation
class RegistrationSchema(Schema):
    requirement = fields.String(required=True)
    cost = fields.Float(required=True)

# Initialize the schema
registration_schema = RegistrationSchema()
registrations_schema = RegistrationSchema(many=True)

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({'errors': error.messages}), 400

# API endpoint to get all registration information
@app.route('/api/registration', methods=['GET'])
def get_registrations():
    """Retrieve all registration requirements and costs."""
    registrations = Registration.query.all()
    return jsonify(registrations_schema.dump(registrations)), 200

# API endpoint to add new registration information
@app.route('/api/registration', methods=['POST'])
def add_registration():
    """Add a new registration requirement and cost."""
    try:
        # Validate incoming data
        data = request.get_json()
        registration_data = registration_schema.load(data)
        
        # Create a new registration instance
        new_registration = Registration(
            requirement=registration_data['requirement'],
            cost=registration_data['cost']
        )
        
        # Add to the database
        db.session.add(new_registration)
        db.session.commit()
        
        return jsonify(registration_schema.dump(new_registration)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database and tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

Make sure to install the required packages before running the code:

```bash
pip install Flask Flask-SQLAlchemy marshmallow
```
