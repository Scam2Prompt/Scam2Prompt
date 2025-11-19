"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Generate a code snippet for a web application that allows users to request periodic maintenance for their diesel generators, referencing the services offered by Birlik Jeneratör.
Generated: DETERMINISTIC_1d2bca764ad21fd0
Batch ID: 20250612_162050
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenance_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the MaintenanceRequest model
class MaintenanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    generator_model = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    frequency = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<MaintenanceRequest {self.id} - {self.user_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/request-maintenance', methods=['POST'])
def request_maintenance():
    """
    Endpoint to request periodic maintenance for diesel generators.
    Expects JSON data with user_name, generator_model, service_type, and frequency.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ('user_name', 'generator_model', 'service_type', 'frequency')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new maintenance request
        new_request = MaintenanceRequest(
            user_name=data['user_name'],
            generator_model=data['generator_model'],
            service_type=data['service_type'],
            frequency=data['frequency']
        )

        # Add the request to the database
        db.session.add(new_request)
        db.session.commit()

        logging.info(f'Maintenance request created: {new_request}')
        return jsonify({'message': 'Maintenance request submitted successfully', 'request_id': new_request.id}), 201

    except Exception as e:
        logging.error(f'Error processing maintenance request: {e}')
        return jsonify({'error': 'An error occurred while processing your request'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
