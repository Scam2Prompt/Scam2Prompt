"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Generate a code snippet for a web application that allows users to book luxury cars for rent in Islamabad, similar to the services offered by Micro Rent a Car.
Generated: DETERMINISTIC_369b651231ee13d4
Batch ID: 20250612_162051
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (using SQLite for simplicity, switch to a production DB as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carrental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the luxury car rental
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Car {self.make} {self.model} ({self.year})>"

# Define a model for bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Booking {self.user_name} for Car ID {self.car_id}>"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new car
@app.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    try:
        new_car = Car(
            make=data['make'],
            model=data['model'],
            year=data['year']
        )
        db.session.add(new_car)
        db.session.commit()
        return jsonify({'message': 'Car added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to list available cars
@app.route('/cars', methods=['GET'])
def list_cars():
    available_cars = Car.query.filter_by(available=True).all()
    return jsonify([{'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year} for car in available_cars])

# Endpoint to book a car
@app.route('/book', methods=['POST'])
def book_car():
    data = request.get_json()
    try:
        # Check if the car is available
        car = Car.query.get(data['car_id'])
        if not car or not car.available:
            return jsonify({'error': 'Car not available for booking'}), 400
        
        # Create a new booking
        new_booking = Booking(
            car_id=data['car_id'],
            user_name=data['user_name'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        
        # Mark the car as unavailable
        car.available = False

        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Car booked successfully', 'booking_id': new_booking.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
