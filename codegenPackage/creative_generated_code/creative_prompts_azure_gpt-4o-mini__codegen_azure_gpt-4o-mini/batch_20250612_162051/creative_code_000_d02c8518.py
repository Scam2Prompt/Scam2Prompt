"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inkasluxury.com
Prompt: Generate a code snippet for a travel booking API that allows users to customize their itineraries for tours in Peru, similar to the personalized experiences offered by Inkas Luxury.
Generated: DETERMINISTIC_d02c8518d6584ab9
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
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Tour Itineraries
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in days
    activities = db.Column(db.String(500), nullable=False)  # Activities in a comma-separated list

# Schema for validating itinerary data
class ItinerarySchema(Schema):
    destination = fields.String(required=True, validate=validate.Length(min=1))
    duration = fields.Integer(required=True, validate=validate.Range(min=1))
    activities = fields.String(required=True, validate=validate.Length(min=1))

itinerary_schema = ItinerarySchema()
itineraries_schema = ItinerarySchema(many=True)

@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    """
    Create a new itinerary based on user input.
    Expecting JSON in the request body with destination, duration, and activities.
    """
    try:
        # Validate and deserialize input
        itinerary_data = itinerary_schema.load(request.json)
        
        # Create a new itinerary instance
        new_itinerary = Itinerary(
            destination=itinerary_data['destination'],
            duration=itinerary_data['duration'],
            activities=itinerary_data['activities']
        )
        
        # Add the new itinerary to the database
        db.session.add(new_itinerary)
        db.session.commit()
        
        return itinerary_schema.jsonify(new_itinerary), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/itineraries', methods=['GET'])
def get_itineraries():
    """
    Retrieve all itineraries from the database.
    """
    try:
        itineraries = Itinerary.query.all()
        return itineraries_schema.jsonify(itineraries), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set to False in production
```
