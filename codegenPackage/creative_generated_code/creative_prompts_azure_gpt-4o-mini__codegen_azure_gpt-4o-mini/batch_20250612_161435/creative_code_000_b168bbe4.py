"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://förderohr.de
Prompt: Generate a code snippet for a web application that allows users to schedule a 24/7 emergency plumbing service for clogged drains in Hamburg, referencing the services offered by ElbeRohr.
Generated: DETERMINISTIC_b168bbe49ac8be8c
Batch ID: 20250612_161435
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
from datetime import datetime
import pytz

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emergency_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the service request model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    request_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    service_type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<ServiceRequest {self.customer_name}, {self.service_type}>'

# API endpoint to schedule a plumbing service
@app.route('/schedule', methods=['POST'])
def schedule_service():
    data = request.get_json()

    # Validate incoming data
    if not data or 'customer_name' not in data or 'phone_number' not in data or 'service_type' not in data:
        return jsonify({'error': 'Missing data'}), 400

    # Create a new service request
    new_request = ServiceRequest(
        customer_name=data['customer_name'],
        phone_number=data['phone_number'],
        service_type=data['service_type']
    )

    try:
        # Add to the database and commit
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'Service scheduled successfully', 'request_id': new_request.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# Error handling for database initialization
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

```markdown
# Dependencies required:
- Flask
- Flask-SQLAlchemy
- pytz (if timezone handling is required)

# To install dependencies, run:
pip install Flask Flask-SQLAlchemy pytz
```
