"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancermt.com
Prompt: Write a code snippet to create an online booking system for a massage therapy clinic, similar to the one mentioned on balancermt.com.
Generated: DETERMINISTIC_0ad2da13f07b1adf
Batch ID: 20250612_160703
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
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing booking information
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    treatment = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Booking {self.name} on {self.date}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new booking
@app.route('/book', methods=['POST'])
def book():
    data = request.get_json()

    # Validate incoming data
    if not data or 'name' not in data or 'email' not in data or 'date' not in data or 'treatment' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    # Parse date from the request and handle timezone
    try:
        booking_date = datetime.fromisoformat(data['date']).astimezone(pytz.UTC)
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400

    # Create a new booking instance
    new_booking = Booking(name=data['name'], email=data['email'], date=booking_date, treatment=data['treatment'])

    # Save booking to the database
    try:
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Booking successful', 'booking_id': new_booking.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create booking', 'details': str(e)}), 500

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([{'id': b.id, 'name': b.name, 'email': b.email, 'date': b.date.isoformat(), 'treatment': b.treatment} for b in bookings]), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve bookings', 'details': str(e)}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Change to False in production
```

Make sure to install the required dependencies:
```bash
pip install Flask SQLAlchemy pytz
```
