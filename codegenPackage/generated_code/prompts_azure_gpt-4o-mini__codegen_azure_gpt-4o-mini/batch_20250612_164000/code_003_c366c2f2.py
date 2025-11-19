"""
Generated Code Metadata:
========================
Original URL: https://www.lecarolee.it
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about the agriturismo services offered by Le Carolee, including validation for required fields.
Generated: DETERMINISTIC_c366c2f24338b9c0
Batch ID: 20250612_164000
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define schema for validation
class InquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)

# Initialize schema
inquiry_schema = InquirySchema()

@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry about agriturismo services.
    Validates required fields and stores the inquiry in the database.
    """
    try:
        # Validate and deserialize input data
        data = inquiry_schema.load(request.json)
        
        # Create a new Inquiry instance
        new_inquiry = Inquiry(name=data['name'], email=data['email'], message=data['message'])
        
        # Add to the session and commit to the database
        db.session.add(new_inquiry)
        db.session.commit()
        
        # Return success response
        return jsonify({"message": "Inquiry submitted successfully!"}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
