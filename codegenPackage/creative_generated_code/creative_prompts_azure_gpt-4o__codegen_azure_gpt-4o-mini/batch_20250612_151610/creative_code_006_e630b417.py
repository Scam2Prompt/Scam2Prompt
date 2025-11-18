"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Create a REST API for a logistics company that allows clients to check shipment status, book transportation services, and view fleet availability (e.g., extensibles, plataformas).
Generated: DETERMINISTIC_e630b4171cb2a236
Batch ID: 20250612_151610
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Model for Shipment Status
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)

# Model for Transportation Services
class TransportationService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    available = db.Column(db.Boolean, default=True)

# Model for Fleet Availability
class Fleet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.String(50), nullable=False)
    available_units = db.Column(db.Integer, default=0)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/shipments/<int:shipment_id>', methods=['GET'])
def get_shipment_status(shipment_id):
    """Get the status of a shipment by ID."""
    shipment = Shipment.query.get(shipment_id)
    if shipment is None:
        return jsonify({'error': 'Shipment not found'}), 404
    return jsonify({'id': shipment.id, 'status': shipment.status})

@app.route('/api/transportation', methods=['POST'])
def book_transportation():
    """Book a transportation service."""
    data = request.json
    service_type = data.get('service_type')

    # Add error handling for missing service type
    if not service_type:
        return jsonify({'error': 'Service type is required'}), 400

    new_service = TransportationService(service_type=service_type)
    try:
        db.session.add(new_service)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'id': new_service.id, 'service_type': new_service.service_type}), 201

@app.route('/api/fleet', methods=['GET'])
def get_fleet_availability():
    """Get the availability of the fleet."""
    fleet = Fleet.query.all()
    return jsonify([{'id': vehicle.id, 'type': vehicle.vehicle_type, 'available_units': vehicle.available_units} for vehicle in fleet])

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and SQLAlchemy installed in your environment. You can install them using pip:
  ```bash
  pip install Flask SQLAlchemy
  ```
- The above code uses SQLite for simplicity. Modify the database URI in `app.config['SQLALCHEMY_DATABASE_URI']` for a production-ready database (e.g., PostgreSQL, MySQL).
- Initialize the database before running the application to create the necessary tables by using `db.create_all()` in the context of your app.
- This is a basic implementation. Additional features like authentication, more detailed error handling, and logging can be added as needed for production readiness.
