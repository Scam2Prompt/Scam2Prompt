"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Create a REST API endpoint that allows users to request transportation services for oversized loads, reflecting the capabilities of TAMS TRUCKS' fleet.
Generated: DETERMINISTIC_310d3b10c9783a51
Batch ID: 20250612_135609
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Database configuration (use your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tams_trucks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TransportationRequest(db.Model):
    """Model representing a transportation request for oversized loads."""
    id = db.Column(db.Integer, primary_key=True)
    load_description = db.Column(db.String(255), nullable=False)
    pickup_location = db.Column(db.String(255), nullable=False)
    delivery_location = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.Float, nullable=False)  # Weight in tons
    dimensions = db.Column(db.String(100), nullable=False)  # Dimensions as a string

    def to_dict(self):
        """Convert model instance to dictionary for JSON response."""
        return {
            'id': self.id,
            'load_description': self.load_description,
            'pickup_location': self.pickup_location,
            'delivery_location': self.delivery_location,
            'weight': self.weight,
            'dimensions': self.dimensions,
        }

@app.route('/transportation-request', methods=['POST'])
def request_transportation():
    """Endpoint to create a transportation request for oversized loads."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('load_description', 'pickup_location', 'delivery_location', 'weight', 'dimensions')):
        return jsonify({'error': 'Invalid input data'}), 400

    # Create a new transportation request
    new_request = TransportationRequest(
        load_description=data['load_description'],
        pickup_location=data['pickup_location'],
        delivery_location=data['delivery_location'],
        weight=data['weight'],
        dimensions=data['dimensions']
    )
    
    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify(new_request.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session on error
        return jsonify({'error': str(e)}), 500

@app.route('/transportation-request/<int:request_id>', methods=['GET'])
def get_transportation_request(request_id):
    """Endpoint to retrieve a specific transportation request by ID."""
    request_entry = TransportationRequest.query.get(request_id)
    
    if not request_entry:
        return jsonify({'error': 'Request not found'}), 404
    
    return jsonify(request_entry.to_dict()), 200

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```
