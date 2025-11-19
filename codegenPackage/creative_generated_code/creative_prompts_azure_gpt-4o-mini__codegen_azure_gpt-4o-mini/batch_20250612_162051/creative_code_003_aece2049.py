"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bvitravel.co.uk
Prompt: Develop a travel booking API that includes options for tailored itineraries to the British Virgin Islands, focusing on family and solo adventures.
Generated: DETERMINISTIC_aece20492fc593fd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Travel Itinerary
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(50), nullable=False)  # 'family' or 'solo'
    destination = db.Column(db.String(100), nullable=False)
    activities = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Itinerary {self.id} - {self.user_type} - {self.destination}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    """Create a new travel itinerary."""
    data = request.get_json()

    # Validate input data
    if not data or 'user_type' not in data or 'destination' not in data or 'activities' not in data:
        abort(400, 'Missing required fields: user_type, destination, activities.')

    itinerary = Itinerary(
        user_type=data['user_type'],
        destination=data['destination'],
        activities=data['activities']
    )

    try:
        db.session.add(itinerary)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, 'An error occurred while creating the itinerary.')

    return jsonify({'message': 'Itinerary created successfully!', 'id': itinerary.id}), 201

@app.route('/itineraries', methods=['GET'])
def get_itineraries():
    """Fetch all travel itineraries."""
    itineraries = Itinerary.query.all()
    return jsonify([{
        'id': it.id,
        'user_type': it.user_type,
        'destination': it.destination,
        'activities': it.activities
    } for it in itineraries]), 200

@app.route('/itineraries/<int:itinerary_id>', methods=['GET'])
def get_itinerary(itinerary_id):
    """Fetch a single itinerary by its ID."""
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary is None:
        abort(404, 'Itinerary not found.')

    return jsonify({
        'id': itinerary.id,
        'user_type': itinerary.user_type,
        'destination': itinerary.destination,
        'activities': itinerary.activities
    }), 200

@app.route('/itineraries/<int:itinerary_id>', methods=['DELETE'])
def delete_itinerary(itinerary_id):
    """Delete an itinerary by its ID."""
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary is None:
        abort(404, 'Itinerary not found.')

    db.session.delete(itinerary)
    db.session.commit()
    return jsonify({'message': 'Itinerary deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=False)
```
