"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tripocost.com
Prompt: Develop a RESTful API endpoint for a travel booking system that includes parameters for origin city, destination city, departure date, return date, and passenger details, inspired by Tripocost's flight search interface.
Generated: DETERMINISTIC_e57ca141ec8cfb36
Batch ID: 20250612_154529
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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Configuring the SQLAlchemy database connection (example with SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Flight Search Parameters
class FlightSearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_city = db.Column(db.String(100), nullable=False)
    destination_city = db.Column(db.String(100), nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    passenger_details = db.Column(db.String(500), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/v1/search_flights', methods=['POST'])
def search_flights():
    """
    API endpoint for searching flights based on user input.
    
    Expected JSON payload:
    {
        "origin_city": "City A",
        "destination_city": "City B",
        "departure_date": "YYYY-MM-DD",
        "return_date": "YYYY-MM-DD",
        "passenger_details": "Details about passengers"
    }
    """
    try:
        data = request.get_json()

        # Validate required fields
        if not all(key in data for key in ('origin_city', 'destination_city', 'departure_date', 'passenger_details')):
            raise BadRequest("Missing required fields.")
        
        # Parse and validate dates
        departure_date = datetime.strptime(data['departure_date'], '%Y-%m-%d').date()
        return_date = datetime.strptime(data['return_date'], '%Y-%m-%d').date() if data.get('return_date') else None

        if return_date and return_date < departure_date:
            raise BadRequest("Return date must be after or equal to departure date.")

        # Create a new flight search entry
        flight_search = FlightSearch(
            origin_city=data['origin_city'],
            destination_city=data['destination_city'],
            departure_date=departure_date,
            return_date=return_date,
            passenger_details=data['passenger_details']
        )
        
        db.session.add(flight_search)
        db.session.commit()

        return jsonify({"message": "Flight search recorded successfully.", "search_id": flight_search.id}), 201

    except ValueError as e:
        raise BadRequest(f"Invalid date format: {str(e)}")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
