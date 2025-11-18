"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Recommend a library or API to integrate a booking system for Winger R&R's services, such as scheduling "custom stone/tile work" or "drywall repair and painting."
Generated: DETERMINISTIC_6ff2effff336fb5e
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of a Python implementation of a simple booking system using Flask and SQLAlchemy. The code integrates RESTful APIs to manage scheduling for services such as "custom stone/tile work" or "drywall repair and painting." It uses SQLite as the database for simplicity.

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100), nullable=False)  # e.g., "custom stone/tile work"
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(120), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "service_type": self.service_type,
            "customer_name": self.customer_name,
            "customer_email": self.customer_email,
            "booking_date": self.booking_date.strftime('%Y-%m-%d %H:%M:%S'),
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Route to create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    try:
        data = request.get_json()
        service_type = data.get('service_type')
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        booking_date = datetime.strptime(data.get('booking_date'), '%Y-%m-%d %H:%M:%S')

        if not all([service_type, customer_name, customer_email, booking_date]):
            return jsonify({"error": "All fields are required"}), 400

        new_booking = Booking(
            service_type=service_type,
            customer_name=customer_name,
            customer_email=customer_email,
            booking_date=booking_date
        )
        db.session.add(new_booking)
        db.session.commit()

        return jsonify(new_booking.to_dict()), 201
    except Exception as e:
        return jsonify({"error": "Failed to create booking", "message": str(e)}), 500

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([booking.to_dict() for booking in bookings]), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch bookings", "message": str(e)}), 500

# Route to get a specific booking by ID
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    try:
        booking = Booking.query.get(booking_id)
        if not booking:
            return jsonify({"error": "Booking not found"}), 404
        return jsonify(booking.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch booking", "message": str(e)}), 500

# Route to delete a booking by ID
@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    try:
        booking = Booking.query.get(booking_id)
        if not booking:
            return jsonify({"error": "Booking not found"}), 404
        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to delete booking", "message": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features
1. **Endpoints**:
   - `POST /bookings` to create a new booking.
   - `GET /bookings` to retrieve all bookings.
   - `GET /bookings/<int:booking_id>` to retrieve a specific booking by ID.
   - `DELETE /bookings/<int:booking_id>` to delete a booking by ID.

2. **Database**:
   - Uses SQLAlchemy with SQLite for storage. Replace `sqlite:///bookings.db` with your production database URL.

3. **Error Handling**:
   - Handles missing fields, invalid data, and server errors.

### Instructions
1. Install dependencies: `pip install flask flask-sqlalchemy`.
2. Run the app: `python app.py`.
3. Use tools like Postman or `curl` to interact with the API.
