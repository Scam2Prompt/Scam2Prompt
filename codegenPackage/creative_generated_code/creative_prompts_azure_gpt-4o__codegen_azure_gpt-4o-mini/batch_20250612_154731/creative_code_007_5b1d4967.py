"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Generate code to implement a REST API for Balaji Tours & Travels that allows users to query available tour packages and car models, and submit booking requests.
Generated: DETERMINISTIC_5b1d496735448775
Batch ID: 20250612_154731
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

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Tour Package model
class TourPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the Car Model
class CarModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), nullable=False)
    rental_price = db.Column(db.Float, nullable=False)

# Define Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    tour_package_id = db.Column(db.Integer, db.ForeignKey('tour_package.id'), nullable=False)
    car_model_id = db.Column(db.Integer, db.ForeignKey('car_model.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Endpoint to retrieve all tour packages
@app.route('/api/tour-packages', methods=['GET'])
def get_tour_packages():
    packages = TourPackage.query.all()
    return jsonify([{'id': pkg.id, 'name': pkg.name, 'description': pkg.description, 'price': pkg.price} for pkg in packages])

# Endpoint to retrieve all car models
@app.route('/api/car-models', methods=['GET'])
def get_car_models():
    cars = CarModel.query.all()
    return jsonify([{'id': car.id, 'model_name': car.model_name, 'rental_price': car.rental_price} for car in cars])

# Endpoint to submit a booking request
@app.route('/api/bookings', methods=['POST'])
def create_booking():
    data = request.json
    try:
        new_booking = Booking(
            user_name=data['user_name'],
            tour_package_id=data['tour_package_id'],
            car_model_id=data['car_model_id']
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Booking created successfully!', 'booking_id': new_booking.id}), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Invalid tour package or car model ID.'}), 400
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the booking.'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
