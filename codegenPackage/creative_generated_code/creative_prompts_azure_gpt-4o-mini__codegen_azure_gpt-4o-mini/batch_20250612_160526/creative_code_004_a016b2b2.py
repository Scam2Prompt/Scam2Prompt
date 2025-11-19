"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderplanet.ee
Prompt: Write a code example that integrates a booking system for party services, referencing the unique offerings of Wonderplanet.ee, including themed parties and special character appearances.
Generated: DETERMINISTIC_a016b2b208ad2bc4
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the PartyBooking model
class PartyBooking(db.Model):
    """Model to store party bookings."""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    party_type = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    special_requests = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Booking {self.id} - {self.party_type} for {self.customer_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/book_party', methods=['POST'])
def book_party():
    """Endpoint to book a party with specified details."""
    try:
        # Parse JSON data from the request
        data = request.get_json()
        customer_name = data['customer_name']
        party_type = data['party_type']
        date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
        special_requests = data.get('special_requests', "")

        # Validate the party type
        if party_type not in ['themed', 'character_appearance']:
            return jsonify({"error": "Invalid party type. Please choose 'themed' or 'character_appearance'."}), 400

        # Create a new booking instance
        new_booking = PartyBooking(
            customer_name=customer_name,
            party_type=party_type,
            date=date,
            special_requests=special_requests
        )

        # Add the booking to the session and commit
        db.session.add(new_booking)
        db.session.commit()

        return jsonify({"message": "Party booked successfully!", "booking_id": new_booking.id}), 201

    except Exception as e:
        # Log the error and return a response
        print(f"Error occurred: {e}")
        return jsonify({"error": "Failed to book party. Please check your input and try again."}), 500

@app.route('/get_bookings', methods=['GET'])
def get_bookings():
    """Endpoint to retrieve all party bookings."""
    try:
        # Query all bookings from the database
        bookings = PartyBooking.query.all()
        result = []

        for booking in bookings:
            result.append({
                "id": booking.id,
                "customer_name": booking.customer_name,
                "party_type": booking.party_type,
                "date": booking.date.strftime('%Y-%m-%d %H:%M:%S'),
                "special_requests": booking.special_requests
            })

        return jsonify(result), 200

    except Exception as e:
        # Log the error and return a response
        print(f"Error occurred: {e}")
        return jsonify({"error": "Failed to retrieve bookings."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
