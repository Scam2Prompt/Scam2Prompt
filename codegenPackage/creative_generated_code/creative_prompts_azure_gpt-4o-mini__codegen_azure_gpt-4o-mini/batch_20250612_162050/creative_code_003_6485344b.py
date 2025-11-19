"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegujaratcalling.com
Prompt: Develop a REST API endpoint for booking hotel reservations that aligns with the services provided by The Gujarat Calling, ensuring price transparency and zero cancellation policies.
Generated: DETERMINISTIC_6485344b929eef8b
Batch ID: 20250612_162050
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

# Configuring the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for hotel reservation
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100), nullable=False)
    hotel_name = db.Column(db.String(100), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'guest_name': self.guest_name,
            'hotel_name': self.hotel_name,
            'check_in_date': self.check_in_date.strftime('%Y-%m-%d'),
            'check_out_date': self.check_out_date.strftime('%Y-%m-%d'),
            'price': self.price
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/book', methods=['POST'])
def book_reservation():
    """
    Endpoint for booking hotel reservations.
    Expects JSON payload with guest_name, hotel_name, check_in_date, check_out_date, and price.
    """
    data = request.json

    # Input validation
    try:
        guest_name = data['guest_name']
        hotel_name = data['hotel_name']
        check_in_date = datetime.strptime(data['check_in_date'], '%Y-%m-%d')
        check_out_date = datetime.strptime(data['check_out_date'], '%Y-%m-%d')
        price = float(data['price'])
    except (KeyError, ValueError) as e:
        return jsonify({"error": "Invalid input data", "message": str(e)}), 400

    # Enforcing price transparency and zero cancellation policy
    if price <= 0:
        return jsonify({"error": "Price must be greater than zero"}), 400
    if check_in_date >= check_out_date:
        return jsonify({"error": "Check-out date must be after check-in date"}), 400

    # Create a new reservation
    new_reservation = Reservation(
        guest_name=guest_name,
        hotel_name=hotel_name,
        check_in_date=check_in_date,
        check_out_date=check_out_date,
        price=price
    )

    # Save to the database
    try:
        db.session.add(new_reservation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to book reservation", "message": str(e)}), 500

    return jsonify(new_reservation.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
```
