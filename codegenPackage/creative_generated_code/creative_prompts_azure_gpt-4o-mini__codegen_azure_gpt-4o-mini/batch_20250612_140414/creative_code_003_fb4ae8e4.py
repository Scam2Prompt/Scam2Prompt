"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trysonicsolutions.com
Prompt: Can you provide a code example for integrating ultrasonic cleaning service requests into a manufacturing management system?
Generated: DETERMINISTIC_fb4ae8e4840123cf
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manufacturing.db'  # Example: using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for ultrasonic cleaning service requests
class CleaningServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Pending')  # Status can be Pending, In Progress, Completed
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON response."""
        return {
            'id': self.id,
            'order_id': self.order_id,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/request-cleaning', methods=['POST'])
def request_cleaning():
    """Endpoint to create a new ultrasonic cleaning service request."""
    data = request.get_json()
    
    order_id = data.get('order_id')
    if not order_id:
        return jsonify({'error': 'Order ID is required.'}), 400

    try:
        new_request = CleaningServiceRequest(order_id=order_id)
        db.session.add(new_request)
        db.session.commit()
        return jsonify(new_request.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/cleaning-requests', methods=['GET'])
def get_cleaning_requests():
    """Endpoint to retrieve all ultrasonic cleaning service requests."""
    try:
        requests = CleaningServiceRequest.query.all()
        return jsonify([request.to_dict() for request in requests]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/cleaning-request/<int:request_id>', methods=['PUT'])
def update_cleaning_request(request_id):
    """Endpoint to update the status of a cleaning service request."""
    data = request.get_json()
    status = data.get('status')

    if status not in ['Pending', 'In Progress', 'Completed']:
        return jsonify({'error': 'Invalid status value.'}), 400

    try:
        request_to_update = CleaningServiceRequest.query.get_or_404(request_id)
        request_to_update.status = status
        db.session.commit()
        return jsonify(request_to_update.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production use
```
