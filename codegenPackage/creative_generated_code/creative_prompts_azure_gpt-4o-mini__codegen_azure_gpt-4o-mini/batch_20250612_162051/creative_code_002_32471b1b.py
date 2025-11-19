"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Create a REST API endpoint for a computer repair service that allows users to submit their repair requests and receive updates, based on the customer service model of Geeks on Repair.
Generated: DETERMINISTIC_32471b1b90762f68
Batch ID: 20250612_162051
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

# Initialize Flask application
app = Flask(__name__)

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repairs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Repair Request model
class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    device_type = db.Column(db.String(100), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the RepairRequest object to a dictionary."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'device_type': self.device_type,
            'issue_description': self.issue_description,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/repair_requests', methods=['POST'])
def submit_repair_request():
    """Endpoint to submit a new repair request."""
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'customer_name' not in data or 'device_type' not in data or 'issue_description' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Create new repair request
        new_request = RepairRequest(
            customer_name=data['customer_name'],
            device_type=data['device_type'],
            issue_description=data['issue_description']
        )
        db.session.add(new_request)
        db.session.commit()

        return jsonify(new_request.to_dict()), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/repair_requests/<int:request_id>', methods=['GET'])
def get_repair_request(request_id):
    """Endpoint to retrieve a repair request by ID."""
    try:
        repair_request = RepairRequest.query.get_or_404(request_id)
        return jsonify(repair_request.to_dict()), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/repair_requests/<int:request_id>', methods=['PUT'])
def update_repair_request(request_id):
    """Endpoint to update the status of a repair request."""
    try:
        data = request.get_json()
        repair_request = RepairRequest.query.get_or_404(request_id)

        # Validate input data
        if not data or 'status' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Update the status of the repair request
        repair_request.status = data['status']
        db.session.commit()

        return jsonify(repair_request.to_dict()), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
