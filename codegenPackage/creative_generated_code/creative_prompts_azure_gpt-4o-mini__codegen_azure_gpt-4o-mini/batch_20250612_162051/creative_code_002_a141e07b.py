"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://filmdailyweb.com
Prompt: How can I implement a feature to book visits to showflats using a web API? Provide a sample code for this functionality.
Generated: DETERMINISTIC_a141e07b5c415728
Batch ID: 20250612_162051
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
import re

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///showflat_bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Showflat bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Booking {self.name} at {self.date_time}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/book_showflat', methods=['POST'])
def book_showflat():
    """
    Endpoint to book a visit to a showflat.
    Expects a JSON payload with 'name', 'email', and 'date_time'.
    """
    data = request.get_json()

    # Validate request data
    if not data or 'name' not in data or 'email' not in data or 'date_time' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    name = data['name']
    email = data['email']
    date_time_str = data['date_time']

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email format"}), 400

    # Validate date_time format
    try:
        date_time = datetime.fromisoformat(date_time_str)
    except ValueError:
        return jsonify({"error": "Invalid date_time format. Use ISO format."}), 400

    # Create and save the booking
    new_booking = Booking(name=name, email=email, date_time=date_time)
    
    try:
        db.session.add(new_booking)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to book showflat. Please try again."}), 500

    return jsonify({"message": "Booking successful", "booking_id": new_booking.id}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
