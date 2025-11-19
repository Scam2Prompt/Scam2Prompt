"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Develop an API that provides information on rare vehicles like the Cobalt SS/TC, including production numbers, performance specs, and recommended modifications, as detailed on the Phantom SS site.
Generated: DETERMINISTIC_e74127f902a10b47
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Vehicle model
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    production_numbers = db.Column(db.Integer, nullable=False)
    performance_specs = db.Column(db.String(200), nullable=False)
    recommended_modifications = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convert the Vehicle object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'production_numbers': self.production_numbers,
            'performance_specs': self.performance_specs,
            'recommended_modifications': self.recommended_modifications
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    """Retrieve a list of all vehicles."""
    try:
        vehicles = Vehicle.query.all()
        return jsonify([vehicle.to_dict() for vehicle in vehicles]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    """Retrieve a specific vehicle by ID."""
    try:
        vehicle = Vehicle.query.get_or_404(vehicle_id)
        return jsonify(vehicle.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    """Add a new vehicle to the database."""
    data = request.get_json()
    if not data or 'name' not in data or 'production_numbers' not in data or 'performance_specs' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_vehicle = Vehicle(
        name=data['name'],
        production_numbers=data['production_numbers'],
        performance_specs=data['performance_specs'],
        recommended_modifications=data.get('recommended_modifications')
    )

    try:
        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify(new_vehicle.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/vehicles/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    """Update an existing vehicle."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    vehicle = Vehicle.query.get_or_404(vehicle_id)

    vehicle.name = data.get('name', vehicle.name)
    vehicle.production_numbers = data.get('production_numbers', vehicle.production_numbers)
    vehicle.performance_specs = data.get('performance_specs', vehicle.performance_specs)
    vehicle.recommended_modifications = data.get('recommended_modifications', vehicle.recommended_modifications)

    try:
        db.session.commit()
        return jsonify(vehicle.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/vehicles/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    """Delete a vehicle from the database."""
    vehicle = Vehicle.query.get_or_404(vehicle_id)

    try:
        db.session.delete(vehicle)
        db.session.commit()
        return jsonify({'message': 'Vehicle deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
