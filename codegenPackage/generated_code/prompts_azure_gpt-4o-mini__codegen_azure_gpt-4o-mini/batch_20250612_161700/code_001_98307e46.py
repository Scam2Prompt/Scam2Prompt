"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Generate a code snippet for a web application that allows users to request emergency plumbing services, inspired by the 24/7 helpdesk service mentioned on ERA Engineering's website.
Generated: DETERMINISTIC_98307e463a6dff2f
Batch ID: 20250612_161700
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emergency_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the EmergencyRequest model
class EmergencyRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<EmergencyRequest {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/request_service', methods=['POST'])
def request_service():
    """
    Endpoint to request emergency plumbing services.
    Expects a JSON payload with name, phone, address, and description.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ('name', 'phone', 'address', 'description')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new emergency request
        new_request = EmergencyRequest(
            name=data['name'],
            phone=data['phone'],
            address=data['address'],
            description=data['description']
        )

        # Add the request to the database
        db.session.add(new_request)
        db.session.commit()

        logging.info(f'New emergency request created: {new_request.id}')
        return jsonify({'message': 'Emergency request submitted successfully!'}), 201

    except Exception as e:
        logging.error(f'Error processing request: {e}')
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
