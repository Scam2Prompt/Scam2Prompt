"""
Generated Code Metadata:
========================
Original URL: https://drivemiami.com
Prompt: Create a script for scheduling service and parts inquiries on a vehicle dealership website, as described in DriveCities' offerings.
Generated: DETERMINISTIC_463a938694b4ead6
Batch ID: 20250612_135839
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
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dealership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    parts_needed = db.Column(db.String(200), nullable=True)
    date_requested = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Inquiry {self.id} - {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/inquiry', methods=['POST'])
def create_inquiry():
    """
    Create a new service or parts inquiry.
    Expects JSON data with name, email, phone, service_type, and optional parts_needed.
    Returns the created inquiry or an error message.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ('name', 'email', 'phone', 'service_type')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new inquiry
        new_inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            service_type=data['service_type'],
            parts_needed=data.get('parts_needed')
        )

        # Add to the session and commit to the database
        db.session.add(new_inquiry)
        db.session.commit()

        logging.info(f'Inquiry created: {new_inquiry}')
        return jsonify({'message': 'Inquiry created successfully', 'inquiry_id': new_inquiry.id}), 201

    except Exception as e:
        logging.error(f'Error creating inquiry: {e}')
        return jsonify({'error': 'An error occurred while creating the inquiry'}), 500

@app.route('/inquiry/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    """
    Retrieve an inquiry by its ID.
    Returns the inquiry details or an error message if not found.
    """
    try:
        inquiry = Inquiry.query.get_or_404(inquiry_id)
        return jsonify({
            'id': inquiry.id,
            'name': inquiry.name,
            'email': inquiry.email,
            'phone': inquiry.phone,
            'service_type': inquiry.service_type,
            'parts_needed': inquiry.parts_needed,
            'date_requested': inquiry.date_requested.isoformat()
        }), 200

    except Exception as e:
        logging.error(f'Error retrieving inquiry {inquiry_id}: {e}')
        return jsonify({'error': 'An error occurred while retrieving the inquiry'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
