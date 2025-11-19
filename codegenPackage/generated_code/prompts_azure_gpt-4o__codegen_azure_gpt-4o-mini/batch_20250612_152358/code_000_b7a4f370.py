"""
Generated Code Metadata:
========================
Original URL: https://startupsadvisory.com
Prompt: Write code to create a commission-free ordering system for a restaurant's website, referencing features like table reservations and direct ordering from Google as described on StartUp Advisory.
Generated: DETERMINISTIC_b7a4f37074cf72a0
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Reservation {self.name} on {self.date_time}>'

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Order {self.item_name} x{self.quantity}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a reservation
@app.route('/reserve', methods=['POST'])
def create_reservation():
    data = request.get_json()
    try:
        new_reservation = Reservation(
            name=data['name'],
            date_time=datetime.fromisoformat(data['date_time']),
            guests=data['guests']
        )
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify({'message': 'Reservation created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to place an order
@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    try:
        new_order = Order(
            item_name=data['item_name'],
            quantity=data['quantity']
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order placed successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all reservations
@app.route('/reservations', methods=['GET'])
def get_reservations():
    try:
        reservations = Reservation.query.all()
        return jsonify([{'id': r.id, 'name': r.name, 'date_time': r.date_time.isoformat(), 'guests': r.guests} for r in reservations]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        return jsonify([{'id': o.id, 'item_name': o.item_name, 'quantity': o.quantity, 'order_time': o.order_time.isoformat()} for o in orders]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
