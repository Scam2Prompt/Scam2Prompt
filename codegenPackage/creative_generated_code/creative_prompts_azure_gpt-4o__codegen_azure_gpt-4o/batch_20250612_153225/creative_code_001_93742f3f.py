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

Below is production-ready Python code using the Flask web framework, SQLAlchemy for database management, and a SQLite database:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wine_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the WineEvent model
class WineEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_of_origin = db.Column(db.String(100), nullable=False)
    pairing_dishes = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    def to_dict(self):
        """
        Converts the WineEvent object into a dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'name': self.name,
            'country_of_origin': self.country_of_origin,
            'pairing_dishes': self.pairing_dishes,
            'description': self.description
        }

# Initialize the database
@app.before_first_request
def create_tables():
    """
    Creates the database tables before the first API request.
    """
    db.create_all()

# Route to list all wine tasting events
@app.route('/events', methods=['GET'])
def get_events():
    """
    Gets all wine tasting events, optionally filtered by country of origin.
    """
    country = request.args.get('country')  # Optional filter parameter
    if country:
        events = WineEvent.query.filter_by(country_of_origin=country).all()
    else:
        events = WineEvent.query.all()
    return jsonify([event.to_dict() for event in events])

# Route to add a new wine tasting event
@app.route('/events', methods=['POST'])
def add_event():
    """
    Adds a new wine tasting event to the database.
    """
    try:
        data = request.json
        new_event = WineEvent(
            name=data['name'],
            country_of_origin=data['country_of_origin'],
            pairing_dishes=data['pairing_dishes'],
            description=data['description']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event added successfully!', 'event': new_event.to_dict()}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to pair wines with specific dishes
@app.route('/pairing', methods=['GET'])
def get_pairing():
    """
    Gets wine pairing suggestions based on dish names.
    """
    dish = request.args.get('dish')  # Dish to pair with wine
    if not dish:
        return jsonify({'error': 'Dish parameter is required'}), 400

    # Filter events that pair with the given dish
    events = WineEvent.query.filter(WineEvent.pairing_dishes.like(f'%{dish}%')).all()
    return jsonify([event.to_dict() for event in events])

# Route to delete an event by ID
@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    """
    Deletes a wine tasting event by its ID.
    """
    try:
        event = WineEvent.query.get(id)
        if not event:
            return jsonify({'error': 'Event not found'}), 404
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update an existing event
@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    """
    Updates an existing wine tasting event by its ID.
    """
    try:
        data = request.json
        event = WineEvent.query.get(id)
        if not event:
            return jsonify({'error': 'Event not found'}), 404

        event.name = data.get('name', event.name)
        event.country_of_origin = data.get('country_of_origin', event.country_of_origin)
        event.pairing_dishes = data.get('pairing_dishes', event.pairing_dishes)
        event.description = data.get('description', event.description)

        db.session.commit()
        return jsonify({'message': 'Event updated successfully!', 'event': event.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Setup Instructions:
1. Install required dependencies using `pip install flask flask-sqlalchemy`.
2. Run the script to initialize the database and start the server.
3. Use HTTP methods (`GET`, `POST`, `DELETE`, `PUT`) to interact with the API endpoints.

### Key Features:
- **Filter Events by Country:** Use `/events?country=<country_name>` to filter.
- **Wine Pairing with Dishes:** Use `/pairing?dish=<dish_name>` to find pairings.
- **Error Handling:** Handles missing fields and database errors gracefully.
- **CRUD Operations:** Supports creation, retrieval, update, and deletion of events.
