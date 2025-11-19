"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: Generate a code snippet for a web application that allows users to request printing services for items like flyers and business cards, similar to the offerings of Detalj Reklam.
Generated: DETERMINISTIC_e73ce228601b3396
Batch ID: 20250612_161500
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///printing_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model for print requests
class PrintRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)

# Create a schema for validating input data
class PrintRequestSchema(Schema):
    item_type = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)
    customer_name = fields.Str(required=True)
    customer_email = fields.Email(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to request printing services
@app.route('/api/print-request', methods=['POST'])
def request_printing():
    # Parse and validate the incoming JSON data
    schema = PrintRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new print request
    new_request = PrintRequest(
        item_type=data['item_type'],
        quantity=data['quantity'],
        customer_name=data['customer_name'],
        customer_email=data['customer_email']
    )

    # Add the request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create print request", "details": str(e)}), 500

    return jsonify({"message": "Print request created successfully", "id": new_request.id}), 201

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
