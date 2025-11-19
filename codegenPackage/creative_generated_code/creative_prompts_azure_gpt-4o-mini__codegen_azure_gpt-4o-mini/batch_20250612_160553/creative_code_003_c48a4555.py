"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cymrepuestos.com.ar
Prompt: Develop a RESTful API endpoint for CYM Repuestos that allows users to submit inquiries about automotive parts and receive a response with available options.
Generated: DETERMINISTIC_c48a4555085e39d5
Batch ID: 20250612_160553
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cym_repuestos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(100), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, part_name, customer_name, email):
        self.part_name = part_name
        self.customer_name = customer_name
        self.email = email

# Define the Inquiry schema
class InquirySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inquiry

# Initialize the schema
inquiry_schema = InquirySchema()
inquiries_schema = InquirySchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# RESTful API endpoint to submit inquiries
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or 'part_name' not in data or 'customer_name' not in data or 'email' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Create a new inquiry
        new_inquiry = Inquiry(part_name=data['part_name'], customer_name=data['customer_name'], email=data['email'])
        
        # Add the inquiry to the database
        db.session.add(new_inquiry)
        db.session.commit()

        # Return the created inquiry
        return inquiry_schema.jsonify(new_inquiry), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# RESTful API endpoint to get all inquiries
@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = Inquiry.query.all()
        return inquiries_schema.jsonify(inquiries), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
