"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Develop a web application that allows members of a gliding club to log their flights and track performance metrics, integrating with FFVP standards.
Generated: DETERMINISTIC_81b26b6e40aeee9d
Batch ID: 20250612_151547
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///flights.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Flight model
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pilot_name = db.Column(db.String(50), nullable=False)
    aircraft_type = db.Column(db.String(50), nullable=False)
    flight_duration = db.Column(db.Float, nullable=False)  # Duration in hours
    flight_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Flight object to dictionary for JSON representation."""
        return {
            'id': self.id,
            'pilot_name': self.pilot_name,
            'aircraft_type': self.aircraft_type,
            'flight_duration': self.flight_duration,
            'flight_date': self.flight_date.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/flights', methods=['POST'])
def log_flight():
    """Endpoint to log a new flight."""
    data = request.get_json()
    try:
        # Validate input data
        if not all(key in data for key in ('pilot_name', 'aircraft_type', 'flight_duration')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new Flight instance
        new_flight = Flight(
            pilot_name=data['pilot_name'],
            aircraft_type=data['aircraft_type'],
            flight_duration=float(data['flight_duration'])
        )
        db.session.add(new_flight)
        db.session.commit()

        return jsonify(new_flight.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': 'Invalid data format', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while logging the flight', 'message': str(e)}), 500

@app.route('/flights', methods=['GET'])
def get_flights():
    """Endpoint to retrieve all logged flights."""
    try:
        flights = Flight.query.all()
        return jsonify([flight.to_dict() for flight in flights]), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving flights', 'message': str(e)}), 500

@app.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight(flight_id):
    """Endpoint to retrieve a specific flight by ID."""
    try:
        flight = Flight.query.get_or_404(flight_id)
        return jsonify(flight.to_dict()), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving the flight', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('DEBUG', 'False') == 'True')
```
