"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purebite.fi
Prompt: Generate a code snippet for a restaurant management system that includes features for online table reservations and takeout orders, inspired by the services offered by Purebite.
Generated: DETERMINISTIC_a81156092e0796ed
Batch ID: 20250612_161616
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Table Reservations
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Reservation {self.name} on {self.reservation_time}>'

# Database model for Takeout Orders
class TakeoutOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<TakeoutOrder {self.customer_name} for {self.item}>'

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for online table reservation
@app.route('/reserve', methods=['POST'])
def reserve_table():
    data = request.json
    try:
        new_reservation = Reservation(
            name=data['name'],
            number_of_people=data['number_of_people'],
            reservation_time=datetime.fromisoformat(data['reservation_time'])
        )
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify({'message': 'Reservation successful!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route for placing takeout orders
@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    try:
        new_order = TakeoutOrder(
            customer_name=data['customer_name'],
            item=data['item'],
            quantity=data['quantity']
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order placed successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route for viewing all reservations
@app.route('/reservations', methods=['GET'])
def get_reservations():
    try:
        reservations = Reservation.query.all()
        return jsonify([{'name': r.name, 'number_of_people': r.number_of_people, 'reservation_time': r.reservation_time.isoformat()} for r in reservations]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route for viewing all takeout orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = TakeoutOrder.query.all()
        return jsonify([{'customer_name': o.customer_name, 'item': o.item, 'quantity': o.quantity, 'order_time': o.order_time.isoformat()} for o in orders]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
