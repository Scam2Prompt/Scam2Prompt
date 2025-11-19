"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanaclochayasociados.com
Prompt: Create a REST API endpoint that allows clients to submit inquiries about legal services related to matrimonial and financial law.
Generated: DETERMINISTIC_cf73334450d60011
Batch ID: 20250612_162050
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    legal_area = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define a schema for input validation
class InquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)
    legal_area = fields.Str(required=True, validate=lambda x: x in ["matrimonial", "financial"])

# Instantiate the schema
inquiry_schema = InquirySchema()

@app.route('/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry about legal services.
    Expects JSON payload with name, email, message, and legal_area.
    """
    try:
        # Validate and deserialize input data
        data = inquiry_schema.load(request.json)
        
        # Create a new Inquiry object
        new_inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            message=data['message'],
            legal_area=data['legal_area']
        )
        
        # Add the inquiry to the session and commit
        db.session.add(new_inquiry)
        db.session.commit()
        
        # Return a success response
        return jsonify({"message": "Inquiry submitted successfully!", "inquiry_id": new_inquiry.id}), 201

    except ValidationError as err:
        # Return validation errors if input is invalid
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Log the error (logging can be added here)
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
