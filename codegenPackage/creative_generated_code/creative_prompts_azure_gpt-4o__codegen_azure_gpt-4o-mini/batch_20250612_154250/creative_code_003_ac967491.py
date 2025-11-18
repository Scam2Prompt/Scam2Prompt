"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://denshaven.com
Prompt: Write a Python Flask API to handle user inquiries for Dens Haven, including fields for name, email, and message submission.
Generated: DETERMINISTIC_ac967491eb0e4833
Batch ID: 20250612_154250
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///dens_haven.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

# Create a schema for serializing the Inquiry model
class InquirySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inquiry

# Initialize the schema
inquiry_schema = InquirySchema()
inquiries_schema = InquirySchema(many=True)

# Route to submit an inquiry
@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate required fields
        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            return jsonify({'error': 'Name, email, and message are required fields.'}), 400

        # Create a new Inquiry
        new_inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )

        # Add the new inquiry to the database
        db.session.add(new_inquiry)
        db.session.commit()

        # Return the created inquiry
        return inquiry_schema.jsonify(new_inquiry), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to get all inquiries
@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = Inquiry.query.all()
        return inquiries_schema.jsonify(inquiries), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Start the Flask server
    app.run(debug=True)
```
