"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vracarbvk.rs
Prompt: Develop a RESTful API endpoint for managing reservations at Vila Vračar, ensuring it includes features for checking availability and confirming bookings.
Generated: DETERMINISTIC_979eec2ed0fa8055
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Reservation {self.id}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    """
    Create a new reservation.
    Request body should contain name, email, date, and guests.
    """
    data = request.get_json()
    
    # Validate request data
    if not data or not all(key in data for key in ['name', 'email', 'date', 'guests']):
        return jsonify({"error": "Missing data"}), 400

    try:
        reservation_date = datetime.fromisoformat(data['date'])
        new_reservation = Reservation(
            name=data['name'],
            email=data['email'],
            date=reservation_date,
            guests=data['guests']
        )
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify({"message": "Reservation created", "id": new_reservation.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/reservations/availability', methods=['GET'])
def check_availability():
    """
    Check availability for a given date.
    Query parameters should include 'date'.
    """
    date_str = request.args.get('date')
    if not date_str:
        return jsonify({"error": "Missing date parameter"}), 400

    try:
        check_date = datetime.fromisoformat(date_str)
        existing_reservations = Reservation.query.filter(
            db.func.date(Reservation.date) == check_date.date()
        ).count()
        
        # Assume the limit for guests is 20 for this example
        max_guests = 20
        available_spots = max_guests - existing_reservations
        
        return jsonify({
            "date": check_date.date(),
            "available_spots": max(available_spots, 0)
        }), 200
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes
- Ensure to install Flask and Flask-SQLAlchemy using pip if you haven't done so:
```bash
pip install Flask Flask-SQLAlchemy
```
- The SQLite database will be created in the same directory as the script. Adjust the database URI for other databases as needed.
- The API includes endpoints for creating reservations and checking availability based on a specified date.
