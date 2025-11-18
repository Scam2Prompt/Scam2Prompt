"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Develop a code snippet to implement a "quote request" feature for renting vehicles, allowing users to select vehicle types and specify their needs, as outlined on the Innova Renting website.
Generated: DETERMINISTIC_18d192ed23ea9609
Batch ID: 20250612_153225
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicles.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model representing a vehicle type
class VehicleType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Model representing a quote request
class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey('vehicle_type.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    rental_duration = db.Column(db.Integer, nullable=False)  # in days
    special_requests = db.Column(db.String(200), nullable=True)

    vehicle_type = db.relationship('VehicleType', backref='quote_requests')

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/quote-request', methods=['POST'])
def create_quote_request():
    """Endpoint to create a new quote request for vehicle rental."""
    data = request.json
    
    # Validate incoming data
    if not data or 'vehicle_type_id' not in data or 'user_name' not in data or 'rental_duration' not in data:
        return jsonify({'error': 'Invalid request data.'}), 400

    try:
        # Create a new quote request
        quote_request = QuoteRequest(
            vehicle_type_id=data['vehicle_type_id'],
            user_name=data['user_name'],
            rental_duration=data['rental_duration'],
            special_requests=data.get('special_requests')
        )

        db.session.add(quote_request)
        db.session.commit()

        return jsonify({'message': 'Quote request created successfully!', 'request_id': quote_request.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/vehicle-types', methods=['GET'])
def get_vehicle_types():
    """Endpoint to retrieve all available vehicle types."""
    vehicle_types = VehicleType.query.all()
    return jsonify([{'id': vt.id, 'name': vt.name, 'description': vt.description} for vt in vehicle_types]), 200

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application
```
