"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meje.cc
Prompt: Create a REST API in Flask to manage customer inquiries for "Smart Bidet Seat" products, including features like heated bidet and dryer, as described on the MEJE website.
Generated: DETERMINISTIC_53bb45ea11486806
Batch ID: 20250612_151506
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database
db = SQLAlchemy(app)

# Customer Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    product = db.Column(db.String(100), default="Smart Bidet Seat")

# Schema for validating inquiries
class InquirySchema(Schema):
    customer_name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Create a new inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    try:
        # Validate and deserialize input
        schema = InquirySchema()
        inquiry_data = schema.load(request.json)

        # Create a new Inquiry object
        new_inquiry = Inquiry(**inquiry_data)

        # Add the inquiry to the session and commit
        db.session.add(new_inquiry)
        db.session.commit()

        # Return the created inquiry with status code 201
        return jsonify(schema.dump(new_inquiry)), 201

    except ValidationError as err:
        # Return validation errors with status code 400
        return jsonify(err.messages), 400
    except Exception as e:
        # Return internal server error with status code 500
        return jsonify({"error": str(e)}), 500

# Retrieve all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = Inquiry.query.all()
        schema = InquirySchema(many=True)
        return jsonify(schema.dump(inquiries)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve an inquiry by ID
@app.route('/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    try:
        inquiry = Inquiry.query.get_or_404(inquiry_id)
        schema = InquirySchema()
        return jsonify(schema.dump(inquiry)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an inquiry by ID
@app.route('/inquiries/<int:inquiry_id>', methods=['PUT'])
def update_inquiry(inquiry_id):
    try:
        inquiry = Inquiry.query.get_or_404(inquiry_id)
        schema = InquirySchema()
        updated_data = schema.load(request.json)

        # Update inquiry fields
        for key, value in updated_data.items():
            setattr(inquiry, key, value)

        # Commit the changes
        db.session.commit()

        return jsonify(schema.dump(inquiry)), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete an inquiry by ID
@app.route('/inquiries/<int:inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    try:
        inquiry = Inquiry.query.get_or_404(inquiry_id)

        # Delete the inquiry
        db.session.delete(inquiry)
        db.session.commit()

        return jsonify({"message": "Inquiry deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
