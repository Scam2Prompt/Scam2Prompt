"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bepretty.hamburg
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries for makeup and styling services, similar to the contact form on bePretty Hamburg.
Generated: DETERMINISTIC_cfd52757f3bce26c
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Define the schema for validation
class InquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)

# Create an instance of the schema
inquiry_schema = InquirySchema()

@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry for makeup and styling services.
    Expects JSON payload with 'name', 'email', and 'message'.
    """
    try:
        # Validate and deserialize input data
        data = inquiry_schema.load(request.json)
        
        # Create a new Inquiry instance
        new_inquiry = Inquiry(**data)
        
        # Add the inquiry to the session and commit to the database
        db.session.add(new_inquiry)
        db.session.commit()
        
        # Return a success response
        return jsonify({"message": "Inquiry submitted successfully."}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify({"errors": err.messages}), 400

    except Exception as e:
        # Log the exception and return a generic error message
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
