"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Suggest an API design for a car rental service that includes features like luxury car rentals, wedding cars, and trip vehicles, as described on the Micro Rent a Car website.
Generated: DETERMINISTIC_cbbe092e7ac3edf5
Batch ID: 20250612_153224
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
from datetime import datetime

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)

# Database model for Car
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'luxury', 'wedding', 'trip'
    availability = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'category': self.category,
            'availability': self.availability
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/cars', methods=['GET'])
def get_cars():
    """Retrieve all cars, optionally filter by category."""
    category = request.args.get('category')
    if category:
        cars = Car.query.filter_by(category=category).all()
    else:
        cars = Car.query.all()
    return jsonify([car.to_dict() for car in cars])

@app.route('/api/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    """Retrieve a specific car by ID."""
    car = Car.query.get(car_id)
    if car:
        return jsonify(car.to_dict())
    else:
        return jsonify({"error": "Car not found"}), 404

@app.route('/api/cars', methods=['POST'])
def add_car():
    """Add a new car to the inventory."""
    data = request.get_json()
    try:
        new_car = Car(
            make=data['make'],
            model=data['model'],
            year=data['year'],
            category=data['category']
        )
        db.session.add(new_car)
        db.session.commit()
        return jsonify(new_car.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    """Update the details of a specific car."""
    car = Car.query.get(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404

    data = request.get_json()
    try:
        car.make = data.get('make', car.make)
        car.model = data.get('model', car.model)
        car.year = data.get('year', car.year)
        car.category = data.get('category', car.category)
        car.availability = data.get('availability', car.availability)
        db.session.commit()
        return jsonify(car.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    """Delete a car from the inventory."""
    car = Car.query.get(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404

    try:
        db.session.delete(car)
        db.session.commit()
        return jsonify({"message": "Car deleted successfully"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
