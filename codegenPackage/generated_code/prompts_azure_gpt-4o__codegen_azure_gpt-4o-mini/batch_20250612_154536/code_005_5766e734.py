"""
Generated Code Metadata:
========================
Original URL: https://airlinesmanagebooking.com
Prompt: Create a REST API that allows users to query flight change policies for airlines such as Southwest, United, and Turkish Airlines, using the details from Airlines Manage Booking.
Generated: DETERMINISTIC_5766e734d280e668
Batch ID: 20250612_154536
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing flight change policies
class FlightChangePolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    airline = db.Column(db.String(50), nullable=False)
    policy_details = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'airline': self.airline,
            'policy_details': self.policy_details
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get flight change policies by airline
@app.route('/api/policies', methods=['GET'])
def get_flight_change_policy():
    airline = request.args.get('airline')
    
    if not airline:
        return jsonify({'error': 'Airline parameter is required'}), 400

    try:
        policy = FlightChangePolicy.query.filter_by(airline=airline).first()
        
        if policy:
            return jsonify(policy.to_dict()), 200
        else:
            return jsonify({'error': 'Policy not found for the specified airline'}), 404

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new flight change policy
@app.route('/api/policies', methods=['POST'])
def add_flight_change_policy():
    data = request.get_json()
    
    if not data or 'airline' not in data or 'policy_details' not in data:
        return jsonify({'error': 'Airline and policy details are required'}), 400

    new_policy = FlightChangePolicy(
        airline=data['airline'],
        policy_details=data['policy_details']
    )

    try:
        db.session.add(new_policy)
        db.session.commit()
        return jsonify(new_policy.to_dict()), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
