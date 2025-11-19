"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Create a RESTful API in Flask to handle customer inquiries for machinery parts and technical assistance, referencing the brands and services offered by Track Diesel Peru.
Generated: DETERMINISTIC_d61c0f7cffc9c240
Batch ID: 20250612_151610
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///track_diesel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the CustomerInquiry model
class CustomerInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    inquiry_type = db.Column(db.String(50), nullable=False)  # e.g., 'Parts', 'Technical Assistance'
    message = db.Column(db.Text, nullable=False)

# Create a schema for validation
class CustomerInquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    inquiry_type = fields.Str(required=True)
    message = fields.Str(required=True)

# Initialize the schema
inquiry_schema = CustomerInquirySchema()

# Create the database tables
with app.app_context():
    db.create_all()

# Route to handle customer inquiries
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    """Create a new customer inquiry."""
    try:
        # Validate and deserialize input
        inquiry_data = inquiry_schema.load(request.json)
        
        # Create a new inquiry instance
        new_inquiry = CustomerInquiry(**inquiry_data)
        
        # Add to the session and commit to the database
        db.session.add(new_inquiry)
        db.session.commit()
        
        # Return a success response
        return jsonify({"message": "Inquiry submitted successfully!", "inquiry_id": new_inquiry.id}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to retrieve all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    """Retrieve all customer inquiries."""
    try:
        inquiries = CustomerInquiry.query.all()
        inquiries_data = inquiry_schema.dump(inquiries, many=True)
        return jsonify(inquiries_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
