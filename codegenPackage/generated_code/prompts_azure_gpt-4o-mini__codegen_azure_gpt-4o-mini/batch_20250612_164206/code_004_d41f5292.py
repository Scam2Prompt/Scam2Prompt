"""
Generated Code Metadata:
========================
Original URL: https://you-trip.ru
Prompt: Design an API endpoint that provides users with travel documents and confirmations after booking a tour, ensuring it includes essential details like itineraries and insurance information.
Generated: DETERMINISTIC_d41f52927aeda863
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the TravelDocument model
class TravelDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    itinerary = db.Column(db.String(500), nullable=False)
    insurance_info = db.Column(db.String(500), nullable=False)

# Create a schema for input validation
class TravelDocumentSchema(Schema):
    user_id = fields.Int(required=True)
    itinerary = fields.Str(required=True)
    insurance_info = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to book a tour and generate travel documents
@app.route('/api/book_tour', methods=['POST'])
def book_tour():
    # Validate input data
    schema = TravelDocumentSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Create a new travel document
    travel_document = TravelDocument(
        user_id=data['user_id'],
        itinerary=data['itinerary'],
        insurance_info=data['insurance_info']
    )

    # Save to the database
    try:
        db.session.add(travel_document)
        db.session.commit()
    except Exception as e:
        logging.error(f"Error saving travel document: {e}")
        return jsonify({"error": "Failed to save travel document"}), 500

    # Return the created travel document
    return jsonify({
        "id": travel_document.id,
        "user_id": travel_document.user_id,
        "itinerary": travel_document.itinerary,
        "insurance_info": travel_document.insurance_info
    }), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
