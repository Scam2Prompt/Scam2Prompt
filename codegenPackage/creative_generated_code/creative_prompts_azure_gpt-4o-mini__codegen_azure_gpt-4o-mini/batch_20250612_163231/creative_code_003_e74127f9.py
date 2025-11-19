"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-ss.com
Prompt: Develop an API that provides information on rare vehicles like the Cobalt SS/TC, including production numbers, performance specs, and recommended modifications, as detailed on the Phantom SS site.
Generated: DETERMINISTIC_e74127f902a10b47
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Vehicle model for the database
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    production_numbers = db.Column(db.Integer, nullable=False)
    performance_specs = db.Column(db.String(200), nullable=False)
    recommended_modifications = db.Column(db.String(500), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'production_numbers': self.production_numbers,
            'performance_specs': self.performance_specs,
            'recommended_modifications': self.recommended_modifications,
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    """
    Retrieve all vehicles from the database.
    :return: JSON list of vehicles
    """
    vehicles = Vehicle.query.all()
    return jsonify([vehicle.serialize() for vehicle in vehicles]), 200

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    """
    Retrieve a specific vehicle by ID.
    :param vehicle_id: ID of the vehicle to retrieve
    :return: JSON representation of the vehicle
    """
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle is None:
        return jsonify({'error': 'Vehicle not found'}), 404
    return jsonify(vehicle.serialize()), 200

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    """
    Add a new vehicle to the database.
    :return: JSON representation of the added vehicle
    """
    data = request.get_json()
    new_vehicle = Vehicle(
        name=data['name'],
        production_numbers=data['production_numbers'],
        performance_specs=data['performance_specs'],
        recommended_modifications=data.get('recommended_modifications')
    )
    try:
        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify(new_vehicle.serialize()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Vehicle with this name already exists'}), 400

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """Handles 404 Not Found error."""
    return jsonify({'error': 'Not Found'}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
