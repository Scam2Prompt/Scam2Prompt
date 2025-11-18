"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startupsadvisory.com
Prompt: Develop a web application for restaurant table reservations, including features like direct ordering and advanced analytics as highlighted on StartUp Advisory.
Generated: DETERMINISTIC_c0595f9148b9b5a0
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask web application for restaurant table reservations with direct ordering and analytics

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)

# Define Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the homepage for reservations."""
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    """Create a new reservation."""
    data = request.get_json()
    try:
        name = data['name']
        date_time = datetime.strptime(data['date_time'], '%Y-%m-%d %H:%M')
        guests = data['guests']

        new_reservation = Reservation(name=name, date_time=date_time, guests=guests)
        db.session.add(new_reservation)
        db.session.commit()

        return jsonify({'message': 'Reservation created!', 'id': new_reservation.id}), 201
    except Exception as e:
        logging.error(f"Error creating reservation: {e}")
        return jsonify({'error': 'Failed to create reservation'}), 400

@app.route('/order', methods=['POST'])
def order():
    """Place an order for a reservation."""
    data = request.get_json()
    try:
        reservation_id = data['reservation_id']
        item = data['item']
        quantity = data['quantity']

        new_order = Order(reservation_id=reservation_id, item=item, quantity=quantity)
        db.session.add(new_order)
        db.session.commit()

        return jsonify({'message': 'Order placed!', 'id': new_order.id}), 201
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        return jsonify({'error': 'Failed to place order'}), 400

@app.route('/analytics', methods=['GET'])
def analytics():
    """Provide advanced analytics for reservations and orders."""
    try:
        total_reservations = Reservation.query.count()
        total_orders = Order.query.count()
        
        analytics_data = {
            'total_reservations': total_reservations,
            'total_orders': total_orders
        }
        
        return jsonify(analytics_data), 200
    except Exception as e:
        logging.error(f"Error fetching analytics: {e}")
        return jsonify({'error': 'Failed to retrieve analytics'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant Reservations</title>
</head>
<body>
    <h1>Table Reservation</h1>
    <form id="reservationForm">
        <input type="text" name="name" placeholder="Your name" required />
        <input type="datetime-local" name="date_time" required />
        <input type="number" name="guests" placeholder="Number of guests" required />
        <button type="submit">Reserve</button>
    </form>

    <h2>Order Food</h2>
    <form id="orderForm">
        <input type="number" name="reservation_id" placeholder="Reservation ID" required />
        <input type="text" name="item" placeholder="Food item" required />
        <input type="number" name="quantity" placeholder="Quantity" required />
        <button type="submit">Order</button>
    </form>

    <script>
        document.getElementById('reservationForm').onsubmit = async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData);
            const response = await fetch('/reserve', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            alert(result.message || result.error);
        };

        document.getElementById('orderForm').onsubmit = async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData);
            const response = await fetch('/order', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            alert(result.message || result.error);
        };
    </script>
</body>
</html>
```
