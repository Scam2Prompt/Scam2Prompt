"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strk.site
Prompt: Generate a code snippet for a web application that allows users to request a free measurement for apartment renovations in Kazan.
Generated: DETERMINISTIC_6e3600facc378e99
Batch ID: 20250612_135324
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

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///renovations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the MeasurementRequest model
class MeasurementRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

# Define the measurement request schema
class MeasurementRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MeasurementRequest

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Define the endpoint for requesting a measurement
@app.route('/request_measurement', methods=['POST'])
def request_measurement():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Validate input data
        if not data or not all(key in data for key in ('name', 'email', 'phone', 'address')):
            return jsonify({'error': 'Missing data'}), 400

        # Create a new measurement request
        new_request = MeasurementRequest(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address']
        )
        
        # Add the request to the database
        db.session.add(new_request)
        db.session.commit()

        # Log the successful request
        logging.info(f"New measurement request received: {data['name']} at {data['address']}")

        # Return a success response
        return MeasurementRequestSchema().jsonify(new_request), 201

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
