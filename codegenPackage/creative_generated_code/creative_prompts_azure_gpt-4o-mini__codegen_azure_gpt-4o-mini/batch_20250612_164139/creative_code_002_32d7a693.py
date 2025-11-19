"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Create an API endpoint for a property management service that allows users to submit inquiries about tailored investment solutions, similar to the services offered by Bebold Properties.
Generated: DETERMINISTIC_32d7a6933b8f93ca
Batch ID: 20250612_164139
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

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

# Define the Inquiry schema
class InquirySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inquiry

# Initialize the inquiry schema
inquiry_schema = InquirySchema()
inquiries_schema = InquirySchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to submit an inquiry
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate request data
        if not all(key in data for key in ('name', 'email', 'message')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new Inquiry object
        new_inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )

        # Add and commit to the database
        db.session.add(new_inquiry)
        db.session.commit()

        # Log the successful inquiry submission
        logging.info(f'New inquiry submitted by {new_inquiry.name}')

        # Return the created inquiry as a response
        return inquiry_schema.jsonify(new_inquiry), 201

    except Exception as e:
        # Handle exceptions and return error response
        logging.error(f'Error while submitting inquiry: {str(e)}')
        return jsonify({'error': 'An error occurred while submitting your inquiry'}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
