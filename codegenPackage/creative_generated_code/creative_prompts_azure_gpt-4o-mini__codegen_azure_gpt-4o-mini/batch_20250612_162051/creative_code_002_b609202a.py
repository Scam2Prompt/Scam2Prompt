"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-almamlaka.com
Prompt: Generate a code snippet for a web application that allows users to request cleaning services, similar to the comprehensive services offered by شمس المملكة.
Generated: DETERMINISTIC_b609202a1f94fe16
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Cleaning Service model
class CleaningService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)

# Create a schema for input validation
class CleaningServiceSchema(Schema):
    customer_name = fields.Str(required=True, validate=validate.Length(min=1))
    service_type = fields.Str(required=True, validate=validate.OneOf(["Home", "Office", "Commercial"]))
    contact_number = fields.Str(required=True, validate=validate.Length(min=10, max=15))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to request a cleaning service
@app.route('/request_service', methods=['POST'])
def request_service():
    # Parse and validate incoming JSON data
    schema = CleaningServiceSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new cleaning service request
    new_service = CleaningService(**data)

    # Add the service request to the database
    try:
        db.session.add(new_service)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Cleaning service requested successfully!"}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
