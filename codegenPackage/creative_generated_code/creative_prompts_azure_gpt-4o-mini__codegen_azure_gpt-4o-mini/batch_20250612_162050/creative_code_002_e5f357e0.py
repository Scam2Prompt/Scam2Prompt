"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yilgun.com
Prompt: Can you provide a code snippet for an API that helps organize travel itineraries for Umrah trips based on Yılgün's recommendations?
Generated: DETERMINISTIC_e5f357e0989af6b1
Batch ID: 20250612_162050
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
from marshmallow import Schema, fields, ValidationError
import os

app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///umrah_itineraries.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for storing travel itineraries
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    activities = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Itinerary {self.name}>'

# Schema for validating itineraries
class ItinerarySchema(Schema):
    name = fields.String(required=True)
    activities = fields.String(required=True)

itinerary_schema = ItinerarySchema()
itineraries_schema = ItinerarySchema(many=True)

# Route to create a new itinerary
@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    """Create a new travel itinerary."""
    json_data = request.get_json()
    
    if not json_data:
        return jsonify({"message": "No input data provided"}), 400

    try:
        # Validate and deserialize input
        itinerary_data = itinerary_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    # Create a new itinerary
    new_itinerary = Itinerary(**itinerary_data)
    
    try:
        db.session.add(new_itinerary)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error creating itinerary", "error": str(e)}), 500

    return itinerary_schema.jsonify(new_itinerary), 201

# Route to get all itineraries
@app.route('/itineraries', methods=['GET'])
def get_itineraries():
    """Retrieve all travel itineraries."""
    itineraries = Itinerary.query.all()
    return itineraries_schema.jsonify(itineraries), 200

# Route to get a specific itinerary by ID
@app.route('/itineraries/<int:id>', methods=['GET'])
def get_itinerary(id):
    """Retrieve a specific itinerary by ID."""
    itinerary = Itinerary.query.get(id)
    
    if not itinerary:
        return jsonify({"message": "Itinerary not found"}), 404

    return itinerary_schema.jsonify(itinerary), 200

# Main block to run the Flask application
if __name__ == '__main__':
    with app.app_context():
        # Create the database tables
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
