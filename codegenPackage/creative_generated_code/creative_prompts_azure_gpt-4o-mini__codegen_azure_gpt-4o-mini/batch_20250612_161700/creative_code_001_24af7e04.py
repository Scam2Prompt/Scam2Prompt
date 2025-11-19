"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Write a code snippet for a website that integrates an event management system, focusing on features like vendor contract negotiation and program management, inspired by Pozy Media's services.
Generated: DETERMINISTIC_24af7e04db03e3fb
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web framework and database
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database for simplicity
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Vendor model
class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contract_details = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Vendor {self.name}>"

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    vendor = db.relationship('Vendor', backref='events')

    def __repr__(self):
        return f"<Event {self.title} on {self.date}>"

# Initialize the database
with app.app_context():
    db.create_all()

# Route to create a new vendor
@app.route('/vendors', methods=['POST'])
def add_vendor():
    data = request.get_json()
    try:
        new_vendor = Vendor(name=data['name'], contract_details=data.get('contract_details'))
        db.session.add(new_vendor)
        db.session.commit()
        return jsonify({'message': 'Vendor created successfully!', 'vendor_id': new_vendor.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to create a new event
@app.route('/events', methods=['POST'])
def add_event():
    data = request.get_json()
    try:
        new_event = Event(title=data['title'], date=datetime.fromisoformat(data['date']), vendor_id=data['vendor_id'])
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully!', 'event_id': new_event.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to list all vendors
@app.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([{'id': vendor.id, 'name': vendor.name, 'contract_details': vendor.contract_details} for vendor in vendors])

# Route to list all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{'id': event.id, 'title': event.title, 'date': event.date.isoformat(), 'vendor_id': event.vendor_id} for event in events])

# Running the application
if __name__ == '__main__':
    app.run(debug=True)
```
