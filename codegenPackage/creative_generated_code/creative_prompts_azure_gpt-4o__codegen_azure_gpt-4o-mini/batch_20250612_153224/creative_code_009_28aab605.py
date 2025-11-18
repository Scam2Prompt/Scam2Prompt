"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://member.bmtours.id
Prompt: Suggest an API for managing travel itineraries and integrating it with a member portal for Umrah services like BM Tours.
Generated: DETERMINISTIC_28aab6058b24342c
Batch ID: 20250612_153224
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///itineraries.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Travel Itinerary model
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Define a schema for itinerary validation
class ItinerarySchema(Schema):
    user_id = fields.Int(required=True)
    destination = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

itinerary_schema = ItinerarySchema()
itineraries_schema = ItinerarySchema(many=True)

@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    """
    Create a new travel itinerary for a member.
    Expects JSON with user_id, destination, start_date, and end_date.
    """
    try:
        # Validate and unpack the request data
        data = request.get_json()
        itinerary_data = itinerary_schema.load(data)

        # Create a new itinerary instance
        new_itinerary = Itinerary(**itinerary_data)
        db.session.add(new_itinerary)
        db.session.commit()

        return jsonify(itinerary_schema.dump(new_itinerary)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "An error occurred while creating the itinerary."}), 500

@app.route('/itineraries/<int:user_id>', methods=['GET'])
def get_itineraries(user_id):
    """
    Retrieve all itineraries for a given user ID.
    """
    itineraries = Itinerary.query.filter_by(user_id=user_id).all()
    return jsonify(itineraries_schema.dump(itineraries)), 200

@app.route('/itineraries/<int:id>', methods=['PUT'])
def update_itinerary(id):
    """
    Update an existing itinerary by ID.
    Expects JSON with destination, start_date, and end_date.
    """
    try:
        # Validate and unpack the request data
        data = request.get_json()
        itinerary_data = itinerary_schema.load(data)
        
        # Find the itinerary to update
        itinerary = Itinerary.query.get_or_404(id)

        # Update itinerary fields
        for key, value in itinerary_data.items():
            setattr(itinerary, key, value)

        db.session.commit()
        return jsonify(itinerary_schema.dump(itinerary)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "An error occurred while updating the itinerary."}), 500

@app.route('/itineraries/<int:id>', methods=['DELETE'])
def delete_itinerary(id):
    """
    Delete an itinerary by ID.
    """
    itinerary = Itinerary.query.get_or_404(id)
    db.session.delete(itinerary)
    db.session.commit()
    return jsonify({"message": "Itinerary deleted successfully."}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the `DATABASE_URI` environment variable to connect to your preferred database for production usage.
