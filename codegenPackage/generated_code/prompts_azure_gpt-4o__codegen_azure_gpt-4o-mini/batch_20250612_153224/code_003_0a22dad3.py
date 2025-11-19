"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: Develop a REST API for managing international tourism alliances, including endpoints for adding new partners and organizing events like the Turkish-Arab Summit for International Economy and Trade.
Generated: DETERMINISTIC_0a22dad30e873ba2
Batch ID: 20250612_153224
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tourism_alliances.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Partner model
class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    country = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country
        }

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'location': self.location
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new partner
@app.route('/partners', methods=['POST'])
def add_partner():
    data = request.get_json()
    if not data or 'name' not in data or 'country' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_partner = Partner(name=data['name'], country=data['country'])
    try:
        db.session.add(new_partner)
        db.session.commit()
        return jsonify(new_partner.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Partner already exists'}), 409

# Endpoint to list all partners
@app.route('/partners', methods=['GET'])
def list_partners():
    partners = Partner.query.all()
    return jsonify([partner.to_dict() for partner in partners]), 200

# Endpoint to create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    if not data or 'name' not in data or 'date' not in data or 'location' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_event = Event(name=data['name'], date=data['date'], location=data['location'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify(new_event.to_dict()), 201

# Endpoint to list all events
@app.route('/events', methods=['GET'])
def list_events():
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
