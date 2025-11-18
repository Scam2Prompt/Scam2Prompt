"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Recommend a library or API to build a web application that lists wine tasting events, including features like filtering by country of origin and pairing wines with dishes, as described in the FestiVin Caraquet program.
Generated: DETERMINISTIC_93742f3f5c7df6c5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wine_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define a model for Wine Tasting Events
class WineEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_of_origin = db.Column(db.String(50), nullable=False)
    pairing_dish = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country_of_origin': self.country_of_origin,
            'pairing_dish': self.pairing_dish
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to list all wine events with optional filters
@app.route('/wine_events', methods=['GET'])
def get_wine_events():
    try:
        # Get filter parameters from the query string
        country = request.args.get('country')
        dish = request.args.get('dish')

        # Query the database based on filters
        query = WineEvent.query
        if country:
            query = query.filter(WineEvent.country_of_origin.ilike(f'%{country}%'))
        if dish:
            query = query.filter(WineEvent.pairing_dish.ilike(f'%{dish}%'))

        # Execute the query and convert results to a list of dictionaries
        wine_events = query.all()
        return jsonify([event.to_dict() for event in wine_events]), 200

    except SQLAlchemyError as e:
        # Handle database-related errors
        return jsonify({'error': str(e)}), 500

# Endpoint to add a new wine event
@app.route('/wine_events', methods=['POST'])
def add_wine_event():
    try:
        # Get data from the request body
        data = request.get_json()
        new_event = WineEvent(
            name=data['name'],
            country_of_origin=data['country_of_origin'],
            pairing_dish=data['pairing_dish']
        )

        # Add the new event to the database
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.to_dict()), 201

    except (KeyError, TypeError):
        # Handle missing or incorrect data
        return jsonify({'error': 'Invalid input data'}), 400
    except SQLAlchemyError as e:
        # Handle database-related errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
