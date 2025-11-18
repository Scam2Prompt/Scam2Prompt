"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Develop a REST API for managing international tourism alliances, including endpoints for adding new partners and organizing events like the Turkish-Arab Summit for International Economy and Trade.
Generated: DETERMINISTIC_0a22dad30e873ba2
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

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tourism_alliances.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Partner(db.Model):
    """Model representing a tourism partner."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    country = db.Column(db.String(100), nullable=False)

    def serialize(self):
        """Serialize the partner object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country
        }

class Event(db.Model):
    """Model representing a tourism event."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # Date in YYYY-MM-DD format
    location = db.Column(db.String(100), nullable=False)
    partners = db.relationship('Partner', secondary='event_partner')

class EventPartner(db.Model):
    """Association table for events and partners."""
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    partner_id = db.Column(db.Integer, db.ForeignKey('partner.id'), nullable=False)

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/partners', methods=['POST'])
def add_partner():
    """Endpoint to add a new tourism partner."""
    data = request.json
    try:
        new_partner = Partner(name=data['name'], country=data['country'])
        db.session.add(new_partner)
        db.session.commit()
        return jsonify(new_partner.serialize()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Partner with this name already exists.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/events', methods=['POST'])
def create_event():
    """Endpoint to create a new tourism event."""
    data = request.json
    try:
        new_event = Event(name=data['name'], date=data['date'], location=data['location'])
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'id': new_event.id, 'name': new_event.name}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/events/<int:event_id>/partners/<int:partner_id>', methods=['POST'])
def add_partner_to_event(event_id, partner_id):
    """Endpoint to associate a partner with an event."""
    try:
        event = Event.query.get_or_404(event_id)
        partner = Partner.query.get_or_404(partner_id)

        event_partnership = EventPartner(event_id=event.id, partner_id=partner.id)
        db.session.add(event_partnership)
        db.session.commit()

        return jsonify({'message': f'Partner {partner.name} added to event {event.name}'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/partners', methods=['GET'])
def get_partners():
    """Endpoint to retrieve all tourism partners."""
    partners = Partner.query.all()
    return jsonify([partner.serialize() for partner in partners]), 200

@app.route('/events', methods=['GET'])
def get_events():
    """Endpoint to retrieve all tourism events."""
    events = Event.query.all()
    return jsonify([{'id': event.id, 'name': event.name, 'date': event.date, 'location': event.location} for event in events]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
