"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Create a web application for truck hire and leasing services, incorporating features like vehicle availability tracking, as described by Kalgate Technology.
Generated: DETERMINISTIC_018c7805704c1d1e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///truck_hire.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Vehicle model
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Vehicle {self.model}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to get all vehicles
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    """Retrieve all vehicles and their availability status."""
    vehicles = Vehicle.query.all()
    return jsonify([{'id': v.id, 'model': v.model, 'availability': v.availability} for v in vehicles])

# Route to add a new vehicle
@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    """Add a new vehicle to the inventory."""
    data = request.get_json()
    if not data or 'model' not in data:
        return jsonify({'error': 'Model is required'}), 400

    new_vehicle = Vehicle(model=data['model'])
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle added', 'id': new_vehicle.id}), 201

# Route to update vehicle availability
@app.route('/vehicles/<int:vehicle_id>', methods=['PATCH'])
def update_availability(vehicle_id):
    """Update the availability status of a vehicle."""
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404

    data = request.get_json()
    if 'availability' in data:
        vehicle.availability = data['availability']
        db.session.commit()
        return jsonify({'message': 'Availability updated'}), 200

    return jsonify({'error': 'Invalid data'}), 400

# Route to delete a vehicle
@app.route('/vehicles/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    """Delete a vehicle from the inventory."""
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404

    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle deleted'}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected errors."""
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
