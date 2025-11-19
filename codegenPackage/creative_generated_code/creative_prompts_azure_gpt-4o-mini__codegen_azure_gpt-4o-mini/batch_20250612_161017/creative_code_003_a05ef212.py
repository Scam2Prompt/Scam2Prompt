"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Develop an event photography booking system that tailors services for various occasions, reflecting the custom solutions provided by Officine dell’Immagine.
Generated: DETERMINISTIC_a05ef212b2e130f1
Batch ID: 20250612_161017
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Event Booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.String(20), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    services = db.Column(db.String(200), nullable=True)

# Schema for input validation
class BookingSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    event_date = fields.Str(required=True)
    event_type = fields.Str(required=True)
    services = fields.Str()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/book', methods=['POST'])
def book_event():
    """Endpoint to book an event photography session"""
    data = request.get_json()
    schema = BookingSchema()

    try:
        # Validate input data using schema
        booking_data = schema.load(data)
        # Create a new booking instance
        new_booking = Booking(**booking_data)
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking successful!", "booking_id": new_booking.id}), 201
    except ValidationError as err:
        # Return validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """Endpoint to retrieve all bookings"""
    bookings = Booking.query.all()
    results = []
    for booking in bookings:
        results.append({
            "id": booking.id,
            "name": booking.name,
            "email": booking.email,
            "event_date": booking.event_date,
            "event_type": booking.event_type,
            "services": booking.services
        })
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=False)
```

Make sure to install the necessary dependencies using:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```

You can run the application using:
```bash
python your_script_name.py
``` 

Remember to replace `your_script_name.py` with the actual filename where the code is saved.
