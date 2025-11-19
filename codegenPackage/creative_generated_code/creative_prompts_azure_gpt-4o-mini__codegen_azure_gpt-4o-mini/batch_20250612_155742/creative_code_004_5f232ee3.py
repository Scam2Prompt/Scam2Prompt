"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcsprayfoamsolutions.com
Prompt: Suggest a library for managing customer inquiries and estimates related to spray foam insulation services, focusing on user experience and efficiency.
Generated: DETERMINISTIC_5f232ee3b43fbe8d
Batch ID: 20250612_155742
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Customer Inquiry model
class CustomerInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    inquiry = db.Column(db.String(500), nullable=False)
    estimate = db.Column(db.String(200), nullable=True)

# Create a schema for validating incoming data
class CustomerInquirySchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    inquiry = fields.String(required=True)
    estimate = fields.String()

# Initialize the schema
inquiry_schema = CustomerInquirySchema()

# Route to create a new customer inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    try:
        # Validate and deserialize incoming JSON data
        inquiry_data = inquiry_schema.load(request.json)
        
        # Create a new CustomerInquiry instance
        new_inquiry = CustomerInquiry(**inquiry_data)
        
        # Add the new inquiry to the session and commit
        db.session.add(new_inquiry)
        db.session.commit()

        # Return a success response
        return jsonify(inquiry_schema.dump(new_inquiry)), 201
        
    except ValidationError as err:
        # Handle validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

# Route to get all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = CustomerInquiry.query.all()
        return jsonify(inquiry_schema.dump(inquiries, many=True)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
