"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Create a REST API that allows users to query flight change policies for airlines such as Southwest, United, and Turkish Airlines, using the details from Airlines Manage Booking.
Generated: DETERMINISTIC_5766e734d280e668
Batch ID: 20250612_154536
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

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flight_policies.db'
db = SQLAlchemy(app)

# Model to represent flight change policies
class FlightChangePolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    airline = db.Column(db.String(50), nullable=False)
    policy_details = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            'id': self.id,
            'airline': self.airline,
            'policy_details': self.policy_details
        }

# Endpoint to retrieve flight change policies by airline
@app.route('/api/policies', methods=['GET'])
def get_policies():
    """
    Get flight change policies for a specified airline.
    Query parameter 'airline' must be provided.
    """
    airline = request.args.get('airline')
    if not airline:
        return jsonify({'error': 'Airline query parameter is required.'}), 400

    try:
        policies = FlightChangePolicy.query.filter_by(airline=airline).all()
        if not policies:
            return jsonify({'error': 'No policies found for the specified airline.'}), 404

        return jsonify([policy.to_dict() for policy in policies]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.', 'details': str(e)}), 500

# Endpoint to add a new flight change policy
@app.route('/api/policies', methods=['POST'])
def add_policy():
    """
    Add a new flight change policy.
    Expects a JSON body with 'airline' and 'policy_details'.
    """
    data = request.get_json()
    if not data or 'airline' not in data or 'policy_details' not in data:
        return jsonify({'error': 'Invalid input. Please provide airline and policy_details.'}), 400

    new_policy = FlightChangePolicy(airline=data['airline'], policy_details=data['policy_details'])
    
    try:
        db.session.add(new_policy)
        db.session.commit()
        return jsonify(new_policy.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add policy.', 'details': str(e)}), 500

# Initialize the database (for demonstration purposes)
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
