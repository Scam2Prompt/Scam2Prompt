"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: How can I implement a car rental API for different vehicle models like Innova and Tempo Traveler as offered by Balaji Tours and Travels?
Generated: DETERMINISTIC_061250f7f0cf3c6c
Batch ID: 20250612_160912
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

# Configure database URL for SQLite (can be changed based on requirements)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a Car model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'model': self.model,
            'price_per_day': self.price_per_day,
            'availability': self.availability
        }

# Create the database and the Car table
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all available cars
@app.route('/cars', methods=['GET'])
def get_cars():
    try:
        cars = Car.query.filter_by(availability=True).all()
        return jsonify([car.to_dict() for car in cars]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to rent a car
@app.route('/rent/<int:car_id>', methods=['POST'])
def rent_car(car_id):
    try:
        car = Car.query.get(car_id)
        if car is None or not car.availability:
            return jsonify({'error': 'Car not available'}), 404
        
        # Mark car as rented (not available)
        car.availability = False
        db.session.commit()
        return jsonify({'message': f'You have rented {car.model}'}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to add a new car
@app.route('/cars', methods=['POST'])
def add_car():
    data = request.json
    # Validate input
    if not data or 'model' not in data or 'price_per_day' not in data:
        return jsonify({'error': 'Model and price_per_day required'}), 400
    
    try:
        new_car = Car(model=data['model'], price_per_day=data['price_per_day'])
        db.session.add(new_car)
        db.session.commit()
        return jsonify(new_car.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to return rented cars
@app.route('/rented_cars', methods=['GET'])
def get_rented_cars():
    try:
        rented_cars = Car.query.filter_by(availability=False).all()
        return jsonify([car.to_dict() for car in rented_cars]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
