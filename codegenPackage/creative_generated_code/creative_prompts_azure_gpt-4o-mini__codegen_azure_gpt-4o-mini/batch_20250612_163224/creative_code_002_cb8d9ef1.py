"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Create an API endpoint for submitting paving service requests, incorporating the unique two-step process mentioned on the Hyperswap Bedford Paving page.
Generated: DETERMINISTIC_cb8d9ef11e76a358
Batch ID: 20250612_163224
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
import logging

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paving_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for paving service requests
class PavingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_address = db.Column(db.String(200), nullable=False)
    request_details = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<PavingRequest {self.id} - {self.customer_name}>'

# Schema for validating input data
class PavingRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    service_address = fields.Str(required=True)
    request_details = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint for submitting paving service requests
@app.route('/api/paving_requests', methods=['POST'])
def submit_request():
    # Load and validate the incoming JSON data
    schema = PavingRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        logging.error(f'Validation error: {err.messages}')
        return jsonify({'error': 'Validation error', 'messages': err.messages}), 400

    # Create a new paving request instance
    new_request = PavingRequest(
        customer_name=data['customer_name'],
        service_address=data['service_address'],
        request_details=data['request_details']
    )

    # Save the request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        logging.error(f'Database error: {str(e)}')
        db.session.rollback()
        return jsonify({'error': 'Internal server error'}), 500

    logging.info(f'Successfully submitted request: {new_request}')
    return jsonify({'message': 'Paving service request submitted successfully', 'request_id': new_request.id}), 201

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
