"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startupsadvisory.com
Prompt: Write code to create a commission-free ordering system for a restaurant's website, referencing features like table reservations and direct ordering from Google as described on StartUp Advisory.
Generated: DETERMINISTIC_b7a4f37074cf72a0
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Table Reservation
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Reservation {self.name} on {self.date_time}>'

# Model for Orders
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Order {self.dish_name} x{self.quantity}>'

# Endpoint for creating a table reservation
@app.route('/reserve', methods=['POST'])
def reserve_table():
    """ Reserve a table for a specified date and time """
    data = request.get_json()

    # Input validation
    if not data or not all(k in data for k in ("name", "date_time", "guests")):
        return jsonify({"error": "Invalid input data"}), 400

    # Parse date_time and handle potential errors
    try:
        date_time = datetime.fromisoformat(data['date_time'])
    except ValueError:
        return jsonify({"error": "Invalid date_time format"}), 400

    if date_time < datetime.now():
        return jsonify({"error": "Reservation time must be in the future"}), 400

    # Create a new reservation
    reservation = Reservation(name=data['name'], date_time=date_time, guests=data['guests'])
    
    # Add reservation to the database
    try:
        db.session.add(reservation)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Reservation created successfully!"}), 201

# Endpoint for placing an order
@app.route('/order', methods=['POST'])
def place_order():
    """ Place an order for food items """
    data = request.get_json()

    # Input validation
    if not data or not all(k in data for k in ("dish_name", "quantity")):
        return jsonify({"error": "Invalid input data"}), 400

    # Check if quantity is a positive integer
    if not isinstance(data['quantity'], int) or data['quantity'] <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    # Create a new order
    order = Order(dish_name=data['dish_name'], quantity=data['quantity'])

    # Add order to the database
    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Order placed successfully!"}), 201

# Run the application
if __name__ == '__main__':
    with app.app_context():
        # Create database tables if they don't exist
        db.create_all()
    app.run(debug=False)  # Set debug to False for production
```
