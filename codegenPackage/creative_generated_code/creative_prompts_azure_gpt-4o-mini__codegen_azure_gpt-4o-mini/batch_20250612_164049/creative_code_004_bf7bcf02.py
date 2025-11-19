"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Suggest an API that can help beauty centers manage customer bookings and inquiries, similar to the services offered by TuBella Estetica 2.0.
Generated: DETERMINISTIC_bf7bcf02de73ee68
Batch ID: 20250612_164049
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///beauty_center.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Customer
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)

# Model for Booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    customer = db.relationship('Customer', backref='bookings')

# Endpoint to create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    try:
        new_customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Customer created", "customer_id": new_customer.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    try:
        new_booking = Booking(
            customer_id=data['customer_id'],
            service=data['service'],
            date_time=datetime.strptime(data['date_time'], '%Y-%m-%d %H:%M:%S'),
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created", "booking_id": new_booking.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to get all bookings for a customer
@app.route('/customers/<int:customer_id>/bookings', methods=['GET'])
def get_customer_bookings(customer_id):
    try:
        bookings = Booking.query.filter_by(customer_id=customer_id).all()
        return jsonify([{
            "id": booking.id,
            "service": booking.service,
            "date_time": booking.date_time.strftime('%Y-%m-%d %H:%M:%S'),
            "status": booking.status
        } for booking in bookings]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
