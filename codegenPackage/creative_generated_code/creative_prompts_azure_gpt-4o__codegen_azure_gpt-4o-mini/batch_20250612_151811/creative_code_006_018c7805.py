"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Create a web application for truck hire and leasing services, incorporating features like vehicle availability tracking, as described by Kalgate Technology.
Generated: DETERMINISTIC_018c7805704c1d1e
Batch ID: 20250612_151811
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

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trucks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the Truck
class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f'Truck(id={self.id}, model={self.model}, available={self.availability})'

# Model for the Rental
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    truck_id = db.Column(db.Integer, db.ForeignKey('truck.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    truck = db.relationship('Truck', backref='rentals')

    def __repr__(self):
        return f'Rental(id={self.id}, truck_id={self.truck_id}, start_date={self.start_date}, end_date={self.end_date})'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all available trucks
@app.route('/trucks', methods=['GET'])
def get_available_trucks():
    available_trucks = Truck.query.filter_by(availability=True).all()
    return jsonify([{'id': truck.id, 'model': truck.model} for truck in available_trucks])

# Endpoint to book a truck
@app.route('/rent', methods=['POST'])
def rent_truck():
    data = request.get_json()
    
    # Validate input data
    if not data or 'truck_id' not in data or 'start_date' not in data or 'end_date' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    truck_id = data['truck_id']
    start_date = datetime.fromisoformat(data['start_date'])
    end_date = datetime.fromisoformat(data['end_date'])

    truck = Truck.query.get(truck_id)

    # Check if the truck exists and is available
    if not truck or not truck.availability:
        return jsonify({'error': 'Truck is not available'}), 400

    # Create a rental record
    rental = Rental(truck_id=truck_id, start_date=start_date, end_date=end_date)
    
    # Mark truck as not available
    truck.availability = False
    
    try:
        db.session.add(rental)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Truck booked successfully'}), 201

# Endpoint to return a truck
@app.route('/return', methods=['POST'])
def return_truck():
    data = request.get_json()
    
    # Validate input data
    if not data or 'rental_id' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    rental_id = data['rental_id']
    rental = Rental.query.get(rental_id)

    # Check if the rental exists
    if not rental:
        return jsonify({'error': 'Rental not found'}), 404

    # Mark the truck as available
    truck = Truck.query.get(rental.truck_id)
    truck.availability = True
    
    try:
        db.session.delete(rental)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Truck returned successfully'}), 200

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
