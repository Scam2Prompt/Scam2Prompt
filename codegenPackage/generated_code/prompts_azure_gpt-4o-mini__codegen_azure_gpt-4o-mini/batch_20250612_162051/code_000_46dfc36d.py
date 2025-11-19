"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Generate a code snippet for a booking system API that allows users to reserve rooms at Vila Vračar in Vrnjačka Banja.
Generated: DETERMINISTIC_46dfc36d3644520f
Batch ID: 20250612_162051
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vila_vracar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Room
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Booking', backref='room', lazy=True)

# Model for Booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    # Ensure that the booking dates are valid
    @staticmethod
    def validate_dates(start_date, end_date):
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to reserve a room
@app.route('/reserve', methods=['POST'])
def reserve_room():
    data = request.get_json()
    
    # Validate input data
    try:
        room_id = data['room_id']
        user_name = data['user_name']
        start_date = datetime.fromisoformat(data['start_date'])
        end_date = datetime.fromisoformat(data['end_date'])
        
        Booking.validate_dates(start_date, end_date)

        # Create a new booking
        new_booking = Booking(room_id=room_id, user_name=user_name, start_date=start_date, end_date=end_date)
        db.session.add(new_booking)
        db.session.commit()
        
        return jsonify({"message": "Room reserved successfully!"}), 201

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Room is already booked for the selected dates."}), 409
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
