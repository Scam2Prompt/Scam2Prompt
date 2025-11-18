"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Recommend a library or API for managing boat rental reservations, including features for fleet management, customer details, and scheduling, specifically for RIB charter services like those offered by OpenSea.
Generated: DETERMINISTIC_29c7fcd25e20f374
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This script demonstrates how to use the `Flask` web framework along with `SQLAlchemy` for managing boat rental reservations.
# It sets up a backend API for managing fleets, customers, and scheduling reservations for a RIB charter service.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Models
class Boat(db.Model):
    __tablename__ = 'boats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    boat_id = db.Column(db.Integer, db.ForeignKey('boats.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    customer = db.relationship('Customer', backref=db.backref('reservations', lazy=True))
    boat = db.relationship('Boat', backref=db.backref('reservations', lazy=True))

# Initialize database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route('/boats', methods=['GET', 'POST'])
def manage_boats():
    if request.method == 'POST':
        # Add a new boat
        data = request.json
        try:
            new_boat = Boat(name=data['name'], type=data['type'], capacity=data['capacity'])
            db.session.add(new_boat)
            db.session.commit()
            return jsonify({"message": "Boat added successfully!"}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    elif request.method == 'GET':
        # Get all boats
        boats = Boat.query.all()
        return jsonify([{"id": boat.id, "name": boat.name, "type": boat.type, "capacity": boat.capacity} for boat in boats])

@app.route('/customers', methods=['GET', 'POST'])
def manage_customers():
    if request.method == 'POST':
        # Add a new customer
        data = request.json
        try:
            new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
            db.session.add(new_customer)
            db.session.commit()
            return jsonify({"message": "Customer added successfully!"}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    elif request.method == 'GET':
        # Get all customers
        customers = Customer.query.all()
        return jsonify([{"id": customer.id, "name": customer.name, "email": customer.email, "phone": customer.phone} for customer in customers])

@app.route('/reservations', methods=['GET', 'POST'])
def manage_reservations():
    if request.method == 'POST':
        # Create a new reservation
        data = request.json
        try:
            start_time = datetime.strptime(data['start_time'], "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(data['end_time'], "%Y-%m-%d %H:%M:%S")
            new_reservation = Reservation(
                customer_id=data['customer_id'],
                boat_id=data['boat_id'],
                start_time=start_time,
                end_time=end_time
            )
            db.session.add(new_reservation)
            db.session.commit()
            return jsonify({"message": "Reservation created successfully!"}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    elif request.method == 'GET':
        # Get all reservations
        reservations = Reservation.query.all()
        return jsonify([{
            "id": res.id,
            "customer_id": res.customer_id,
            "boat_id": res.boat_id,
            "start_time": res.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": res.end_time.strftime("%Y-%m-%d %H:%M:%S")
        } for res in reservations])

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
