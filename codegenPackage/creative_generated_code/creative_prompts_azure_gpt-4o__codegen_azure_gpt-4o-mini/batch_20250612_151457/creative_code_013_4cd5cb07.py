"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Generate code to set up a consultation booking system for artists using the VIP Management service structure.
Generated: DETERMINISTIC_4cd5cb071072526f
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultation_bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the Consultation Booking
class ConsultationBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False)
    consultation_date = db.Column(db.DateTime, nullable=False)
    contact_info = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Booking {self.artist_name} on {self.consultation_date}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/book', methods=['POST'])
def book_consultation():
    """
    Endpoint to book a consultation for an artist.
    Expects JSON data in the request body.
    Required fields: artist_name, consultation_date, contact_info
    """
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('artist_name', 'consultation_date', 'contact_info')):
        return jsonify({"error": "Missing required fields"}), 400

    # Parse and validate the consultation date
    try:
        consultation_date = datetime.fromisoformat(data['consultation_date'])
    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO format."}), 400

    # Create a new booking
    new_booking = ConsultationBooking(
        artist_name=data['artist_name'],
        consultation_date=consultation_date,
        contact_info=data['contact_info']
    )

    # Attempt to save the booking to the database
    try:
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking successful", "booking_id": new_booking.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Booking conflict. Please choose a different date."}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/bookings', methods=['GET'])
def list_bookings():
    """
    Endpoint to retrieve all consultation bookings.
    Returns a list of all bookings in JSON format.
    """
    bookings = ConsultationBooking.query.all()
    return jsonify([{
        'id': booking.id,
        'artist_name': booking.artist_name,
        'consultation_date': booking.consultation_date.isoformat(),
        'contact_info': booking.contact_info
    } for booking in bookings]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Remove debug=True for production
```
