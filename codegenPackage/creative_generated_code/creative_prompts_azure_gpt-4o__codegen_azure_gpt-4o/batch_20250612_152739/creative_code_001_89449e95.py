"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Recommend a library for managing memberships and event registrations for a sports organization like "Grad košarke."
Generated: DETERMINISTIC_89449e95d161881b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python example using the `Flask` web framework and the SQLAlchemy library for managing memberships and event registrations. This code demonstrates how to set up models, routes, and basic CRUD functionality. These libraries are widely used and suitable for production applications.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_org.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Membership model
class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Membership {self.name}>"

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Event {self.name}>"

# Define the Registration model (linking memberships and events)
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    membership_id = db.Column(db.Integer, db.ForeignKey('membership.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    membership = db.relationship('Membership', backref='registrations')
    event = db.relationship('Event', backref='registrations')

    def __repr__(self):
        return f"<Registration Membership: {self.membership_id}, Event: {self.event_id}>"

# Error handling middleware
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="An internal server error occurred"), 500

# Route to add a new membership
@app.route('/memberships', methods=['POST'])
def add_membership():
    try:
        data = request.json
        new_member = Membership(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', None)
        )
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Membership added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to retrieve all memberships
@app.route('/memberships', methods=['GET'])
def get_memberships():
    memberships = Membership.query.all()
    return jsonify([{
        'id': m.id,
        'name': m.name,
        'email': m.email,
        'phone': m.phone,
        'active': m.active
    } for m in memberships]), 200

# Route to add a new event
@app.route('/events', methods=['POST'])
def add_event():
    try:
        data = request.json
        new_event = Event(
            name=data['name'],
            date=data['date'],
            location=data['location'],
            capacity=data['capacity']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to register a member for an event
@app.route('/registrations', methods=['POST'])
def add_registration():
    try:
        data = request.json
        new_registration = Registration(
            membership_id=data['membership_id'],
            event_id=data['event_id']
        )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify({'message': 'Registration created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all registrations
@app.route('/registrations', methods=['GET'])
def get_registrations():
    registrations = Registration.query.all()
    return jsonify([{
        'id': r.id,
        'membership_id': r.membership_id,
        'event_id': r.event_id
    } for r in registrations]), 200

# Main entry point
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Key Notes:
- Install required dependencies: `Flask` and `SQLAlchemy`.
- Use `pip install flask flask-sqlalchemy` to set up the libraries.
- Replace SQLite with a production-grade database (e.g., PostgreSQL or MySQL) for deployment. Adjust `SQLALCHEMY_DATABASE_URI` accordingly.
- Set `debug=False` in production and use proper logging.
- Secure user inputs to prevent SQL injection, and consider using a library like `Flask-WTF` for form handling.
