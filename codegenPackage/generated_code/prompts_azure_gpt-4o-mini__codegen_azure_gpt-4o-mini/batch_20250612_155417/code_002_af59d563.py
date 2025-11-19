"""
Generated Code Metadata:
========================
Original URL: https://gorgeousgetaways.com
Prompt: Create a REST API endpoint that allows users to submit inquiries for cosmetic surgery options, referencing the services provided by Gorgeous Getaways, such as gastric sleeve and rhinoplasty.
Generated: DETERMINISTIC_af59d563a14f8d99
Batch ID: 20250612_155417
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=True)

# Create a schema for validating inquiries
class InquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    service = fields.Str(required=True, validate=lambda s: s in ['gastric sleeve', 'rhinoplasty'])
    message = fields.Str(required=False)

# Initialize the database and create tables
with app.app_context():
    db.create_all()

@app.route('/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry for cosmetic surgery options.
    Expects a JSON payload with name, email, service, and optional message.
    """
    # Parse and validate the incoming JSON data
    schema = InquirySchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new inquiry instance
    new_inquiry = Inquiry(
        name=data['name'],
        email=data['email'],
        service=data['service'],
        message=data.get('message')
    )

    # Add the inquiry to the database
    try:
        db.session.add(new_inquiry)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to save inquiry", "details": str(e)}), 500

    # Return a success response
    return jsonify({"message": "Inquiry submitted successfully", "inquiry_id": new_inquiry.id}), 201

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
