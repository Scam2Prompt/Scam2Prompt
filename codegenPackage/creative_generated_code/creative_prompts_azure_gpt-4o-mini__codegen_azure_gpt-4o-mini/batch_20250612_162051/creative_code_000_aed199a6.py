"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehiletes.com
Prompt: Generate a code snippet for a travel booking API that allows users to create custom itineraries for group trips, similar to the unique itineraries offered by Rehiletes.
Generated: DETERMINISTIC_aed199a6ef403a4a
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
from marshmallow import Schema, fields, ValidationError
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///itineraries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model representing a trip itinerary
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    participants = db.Column(db.Integer, nullable=False)

# Schema for validating itinerary data
class ItinerarySchema(Schema):
    title = fields.Str(required=True)
    destination = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    participants = fields.Int(required=True)

itinerary_schema = ItinerarySchema()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for creating a new itinerary
@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    try:
        # Validate and deserialize input
        data = request.get_json()
        itinerary_data = itinerary_schema.load(data)

        # Create a new itinerary instance
        new_itinerary = Itinerary(
            title=itinerary_data['title'],
            destination=itinerary_data['destination'],
            start_date=datetime.strptime(itinerary_data['start_date'], '%Y-%m-%d').date(),
            end_date=datetime.strptime(itinerary_data['end_date'], '%Y-%m-%d').date(),
            participants=itinerary_data['participants']
        )

        # Add the new itinerary to the database
        db.session.add(new_itinerary)
        db.session.commit()

        return jsonify(itinerary_schema.dump(new_itinerary)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for retrieving all itineraries
@app.route('/itineraries', methods=['GET'])
def get_itineraries():
    try:
        itineraries = Itinerary.query.all()
        return jsonify(itinerary_schema.dump(itineraries, many=True)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for retrieving a single itinerary by ID
@app.route('/itineraries/<int:id>', methods=['GET'])
def get_itinerary(id):
    try:
        itinerary = Itinerary.query.get_or_404(id)
        return jsonify(itinerary_schema.dump(itinerary)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
```
